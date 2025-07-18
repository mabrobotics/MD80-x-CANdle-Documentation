# CANdlelib

CANdlelib is a library written in C++ to provide the user with API for using MAB products.

## Main Features

- Provides API for communicating with [CANdle](/CANdle/intro.md), and through it with:
    - [MAB Drivers (MD)](/MD/intro.md)
    - [Power Distribution Systems (PDS)](/PDS/intro)
- Provides helper functions for most of the tasks tied to motor control in robotics and automation.
- Provides usage examples for the devices.

[CANdle](/CANdle/intro) and [CANdle HAT](/CANdle/intro) devices come equipped with both **SPI** and **USB** interfaces.

```{note}
Using CANdlelib is a recommended way of integrating MAB products into the system. However we also provide support for clients that want to customize their main controllers.

Our [MAB FDCAN protocol](/MD/Communication/fdcan) is fully open-source and documented on this site.
```

## Architecture

Access to devices is split into corresponding modules:
- [CANdle Module](CANdlelib/CANdleModule.md)
- [MD Module](CANdlelib/MDModule.md)
- [PDS Module](CANdlelib/PDSModule.md)

Each module, groups functions and helper-wrapper methods for interacting with devices. For example of use, see [EXAMPLES](TODO TODO TODO) section.
