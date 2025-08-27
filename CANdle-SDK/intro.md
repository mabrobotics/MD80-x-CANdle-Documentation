# CANdleSDK

## Overview

[CANdleSDK](https://github.com/mabrobotics/CANdle-SDK) is a software package with tools to help user
configure, test and integrate MAB devices into their systems. Currently CANdleSDK includes:

- CANdlelib - a C++ library for using candle, MD and PDS,
- CANdleTool - a CLI toolset for configuring, updating and testing MAB Ecosystem products,
- pycandlesdk - a Python bindings package of CANdlelib,
- examples - set of examples for both C++ and Python, for all of MAB Ecosystem devices.

In the near future, SDK will be expanded to include:

- ROS2 nodes, for MD and PDS

## Supported platforms

Both CANdlelib and CANdleTool are currently supported onjhj

- Linux systems (mainly Ubuntu, and Debian based distros),
- Windows 10,
- Windows 11.

```{note}
MacOS (Apple Silicon) support will be introduced later this year.
```

Supported architectures:

- ARM64 (Armv7), including Raspberry PI 3+,
- x86_64

Minimal requirements:

- 64-bit system,
- \>128 MB of LPDDR2 RAM,
- \>512 MB of disk space,
- \>1 GHz single-core CPU.

Recommended requirements:

- 64-bit system,
- USB 2.0 (or SPI in case of Linux),
- \>1 GB of LPDDR3 RAM,
- \>2 GB of disk space,
- \>2 GHz dual-core CPU.

## Installation

For installation and integration instructions checkout
[README](https://github.com/mabrobotics/CANdle-SDK) file of the main repository.
