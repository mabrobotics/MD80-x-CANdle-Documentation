# MD Node

The **MD ROS2 Node** provides operational control and telemetry for MAB Robotics MD drive controllers.  
It is intended as a *runtime* interface and **does not** perform device configuration.  
For configuration, use [**CANdleTool**](/CANdle-SDK/CANdleTool.md).

## MD Node Services

The following services provide runtime control over MD drive controllers.

| Service Name   | Description                         | Service Type             |
| -------------- | ----------------------------------- | ------------------------ |
| `/md/add_mds`  | Registers MD drives in the system   | `candle_ros2/AddDevices` |
| `/md/enable`   | Enables selected registered drives  | `candle_ros2/Generic`    |
| `/md/disable`  | Disables selected registered drives | `candle_ros2/Generic`    |
| `/md/set_mode` | Changes the operating mode          | `candle_ros2/SetMode`    |
| `/md/zero`     | Performs a zeroing operation        | `candle_ros2/Generic`    |

## MD Node Topics

### Subscribed Topics

| Topic Name              | Description                      | Message Type                 |
| :---------------------- | :------------------------------- | :--------------------------- |
| `/md/motion_command`    | General motion command input     | `candle_ros2/MotionCmd`      |
| `/md/position_command`  | Position PID controller commands | `candle_ros2/PositionPidCmd` |
| `/md/velocity_command`  | Velocity PID controller commands | `candle_ros2/VelocityPidCmd` |
| `/md/impedance_command` | Impedance PD controller commands | `candle_ros2/ImpedanceCmd`   |

### Published Topics

| Topic Name         | Description                            | Message Type             |
| ------------------ | -------------------------------------- | ------------------------ |
| `/md/joint_states` | Joint state feedback for all MD drives | `sensor_msgs/JointState` |


