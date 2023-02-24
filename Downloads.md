(downloads)=
# Downloads

(hardware_downloads)=
## 3D models

Simplified (lightweight) 3D *.STEP models of MABRobotics products can be found [here](https://drive.google.com/drive/folders/1HMs3-LDdo9Fq8obLJfhrmhvfJQhLiTa4?usp=sharing).

(software_downloads)=
## Software (stable)

Main stable releases:

```{list-table} 
:header-rows: 1

* - 
  - CANdle lib
  - MDtool
  - pyCANdle
  - CANdle ROS
  - CANdle ROS2
  - CANdle device
  - MD80
* - earlier
  - [3.0](https://github.com/mabrobotics/candle/releases/tag/v3.0)
  - [1.1.0](https://github.com/mabrobotics/mdtool/releases/tag/v1.1)
  - [1.2.0](https://pypi.org/project/pyCandleMAB/1.2.0/)
  - [1.1.0](https://github.com/mabrobotics/candle_ros/releases/tag/v1.1)
  - [1.1.0](https://github.com/mabrobotics/candle_ros2/releases/tag/v1.1)
  - 1.4
  - 1.0
* - 12.12.2022 (latest)
  - [3.1](https://github.com/mabrobotics/candle/releases/tag/v3.1_hotfix)
  - [1.2.1](https://github.com/mabrobotics/mdtool/releases/tag/v1.2.1)
  - [1.3.1](https://pypi.org/project/pyCandleMAB/)
  - [1.2.0](https://github.com/mabrobotics/candle_ros/releases/tag/v1.2)
  - [1.2.0](https://github.com/mabrobotics/candle_ros2/releases/tag/v1.2)
  - [2.0](https://drive.google.com/drive/folders/10wIX2uEaf42pkwGgW9fVAcGT7zrbptN9?usp=share_link)
  - [2.0](https://drive.google.com/drive/folders/10wIX2uEaf42pkwGgW9fVAcGT7zrbptN9?usp=share_link)
```

## Software (devel)

Table below summarizes the devel software releases. These revisions may have some bugs, however they include the latest features

```{list-table} 
:header-rows: 1

* - 
  - CANdle lib
  - MDtool
  - pyCANdle
  - CANdle ROS
  - CANdle ROS2
  - CANdle device
  - MD80
* - 17.03.2023
  - [3.2.0.d](https://drive.google.com/drive/folders/1XKJnNAEghF8Jh2HlLuUUaDgkVnVy6OfJ?usp=share_link)
  - [1.2.2.d](https://drive.google.com/drive/folders/1LcdnHda-m0qAY4UQbjLMrsXUz_42LABR?usp=share_link)
  - x
  - x
  - x
  - [2.1.0.d](https://drive.google.com/drive/folders/1GAVajHGv3E2Ztz91iTGgU-HBfVtfEJ5R?usp=share_link)
  - [2.1.0.d](https://drive.google.com/drive/folders/1Gq0XDg758q5lsCxbxaYgVc85BizdQZzE?usp=share_link)
* - 23.03.2023
  - [3.2.1.d]()
  - [1.2.21.d]()
  - [1.3.24.d](https://test.pypi.org/project/pyCandleMAB/)
  - coming soon
  - coming soon
  - [2.1.0.d](https://drive.google.com/drive/folders/1GAVajHGv3E2Ztz91iTGgU-HBfVtfEJ5R?usp=share_link)
  - [2.1.1.d]()
```

### 23.03.2023 Devel notes:
- fixed skipping steps during output encoder calibration
- removed the calibration requirement in REPORT output encoder mode 
- added output encoder calibration mode (full / direction only) in STARTUP and MOTION mode (only for in-axis encoder)


## MD80 update tool - MAB CAN Flasher 

MAB_CAN_Flasher is a console application used to update the MD80 controller software using CANdle. When an update is released our engineers will prepare a MAB_CAN_Flasher application and send it to you. The MD80 firmware is contained in the MAB_CAN_Flasher application itself. To update the firmware connect the CANdle to the PC and the MD80 controller(s), and apply the power supply. You can make sure all the controllers are functional using MDtool and the [`mdtool ping all`](mdtool_ping) command before you proceed to update the controllers. After that, you are ready to run the update tool. We highly advise you to call `./MAB_CAN_Flasher --help` command on the first use to get acquainted with the available options.

### Example use cases 
`./MAB_CAN_Flasher --id 150 --baud 1M` - update the md80 controller with id equal to 150, which current CAN speed is 1M (the default CAN speed is 1M). Example output of this command for an ak80-64 motor:

```{figure} images/flashing1.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
`./MAB_CAN_Flasher --all -baud 1M` - update all available md80 controllers, whose current CAN speed is 1M (all controllers need to have the same speed). Example command output for two md80 controllers:

```{figure} images/flashing2.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In case the update process is interrupted and the md80 controller seems to be broken, you can disconnect the power supply, call:
```
./MAB_CAN_Flasher --id 9 --baud 1M --wait 
```
and while the command is running connect the power supply. This command will wait for the bootloader response and try to recover the firmware. If the flashing does not occur in the first power cycle you can repeat it until the bootloader is detected. An example output of the wait option for the ak80-64 motor is shown below:

```{figure} images/flashing3_wait.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## CANdle update tool - MAB USB Flasher

**MAB_USB_Flasher** is a console application used to update the CANdle software using USB bus. Currently, only updates over USB are supported (updates over SPI and UART are not supported). To update, first turn off all applications that may be using CANdle, and simply run `./MAB_USB_Flasher`.

```{figure} images/mab_usb_flasher.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

After a successful update, the CANdle device is ready. 


