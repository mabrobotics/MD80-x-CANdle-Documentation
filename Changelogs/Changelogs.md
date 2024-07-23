# Changelogs

# Latest [23.07.2024]

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
    - `runCalibrateOutpuEncoderCmd` &rarr; `runCalibrateOutputEncoderCmd`
    - `motorTorgueBandwidth` &rarr; `motorTorqueBandwidth`
    - `motorStiction` &rarr; `motorStriction`
- Added support for MD20 driver

### MDtool

- Added compatibility with the newest CANdle lib functionalities 