(mdco)=

# MDCO Module

The **MDCO module** stands for *Motor Drive CANopen* and mainly hosts the `MDCO` class, which
represents physical [MDCO](mdco) drivers using the CANopen communication layer instead of CAN-FD.

The **CANdle** now supports communication with drivers through the **CANopen** protocol.\
This feature enables simpler and standardized integration into industrial or robotic systems that
use CANopen as their primary protocol.

It can be included in your project via the header file:

```cpp
#include "MDCO.hpp"
```

## Installation

Before using MDCO module you should migrate the motor driver in CANopen, cf:
https://mabrobotics.github.io/MD80-x-CANdle-Documentation/md_canopen/TransitionProcedure.html. If
you want to use candle features don't forget to update your candle with the latest version
available.

## Main Features

- **CANopen compatibility**: Supports the CiA 301 standard communication profile.
- **SDO/PDO exchanges**: Read and write driver object dictionary entries.
- **Node detection and management**: Automatic identification of devices on the CAN bus.
- **Synchronization**: Use of SYNC frames to align real-time communication.
- **NMT state management**: Transition between *Pre-operational*, *Operational*, and *Stopped*
  modes.
- **EMCY management**: Handling of emergency messages.
- **TIME-STAMP management**: Handling of messages containing the *TIME_OF_DAY* object (cf. CiA 301).
- **Heartbeat management**: Handling of heartbeat messages.


### [Speed loop](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/mdco_example_speed_loop.cpp)

This example shows how to run the motor using only **SDO expedited transfers**.

You must first configure the registers (Max current, Max torque, etc.). Once the registers are set,
you can create a loop to run your motor at the desired speed.

