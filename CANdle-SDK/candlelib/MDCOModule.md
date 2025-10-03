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

## Code Examples

All codes examples are available in python or c++

### [ID detection](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/mdco_example_id_motor_detection.cpp)

This is the simplest example to use and the recommended starting point.

The program displays the IDs of all motors connected to the CANdle via CANopen and makes the
drivers’ LEDs blink one by one, allowing the user to identify which motor corresponds to which ID.

### [Read & write register](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/mdco_example_read_write_register.cpp)

This example demonstrates the different ways to communicate with the MD80 using the CANopen
protocol.

- Send **SDO expedited transfer** requests to write and read values contained in most registers.
- Use **PDOs** for faster communication.
- Use **SDO segmented transfers** for registers larger than 4 bytes.
- Use **NMT (Network Management)** to easily manage the motor driver’s state machine (cf. CiA 301).

### [Speed loop](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/mdco_example_speed_loop.cpp)

This example shows how to run the motor using only **SDO expedited transfers**.

You must first configure the registers (Max current, Max torque, etc.). Once the registers are set,
you can create a loop to run your motor at the desired speed.

### [Impedance](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/mdco_example_impedance.cpp)

This example shows a use case of the MD module where we connect to the CANdle device, scan the CAN
network for MDs, set its mode to *impedance* (or any other available mode from the enum), and start
the control loop.

> **Warning**\
> Be careful using this mode, raw torque can be dangerous.

### [Heartbeat](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/mdco_example_heartbeat.cpp)

The **Heartbeat protocol** is used to monitor the nodes in the network and verify that they are
alive.\
A heartbeat producer (usually a slave device) periodically sends a message with its node ID
(`0x700 + node ID`).

This example shows how to use the heartbeat protocol:

1. The program first listens to the motor driver to check if it is sending heartbeats correctly.
1. Then, a second test is performed where the motor driver is set as a heartbeat listener and the
   CANdle sends it heartbeat messages. After a few iterations, the CANdle stops sending heartbeat
   messages, and the motor driver should switch to *stop mode* in the NMT state machine.
