# Quick start - ROS2

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

```{figure} ../images/candleros2_usb8m.png
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

```{figure} ../images/candle_ros2_added_drives.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

According to the status messages we have added two MD80 actuators.

## Set mode

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

## Set Zero 

Often when starting, setting a current position to zero is desired. This can be accomplished with a call to `/candle_ros2_node/zero_md80s` service.
```
ros2 service call /candle_ros2_node/zero_md80s candle_ros2/srv/GenericMd80Msg "{drive_ids:[200,800]}"
```

## Enabling/Disabling drives

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

## Controlling drives

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