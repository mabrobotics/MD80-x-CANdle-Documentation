# CANopen

MD controllers provide support for the CANopen communication protocol in full compliance with the CiA 402 device profile, which defines standardized mechanisms for motion control, state management, and parameter handling. This section serves as a guide for configuring, controlling, and integrating MD controllers into a CANopen network.

The following chapters are included:

- [**Object Dictionary**](/CANopen/object_dictionary.md): Provides a complete description of all communication objects available in MD controllers.
 It contains detailed definitions of each entry, supported access types, default values, and the communication mechanisms used for data exchange within the CANopen framework. This section is essential for understanding how to configure and interact with the device programmatically.
- [**System Units**](/CANopen/units.md): Describes the SI units and their definitions used across MD CANopen devices, ensuring consistent interpretation of physical values such as position, velocity, and torque.
- [**Setting Up a New Motor**](/CANopen/setting_up_new_motor.md): Provides instructions for initializing and configuring a new motor with the MD controller, including recommended procedures for calibration and communication setup.

```{note}
Before working with CANopen, ensure that you have contacted MAB Robotics to obtain the appropriate firmware update.  
The standard MD flasher provides support only for the CANdle protocol, and CANopen functionality requires a dedicated firmware version.
```
