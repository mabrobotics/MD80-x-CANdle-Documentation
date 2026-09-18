# Communication Overview

MD communication is based on the CAN and CAN-FD bus. A drive runs one of two application layers, and
which one it runs is decided by the firmware flashed onto it:

- [MD Protocol](md_protocol), MAB's own protocol,
- [CANopen](md_canopen), the industry standard.

## MD Protocol

MD Protocol offers a dead simple, yet quite efficient interface based around register access,
similar to Modbus. It follows a strict master and slave model where registers can be accessed one by
one, or by batch reads and writes. This is the protocol used by
[CANdle and CANdleHAT](candle_and_hat).

MD Protocol runs on CAN-FD, at up to 8 Mbit/s with 64 bytes per frame, and on CAN 2.0. Unless you
already have a CANopen network to join, this is the protocol to choose. It is faster, simpler and
better supported by MAB's own tooling.

## CANopen

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
| [CANopen](md_canopen)                | current  | revision 2.0      | actively developed              |
| [CANopen \[LEGACY\]](md_canopen_co25) | 2.5.x   | revision 1.1      | supported, no longer updated    |

To tell which firmware a drive is running, read Store Parameters 0x1010 over SDO. The legacy
firmware answers; the current firmware aborts with 0x06020000, object does not exist, because saving
moved to Save Config 0x2023:1. On the current firmware you can then read Firmware Version 0x2021:2,
which the legacy dictionary does not have.

```{important}
Do not mix the two references. Several indices exist in both generations with different meanings.
0x2000 is Motor Settings on the legacy firmware and Actuator Config on the current one, so a value
written from the wrong chapter can be accepted and act on something you did not intend.
```

## Switching between protocols

A drive runs either MD Protocol or CANopen, never both. Changing between them means flashing the
other firmware variant, which is published in [Downloads](downloads). The procedure for drives on
the legacy CANopen firmware is described in
[Migration to and from CANopen](canopen_migration_co25).
