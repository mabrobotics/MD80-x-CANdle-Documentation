# Changelogs

## Latest

- Released CANdle-SDK 1.0
- PDS information added

## [30.01.2025]

### CANdle lib

- GPIO status was not updating values in diagnostics, fixed by downloading value from the controller
  when diagnostics called

### MDtool

- Encoder names changed
- Added DualRLS encoder mode
- Added MA-hs config

### MD Firmware

- Brake power now constant due to relationship with power supply voltage measurement
- Watchdog now changes w/o reset
- Added support for MD80HV (with 0,5 mOhm shunt resistors)

## [22.08.2024]

### CANdle lib

- Changed license to MIT
- Minor bug-fixes

### MDtool

- Changed license to MIT
- Minor bug-fixes

## [23.07.2024]

### MD Firmware

- Removed homing feature for safety, will be brought back in future releases
- Added GPIO general functionality - `GPIO Input`
- Relabeled Brake Mode as a GPIO mode, address and values stayed the same
- Added support for MD20 driver

### CANdle lib

- Removed homing feature support for safety, will be brought back in future releases
- Added GPIO general functionality support
- Relabeled Brake Mode as a GPIO mode, address and values stayed the same
- Fixed typos in register names:
  - `runCalibrateOutputEncoderCmd` → `runCalibrateOutputEncoderCmd`
  - `motorTorgueBandwidth` → `motorTorqueBandwidth`
- Added support for MD20 driver

### MDtool

- Added compatibility with the newest CANdle lib functionalities
