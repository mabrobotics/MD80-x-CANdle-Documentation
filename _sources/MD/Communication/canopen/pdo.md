(canopen_pdo)=
# Process Data Objects

PDOs carry cyclic process data without the request and response overhead of an SDO. The drive
supports four receive PDOs for setpoints and four transmit PDOs for feedback. Each PDO carries up to
8 bytes.

PDOs are exchanged only in NMT Operational. See [Network Management](canopen_nmt).

## Receive PDOs

Receive PDOs use the CiA 301 predefined connection set, offset by the node ID.

| PDO   | COB-ID      | Parameters | Mapping | Default content                                                  |
| ----- | ----------- | ---------- | ------- | ---------------------------------------------------------------- |
| RPDO1 | 0x200 + *n* | 0x1400     | 0x1600  | Target Position 0x607A, Target Torque 0x6071                     |
| RPDO2 | 0x300 + *n* | 0x1401     | 0x1601  | Target Velocity 0x60FF, Target Torque 0x6071                     |
| RPDO3 | 0x400 + *n* | 0x1402     | 0x1602  | Controlword 0x6040, Target Position 0x607A, Target Torque 0x6071 |
| RPDO4 | 0x500 + *n* | 0x1403     | 0x1603  | Controlword 0x6040, Target Velocity 0x60FF, Target Torque 0x6071 |

RPDO3 and RPDO4 are the useful ones for closed loop control, because they carry the controlword
alongside the setpoint. That lets a master enable the drive, command motion and apply a torque limit
in a single frame.

```{note}
Which identifier a receive PDO listens on is fixed by the node ID and cannot be changed. The COB-ID
in 0x1400:1 through 0x1403:1 is stored and read back, but the drive does not use it to decide which
frames to accept.
```

## Transmit PDOs

| PDO   | Default COB-ID | Parameters | Mapping | Default content                                                             |
| ----- | -------------- | ---------- | ------- | --------------------------------------------------------------------------- |
| TPDO1 | 0x180          | 0x1800     | 0x1A00  | Statusword 0x6041, Quick Status 0x2022:1                                    |
| TPDO2 | 0x280          | 0x1801     | 0x1A01  | Position Actual Value 0x6064, Velocity Actual Value 0x606C                  |
| TPDO3 | 0x380          | 0x1802     | 0x1A02  | Torque Actual Value 0x6077, Power Stage Temperature 0x2004:1, Motor Temperature 0x2004:2 |
| TPDO4 | 0x480          | 0x1803     | 0x1A03  | DC Link Circuit Voltage 0x6079                                              |

```{warning}
Transmit COB-IDs are used exactly as stored, with no node ID offset. Every drive leaves the factory
transmitting TPDO1 on 0x180. Put two drives on one bus without reconfiguring and their transmit PDOs
will collide.

Before connecting a second drive, write 0x1800:1 through 0x1803:1 on each drive to an identifier of
its own. Following the predefined connection set and using 0x180 + node ID, 0x280 + node ID and so
on keeps the bus conventional and readable.
```

## Getting a transmit PDO to send

By default every PDO has transmission type 255 and an event timer of 0. In that combination nothing
triggers a transmission, so **a drive out of the box produces no PDO traffic at all**. You have to
choose a trigger.

| Transmission type | Behaviour for a transmit PDO                   | Behaviour for a receive PDO                       |
| ----------------- | ---------------------------------------------- | -------------------------------------------------- |
| 0                 | Transmit on every SYNC                          | Apply buffered data on every SYNC                  |
| 1 to 240          | Transmit on every *n*-th SYNC                   | Apply buffered data on every *n*-th SYNC           |
| 241 to 253        | Rejected with abort 0x06090030                  | Rejected with abort 0x06090030                     |
| 254, 255          | Transmit only on the event timer                | Apply data immediately on arrival                  |

Two ways to produce feedback, then:

- **Time driven.** Leave the transmission type at 255 and write the period in milliseconds to the
  event timer, sub-index 5. Writing 20 to 0x1800:5 makes TPDO1 transmit at 50 Hz.
- **SYNC driven.** Set the transmission type to 1 and have the master produce SYNC frames. Every
  drive then samples and answers in lockstep, which is what you want for coordinated multi-axis
  motion.

```{note}
Inhibit time, sub-index 3, is accepted and read back but is not enforced. SYNC start value,
sub-index 6, is declared in the EDS for transmit PDOs but is not implemented, and accessing it
aborts with 0x06090011. Sub-index 0 of every PDO communication parameter reports 5.

The event timer field of a receive PDO is stored but has no effect. To make the drive react to a
master that stops talking, use the [heartbeat consumer](canopen_nmt) instead.
```

## Remapping

A mapping entry is a 32-bit value laid out as index, sub-index, then length in bits.

| Bits  | Content            |
| ----- | ------------------ |
| 16-31 | Object index       |
| 8-15  | Object sub-index   |
| 0-7   | Object length in bits |

For example 0x607A0020 maps Target Position, which is 32 bits.

Remapping follows the standard CiA 301 sequence, and the drive enforces it:

1. Write 0 to sub-index 0 of the mapping object. This disables the mapping.
2. Write the new entries to sub-indices 1 to 8.
3. Write the number of entries back to sub-index 0. This re-enables the mapping.

Skipping the first step is the usual mistake. Writing an entry while the mapping is still enabled is
rejected with abort 0x06010000.

The drive validates each entry as you write it. The object must exist, must be PDO mappable, and the
length you declare must match the object's real length, otherwise the write aborts with 0x06040041.
When you write the count back, the drive adds up the mapped lengths and rejects anything over 64
bits with 0x06040042.

Objects that can be mapped are marked in the [object dictionary](canopen_od). All the measurement
and status registers are mappable, which makes it practical to build a feedback PDO carrying exactly
the diagnostics your application cares about.

```{important}
A remapped PDO lives in RAM. Run Save Config, 0x2023:1, to make the new mapping survive a power
cycle.
```
