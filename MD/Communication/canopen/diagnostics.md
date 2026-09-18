(canopen_diagnostics)=
# Diagnostics

The drive reports problems through three layers. The manufacturer status registers in 0x2022 hold
the detail, the CiA 402 objects 0x1001 and 0x603F summarise it, and an emergency message announces
one specific failure.

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

Quick Status is the one to poll first. It carries one summary bit per category plus, in bit 15, the
target reached flag. It is mapped into TPDO1 by default alongside the statusword.

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

0x603F Error Code holds a CiA 402 code for the most recent fault. The drive derives both this object
and the error register from the status registers, according to the table below.

| Condition                       | Error register bit | 0x603F |
| ------------------------------- | ------------------ | ------ |
| Output over current             | Current            | 0x2110 |
| Internal current sensing fault  | Current            | 0x2120 |
| DC link over voltage            | Voltage            | 0x3210 |
| DC link under voltage           | Voltage            | 0x3220 |
| Power stage over temperature    | Temperature        | 0x4210 |
| Motor over temperature          | Temperature        | 0x4310 |
| Velocity limit exceeded         | Device profile     | 0x8400 |
| Position limit exceeded         | Device profile     | 0x8500 |
| Calibration failure             | Manufacturer       | 0x6100 |
| Configuration error             | Manufacturer       | 0x6200 |
| Main encoder error              | Manufacturer       | 0x7200 |
| Auxiliary encoder error         | Manufacturer       | 0x7300 |
| Heartbeat consumer timeout      | Communication      | not set |

```{important}
0x1001 and 0x603F latch. Clearing the fault with Clear Errors 0x2023:10 clears the status registers
in 0x2022, but the error register and the error code keep their values until the drive is reset.

Treat 0x2022 as the live state of the drive and 0x1001 together with 0x603F as a record of what went
wrong since power on.
```

## Emergency messages

The drive transmits an emergency message on COB-ID 0x080 + node ID.

| Byte | Content                                |
| ---- | -------------------------------------- |
| 0-1  | Emergency error code, always 0x1000    |
| 2    | Error register, the value of 0x1001    |
| 3-4  | Quick Status, the value of 0x2022:1    |
| 5-7  | Zero                                   |

Two limitations are worth knowing before you build alarm handling on this:

- The emergency error code field is fixed at 0x1000, generic error. The specific cause is in the
  Quick Status bytes, and in 0x603F over SDO.
- An emergency message is produced by exactly one condition, a
  [heartbeat consumer timeout](canopen_nmt). Faults such as over current or an encoder failure change
  the status registers, the error register and the state machine, but do not generate an emergency
  message.

For fault detection, monitor the statusword and Quick Status through a transmit PDO rather than
waiting for an emergency message. A drive entering Fault reports statusword 0x0008.

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
