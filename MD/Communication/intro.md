# Communication Overview

MD communication is based on the CAN and CAN-FD bus. A drive runs one of two application layers, and
which one it runs is decided by the firmware flashed onto it:

- [MD Protocol](md_protocol), MAB's own protocol,
- [CANopen](md_canopen), the industry standard.

## MD Protocol (MD)

MD Protocol offers a dead simple, yet quite efficient interface based around register access,
similar to Modbus. It follows a strict master and slave model where registers can be accessed one by
one, or by batch reads and writes. This is the protocol used by
[CANdle and CANdleHAT](candle_and_hat).

MD Protocol runs on CAN-FD, at up to 8 Mbit/s with 64 bytes per frame, and on CAN 2.0. Unless you
already have a CANopen network to join, this is the protocol to choose. It is faster, simpler and
better supported by MAB's own tooling.

## CANopen (MDCO)

[CANopen](https://www.can-cia.org/can-knowledge/canopen) is an older but widely used industrial
protocol. It offers high configurability and drops into existing industrial control systems without
custom integration work, at the cost of complexity and of CAN 2.0 bandwidth limits, meaning up to 8
bytes per frame. MD implements CANopen according to the
[CiA 402](https://www.can-cia.org/can-knowledge/cia-402-series-canopen-device-profile-for-drives-and-motion-control)
device profile for drives and motion control.

### Which CANopen section applies to your drive

Two generations of MD CANopen firmware are in the field, and their object dictionaries are not
compatible. Both are documented here.

| Section                              | Firmware | Object dictionary | Status                          |
| ------------------------------------ | -------- | ----------------- | ------------------------------- |
| [CANopen](md_canopen)                | current  | revision 1.2      | actively developed              |
| [CANopen \[LEGACY\]](md_canopen_co25) | 2.5.x   | revision 1.1      | supported, no longer updated    |

To tell which firmware a drive is running, read Firmware Version 0x2021:2 over SDO. The current
firmware answers; the legacy firmware aborts with 0x06020000, object does not exist, because it
keeps its firmware information at 0x200A instead.

```{important}
Do not mix the two references. Several indices exist in both generations with different meanings.
0x2000 is Motor Settings on the legacy firmware and Actuator Config on the current one, so a value
written from the wrong chapter can be accepted and act on something you did not intend.
```

## Switching between protocols

A drive runs either MD Protocol or CANopen, never both. Changing between them means flashing the
other firmware variant, which is published in [Downloads](downloads).

### Migration between MD Protocol (MD) and MD CANOpen (MDCO) Protocol 
For drives with firmware v3.0.0+ and with `candletool` v1.5.1+, the migration process is
straightforward. 

#### From MD to MDCO:
1. Set canId of the drive to range 10 - 127 with: 
```
candletool md can --id <current-ID> --new_id <new-ID> --save
for example:
candletool md can --id 675 --new_id 100 --save
```
2. Update the drive with:
```
candletool md update --mdco <version> --id <current-ID>
for example:
candletool md update --mdco latest --id 100
or:
candletool md update --mdco 3.0.1 --id 100
```

3. Validate migration
```
candletool mdco info -i <ID>
for example:
candletool mdco info -i 100
```

#### From MDCO to MD:
```{note}
The update process uses FDCAN protocol and will corrupt (and get corrupted),
by any other CANOpen devices present on the bus. The update procedure 
is only possible when the target device is THE ONLY DEVICE ON THE CAN BUS.
```
1. Update the drive with:
```
candletool mdco update --md <version> --id <ID>
for example:
candletool mdco update --md latest --id 100
or:
candletool mdco update --md 3.0.1 --id 100
```

2. Validate migration
```
candletool md info -i <ID>
for example:
candletool md info -i 100
```

### Remote update
When no internet connection is available, the update can be done with
local .mab files downloaded from [Downloads](downloads) section.
Then you can upload firmware to MD drive with:
```
candletool md update -p path/to/file.mab --id <ID>
```
or for MDCO drive with:
```
candletool mdco update -p path/to/file.mab --id <nodeId>
```

### Legacy (pre 3.0.0) firmware versions

The procedure for drives on the legacy CANopen firmware is described in
[Migration to and from CANopen](canopen_migration_co25).

#### MDCO v2.x.x update to v3.0.1+
To update the drive from legacy MDCO firmware to new, actively
supported firmware, a special procedure has been implemented in
**candletool v1.5.1+**:
```
candletool mdco update <version> -i <nodeId> --legacy-migration
for example
candletool mdco update latest -i 69 --legacy-migration
or
candletool mdco update 3.0.1 -i 69 --legacy-migration
```
```{warning}
This migration will cause the drive configuration to be mostly dropped.
Config upload and calibration will be required in majority of cases.
This will also make drive use `md_1.2.eds` instead of `md_1.1.eds`.
```