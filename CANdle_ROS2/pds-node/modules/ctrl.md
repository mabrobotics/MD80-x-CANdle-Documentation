# Control Module

**Topic:**

`/pds/id_<id>/ctrl`

## Published Data

| Name                    | Type            | Description                                                                                 |
| ----------------------- | --------------- | ------------------------------------------------------------------------------------------- |
| header                  | std_msgs/Header | Standard ROS header                                                                         |
| bus_voltage             | uint32          | Input bus voltage                                                                           |
| battery_voltage_level_1 | uint32          | Battery level threshold: values ≤ this level represent **low**, above represent **medium**  |
| battery_voltage_level_2 | uint32          | Battery level threshold: values ≤ this level represent **medium**, above represent **high** |
| brake_trigger_voltage   | uint32          | Voltage threshold (mV) at which the brake resistor will be activated                        |
| temperature             | float32         | Module temperature (°C)                                                                     |
| temperature_limit       | float32         | Temperature limit (°C) that disables the module when exceeded                               |

