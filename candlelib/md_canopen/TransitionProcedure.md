# Migration to and from CANopen

## Preparation

Download flasher programs from here:

- [MD CANopen](canopen-flashers_legacy)
- [MD FDCAN Protocol](software_downloads_legacy)

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

## Migration to CANopen

### First step

When switching to CANopen the driver ID must be within the range of valid nodeIDs in CANopen. To set
this up we usually use the lowest valid nodeID in our protocol which is 10. So the first command
issued should be:

```
mdtool config can <previous_id> <new_id> <baudrate> <watchdog>
```

Example:

```
mdtool config can 100 10 1M 200
```

### Second step

It is necessary to save this new ID to the persistent memory using save command as follows:

```
mdtool config save <id>
```

Example:

```
mdtool config save 10
```

### Third step

Use flasher to flash firmware onto the board:

```
<path_to_canopen_flasher> --id <id> --baud <baudrate>
```

Example:

```
./MAB_CAN_Flasher_CANopen_7fd0626 --id 10 --baud 1M
```

## Migration from CANopen

Using the recovery procedure, the driver can be reverted to version with MD FDCAN protocol. The
recovery command looks like this:

```
<path_to_fdcan_protocol_flasher> --id 9 --baud 1M --wait
```

Example:

```
./MAB_CAN_Flasher --id 9 --baud 1M --wait
```

After starting this command, the driver needs to be restarted manually and then the recovery
re-flashing procedure will begin. The driver should then operate in MD FDCAN protocol mode.

If the nodeID was lower than 10 the driver should automatically assign itself an ID of 10.
