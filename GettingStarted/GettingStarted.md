# Getting Started

## With CANdle-SDK
### Prerequisites
For running CANdle-SDK as a configuration package (candletool), the following prerequisites must be met:
- Linux based OS (Ubuntu 24.04 or higher recommended) or Windows 10/11
- Glibc 2.39 or higher
- libusb 1.0.23 or higher

Additionally for building your own applications with CANdle-SDK in C++, the following prerequisites must be met:
- A C++20 compatible compiler (GCC 13 or higher or MinGW-w64 on Windows)
- CMake 3.25 or higher
- libusb-dev package 1.0.23 or higher

Additionally, for Python applications, the following prerequisites must be met:
- Python 3.12 or higher (glibc or mingw-w64 compatible)

To communicate with MDxx or PDS devices, you will need to purchase a CAN interface device from MAB Robotics, such as CANdle or CANdle-HAT. You can find them [here](https://www.mabrobotics.pl/product-page/candle).

### Installation

You can always find the latest installation instructions in the [CANdle-SDK repository](https://github.com/mabrobotics/CANdle-SDK) readme file.

Connect the CANdle device to your computer via USB and follow the installation instructions for your operating system.

```{note}

For Windows users running the candletool for the first time it is required to run the [candlesdk-win-driver.exe](https://github.com/mabrobotics/CANdle-SDK/blob/main/candletool/tools/candlesdk-win-driver.exe) installer as administrator with CANdle device connected to the computer. This step is not required for subsequent runs of candletool.

```

### First Steps

After installing the CANdle-SDK, you can start by running the candletool application to configure and test your MD-based actuators. You can find the detailed instructions on how to use candletool in the [canletool directory readme file](https://github.com/mabrobotics/CANdle-SDK/tree/main/candletool).

## With MD
### Prerequisites
### Installation
### First Steps

## With PDS
### Prerequisites
### Installation
### First Steps