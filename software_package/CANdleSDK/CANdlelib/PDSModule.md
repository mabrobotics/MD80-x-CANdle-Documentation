# PDS Module

PDS module is a host to the ``pds`` class which represents modular [Power Distribution System](pds) physical setup.

Due to modularity PDS is very customizable and examples only cover basic setups that need to be modified to the particular modules stack used by the user.

It can be used using the following header inclusion:
```
#include "pds.hpp"
```

## Functionalities
Main features of PDS module include:

- Creating PDS instances tied to particular CAN node ID and CANdle device
- Manage parameters of each module via individual references in each pds object
- Manage global modular properties like for example: ``shutdown()``, ``reboot()``,``getBusVoltage()``

## Examples

### [Ping and status](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_ping_and_status.cpp)

This example shows how to gather basic system diagnostics and configuration from the PDS.

- Firmware and hardware version
- Connected submodules
- Over-temperature status
- Device status (enabled, faults, STO, etc.)
- Shutdown time
- Braking resistor configuration
- Bus voltage and battery levels


### [Power stage and braking resistor](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_power_stage.cpp)

This example demonstrates how to configure and monitor a **Power Stage** and **Braking Resistor** using the PDS.

- Configure: Overcurrent Detection (OCD) limit and delay, temperature limits, braking resistor trigger voltage
- Bind a Braking resistor to the power stage
- Read runtime status: voltage, current, temperature, and protection states

```{note}
- Ensure correct socket assignments (`SOCKET_1`, `SOCKET_3`) match your physical wiring.
- You must call `powerStage->enable()` before attempting to monitor runtime data.
```

### [Isolated converter](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_isolated_converter.cpp)

This example demonstrates how to configure and monitor an **Isolated Converter** using the PDS.

- Configure: temperature limit, OCD level
- Read runtime status: Output voltage, load current, temperature, OCD configuration

```{note}
- All values are converted to human-readable units (V, A, °C) for logging.
- Socket index used: `SOCKET_2`
```

### [Braking resistor](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/pds_example_braking_resistor.cpp)

This example demonstrates how to configure and monitor a **Braking Resistor** connected to the PDS.

- Configure: temperature limit
- Read runtime status: enabled state, current temperature, configured temperature limit

```{note}
- The brake resistor is **normally enabled automatically** by the **Power Stage** module.
- This example focuses on standalone monitoring and configuration of the resistor.
- Socket index used: `SOCKET_3`
```