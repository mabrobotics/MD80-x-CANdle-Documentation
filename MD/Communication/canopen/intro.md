(md_canopen)=
# CANopen

MD controllers can run a CANopen application layer in place of the MAB MD Protocol. The
implementation follows [CiA 301](https://www.can-cia.org/can-knowledge/canopen) for communication
and the
[CiA 402](https://www.can-cia.org/can-knowledge/cia-402-series-canopen-device-profile-for-drives-and-motion-control)
device profile for drives and motion control.

CANopen is a separate firmware variant. A drive runs either the MD Protocol or CANopen, never both,
and switching between them means reflashing the drive with the other firmware. Both variants are
published in [Downloads](downloads).

```{note}
This section describes the CANopen firmware **v3.0.0** and later built around object dictionary 
revision **1.2** (`md_1.2.eds`). Drives running the older 2.5.x CANopen firmware are covered by the
[legacy CANopen section](md_canopen_co25), which describes a different object dictionary.
```

## Bus parameters

| Property            | Value                                          |
| ------------------- | ---------------------------------------------- |
| Physical layer      | CAN 2.0A, 11-bit identifiers, up to 8 data bytes |
| Bit rate            | 1 Mbit/s                                        |
| Node ID range       | 10 to 127                                       |
| Default node ID     | 100                                             |
| Node ID object      | 0x2000:1 Actuator Config, CAN ID                |

The node ID is the only address the drive answers to. Writing 0x2000:1 reinitialises the CAN
peripheral immediately, so the drive stops responding on its old identifiers as soon as the SDO is
acknowledged. Save the configuration afterwards or the change is lost on the next power cycle.

```{important}
1 Mbit/s is the only bit rate the firmware declares. The drive does not perform automatic bit rate
detection.
```

## Identification

| Object   | Name         | Value      | Meaning                                       |
| -------- | ------------ | ---------- | --------------------------------------------- |
| 0x1000   | Device Type  | 0x00020192 | Device profile 402, servo drive                |
| 0x6502   | Supported Drive Modes | 0x00000185 | Profile Position, Profile Velocity, Cyclic Sync Position, Cyclic Sync Velocity |
| 0x1018:1 | Vendor ID    | 0          | MAB Robotics has no CiA-assigned vendor ID yet |
| 0x1018:2 | Product Code | 1          | MD series                                      |

## Predefined connection set

Communication objects use the CiA 301 predefined connection set. In the table below, *n* is the node
ID of the drive.

| Object            | COB-ID          | Direction         |
| ----------------- | --------------- | ----------------- |
| NMT               | 0x000           | Master to drive   |
| SYNC              | 0x080           | Master to drive   |
| EMCY              | 0x080 + *n*     | Drive to master   |
| TPDO1 to TPDO4    | Configurable, see [PDO](canopen_pdo) | Drive to master |
| RPDO1             | 0x200 + *n*     | Master to drive   |
| RPDO2             | 0x300 + *n*     | Master to drive   |
| RPDO3             | 0x400 + *n*     | Master to drive   |
| RPDO4             | 0x500 + *n*     | Master to drive   |
| SDO response      | 0x580 + *n*     | Drive to master   |
| SDO request       | 0x600 + *n*     | Master to drive   |
| Heartbeat         | 0x700 + *n*     | Drive to master   |

The drive accepts any frame whose lowest seven identifier bits match its node ID, plus the NMT,
SYNC and heartbeat identifiers. TIME stamp frames are accepted by the object dictionary layout but
are discarded without action.

```{warning}
Transmit PDO identifiers are **not** offset by the node ID automatically. Out of the box every
drive transmits TPDO1 on 0x180, TPDO2 on 0x280, TPDO3 on 0x380 and TPDO4 on 0x480. On a bus with
more than one drive you must assign each drive its own transmit identifiers through 0x1800:1 to
0x1803:1. See [PDO](canopen_pdo).
```

## Electronic data sheet

The EDS file describing this object dictionary is `md_1.2.eds`, available from
[Downloads](device_firmware). Load it into your CANopen master or configuration tool to get object
names, data types and default values without transcribing them by hand.

## What is in this section

- [System Units](canopen_units) explains how physical quantities are encoded. Read this first,
  because position, velocity, torque and current all use scaled integers rather than SI values.
- [Network Management](canopen_nmt) covers NMT states, boot behaviour, heartbeat and SYNC.
- [Service Data Objects](canopen_sdo) covers SDO transfers and abort codes.
- [Process Data Objects](canopen_pdo) covers the default PDO layout and how to remap it.
- [State Machine](canopen_state_machine) covers the CiA 402 controlword and statusword.
- [Modes of Operation](canopen_modes) covers the supported motion modes and how to select them.
- [Diagnostics](canopen_diagnostics) covers the error register, emergency messages and the
  manufacturer status registers.
- [Setting Up a New Motor](canopen_setup) is the commissioning order for a drive out of the box.
- [Object Dictionary](canopen_od) is the complete object reference.
