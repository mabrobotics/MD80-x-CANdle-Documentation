# MD Module

MD module is mostly a host to `MD` class which represents physical [MD](../../MD/intro) drivers.

MD module is intended to help user manage each MD in the CAN network via reads and writes to the
internal MD registers.

It can be included into your project via header-file:

```
#include "MD.hpp"
```

## Functionalities

Main features of MD module include:

- Creating MDs assigned to CANdle instance with unique IDs
- Managing internal registers of MDs
- Interpreting MD status bits
- Provides helper functions for managing MDs, for example: `getPosition()`, `zero()`,
  `setTargetPosition()`

## How-To

MD FDCAN protocol is based around accessing data on the drive via registers. Keeping that in mind,
MD Module functionality is based around reading and writing registers efficiently via CANdle.

### Basic Setup

Basically every program using CANdlelib and MD has the following workflow:

1. Create CANdle object
1. Create MD objects
1. Setup Motion Mode, Limits etc.
1. Enable MD
1. Enter a loop, with regular read/writes of registers.
1. Disable MD, free CANdle

Simple working example would look something like this:

```
#include "candle.hpp"
#include "MD.hpp"

int main()
{
    mab::Candle* candle = mab::attachCandle(mab::CANdleBaudrate_E::CAN_BAUD_1M, mab::candleTypes::busTypes_t::USB);

    mab::MD md(100, candle);    

    md.setMotionMode(mab::MdMode_E::IMPEDANCE);
    md.setImpedanceParams(0., 1.);
    md.setTargetVelocity(3.0);

    md.enable();

    mab::MDRegisters_S regs;
    for (u16 i = 0; i < 100; i++)
    {
        md.readRegisters(regs.mainEncoderPosition, regs.mainEncoderVelocity);
        usleep(100'000);
    }
    md.setTargetVelocity(0.);
    usleep(100'000);

    md.disable();  
    mab::detachCandle(candle);
    return EXIT_SUCCESS;
}
```

## Code Examples

### [Impedance](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/md_example_impedance.cpp)

This example shows use case of MD module in which we connect with CANdle device, scan the CAN
network in search of MDs, than we zero the drive, set its mode to impedance (can be any other mode
within the enum) and start the control loop.

```{note}
One of the important things to remember when using MD module is to be mindful of MDs internal timeout mechanic which after not receiving messages for some time, if not disabled, will set MD back to idle state. More information on that [here](watchdog).
```

### [Dual Channel](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/md_example_dual_chanel.cpp)

This example shows how to attach a unique CANdle to the MD device (in case two or more candles are
needed for latency improvements over CAN).

It also show how to manually connect the bus interface to CANdle.

### [Diagnostics](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/md_example_diagnostics.cpp)

This example shows how to read arbitrary registers during MD operation. List of available registers
can be found [here](registers).
