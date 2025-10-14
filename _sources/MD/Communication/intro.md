# Communication Overview

MD communication protocols are based on CAN and CAN-FD bus. One of the communication modes can be used:
- [MABs MD Protocol](md_protocol),
- [CANOpen](md_canopen).

MD Protocol, offers dead simple, yet quite efficient interface based around register access, similarly to 
modbus. It follows strict Master-Slave communication model where registers can be accessed one by one, 
or by batch read and writes. This is the protocol used by [CANdle and CANdleHAT](candle_and_hat).
MD Protocol can be used both with CAN-FD (up to 8M datarate and 64 bytes per frame) and CAN2.0.

The other option is [CANOpen](https://www.can-cia.org/can-knowledge/canopen), which is and older, but 
widely used industrial communication protocol. While offering high configurability it is limited by
CAN2.0 bandwidth restrictiong (data up to 8 bytes per frame), and is far more complex than MD Protocol. 
MD implements CANOpen compatible with [CiA 402](https://www.can-cia.org/can-knowledge/cia-402-series-canopen-device-profile-for-drives-and-motion-control)
device profile for drives and motion control.

## Migration to and from CANopen

### Preparation

Download flasher programs from here:

- [MD CANopen](canopen-flashers_legacy)
- [MD FDCAN Protocol](downloads)

The migration is performed via flashing appropriate firmware onto the MD device. Necessary
components for this procedure are:

- Candle or Candle HAT device
- MD driver
- PC or SBC with mdtool installed

Connect your candle device to the driver and power it. Make sure that candle device is connected via
the USB to the host.

```{important}
Only one device can be connected on the can line during the procedure, so all the drivers need to be updated individually.
```

### Migration to CANopen

#### First step

When switching to CANopen the driver ID must be within the range of valid nodeIDs in CANopen. To set
this up we usually use the lowest valid nodeID in our protocol which is 10. So the first command
issued should be for example:

```
candletool md can --id 100 --new_id 10
```

#### Second step

It is necessary to save this new ID to the persistent memory using save command as follows:

```
candletool md save --id 100
```

#### Third step

Use flasher to flash firmware onto the board:

```
<path_to_canopen_flasher> --id <id> --baud <baudrate>
```

Example:

```
./MAB_CAN_Flasher_CANopen_7fd0626 --id 10 --baud 1M
```

### Migration from CANopen

Using the recovery procedure, the driver can be reverted to version with MD FDCAN protocol. The
recovery command looks like this:

```
candletool md update --id 9 --recovery ./path_to_mab_file.mab
```

Example:

```
candletool md update --id 9 --recovery ./md_3_X_X_xxxxxxx.mab
```

After starting this command, the driver needs to be restarted (power cycled) manually and then the
recovery re-flashing procedure will begin. The driver should then operate in MD FDCAN protocol mode.

If the nodeID was lower than 10 the driver should automatically assign itself an ID of 10.

### Migration from CANopen to Legacy firmware

Using the recovery procedure, the driver can be reverted to version with MD FDCAN protocol. The
recovery command looks like this:

```
<path_to_fdcan_protocol_flasher> --id 9 --baud 1M --wait
```

Example:

```
./MAB_CAN_Flasher_xxxxxxx --id 9 --baud 1M --wait
```

After starting this command, the driver needs to be restarted manually and then the recovery
re-flashing procedure will begin. The driver should then operate in MD FDCAN protocol mode.

If the nodeID was lower than 10 the driver should automatically assign itself an ID of 10.
