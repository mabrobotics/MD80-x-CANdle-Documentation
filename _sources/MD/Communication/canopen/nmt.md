(canopen_nmt)=
# Network Management

Network management controls which communication services a drive takes part in. It is independent
of the [CiA 402 state machine](canopen_state_machine), which controls the power stage. A drive can
sit in NMT Operational with its power stage switched off, and the two never interact.

## States

| State           | SDO | PDO | Heartbeat | EMCY |
| --------------- | --- | --- | --------- | ---- |
| Pre-operational | yes | no  | yes       | yes  |
| Operational     | yes | yes | yes       | yes  |
| Stopped         | no  | no  | yes       | yes  |

In Stopped the drive ignores SDO requests entirely. It does not answer with an abort, so a master
will see its own request time out.

```{important}
The MD firmware enters **Operational** directly after initialisation. It does not wait in
Pre-operational for a start command, which is what CiA 301 describes and what most masters expect.
A drive therefore starts producing TPDOs and acting on RPDOs as soon as it has booted.
```

## NMT commands

NMT commands are sent on COB-ID 0x000 with exactly two data bytes. Frames of any other length are
discarded.

| Byte | Content                                              |
| ---- | ---------------------------------------------------- |
| 0    | Command specifier                                    |
| 1    | Target node ID, or 0 to address every node on the bus |

| Command specifier | Name                  | Effect on the drive                                    |
| ----------------- | --------------------- | ------------------------------------------------------ |
| 0x01              | Start remote node     | Enter Operational                                      |
| 0x02              | Stop remote node      | Enter Stopped                                          |
| 0x80              | Enter pre-operational | Enter Pre-operational                                  |
| 0x81              | Reset node            | Reboot the controller, equivalent to 0x2023:8           |
| 0x82              | Reset communication   | Reinitialise the CAN peripheral, equivalent to 0x2023:13 |

Reset node reboots the whole controller, so unsaved object dictionary changes are lost. Reset
communication restarts only the CAN interface and leaves the application running.

## Heartbeat producer

The drive transmits a one byte heartbeat on COB-ID 0x700 + node ID at the interval configured in
0x1017 Producer Heartbeat Time, in milliseconds. The default is 1000 ms. Writing 0 disables the
heartbeat.

| Heartbeat byte | State           |
| -------------- | --------------- |
| 0x04           | Stopped         |
| 0x05           | Operational     |
| 0x7F           | Pre-operational |

The firmware does not implement node guarding. Heartbeat is the only liveness mechanism.

## Heartbeat consumer

The drive can monitor one other node on the bus and treat its silence as a fault. Configure it
through 0x1016:1 Consumer Heartbeat Time, a 32-bit value laid out as follows.

| Bits  | Content                      |
| ----- | ---------------------------- |
| 0-15  | Timeout in milliseconds      |
| 16-23 | Node ID of the node to watch |
| 24-31 | Reserved, write 0            |

Monitoring is active only when both the node ID and the timeout are non-zero. Writing 0 to either
field disables it.

When the monitored node goes quiet for longer than the timeout, the drive does all three of the
following:

1. Sets the communication bit in the [error register](canopen_diagnostics) 0x1001.
2. Transmits an emergency message.
3. Commands its own quick stop, decelerating at the rate in 0x6085.

This is the recommended way to make a drive stop when the master crashes or a cable falls out. Point
it at the node ID of your master and set the timeout to a few times the master's own heartbeat
period.

```{note}
The reaction fires once. After the communication error bit is set, further timeouts produce no new
emergency message until the error is cleared with 0x2023:10.
```

## SYNC

The drive consumes SYNC frames on COB-ID 0x080. The identifier is reported by 0x1005 and is
read-only. The drive never produces SYNC; a master or a dedicated SYNC producer must generate it.

Each SYNC increments an internal counter that drives synchronous PDO handling. SYNC frames are
ignored unless the drive is in Operational. See [PDO](canopen_pdo) for how transmission types use
this counter.
