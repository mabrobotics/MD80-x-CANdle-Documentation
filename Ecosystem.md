# Ecosystem overview 

MD80 x CANdle is a system of brushless actuator controllers (MD80) and translator devices (CANdle) used for interfacing with them. MD80-based actuators can be used in advanced robotic projects like quadrupedal robots, robotic manipulators, exoskeletons, gimbals, and many more. 

## MD80

MD80 is a highly integrated brushless motor controller. It can be interfaced with a great variety of motors to turn them into advanced servo actuators. MD80 can work with both direct drive (no gearbox) and geared motors.

```{image} images/md80.jpg
:alt: MD80
:class: bg-primary mb-1
:width: 400px
:align: center
:class: no-scaled-link
```

## CANdle and CANdle HAT

CANdle (CAN + dongle) is a translator device between the host controller and the MD80 drivers. It is possible to interface CANdle with a regular PC over USB bus or CANdle HAT with SBCs (such as Raspberry PI) over USB, SPI or UART bus. 

```{image} images/candle.jpg
:alt: candle
:class: bg-primary mb-1
:width: 400px
:align: center
:class: no-scaled-link
```

## Safety information 

Even though the MD80 is a small brushless controller it can push a substantial amount of current through the motor windings. This means there are many hazards related to the high torques that the actuator is able to produce as well as elevated temperatures that may occur in close proximity to the MD80 controller or the motor. Always make sure the actuator is mounted firmly and does not pose a threat to its surroundings. Make sure the power supply current limits are set to low values (~1A) as a additional safety measure when you are unsure about the tested behavior of the system. 


## Operating conditions (MD80 and CANdle)

```{list-table}

* - Ambient Temperature (Operating)
  - 0°C - 40°C
* - Ambient Temperature (non-operating)
  - 0°C - 60°C
* - Maximum Humidity (Operating)
  - up to 95%, non-condensing at 40 ºC
* - Maximum Humidity (Non-Operating)
  - up to 95%, non-condensing at 60 ºC
* - Altitude (Operating)
  - -400 m to 2000 m
```
(hardware_setup)=
## Hardware setup 

CAN bus topology is a single-line network structure. A typical hardware connection/wiring scheme for CANdle x MD80 ecosystem is presented in the picture below:

```{image} images/hardware_setup.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
```{hint} In case you’d like to read more about the recommended lengths of the bus segments we suggest the elektormotus guide. 
```

The CAN bus termination is a single Molex connector with an embedded 120Ohm resistor for MD80 versions older than HW V2.0.For MD80 HW V2.0 and newer, the termination resistor is built-in and can be turned on and off using software (`mdtool config can` command) on each controlller. Termination should be always turned on or attached to the last controller in a string. 

```{figure} images/hardware_setup_candle.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

CANdle MD80-actuator string (USB bus)
```

```{figure} images/hardware_setup_candleHAT.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

CANdle HAT MD80-actuator string (SPI/UART bus using Raspberry Pi 4)
```

## Before first use

Here are some things to look out for while playing with the MD80 x CANdle ecosystem for the first time:
1. Always stay cautious when dealing with actuators. Even though they don't seem like it, they may severely hurt you when unintentional movement occurs. It’s recommended to fix the actuator to the workbench. 
2. Get accustomed to the [safety limits](safety_limits) section of this document. While developing your application be sure to keep the limits low, and only if you are sure you know what you're doing - increase the limits. 
3. We recommend using power supply sources that have the ability to work in two quadrants - meaning they can supply and dissipate some of the energy produced by the motor in case it works as a generator. Old trafo-based power supplies usually block current coming into the power supply, causing overvoltage events on the MD80s. The best choice is to use LiPo batteries or at least SMPS power supplies. 

## Quick startup guide

Please see the quick startup guide on our YouTube channel: [MD80 x CANdle - Getting Started Tutorial](https://www.youtube.com/watch?v=bIZuhFpFtus&t=1s)

## Configuring MD80 controller for a new motor

```{hint}
TL;DR this section is only essential when you want to configure a standalone controller with a motor or reconfigure a driver for a new motor. When purchasing an actuator assembly the actuator will come preconfigured. 
```

MDtool is used to set up a new motor to work with the MD80 controller. This approach simplifies the configuration process so that the end user can reconfigure the MD80 driver to work with almost any brushless motor. Below is a list of steps to configure the controller to work with a motor of your choice. 

```{warning}
Steps presented in this section are made on HW 2.0 unit. These steps are universal between the controller hardware revisions, however, be sure to always check the [maximum ratings](ratings) before you apply voltage to the controller. 
```

* First make sure the MD80 controller is able to work with your motor. A vast majority of hobby motors will be suitable, although too big motors in terms of power and gimbal motors (high resistance ones) might not work as expected. Be sure to contact us before you proceed with a gimbal or high-power motor (over 2kW peak power). 

* Place the [diametrically magnetized magnet](https://www.supermagnete.de/eng/disc-magnets-neodymium/disc-magnet-10mm-5mm_S-10-05-DN) on the motor shaft and mount the MD80 controller firmly centered above the magnet. 

```{figure} images/magnet_encoder_asm.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

