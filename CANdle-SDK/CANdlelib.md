# CANdlelib

CANdlelib is a library written in C++ to provide the user with API for using MAB products.

## Main Features

- Provides API for communicating with [CANdle](/CANdle/intro.md), and through it with:
  - [MD - Motor controllers](/MD/intro.md)
  - [PDS - Power Distribution Systems](/PDS/intro)
- Provides helper functions for most of the tasks tied to motor control in robotics and automation.
- Provides usage examples for the devices.

[CANdle](/CANdle/intro) and [CANdle HAT](/CANdle/intro) devices come equipped with both **SPI** and
**USB** interfaces.

```{note}
Using CANdlelib is a recommended way of starting development and integrating MAB products into the
system. However we also provide support for clients that want to customize their main controllers.

Our [MAB FDCAN protocol](/MD/Communication/fdcan) is fully open-source and documented, to allow
connecting to MD and PDS from any FDCAN capable host controller.
```

## Architecture

Access to devices is split into corresponding modules:

- [CANdle Module](candlelib/CANdleModule.md)
- [MD Module](candlelib/MDModule.md)
- [PDS Module](candlelib/PDSModule.md)

Each module, groups functions and helper-wrapper methods for interacting with devices.
