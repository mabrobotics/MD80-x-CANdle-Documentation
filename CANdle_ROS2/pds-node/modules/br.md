# Brake Resistor Module

**Topic:**

`/pds/id_<id>/br_<socket_number>`

**Type:**

[`candle_ros2/BrakeResistorData`](https://github.com/mabrobotics/candle_ros2/blob/main/msg/BrakeResistorData.msg)

## Published Data

| Name              | Type            | Description                                                   |
| ----------------- | --------------- | ------------------------------------------------------------- |
| header            | std_msgs/Header | Standard ROS header                                           |
| enabled           | bool            | Indicates whether the module is enabled                       |
| temperature       | float32         | Module temperature (°C)                                       |
| temperature_limit | float32         | Temperature limit (°C) that disables the module when exceeded |

