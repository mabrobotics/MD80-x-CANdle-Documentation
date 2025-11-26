# Power Stage Module

**Topic:**

`/pds/id_<id>/ps_<socket_number>`

## Published Data

| Name                  | Type            | Description                                                                                  |
| --------------------- | --------------- | -------------------------------------------------------------------------------------------- |
| header                | std_msgs/Header | Standard ROS header                                                                          |
| enabled               | bool            | Indicates whether the module is enabled                                                      |
| brake_resistor_socket | uint8           | Associated brake resistor socket index (links this Power Stage to its brake resistor)        |
| trigger_voltage       | uint32          | Voltage threshold (mV) at which the associated brake resistor will be activated              |
| output_voltage        | uint32          | Output voltage of the module                                                                 |
| autostart             | bool            | Indicates whether the Power Stage autostart feature is enabled                               |
| load_current          | int32           | Output current drawn by devices connected to the module                                      |
| power                 | int32           | The momentary output power (mW)                                                              |
| energy                | uint32          | Accumulated delivered energy (mWh)                                                           |
| ocd_level             | uint32          | Over-current detection limit; exceeding this for longer than `ocd_delay` disables the module |
| ocd_delay             | uint32          | Time threshold (ms) before an over-current condition triggers module shutdown                |
| temperature           | float32         | Module temperature (°C)                                                                      |
| temperature_limit     | float32         | Temperature limit (°C) that disables the module when exceeded                                |
