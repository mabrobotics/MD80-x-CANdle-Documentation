# Software Pack

The MD80 x CANdle software pack consists of a few modules. All of them are based on the main CANdle C++ library which takes care of the low-level communication and provides API for high-level software. 

## CANdle C++ library 

CANdle C++ library is the base module of software that all other modules are based on. It takes care of low-level communication between the host and the MD80 controllers. Using the CANdle C++ library directly is the best option to reach the full performance of the drives when it comes to communication frequency between the host and MD80 controllers. 

### Quick start

The quick startup guide includes cloning the repo, building and running the examples. First, you should clone the candle repo from the MAB Robotics GitHub page to your local machine. Then, make sure you're in the main directory candle/ and run the following commands:
```
mkdir build
cd build 
cmake ..
make 
```
starting from the top one these commands: create a build directory, go into the build directory, generate makefiles using CMake and compile the source code using make. After executing these commands you should be able to see the compiled examples in the candle/build/ directory. To run one of them use the following command:
```
./exampleX 
```
where X is the number of the example. 

### Building as a static lib

Candle C++ library can be built as a static or shared object library. In the quick startup guide, we used the default settings, thus the library was compiled to a shared object file. In case you’d like to build it for a static lib you should pass additional arguments to the cmake .. command:
```
cmake .. -DCANDLE_BUILD_STATIC=TRUE
```
After executing this command you should be able to see the following CMake output:

```{figure} images/candle_build_static.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In case you’d like to go back to shared lib just call: 
```
cmake .. -DCANDLE_BUILD_STATIC=FALSE
```
or delete the build directory contents and call cmake .. again (the default library type is shared). This is what the cmake output looks like when reconfiguring for shared lib: 
```{figure} images/candle_build_shared.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

### CANdle Python library

