(firmware_changelog)=

# Firmware Changelog

Changes in each MD and MD CANopen firmware release listed in [Device Firmware](device_firmware).
Newest release first.

(changelog_3_0_2)=

## 09.11.2026 - v3.0.2

### MD Firmware 3.0.2

**Added**

- Dual-encoder absolute position, updated all the time when the auxiliary encoder mode is DUAL. See
  [Drives with DUAL encoders](dual_encoders).
- [Quick Status](quick_status) bit 14 (drive disabled) and bit 8 (configuration error).

**Changed**

- Register `0x027` is now `dualEncoderAbsPosition` (float32, rad). It was `dualEncoderRevolution`
  (uint8). Requires an updated CANdle-SDK.

**Fixed**

- The reported motion mode now always matches the mode actually running.
- The CAN watchdog warning now clears only when the drive enters Operational.

### MD CANopen 3.0.2

**Added**

- New EDS `md_1.3.eds`. 0x1018:03 (Revision Number) is 0x00010003.
- 0x2010 (Position PID Controller), 0x2011 (Velocity PID Controller) and 0x2012 (Impedance PD
  Controller) gains can be mapped to PDOs.
- 0x2002:07 (Dual Encoder Absolute Position), TPDO-mappable.
- 0x2002 (Auxiliary Encoder) mode accepts DUAL.

**Fixed**

- 0x2002 (Auxiliary Encoder) mode rejects invalid values with an SDO range abort.
- 0x2024 (User GPIO) state reports the real pin levels.
- 0x6061 (Modes of Operation Display) always matches the mode actually running.

(changelog_3_0_1)=

## 06.10.2026 - v3.0.1

### MD Firmware 3.0.1

**Added**

- Motor resistance and inductance can be set by hand. 0 means auto-detect during calibration.

**Changed**

- Max torque and max velocity set to 0 mean no limit.
- Position limits are disabled when min >= max.
- The velocity-limit error is checked only while the drive is enabled, with a 5% + 1 rad/s margin.
- Velocity targets are clamped to max velocity in all velocity and position modes.
- Quick stop works from every mode and no longer changes the profile deceleration.
- Switching into profile position while moving now stops and holds position.
- Disabling the drive keeps the target position instead of setting it to zero.
- The drive no longer reboots after a failed save.

**Fixed**

- Raised the brake holding voltage (4 V → 6 V equivalent).

### MD CANopen 3.0.1

New CANopen stack. It replaces CANopenNode and ships with the EDS `md_1.2.eds`. Drives on 2.5.x
CANopen firmware need the legacy migration, see [Communication Overview](../MD/Communication/intro.md).

**CiA 301**

- NMT, plus heartbeat producer and consumer.
- SDO, expedited and segmented.
- 4 RPDOs and 4 TPDOs:
  - Dynamic mapping, checked for size.
  - SYNC transmission types 0–240.
  - TPDO inhibit time.
  - COB-IDs are saved to non-volatile storage.
- EMCY, with 0x1001 (Error Register), 0x1003 (Pre-defined Error Field) and 0x603F (Error Code).
- 0x1010 (Store Parameters) and 0x1011 (Restore Default Parameters). A save doesn't reboot the drive.
- Classic CAN at 1 Mbit/s, using up to about 96% of the bus.

**CiA 402**

- Power drive state machine. Fault reset triggers on the rising edge of controlword bit 7.
- Modes: Profile Position, Profile Velocity, Cyclic Sync Position and Cyclic Sync Velocity, plus the
  manufacturer modes Impedance and Service.
- Disable operation while moving first slows down at 0x6084 (Profile Deceleration).
- Limits:
  - 0x607A (Target Position) is clamped to 0x607D (Software Position Limit).
  - 0x60C5 (Max Acceleration) and 0x60C6 (Max Deceleration) are applied.
  - 0x6072 (Max Torque) and 0x6080 (Max Motor Speed) set to 0 mean no limit.
- Manufacturer objects 0x2000 (Actuator Config) to 0x2024 (User GPIO) cover motor, encoder, torque
  sensor, temperature, controller, status and command settings.

**Drive core**

Same as MD Firmware 3.0.1.

(changelog_3_0_0)=

## 29.08.2026 - v3.0.0

### MD Firmware 3.0.0

Initial release of the MD v3.0.0 firmware.
