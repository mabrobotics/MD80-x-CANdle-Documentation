(mab_files)=
# MAB Firmware Files

These files were design to contain firmware for MAB devices with all the necessary meta-data. They can be used to update or flash firmware onto the MAB devices using [`candletool 'x' update`](candletool_update), where x is the name of the device intended to be updated.

## Structure
- Tag - Device which the firmware is intended for
- Size - length of the firmware data
- Checksum - CRC32 checksum of firmware
- Version - ASCII encoded version code
- AES IV - Initialization vector for firmware encoding in hex-value string
- Binary - String of hex values containing firmware (encrypted)