Magnet - encoder placement cross section
```

The optimal height between the magnet and the encoder IC is 1mm. The magnet and the encoder must be on the same rotation axis.

MD80 HW2.0 is equipped with seven mounting holes. Please refer to the technical drawing below to find out the hole dimensions and their placement. The PCB 3D models for both HW2.0, HW1.1, and HV1.3 can be found @@@@here. 

```{figure} images/technical_drawing_md80.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{warning}
Always make sure the head of the screw is inside the white hole outline. Otherwise, it may cause permanent damage to the controller when a short circuit occurs between the head screw and any of the copper planes. Using M2.5 socket screws is recommended.
```

```{figure} images/screw_placement.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* Solder the motor wires to the PCB making sure all the individual motor wires within a single phase are connected together (in case the motor is wound with more than one wire on each phase). It is possible to solder the motor from the bottom, however, soldering the wires on the top is also acceptable. Make sure that the phase wires are connected only to their respective polygons. 

```{warning}
The order of the cables does not matter (does not change the rotation direction) as long as the order is not changed after the [calibration](calibration). Each modification in wire order should be followed by a full motor [calibration](calibration). 
```

```{figure} images/soldering.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
```{hint}
Sometimes it may be difficult due to the high-temperature enamel on the copper wires. In that case, try to apply solder at high temperatures using flux until the solder sticks to all wires nicely. 
```
```{warning}
Failing to complete this step may result in failed calibration or/and excessive cogging torque.  
```

* Connect the power supply to the controller through the CANdle device as specified in [this section](hardware_setup). When powered the controller should blink shortly with a green LED once a second. If the red LED is fully on there are some errors that should be cleared after the calibration. 

```{warning}
<font color='red'>Always make sure that the polarity of the power supply is correct. MD80 controllers do not have reverse polarity protection so connecting the power supply in reverse polarity will cause permanent damage to the controller.</font> 
```
* Connect CANdle to the PC using a USB type-C cable. 

* If the current version of your devices is older please always <b> upgrade the MD80 first, then update CANdle, and at the end update the MDtool </b>. For the MDtool installation guide refer to the MDtool section.

* Once installed and run the MDtool will create an MDtool directory in <b>~/.config</b>  directory. 

```{hint}
Press Ctrl+H to view the hidden folders (starting with a dot)
```
```{figure} images/mdtool_dir.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

There, you will find a mdtool.ini file which contains factory settings and should not be modified,  and a mdtool_motors directory, which holds all the motor configuration files you will work with. 

```{figure} images/mdtool_motors_dir.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

Feel free to add a new *.cfg file for your custom motors in there. Use the already existing files as a reference, especially the AK60-6.cfg which contains some additional comments. 


* Check if the MD80 controller can be discovered properly using the `mdtool ping all` command

```{figure} images/mdtool_ping_all.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* To setup the MD80 controller simply call `mdtool setup motor <ID> <*.cfg>` where the ID is the ID that shows up after the `mdtool ping` command is called, and the *.cfg is one of the files existing in the mdtool_motors directory (press tab to list available config files). If anything fails during the process be sure to check your setup and try again. 

```{figure} images/mdtool_setup_motor_EX.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* When succeeded, the motor is set up correctly and now’s the time to calibrate it using mdtool setup calibration <ID>. Please follow the [calibration](calibration) guidelines for more information.

* After the calibration the motor should be ready to use - the best way to find out everything was completed without errors is to check the MD80 info using the command: `mdtool setup info <ID>`. This command lists all the important parameters of the actuator. Errors are shown in red on the bottom if anything has failed during the process.

Correct after-calibration mdtool setup info command output may look like this:

```{figure} images/mdtool_setup_info_correct.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```