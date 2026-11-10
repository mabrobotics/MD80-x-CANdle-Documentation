(canopen_diagnostics)=
# Diagnostics

The drive reports problems through three layers. The manufacturer status registers in 0x2022 hold
the detail, the CiA 301 and CiA 402 objects 0x1001 and 0x603F summarise it, and an emergency
message announces every new error as it is raised.

## Status registers

0x2022 exposes the same status words the MD Protocol uses. Each is a 32-bit field with error flags
in the low 16 bits and warnings in the high 16 bits. The bit meanings are documented once, in
[Status](status), and are identical here.

| Sub-index | Register                 | Bit meanings                          |
| --------- | ------------------------ | ------------------------------------- |
| 1         | Quick Status             | [Quick Status](quick_status), 16 bit  |
| 2         | Main Encoder Status      | [Encoder errors](status)              |
| 3         | Auxiliary Encoder Status | [Encoder errors](status)              |
| 4         | Calibration Status       | [Calibration errors](status)          |
| 5         | Bridge Status            | [Bridge errors](status)               |
| 6         | Hardware Status          | [Hardware errors](status)             |
| 7         | Communication Status     | [Communication errors](status)        |
| 8         | Motion Status            | [Motion status](motion_status)        |
| 9         | Misc Status              | see below                             |
| 10        | Config Status            | see below                             |

Every sub-index is read-only and PDO mappable, so you can stream whichever ones matter to your
application in a transmit PDO.

Quick Status is the one to poll first. It carries one summary bit per category, the drive disabled
flag in bit 14 and, in bit 15, the target reached flag. It is mapped into TPDO1 by default alongside the statusword.

Two bits are worth calling out because they affect commissioning:

- **Misc Status bit 30, routine in progress.** Set while a calibration or test routine from 0x2023
  is running. Wait for it to clear before issuing further commands.
- **Config Status bit 28, saving required.** Set when the configuration in RAM differs from what is
  in flash. Run Save Config 0x2023:1 to clear it.

## Error register

0x1001 Error Register is the CiA 301 one byte summary. It is PDO mappable and is included in every
emergency message.

| Bit | Meaning                  |
| --- | ------------------------ |
| 0   | Generic error, set whenever any other bit is set |
| 1   | Current                  |
| 2   | Voltage                  |
| 3   | Temperature              |
| 4   | Communication            |
| 5   | Device profile specific  |
| 6   | Reserved                 |
| 7   | Manufacturer specific    |

## Error codes

0x603F Error Code holds the CiA code of the most recently raised error that is still active. The drive
derives both this object and the error register from the status registers and the CANopen
communication errors, according to the table below.

| Condition                       | Source                       | Error register bit | Error code |
| ------------------------------- | ---------------------------- | ------------------ | ---------- |
| Over current                    | Hardware Status 0x2022:6     | Current            | 0x2310     |
| Current sensing offset fault    | Hardware Status 0x2022:6     | Current            | 0x2120     |
| DC link over voltage            | Hardware Status 0x2022:6     | Voltage            | 0x3210     |
| DC link under voltage           | Hardware Status 0x2022:6     | Voltage            | 0x3220     |
| Power stage over temperature    | Hardware Status 0x2022:6     | Temperature        | 0x4210     |
| Motor over temperature          | Hardware Status 0x2022:6     | Temperature        | 0x4310     |
| Position limit exceeded         | Motion Status 0x2022:8       | Device profile     | 0x8612     |
| Velocity limit exceeded         | Motion Status 0x2022:8       | Device profile     | 0x8400     |
| Main encoder error              | Main Encoder Status 0x2022:2 | Manufacturer       | 0x7305     |
| Auxiliary encoder error         | Aux Encoder Status 0x2022:3  | Manufacturer       | 0x7306     |
| Calibration error               | Calibration Status 0x2022:4  | Manufacturer       | 0x6100     |
| Configuration error             | Config Status 0x2022:10      | Manufacturer       | 0x6200     |
| Heartbeat consumer timeout      | [NMT](canopen_nmt)           | Communication      | 0x8130     |
| CAN receive overrun, frames dropped | CANopen stack            | Communication      | 0x8110     |

0x1001 and 0x603F are live. They are rebuilt from the active errors, so they clear by themselves once
the condition is gone and the error bits are cleared with Clear Errors 0x2023:10. When several errors
are active and the newest one clears, 0x603F reports one of the others.

