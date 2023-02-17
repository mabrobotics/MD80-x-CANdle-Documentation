# Quick Start Guide

## Before first use

Here are some things to look out for while playing with the MD80 x CANdle ecosystem for the first time:
1. Always stay cautious when dealing with actuators. Even though they don't seem like it, they may severely hurt you when unintentional movement occurs. It’s recommended to fix the actuator to the workbench. 
2. Get accustomed to the [safety limits](safety_limits) section of this document. While developing your application be sure to keep the limits low, and only if you are sure you know what you're doing - increase the limits. 
3. We recommend using power supply sources that can work in two quadrants - meaning they can supply and dissipate some of the energy produced by the motor in case it works as a generator. Old trafo-based power supplies usually block current coming into the power supply, causing overvoltage events on the MD80s. The best choice is to use LiPo batteries or at least SMPS power supplies. 

## Video tutorials

Check out our video tutorials if you prefer this way of presentation:
1. Guide on how to set up a new MD80 to work with a motor of your choice: [MD80 x CANdle - Brushless Motor Setup Guide](https://www.youtube.com/watch?v=74zTUlJ2hmo&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=5)
2. Quick startup guide - watch when your motor is already configured and you'd like to try the examples: [MD80 x CANdle - Getting Started Tutorial](https://www.youtube.com/watch?v=bIZuhFpFtus&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=1) 
3. MDtool guide - a short introduction to MDtool and its basic commands (at this point the MDtool has evolved, however, the main principles are the same) [MD80 x CANdle - MDtool](https://www.youtube.com/watch?v=BrojxsU8oD8&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=2)
4. Motion modes guide - an introduction to motion modes available on MD80 [MD80 x CANdle - motion modes](https://www.youtube.com/watch?v=XnD8sG22zro&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=3)
5. ROS/ROS2 startup guide - an introduction to ROS/ROS2 drivers for MD80 [MD80 x CANdle - ROS/ROS2 startup guide](https://www.youtube.com/watch?v=6sLQNaJKuJY&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=4)

(configuring_MD80_for_new_motor)=
## Configuring the MD80 controller for a new motor

MDtool is used to set up a new motor to work with the MD80 controller. This approach simplifies the configuration process so that the end user can reconfigure the MD80 driver to work with almost any brushless motor. Below is a list of steps to configure the controller to work with a motor of your choice. 

```{warning}
Steps presented in this section are performed on HW 2.0 unit. These steps are universal between the controller hardware revisions, however, be sure to always check the [maximum ratings](ratings) before applying voltage to the controller. 
```

* First, make sure the MD80 controller can work with your motor. A vast majority of hobby motors will be suitable, although too big motors in terms of power and gimbal motors (high resistance ones) might not work as expected. Be sure to contact us before you proceed with a gimbal or high-power motor (over 2kW peak power). 

* Place the [diametrically magnetized magnet](https://www.supermagnete.de/eng/disc-magnets-neodymium/disc-magnet-10mm-5mm_S-10-05-DN) on the motor shaft and mount the MD80 controller firmly centered above the magnet. 

```{figure} images/magnet_encoder_asm.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

Magnet - encoder placement cross section
```

The optimal height between the magnet and the encoder IC is 1mm. The magnet and the encoder must be on the same rotation axis.

MD80 V2.0 is equipped with seven mounting holes. Please refer to the technical drawing below to find out the hole dimensions and their placement. The PCB 3D models for both V2.0, HW1.1, and HV1.3 can be found on the [downloads](hardware_downloads) page. 

```{figure} images/PCB_drawing.png
:class: bg-primary mb-1
:align: center
```

```{figure} images/mount_cross_section.png
:class: bg-primary mb-1
:align: center
```

```{warning}
Always make sure the head of the screw is inside the white hole outline. Otherwise, it may cause permanent damage to the controller when a short circuit occurs between the head screw and any of the copper planes. Using M2.5 DIN912 stainless socket screws is recommended.
```

```{figure} images/screw_placement.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* Solder the motor wires to the PCB making sure all the individual motor wires within a single phase are connected (in case the motor is wound with more than one wire on each phase). It is possible to solder the motor from the bottom, however, soldering the wires on the top is also acceptable. Make sure that the phase wires are connected only to their respective polygons. 

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

* Connect the power supply to the controller through the CANdle device as specified in [this section](hardware_setup). When powered the controller should blink shortly with a green LED once a second. If the red LED is fully on there are some errors that should be cleared after the calibration. 

```{warning}
<font color='red'>Always make sure that the polarity of the power supply is correct. MD80 controllers do not have reverse polarity protection so connecting the power supply in reverse polarity will cause permanent damage to the controller.</font> 
```
* Connect CANdle to the PC using a USB type-C cable. 

* Ensure you've got the latest [MDtool](https://github.com/mabrobotics/mdtool/releases). For the MDtool installation guide refer to the [MDtool](mdtool) section. 

* Please upgrade the setup software if any of your devices (MD80 or CANdle device) is older than the one from "latest" row in the [releases table](downloads). 

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

There, you will find a mdtool.ini file which contains factory settings and **should not** be modified, and a mdtool_motors directory, which holds all the motor configuration files you will work with. 

```{figure} images/mdtool_motors_dir.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

Feel free to add a new *.cfg file for your custom motors in there. Use the already existing files as a reference, especially the AK60-6.cfg which contains some additional comments.  


* Check if the MD80 controller can be discovered properly using the [`mdtool ping all`](mdtool_ping) command

```{figure} images/mdtool_ping_all.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* To setup the MD80 controller simply call [`mdtool setup motor <ID> <*.cfg>`](mdtool_setup_motor) where the ID is the ID that shows up after the [`mdtool ping`](mdtool_ping) command is called, and the *.cfg is one of the files existing in the mdtool_motors directory (press tab to list available config files). If anything fails during the process be sure to check your setup and try again. 

```{figure} images/mdtool_setup_motor_EX.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* Do not worry if at this point there are many errors after calling [`mdtool setup info <ID>`](mdtool_setup_info) command (like below). They should be cleared after a successful calibration.

```{figure} images/after_setup_EX8108.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* When succeeded, the motor is set up correctly and now’s the time to calibrate it using [`mdtool setup calibration <ID>`](mdtool_setup_calibration). Please follow the [calibration](calibration) guidelines for more information on the calibration process itself.

* After the calibration the motor should be ready to use - the best way to find out everything was completed without errors is to check the MD80 info using the [`mdtool setup info <ID>`](mdtool_setup_info). This command lists all the important parameters of the actuator. Errors are shown in red on the bottom if anything has failed during the process. If there are still errors after the calibration be sure to check out the error's description and try the recommended action to clear it [error section](error_codes). 

Correct after-calibration mdtool setup info command output may look like this:

```{figure} images/mdtool_setup_info_correct.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

Your actuator should be now ready to go! To make it move you can try the [`mdtool test move <ID> <pos>`](mdtool_test_move) command, or try the [CANdle lib](https://github.com/mabrobotics/candle) C++ or Python examples.