(downloads)=
# Downloads

(hardware_downloads)=
## 3D models

Simplified (lightweight) 3D *.STEP models of MABRobotics products can be found [here](https://drive.google.com/drive/folders/1HMs3-LDdo9Fq8obLJfhrmhvfJQhLiTa4?usp=sharing).



## Software (devel)

Devel releases contain the latest features, however they might have some bugs:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Date</b></td>
			<td> <b>CANdle lib</b></td>
			<td> <b>MDtool</b></td>
     		<td> <b>pyCANdle</b></td>
			<td> <b>CANdle ROS</b></td>
			<td> <b>CANdle ROS2</b></td>
			<td> <b>CANdle device</b></td>
			<td> <b>MD80</b></td>
			<td> <b>Manual</b></td>
		</tr>
		<tr>
			<td style="color:green;"><b>05.08.2023 (latest)</b></td>
			<td><a href =  >3.3.1.d</a></td>
			<td><a href =  >1.4.0</a></td>
     		<td><a href =  >1.4.0</a></td>
			<td><a href =  >1.3.0</a></td>
			<td><a href =  >1.3.0</a></td>
			<td><a href =  >2.2.0</a></td>
			<td><a href =  >2.2.0</a></td>
			<td>this document</td>
		</tr>
	</tbody>
</table>

(software_downloads)=
## Software (stable)

Main stable releases:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Date</b></td>
			<td> <b>CANdle lib</b></td>
			<td> <b>MDtool</b></td>
     		<td> <b>pyCANdle</b></td>
			<td> <b>CANdle ROS</b></td>
			<td> <b>CANdle ROS2</b></td>
			<td> <b>CANdle device</b></td>
			<td> <b>MD80</b></td>
			<td> <b>Manual</b></td>
		</tr>
		<tr>
			<td>earlier</td>
			<td><a href = https://github.com/mabrobotics/candle/releases/tag/v3.0 > 3.0 </a></td>
			<td><a href = https://github.com/mabrobotics/mdtool/releases/tag/v1.1 > 1.1.0 </a></td>
      		<td><a href = https://pypi.org/project/pyCandleMAB/1.2.0/ >1.2.0</a></td>
			<td><a href = https://github.com/mabrobotics/candle_ros/releases/tag/v1.1 >1.1.0</a></td>
			<td><a href = https://github.com/mabrobotics/candle_ros2/releases/tag/v1.1>1.1.0</a></td>
			<td>1.4</td>
			<td>1.0</td>
			<td>1.0</td>
		</tr>
    	<tr>
			<td>12.12.2022</td>
			<td><a href = https://github.com/mabrobotics/candle/releases/tag/v3.1_hotfix >3.1</a></td>
			<td><a href = https://github.com/mabrobotics/mdtool/releases/tag/v1.2.1 >1.2.1</a></td>
      		<td><a href = https://pypi.org/project/pyCandleMAB/ >1.3.1</a></td>
			<td><a href = https://github.com/mabrobotics/candle_ros/releases/tag/v1.2 >1.2.0</a></td>
			<td><a href = https://github.com/mabrobotics/candle_ros2/releases/tag/v1.2 >1.2.0</a></td>
			<td><a href = https://drive.google.com/drive/folders/10wIX2uEaf42pkwGgW9fVAcGT7zrbptN9?usp=share_link >2.0</a></td>
			<td><a href = https://drive.google.com/drive/folders/10wIX2uEaf42pkwGgW9fVAcGT7zrbptN9?usp=share_link >2.0</a></td>
			<td>1.1.0</td>
		</tr>
		<tr>
			<td><b>05.04.2023</b></td>
			<td><a href = https://github.com/mabrobotics/candle/releases/tag/v3.3.0 >3.3.0</a></td>
			<td><a href = https://github.com/mabrobotics/mdtool/releases/tag/v1.3.0 >1.3.0</a></td>
     		<td><a href = https://pypi.org/project/pyCandleMAB/1.4.0/ >1.4.0</a></td>
			<td><a href = https://github.com/mabrobotics/candle_ros/releases/tag/v1.3.0>1.3.0</a></td>
			<td><a href = https://github.com/mabrobotics/candle_ros2/releases/tag/v1.3.0>1.3.0</a></td>
			<td><a href = https://drive.google.com/drive/folders/1KDQ-C75hCG3vG0TmMa5ZI3u2Hdv0R0jF?usp=share_link>2.2.0</a></td>
			<td><a href = https://drive.google.com/drive/folders/1fc-_x4e1BJuoYAXRuuwuZ3nlq07d4J5S?usp=share_link>2.2.0</a></td>
			<td><a href = https://drive.google.com/drive/folders/1mxcU9kXTvOaDagToViuQLT_6AWqyEF4M?usp=sharing>1.2.0</a></td>
		</tr>
	</tbody>
</table>
<p></p>

## MD80 update tool - MAB CAN Flasher 

MAB_CAN_Flasher is a console application used to update the MD80 controller software using CANdle. When an update is released our engineers will prepare a MAB_CAN_Flasher application and send it to you. The MD80 firmware is contained in the MAB_CAN_Flasher application itself. To update the firmware connect the CANdle to the PC and the MD80 controller(s), and apply the power supply. You can make sure all the controllers are functional using MDtool and the [`mdtool ping all`](mdtool_ping) command before you proceed to update the controllers. After that, you are ready to run the update tool. We highly advise you to call `./MAB_CAN_Flasher --help` command on the first use to get acquainted with the available options.

```{note}
Make sure the MAB_CAN_Flasher can be executed. If not use the `sudo chmod +x ./MAB_CAN_Flasher` command.
```

### Example use cases 
`./MAB_CAN_Flasher --id 150 --baud 1M` - update the md80 controller with id equal to 150, which current CAN speed is 1M (the default CAN speed is 1M). Example output of this command for an ak80-64 motor:

```{figure} images/flashing1.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
`./MAB_CAN_Flasher --all --baud 1M` - update all available md80 controllers, whose current CAN speed is 1M (all controllers need to have the same speed). Example command output for two md80 controllers:

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

```{note}
Make sure the MAB_USB_Flasher can be executed. If not use the `sudo chmod +x ./MAB_USB_Flasher` command.
```

```{figure} images/mab_usb_flasher.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

After a successful update, the CANdle device is ready. 