CANdle Python library is a translated version of the C++ library using pybind11. The package can be found on PyPi: https://pypi.org/project/pyCandleMAB/ and installed using pip:
```
sudo python3 -m pip install pyCandleMAB
```
It can be used to quickly start playing with the actuators, without the need to build the C++ software pack. Example usage of Python examples is shown in the [getting started guide](https://www.youtube.com/watch?v=bIZuhFpFtus&t=1s). To achieve the best performance in low latency systems we advise using the C++ libraries directly.

```{note}
We distribute the binaries as well as sources - in case your platform is not recognized with the available binaries pip will try to build and install the library from the source.
```

```{warning}
Currently only C++ library allows reading and modifying MD80 registers from the script level.
```
(mdtool)=
## MDtool

**MDtool** is a console application for configuring and performing basic diagnostics on MD80 drives via CANdle. The application is available as a standalone executable and as a .deb package. The program is designed as a complementary tool for APIs, reducing the overhead when setting up the drives for the first time or reconfiguring them. It uses the CANdle C++ library on its backend.

### Installation

The easiest way to install the MDtool is to select the appropriate *.deb package from the [MDtool GitHub repo releases page](https://github.com/mabrobotics/mdtool/releases) (compliant with your system’s architecture). To install after the download simply call:
```
sudo apt install ./mdtool_xx-x_xx.deb
```
After the install please make sure the current user is added to the dialout group using the command:
```
sudo adduser <current user> dialout 
```
if it wasn't, please reboot the PC
```
sudo reboot
```
It is also recommended to install the setserial package which allows for higher communication speeds:
```
sudo apt install setserial
```
Be sure to call 
```
mdtool bus <SPI/UART/USB>
```
to configure MDtool for the desired communication bus before first use, if you're using CANdle HAT and SPI or UART bus. 

```{note}
For the command prompt to work after the installation you have to restart the terminal window
```

### Commands

#### `mdtool bus <bus> <device>`

MDtool is able to work with CANdle and CANdle HAT. This is why before the first use it has to be configured for a particular communication bus. Use the bus command to set it to USB, SPI, or UART, based on which device you own. The default bus setting is USB. You don't have to repeat this setting unless you want to change the current communication bus. The device parameter is optional and can be used in case of the UART and SPI bus, if the default device (/dev/spidev0.0 in case of SPI or /dev/ttyAMA0 in case of UART) is not suitable for your application. 

#### `mdtool ping <baud>`

MDtool is able to discover the drives that are connected to the CAN bus. You can ping the drives at a specific speed (1M/2M/5M/8M) or just use the ‘all’ keyword for pinging all speeds in one go. 

```{note}
CANdle does not support working with drives configured with different CAN speeds on the same CAN bus – please make sure when “mdtool ping all” command is executed, all discovered drives lie in a single speed category.
```

#### `mdtool config zero <ID>`

This command sets the current motor position to zero - from the moment this command is called all encoder measurements are referenced from the current position. 

```{note}
This setting has to be saved to be preserved after power down! Please see the config save <ID> command.
```

#### `mdtool config can <current ID> <new ID> <baud> <watchdog period [ms]> <termination>`

This command is used to change MD80’s parameters such as CAN ID, CAN speed, and CAN watchdog.
* CAN IDs should be in range <10:2000>
* Baud should be one of the available speeds (1M/2M/5M/8M)
* Watchdog period should be in range <1:2000> ms, 0 disables the watchdog. For more information on CAN watchdog please refer to section FDCAN Watchdog Timer.
* Termination should be either 1 to turn the termination on or 0 to turn the termination off. 

```{warning}
Software-controlled termination is available since version HW V2.0. It is an optional setting - when not typed in the command this setting will default to zero (off).
```
```{note}
This setting has to be saved to be preserved after power down! Please see the mdtool config save <ID> command.
```

#### `mdtool config current <ID> <current>`

This command is used to set the maximum phase current that is allowed to flow through the motor when high torques are commanded. By default, the maximum current is set to a rather low value that will not lead to motor or driver burnout. However, this also limits the motor's maximum torque capabilities. Using the config current command one can increase the maximum current. The absolute maximum value is 40 A. 

```{warning}
The guarantee does not include burnout actions due to too high current settings. For max continuous driver current please refer to the general parameters and safety limits sections.
```
```{note}
This setting has to be saved to be preserved after power down! Please see the config save <ID> command.
```

#### `mdtool config bandwidth <ID> <torque bandwidth in Hz>`

This command can be used to change the torque bandwidth without recalibrating the actuator. For more information on the torque bandwidth please see the section about [calibration](calibration). 

```{note}
This setting has to be saved to be preserved after power down! Please see the config save <ID> command.
```

#### `mdtool config save <ID>`

For the config commands to take action after the next power cycle a save command has to be executed. This command saves the current drive’s settings to the non-volatile FLASH memory.

#### `mdtool setup calibration <ID>`

This command runs the basic calibration routine. During calibration, the drive has to be able to rotate freely and the power supply should be able to deliver at least 1A of current. For more detail on the calibration process please refer to the calibration section.

#### `mdtool setup calibration_out <ID>`

This command runs the output encoder calibration routine. During output encoder calibration, the drive has to be able to rotate for at least two full rotations of the output shaft and the power supply should be able to deliver at least 1A of current. For more detail on the calibration process please refer to the [output encoder calibration](output_encoder_calibration) section.

#### `mdtool setup motor <*.cfg> <ID>` 

This command is used to write a new motor config. For more information please see the section Configuring MD80 controller for a new motor.

#### `mdtool setup info <ID>`
This command is used to read the motor internal parameters. An example command output might look like this:

```{figure} images/mdtool_setup_info_allok.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
Reading the errors is the easiest way of debugging possible problems with the drive. For errors description please visit the [error codes](error_codes) section. 

#### `mdtool blink <ID>`
This command is mostly used to find an MD80 drive on a long CAN bus using its ID – the command makes the drive flash its onboard LEDs for easy identification.

#### `mdtool test move <ID> <position>`
This command is used to test the actuator movement in impedance mode. It helps to assess if the calibration was successful and if there are no issues visible to the naked eye. The position argument is always the amount of position for the motor to be moved from the current position. 

#### `mdtool test latency <baudrate>`
This command is used to test the PC<>CANdle communication speed which greatly affects the PC<>MD80 communication speed. The higher the measured frequency the better. 

#### `mdtool test encoder <type> <ID>`
This command is used to check how accurate a praticular encoder was calibrated. The <type> argument can be either "main" for onboard encoder, or <output> for output encoder. This command runs a routine that makes one full rotation of the shaft (either motor or output shaft, depending on the chosen encoder type) and after completing fills up the max, min and standard deviation errors that can be accessed using the `mdtool setup info` command. 

#### `mdtool encoder <ID>`
This command is useful when one wants to measure the position of the actuator in the current setup (without writing a custom script). After the command is executed the screen shows the current position of the actuator’s shaft and it does so until you press Ctrl + C. 

## CANdle ROS/ROS2 nodes

```{hint}
TL;DR: [MD80 x CANdle - ROS/ROS2 startup guide](https://www.youtube.com/watch?v=6sLQNaJKuJY&t=3s)
```

While C++ API is the most flexible way of interfacing with CANdle/MD80, ROS/ROS2 APIs are also available. These have been designed as standalone C++ nodes that use the CANdle library on the backend. The nodes are designed to be used with already configured drives, thus functions such as setting FDCAN parameters are unavailable via ROS/2 API. We recommend configuring all drives first using MDtool or C++/Python API.

Nodes use ROS/2 services to perform initialization and enable/disable the drives.
The initialization services available are:
```
/add_md80s
/zero_md80s
/set_mode_md80s
```

There are also two additional services for enabling/disabling the drives:
```
/enable_md80s
/disable_md80s
```

Once the drives are enabled via `enable_md80s` service, the nodes will ignore all calls to services other than `disable_md80s`.
When enabled, communication switches from service-based to topic-based. The nodes will publish to the topic:
```
/md80/joint_states
```
And will subscribe to topics:
```
/md80/motion_command
/md80/impedance_command
/md80/velocity_pid_command
/md80/position_pid_command
```

## Quick startup guide - ROS

Let’s run a simple example of the candle ROS node. In order to run the node, clone it into your local ROS workspace in the src folder. After that, build it with 'catkin' and run using the 'rosrun' command. Be sure to source your workspace with source devel/setup.sh prior to running the package, and in each new terminal window you're going to send commands related to the node. 

First, start the roscore with the roscore command. Then run the node with arguments that fit your MD80 x CANdle setup. The general syntax is:
```
rosrun candle_ros candle_ros_node <BUS> <FDCAN baud> 
```

for more information on how to run the node you can call:
```
rosrun candle_ros candle_ros_node --help 
```

Example output from the terminal after launching the node:

```{figure} images/candleros_usb8m.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In this example, we will be working with USB bus and 8M FDCAN baudrate.


### Adding drives 

Firstly, the node should be informed which drives should be present on the FDCAN bus. This can be done via `/add_md80s service`.
For example:
```
rosservice call /add_md80s "drive_ids: [200, 800]"
```
Should produce the following output:
```
drives_success: [True, True]
total_number_of_drives: 2
```
informing, that both drives (ids: 200 and 800), have been successfully contacted, and were added to the node's drives list.
You can also look for status messages in the terminal window where the node was started:

```{figure} images/candle_ros_added_drives.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
According to the status messages we have added two MD80 actuators.

### Set mode
Next the desired control mode should be selected. This is accomplished with `/set_mode_md80s` service.
For example:
```
rosservice call /set_mode_md80s "{drive_ids: [200, 800], mode:["IMPEDANCE", "IMPEDANCE"]}"
```
Should produce:
```
drives_success: [True, True]
```
Informing that for both drives mode has been set correctly.


### Set Zero 
Often when starting, setting a current position to zero is desired. This can be accomplished with a call to `/zero_md80s service`.
```
rosservice call /zero_md80s "{drive_ids:[200, 800]}"
```

### Enabling/Disabling drives
Using services `/enable_md80s` and `/disable_md80s` the drives and the node publishers and subscribers can be enabled/disabled.

```{note}
After calling /enable_md80s service, no calls to services other than /disable_md80s should be done.
```

After enabling, the node will publish current joint states to `/joint_states` at a frequency dependent on a currently chosen communication bus and speed mode. Joint names are generated based on drive ID, for example, a drive with id 546 will be called `Joint 546`.

The node will also listen for the messages on topics for controlling the drives. All of the above topics are listened to all the time, but currently applied settings are dependent on the md80 mode set before enabling.
```
rosservice call /enable_md80s "{drive_ids:[200, 800]}"
```
```
rosservice call /disable_md80s "{drive_ids:[200, 800]}"
```

### Controlling drives
Controlling the drives is done via the four topics listed above. For commands to be viable, all fields of each message must be filled properly. For example, to set up custom gains for IMPEDANCE mode use:
```
rostopic pub /md80/impedance_command candle_ros/ImpedanceCommand "{drive_ids:[200, 800], kp:[0.25, 1.0], kd:[0.1, 0.05], max_output:[2.0, 2.0]}"
```

Example set up of custom gains for POSITION PID mode:
```
rostopic pub /md80/position_command candle_ros/PositionPidCommand "{drive_ids: [200, 800], position_pid: [{kp: 40.0, ki: 0.5, kd: 0.0, i_windup: 10, max_output: 3.0},{kp: 20.0, ki: 0.5, kd: 0.0, i_windup: 10, max_output: 3.0}], velocity_pid: [{kp: 0.2, ki: 0.3, kd: 0.0, i_windup: 2.0, max_output: 2.0}, {kp: 0.1, ki: 0.1, kd: 0.0, i_windup: 1, max_output: 2.0}]}" 
```

Example set up of custom gains for VELOCITY PID mode:
```
rostopic pub /md80/velocity_command candle_ros/VelocityPidCommand "{drive_ids: [200, 800], velocity_pid: [{kp: 0.2, ki: 0.3, kd: 0.0, i_windup: 2.0, max_output: 2.0}, {kp: 0.1, ki: 0.1, kd: 0.0, i_windup: 1, max_output: 2.0}]}"
```

Setting desired position, velocity, and torque is done via /md80/motion_command topic. Note that for it to take effect, all fields in the message should be correctly filled. For example, to move the drives in impedance mode, it is possible to use the following command
```
rostopic pub /md80/motion_command candle_ros/MotionCommand "{drive_ids:[81,97], target_position:[3.0, -3.0], target_velocity:[0.0, 0.0], target_torque:[0, 0]}" 
```


## Quick start - ROS2

Let’s run a simple example of the candle ROS2 node. In order to run the node, clone it into your local ROS2 workspace. After that, build it with `colcon` and run using the `ros2 run` command. Be sure to source your workspace with `source install/setup.bash` prior to running the package, and in each new terminal window you're going to send commands related to the node. 

First, let’s run the node with arguments that fit your MD80 x CANdle setup. The general syntax is:
```
ros2 run candle_ros2 candle_ros2_node <BUS> <FDCAN baud> 
```
for more information on how to run the node you can call
```
ros2 run candle_ros2 candle_ros2_node --help. 
```

Example output from the terminal after launching the node:

```{figure} images/candleros2_usb8m.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
In this example, we will be working with a USB bus and 8M FDCAN baudrate.

Adding drives 
Firstly, the node should be informed which drives should be present on the FDCAN bus. This can be done via `/candle_ros2_node/add_md80s` service. Note: Do not forget to source your ros2 workspace in new terminal window
For example
```
ros2 service call /candle_ros2_node/add_md80s candle_ros2/srv/AddMd80s "{drive_ids: [200,800]}"
```
Should produce the following output:
response:
```
candle_ros2.srv.AddMd80s_Response(drives_success=[True, True], total_number_of_drives=2)
```
informing, that both drives (ids: 200 and 800), have been successfully contacted, and were added to the node's drives list.
You can also look for status messages in the terminal window where the node was started:

```{figure} images/candle_ros2_added_drives.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

According to the status messages we have added two MD80 actuators.

### Set mode

Next the desired control mode should be selected. This is accomplished with /candle_ros2_node/set_mode_md80s service.

For example:
```
ros2 service call /candle_ros2_node/set_mode_md80s candle_ros2/srv/SetModeMd80s "{drive_ids: [200, 800], mode:["IMPEDANCE", "IMPEDANCE"]}"
```
Should produce:
```
response:
candle_ros2.srv.SetModeMd80s_Response(drives_success=[True, True])
```
Informing that for both drives mode has been set correctly.

### Set Zero 

Often when starting, setting a current position to zero is desired. This can be accomplished with a call to `/candle_ros2_node/zero_md80s` service.
```
ros2 service call /candle_ros2_node/zero_md80s candle_ros2/srv/GenericMd80Msg "{drive_ids:[200,800]}"
```

### Enabling/Disabling drives

Using services `/candle_ros2_node/enable_md80s` and `/candle_ros2_node/disable_md80s` the drives and the node publishers and subscribers can be enabled/disabled.

```{note}
After calling `/candle_ros2_node/enable_md80s` service, no calls to services other than `/candle_ros2_node/disable_md80s` should be done.
```

After enabling, the node will publish current joint states to `/joint_states` at a frequency dependent on a currently chosen communication bus and speed mode. Joint names are generated based on drivie ID, for example, drive with id 546 will be called `Joint 546`.

The node will also listen for the messages on topics for controlling the drives. All of the above topics are listened to all the time, but currently applied settings are dependent on the md80 mode set before enabling.
```
ros2 service call /candle_ros2_node/enable_md80s candle_ros2/srv/GenericMd80Msg "{drive_ids:[200, 800]}"
```
```
ros2 service call /candle_ros2_node/disable_md80s candle_ros2/srv/GenericMd80Msg "{drive_ids:[200, 800]}"
```

### Controlling drives

Controlling the drives is done via the four topics listed above. For commands to be viable, all field of each message must be filled properly. For example, to set up custom gains for IMPEDANCE mode use:
```
ros2 topic pub /md80/impedance_command candle_ros2/msg/ImpedanceCommand "{drive_ids: [200, 800], kp: [1.0,1.0]], kd: [0.001,0.001], max_output: [1.0, 1.0]}"
```

Example set up of custom gains for POSITION PID mode:
```
ros2 topic pub /md80/position_pid_command candle_ros2/msg/PositionPidCommand "{drive_ids: [150, 350], position_pid: [{kp: 40.0, ki: 0.5, kd: 0.0, i_windup: 10, max_output: 3.0},{kp: 20.0, ki: 0.5, kd: 0.0, i_windup: 10, max_output: 3.0}], velocity_pid: [{kp: 0.2, ki: 0.3, kd: 0.0, i_windup: 2.0, max_output: 2.0}, {kp: 0.1, ki: 0.1, kd: 0.0, i_windup: 1, max_output: 2.0}]}" 
```

Example set up of custom gains for VELOCITY PID mode:
```
ros2 topic pub /md80/velocity_pid_command candle_ros2/msg/VelocityPidCommand "{drive_ids: [200, 800], velocity_pid: [{kp: 0.2, ki: 0.3, kd: 0.0, i_windup: 2.0, max_output: 2.0}, {kp: 0.1, ki: 0.1, kd: 0.0, i_windup: 1, max_output: 2.0}]}"
```

Setting desired position, velocity, and torque is done via `/md80/motion_command` topic. Note that for it to take effect, all fields in the message should be correctly filled. For example, to move the drives in impedance mode, it is possible to use the following command
```
ros2 topic pub /md80/motion_command candle_ros2/MotionCommand "{drive_ids: [200, 800], target_position: [3.0, 3.0], target_velocity: [0.0, 0.0], target_torque: [0.0, 0.0]}"
```

## MD80 update tool - MAB CAN Flasher 

MAB_CAN_Flasher is a console application used to update the MD80 controller software using CANdle. When an update is released our engineers will prepare a MAB_CAN_Flasher application and send it to you. The MD80 firmware is contained in the MAB_CAN_Flasher application itself. To update the firmware connect the CANdle to the PC and the MD80 controller(s), and apply the power supply. You can make sure all the controllers are functional using MDtool and the `mdtool ping all` command before you proceed to update the controllers. After that, you are ready to run the update tool. We highly advise you to call `./MAB_CAN_Flasher -help` command on the first use to get acquainted with the available options.

### Example use cases 
`./MAB_CAN_Flasher --id 150 --baud 1M` - update the md80 controller with id equal to 150, which current CAN speed is 1M (the default CAN speed is 1M). Example output of this command for an ak80-64 motor:

```{figure} images/flashing1.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
`./MAB_CAN_Flasher --all -baud 1M` - update all available md80 controllers, whose current CAN speed is 1M (all controllers need to have the same speed). Example command output for two md80 controllers:

```{figure} images/flashing2.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In case the update process is interrupted and the md80 controller seems to be broken, you can disconnect the power supply, call:
```
./MAB_CAN_Flasher --id 9 --baud 1M --wait 
```
and while the command is running connect the power supply. This command will wait for the bootloader response and try to recover the firmware. If the flashing does not occur in the first power cycle you can repeat it until the bootloader is detected. The example output of the wait option for the ak80-64 motor is shown below:

```{figure} images/flashing3_wait.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## CANdle update tool - MAB USB Flasher

**MAB_USB_Flasher** is a console application used to update the CANdle software using USB bus. Currently, only updates over USB are supported (updates over SPI and UART are not supported). When an update is released we will prepare a MAB_USB_Flasher application and send it to you. To update, first turn off all applications that may be using CANdle, and simply run `./MAB_USB_Flasher`.

```{figure} images/mab_usb_flasher.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

After a successful update, the CANdle device is ready. 
