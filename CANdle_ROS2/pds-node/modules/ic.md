# Isolated Converter Module

**Topic:**

`/pds/id_<id>/ic_<socket_number>`

## Published Data

| Name              | Type            | Description                                                                                  |
| ----------------- | --------------- | -------------------------------------------------------------------------------------------- |
| header            | std_msgs/Header | Standard ROS header                                                                          |
| enabled           | bool            | Indicates whether the module is enabled                                                      |
| output_voltage    | uint32          | Output voltage of the DC/DC converter                                                        |
| load_current      | int32           | Output current drawn by devices connected to the module                                      |
| ocd_level         | uint32          | Over-current detection limit; exceeding this for longer than `ocd_delay` disables the module |
| ocd_delay         | uint32          | Time threshold (ms) before an over-current condition triggers module shutdown                |
| temperature       | float32         | Module temperature (°C)                                                                      |
| temperature_limit | float32         | Temperature limit (°C) that disables the module when exceeded                                |

