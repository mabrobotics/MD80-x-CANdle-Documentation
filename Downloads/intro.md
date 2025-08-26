(downloads)=

# Downloads

(hardware_downloads)=

## 3D models

Simplified (lightweight) 3D \*.STEP models of MABRobotics products can be found
[here](https://drive.google.com/drive/folders/1HMs3-LDdo9Fq8obLJfhrmhvfJQhLiTa4?usp=sharing).

## CANdleSDK

Please visit [**releases**](https://github.com/mabrobotics/CANdle-SDK/releases) page for all of the
CANdleSDK binary releases.

## MAB Firmware

Firmware update of MABs products is release in form of propriatary `.mab` files. These files can be
uploaded to devices using [CANdleTool](candletool)

```
candletool md update -i <id> ./path/to/mab/file.mab
candletool pds update -i <id> ./path/to/mab/file.mab
candletool candle update -i <id> ./path/to/mab/file.mab
```

For example:

```
candletool md update -i 100 ./md_3_0_0_abcdefa.mab
```

Below is the list of the most recent releases, that are currently being supported, for each device:

## TODO TODO TODO TODO TODO TODO

<!-- 
| MD  | PDS  | CANdle  |
|-----|------|---------| -->

## Legacy software

For updating older MD and CANdle revisions - products shipped before November 2025 (MD firmware
version up to v2.5.1) - the upload process is possible only via Linux based (x86, x64, arm64)
applications - MAB_CAN_Flashers. The procedure is descriped in the
[legacy section of documentationo](downloads_legacy)