Two event errors are reported only through an emergency message and 0x1003, without setting
0x1001 or 0x603F:

| Event                                         | Error code |
| --------------------------------------------- | ---------- |
| Receive PDO shorter than its mapping, ignored | 0x8210     |
| SYNC frame with data bytes, ignored           | 0x8240     |

## Error history

0x1003 Pre-defined Error Field keeps the last 8 error codes, newest in sub-index 1. Sub-index 0 gives
the number of stored entries. Each entry carries the error code in bits 0-15 and, for errors from the
status registers, the active error flags of that register in bits 16-31. Write 0 to sub-index 0 to
clear the history. Reading a sub-index above the number of entries aborts with 0x08000024.

## Emergency messages

The drive transmits an emergency message on COB-ID 0x080 + node ID:

- once for every newly raised error in the error codes table above, with that error's code,
- once for each event error,
- once with code 0x0000, error reset, when the last active error clears.

| Byte | Content                                |
| ---- | -------------------------------------- |
| 0-1  | Emergency error code                   |
| 2    | Error register, the value of 0x1001    |
| 3-4  | Quick Status, the value of 0x2022:1    |
| 5-7  | Zero                                   |

An error that stays active produces one message, not one per cycle. Up to 8 messages are queued
when several errors are raised at once; if the queue is full, newer ones are dropped and only
recorded in 0x1003. In NMT Stopped no emergency messages are sent, and those raised meanwhile are
dropped.

Statusword and Quick Status mapped into a transmit PDO remain the most direct way to watch the
drive. A drive entering Fault reports statusword 0x0208, 0x0008 after masking with 0x006F.

## Commands

0x2023 holds the manufacturer command objects. Trigger one by writing the value **1**. Any other
value is rejected with abort code 0x06090030.

| Sub-index | Command                           | Effect                                                     |
| --------- | --------------------------------- | ---------------------------------------------------------- |
| 1         | Save Config                       | Write the configuration to flash, then reboot               |
| 2         | Test Main Encoder                 | Run the main encoder test routine                           |
| 3         | Test Auxiliary Encoder            | Run the auxiliary encoder test routine                      |
| 4         | Run Calibration                   | Calibrate the motor and main encoder                        |
| 5         | Run Auxiliary Encoder Calibration | Calibrate the auxiliary encoder                             |
| 6         | Calibrate Current PI Gains        | Recompute current loop gains from resistance and inductance |
| 7         | Revert Factory Settings           | Restore defaults, save and reboot                           |
| 8         | Reset Controller                  | Reboot                                                      |
| 9         | Clear Warnings                    | Clear warning bits in 0x2022                                |
| 10        | Clear Errors                      | Clear error bits in 0x2022                                  |
| 11        | Blink LEDs                        | Flash the onboard LEDs to identify the drive                |
| 12        | Set Zero                          | Make the present shaft position the new zero                |
| 13        | Reinitialise CAN                  | Restart the CAN peripheral                                  |
| 14        | Zero Torque Sensor                | Re-zero the external torque sensor                          |

```{important}
Save Config, Revert Factory Settings and Reset Controller all reboot the drive. It stops answering
on the bus for the duration of the restart, and any SDO in flight is lost. The calibration and test
routines save automatically when they succeed, so they reboot as well.
```

### Standard save and restore

Saving and restoring defaults are also reachable through their CiA 301 objects, which is what a
generic CANopen master or configuration tool will use. Both take a four byte signature rather than
the value 1.

| Object   | Name                                            | Signature  | ASCII  | Equivalent to |
| -------- | ----------------------------------------------- | ---------- | ------ | ------------- |
| 0x1010:1 | Save all Parameters                             | 0x65766173 | `save` | 0x2023:1      |
| 0x1011:1 | Restore all Default Parameters                  | 0x64616F6C | `load` | 0x2023:7      |
| 0x1011:4 | Restore manufacturer defined default Parameters | 0x64616F6C | `load` | 0x2023:7      |

Writing any other value aborts with 0x08000020, data cannot be transferred or stored, which is the
CiA 301 response to a wrong signature. Reading 0x1010:1, 0x1011:1 or 0x1011:4 returns 1, meaning
the drive saves or restores on command.

0x1011:1 and 0x1011:4 behave identically. Restoring defaults always restores everything; there is no
way to reset one parameter group on its own.
