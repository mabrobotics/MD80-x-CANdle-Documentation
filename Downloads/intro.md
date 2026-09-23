(downloads)=

# Downloads

(hardware_downloads)=

## 3D models

Simplified (lightweight) 3D \*.STEP models of MABRobotics products can be found
[here](https://drive.google.com/drive/folders/1HMs3-LDdo9Fq8obLJfhrmhvfJQhLiTa4?usp=sharing).

## Firmware

Firmware update of MABs products is release in form of proprietary `.mab` files. These files can be
uploaded to devices using [CANdleTool](candletool)

```
candletool md update -i <id> -p ./path/to/mab/file.mab
candletool pds update -i <id> -p ./path/to/mab/file.mab
candletool candle update -i <id> -p ./path/to/mab/file.mab
```

For example:

```
candletool md update -i 100 -p ./md_3_0_0_abcdefa.mab
```


````{dropdown} **Firmware change to version v2.5.4 and older:**
Pre 3.0.0 firmware version uses a legacy update procedure, and requires Linux operating system.
The firmware package is compiled into executable binary. Be sure to unpack a .zip package with your
virmware version of choice and select executable appropriate for your system architecture (x86_64, arm64).
You can perform an update with:
```
./MAB_CAN_Flasher_5938df3 --id <id> --baud <can datarate>
```
where:
`<id>` -is your actuator can id i.e. `--id 100`,
`<can datarate>` - can be 1M, 2M, 5M or 8M.

if the update cannot be performed sucessfullt from any reason, there is a recovery procedure:
1. Disconnect your drive from power, and wait for total power loss (no LEDs),
2. Run command `./MAB_CAN_Flasher_5938df3 --id <id> --baud <can datarate> **--wait**`,
3. Connect power to the driver.
This should allow for uploading the firmware even to an otherwise unresponsive drive.
````

(device_firmware)=
## Device Firmware

Main stable releases:

| Date | CANdle device | MD Firmware | MD CANopen | EDS file |
| :--: | :-----------: | :---------: | :--------: | :------: |
| **29.08.2026 (latest)** | [2.4.0](../candlelib/includes/candle-firmware/candle_2.4.0.mab) | [3.0.0](../_static/firmware/md/md_app_3.0.0_3b52568.mab) | pending release | [1.2](../_static/eds/md_1.2.eds) |
| 10.03.2026 | [2.4.0](../candlelib/includes/candle-firmware/candle_2.4.0.mab) | [2.5.4](../candlelib/includes/md-firmware/MAB_CAN_Flasher_2.5.4.zip) | [2.5.4](../candlelib/includes/md-firmware/MAB_CAN_Flasher_CANopen_2.5.4.zip) | [1.1](../_static/eds/md_1.1.eds) |

````{dropdown} Older releases
| Date | CANdle device | MD Firmware | MD CANopen | EDS file |
| :--: | :-----------: | :---------: | :--------: | :------: |
| 02.03.2026 | [2.4.0](../candlelib/includes/candle-firmware/candle_2.4.0.mab) | - | [2.5.3](../candlelib/includes/md-firmware/MAB_CAN_Flasher_CANopen_2.5.3.zip) | [1.1](../_static/eds/md_1.1.eds) |
| 24.11.2025 | [2.4.0](../candlelib/includes/candle-firmware/candle_2.4.0.mab) | [2.5.2](../candlelib/includes/md-firmware/MAB_CAN_Flasher_2.5.2.zip) | [2.5.2](../candlelib/includes/md-firmware/MAB_CAN_Flasher_CANopen_2.5.2.zip) | [1.1](../_static/eds/md_1.1.eds) |
| 11.08.2025 | [2.2.1](../candlelib/includes/candle-firmware/MAB_USB_Flasher_2.2.1.zip) | 2.5.1 | - | - |
| 29.07.2025 | [2.2.1](../candlelib/includes/candle-firmware/MAB_USB_Flasher_2.2.1.zip) | 2.5.0 | - | - |
| 30.01.2025 | [2.2.1](../candlelib/includes/candle-firmware/MAB_USB_Flasher_2.2.1.zip) | [2.4.1](../candlelib/includes/md-firmware/MAB_CAN_Flasher_2.4.1.zip) | [2.4.1](../candlelib/includes/md-firmware/MAB_CAN_Flasher_CANopen_2.4.1.zip) | [1.0](../_static/eds/md_1.0.eds) |
| 22.08.2024 | [2.2.1](../candlelib/includes/candle-firmware/MAB_USB_Flasher_2.2.1.zip) | [2.4.0](../candlelib/includes/md-firmware/MAB_CAN_Flasher_2.4.0.zip) | [2.4.0](../candlelib/includes/md-firmware/MAB_CAN_Flasher_CANopen_2.4.0.zip) | - |
| 31.05.2024 | [2.2.1](../candlelib/includes/candle-firmware/MAB_USB_Flasher_2.2.1.zip) | [2.3.1](https://drive.google.com/file/d/1JEStPSVnSHGrSZuBAMhupySp18OfRDAs/view?usp=sharing) | - | - |
| 05.04.2023 | [2.2.0](https://drive.google.com/drive/folders/1KDQ-C75hCG3vG0TmMa5ZI3u2Hdv0R0jF?usp=share_link) | [2.2.0](https://drive.google.com/drive/folders/1fc-_x4e1BJuoYAXRuuwuZ3nlq07d4J5S?usp=share_link) | - | - |
````

Versions 2.5.0 and 2.5.1 are listed without a download because they were never packaged as an
archive. They exist only as per-architecture flasher executables under
`_static/firmware/md/legacy/`.

## CANdleSDK

Please visit [**releases**](https://github.com/mabrobotics/CANdle-SDK/releases) page for all of the
CANdleSDK binary releases.
