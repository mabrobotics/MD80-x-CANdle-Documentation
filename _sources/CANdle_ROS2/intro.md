# CANdle ROS2

**CANdle ROS2** is a ROS 2 package that provides communication interfaces and runtime control nodes for **MD motor controllers** and the **PDS power delivery system** developed by **MAB Robotics**.

The package has been tested with the following ROS 2 distributions:

| Distribution | Version                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------- |
| **Lyrical**  | `main`                                                                                       |
| **Jazzy**    | `main`                                                                                       |
| **Humble**   | [`v2.1.2`](https://github.com/mabrobotics/candle_ros2/releases/tag/v2.1.2) (last supported)  |

```{note}
Later releases may still work on Humble, but they are not tested on it.
```

It is verified on Linux-based systems including **Ubuntu** and **Debian**.

Two main nodes are available:

- **`md_node`** — operational control of MD motor drives  
- **`pds_node`** — operational control and monitoring of PDS devices and their modules

---

## Features

### MD Node

- Control MD drive controllers
- Publish joint state data
- Accept **position**, **velocity**, **motion**, and **impedance** commands
- Provide services for:
  - enabling/disabling drives  
  - zeroing  
  - setting operating modes  
  - registering MD units  

### PDS Node

- Manage PDS devices and automatically expose per-module topics and services
- Monitor modules such as:
  - Control Board (`ctrl`)
  - Isolated Converter (`ic`)
  - Brake Resistor (`br`)
  - Power Stage (`ps`)
- Provide per-module enable/disable services

---

## Build & Run

For full build and usage instructions, refer to the **[repository README](https://github.com/mabrobotics/candle_ros2)**.