# MD Module

MD module is mostly a host to ``MD`` class which represents physical [MD](md) drivers.

MD module is intended to help user manage each MD in the CAN network via reads and writes to the internal MD registers.

It can be included into your project via header-file:
```
#include "MD.hpp"
```

## Functionalities

Main features of MD module include:
- Creating MDs assigned to CANdle instance with unique IDs
- Managing internal registers of MDs
- Interpreting MD status bits
- Provides helper functions for managing MDs, for example: ``getPosition()``, ``zero()``, ``setTargetPosition()``

## Code Examples

### [Impedance](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/md_example_impedance.cpp)

This example shows use case of MD module in which we connect with CANdle device, scan the CAN network in search of MDs, than we zero the drive, set its mode to impedance (can be any other mode within the enum) and start the control loop.

```{note}
One of the important things to remember when using MD module is to be mindful of MDs internal timeout mechanic which after not receiving messages for some time, if not disabled, will set MD back to idle state. More information on that [here](watchdog).
```

### [Dual Channel](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/md_example_dual_chanel.cpp)

This example shows how to attach a unique CANdle to the MD device (in case two or more candles are needed for latency improvements over CAN).

It also show how to manually connect the bus interface to CANdle.

### [Diagnostics](https://github.com/mabrobotics/CANdle-SDK/blob/devel/examples/cpp/md_example_diagnostics.cpp)

This example shows how to read arbitrary registers during MD operation. List of available registers can be found [here](registers).