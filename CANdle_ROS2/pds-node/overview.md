# PDS Node

The **PDS ROS2 Node** provides operational control and monitoring of MAB Robotics PDS (Power Delivery System) devices.  
It serves as a runtime interface for accessing PDS modules and **does not** perform device configuration.  
For configuration details, refer to the official PDS documentation.

Once a PDS device is registered, the node automatically scans all connected modules and creates module-specific handlers, topics, and services.

## PDS Base Services

The following services allow registering and managing PDS devices.

| Service Name        | Description                          | Service Type             |
| ------------------- | ------------------------------------ | ------------------------ |
| `/pds/add_pds`      | Registers a PDS devices by ID        | `candle_ros2/AddDevices` |
| `/pds/reboot_pds`   | Reboots the specified PDS devices    | `candle_ros2/Generic`    |
| `/pds/shutdown_pds` | Shuts down the specified PDS devices | `candle_ros2/Generic`    |

## PDS Module Topics and Services

The node publishes telemetry data for each detected module.  
Topics follow the naming scheme:

`/pds/id_<id>/<module>_<socket>`

Each module additionally exposes **enable/disable** services using the pattern:

`/pds/id_<id>/enable_<module>_<socket>`

`/pds/id_<id>/disable_<module>_<socket>`

---

### Example

For PDS **ID 100** with an **Isolated Converter** on socket **1**, the node will create:

**Topic**
- `/pds/id_100/ic_1`

**Services**
- `/pds/id_100/enable_ic_1`
- `/pds/id_100/disable_ic_1`

---

## Supported Modules

| Module Name        | Topic Pattern              | Description                                  |
| ------------------ | -------------------------- | -------------------------------------------- |
| Control Board      | `/pds/id_<id>/ctrl`        | System-level telemetry                       |
| Brake Resistor     | `/pds/id_<id>/br_<socket>` | Brake resistor status and temperature        |
| Isolated Converter | `/pds/id_<id>/ic_<socket>` | Output voltage, load current, safety data    |
| Power Stage        | `/pds/id_<id>/ps_<socket>` | Power delivery, current, energy, temperature |

Each PDS device always includes a **Control Board** (`ctrl`) module.

For detailed message structures of each module, see the dedicated module pages:

- [Control Board](modules/ctrl.md)
- [Brake Resistor](modules/br.md)
- [Isolated Converter](modules/ic.md)
- [Power Stage](modules/ps.md)
