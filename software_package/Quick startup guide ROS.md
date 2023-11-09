# Quick startup guide - ROS

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

```{figure} ./images/candleros_usb8m.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In this example, we will be working with USB bus and 8M FDCAN baudrate.


## Adding drives 

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

```{figure} ./images/candle_ros_added_drives.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
According to the status messages we have added two MD80 actuators.

## Set mode
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


## Set Zero 
Often when starting, setting a current position to zero is desired. This can be accomplished with a call to `/zero_md80s` service.
```
rosservice call /zero_md80s "{drive_ids:[200, 800]}"
```

## Enabling/Disabling drives
Using services `/enable_md80s` and `/disable_md80s` the drives and the node publishers and subscribers can be enabled/disabled.

```{note}
After calling `/enable_md80s` service, no calls to services other than `/disable_md80s` should be done.
```

After enabling, the node will publish current joint states to `/joint_states` at a frequency dependent on a currently chosen communication bus and speed mode. Joint names are generated based on drive ID, for example, a drive with id 546 will be called `Joint 546`.

The node will also listen for the messages on topics for controlling the drives. All of the above topics are listened to all the time, but currently applied settings are dependent on the md80 mode set before enabling.
```
rosservice call /enable_md80s "{drive_ids:[200, 800]}"
```
```
rosservice call /disable_md80s "{drive_ids:[200, 800]}"
```

## Controlling drives
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

