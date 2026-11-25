# MD Node

The **MD ROS2 Node** provides operational control and telemetry for MAB Robotics MD drive controllers.  
It is intended as a *runtime* interface and **does not** perform device configuration.  
For configuration, use [**CANdleTool**](/CANdle-SDK/CANdleTool.md).

## MD Node Services

The following services provide runtime control over MD drive controllers.

| Service Name   | Description                         | Service Type                                                                                        |
| -------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| `/md/add_mds`  | Registers MD drives in the system   | [`candle_ros2/AddDevices`](https://github.com/mabrobotics/candle_ros2/blob/main/srv/AddDevices.srv) |
| `/md/enable`   | Enables selected registered drives  | [`candle_ros2/Generic`](https://github.com/mabrobotics/candle_ros2/blob/main/srv/Generic.srv)       |
| `/md/disable`  | Disables selected registered drives | [`candle_ros2/Generic`](https://github.com/mabrobotics/candle_ros2/blob/main/srv/Generic.srv)       |
| `/md/set_mode` | Changes the operating mode          | [`candle_ros2/SetMode`](https://github.com/mabrobotics/candle_ros2/blob/main/srv/SetMode.srv)       |
| `/md/zero`     | Performs a zeroing operation        | [`candle_ros2/Generic`](https://github.com/mabrobotics/candle_ros2/blob/main/srv/Generic.srv)       |

### Set Mode Service Details

The `/md/set_mode` service accepts requests of type `candle_ros2/SetMode`, field `mode` is a string that can take one of the following values:
- `"IDLE"`
- [`"IMPEDANCE"`](impedance-pd)
- [`"POSITION_PID"`](position-pid)
- [`"VELOCITY_PID"`](velocity-pid)
- [`"RAW_TORQUE"`](impedance-pd)

An unrecognized mode sets the drive to `IDLE` and returns `false` in the `success` field for that drive.

### Add MDs Service Details

Drives that are already registered are skipped by `/md/add_mds` and reported with `false` in the `success` field.

## MD Node Topics

### Subscribed Topics

| Topic Name              | Description                      | Message Type                                                                                                |
| :---------------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `/md/motion_command`    | General motion command input     | [`candle_ros2/MotionCmd`](https://github.com/mabrobotics/candle_ros2/blob/main/msg/MotionCmd.msg)           |
| `/md/position_command`  | Position PID controller commands | [`candle_ros2/PositionPidCmd`](https://github.com/mabrobotics/candle_ros2/blob/main/msg/PositionPidCmd.msg) |
| `/md/velocity_command`  | Velocity PID controller commands | [`candle_ros2/VelocityPidCmd`](https://github.com/mabrobotics/candle_ros2/blob/main/msg/VelocityPidCmd.msg) |
| `/md/impedance_command` | Impedance PD controller commands | [`candle_ros2/ImpedanceCmd`](https://github.com/mabrobotics/candle_ros2/blob/main/msg/ImpedanceCmd.msg)     |

### Published Topics

| Topic Name         | Description                            | Message Type             |
| ------------------ | -------------------------------------- | ------------------------ |
| `/md/joint_states` | Joint state feedback for all MD drives | `sensor_msgs/JointState` |

## Control Loop

The node runs a single control loop at **200 Hz** that handles all bus communication with registered drives. In each cycle it:

1. Sends the latest pending `/md/motion_command` targets (position, velocity, torque) to each drive. If several commands arrive between cycles, only the most recent one is sent.
2. Reads position, velocity and torque from each drive and publishes them on `/md/joint_states`. Drives that fail to respond are omitted from that cycle's message.
