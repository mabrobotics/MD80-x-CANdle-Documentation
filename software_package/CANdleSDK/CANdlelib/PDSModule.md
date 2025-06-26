# PDS Module

PDS module is a host to the ``pds`` class which represents modular [Power Distribution System](pds) physical setup.

Due to modularity PDS is very customizable and examples only cover basic setups that need to be modified to the particular modules stack used by the user.

It can be used using the following header inclusion:
```
#include "pds.hpp"
```

## Functionalities
Main features of PDS module include:

- Creating PDS instances tied to particular CAN node ID and CANdle device.
- Manage parameters of each module via individual references in each pds object.
- Manage global modular properties like for example: ``shutdown()``, ``reboot()``,``getBusVoltage()``

## Examples

### [Basic](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_basic.cpp)

This example shows how to gather basic information via PDS properties like:

- Modules connected
- Status of the device
- Voltage and temperature
- STO status
- OT threshold
- Bus voltage

### [Battery monitor and configuration](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_battery_monitor_and_config_save.cpp)

This example shows how to interact with properties of the PDS and save the configuration to the persistent memory.

### [Submodules Access](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_submodules.cpp)

This example shows how to set parameters for specific modules. 

```{note}
This example is setup specific and must be adjusted to user's module stack.
```