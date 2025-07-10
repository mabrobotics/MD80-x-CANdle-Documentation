# Overview

## Main Features

- Provides API for communicating via CANdle device with:
    - [MAB Drivers (MD)](md)
    - [Power Distribution Systems (PDS)](pds)
- Provides helper functions for most of the tasks tied to motor control in robotics and automation.
- Provides usage examples for the devices.

[CANdle](candle_and_hat) and [CANdle HAT](candle_and_hat) devices come equipped with both **SPI** and **USB** interfaces.

```{note}
Using CANdlelib is a recommended way of integrating MAB products into the system. However we also provide support for clients that want to customize their main controllers. 

Our [MAB FDCAN protocol](fd_can_protocol) is fully open-source and documented on this site. 
```

