# Getting Started

## With CANdle-SDK

### Prerequisites

For running CANdle-SDK as a **configuration package** (candletool), the following prerequisites must be met:

> - Linux based OS (Ubuntu 24.04 or higher recommended) or Windows 10/11
> - For linux glibc 2.38 or higher
> - libusb 1.0.23 or higher

Additionally for **building your own applications** with CANdle-SDK in C++, the following prerequisites must be met:

> - A C++20 compatible compiler (GCC 13 or higher or MinGW-w64 on Windows)
> - CMake 3.25 or higher
> - libusb-dev package 1.0.23 or higher

Additionally, for **Python applications**, the following prerequisites must be met:

> - Python 3.12 or higher (glibc or mingw-w64 compatible)

To communicate with MDxx or PDS devices, you will need to purchase a CAN interface device from MAB Robotics, such as CANdle or CANdle-HAT. You can find them [here](https://www.mabrobotics.pl/product-page/candle).

### Installation

You can always find the latest installation instructions in the [CANdle-SDK repository](https://github.com/mabrobotics/CANdle-SDK) readme file.

Connect the CANdle device to your computer via USB-C cable.

```{note}

For Windows users running the candletool for the first time it is required to run the [candlesdk-win-driver.exe](https://github.com/mabrobotics/CANdle-SDK/blob/main/candletool/tools/candlesdk-win-driver.exe) installer as administrator with CANdle device connected to the computer. This step is not required for subsequent runs of candletool.

```

### First Steps

After installing the CANdle-SDK, you can start by running the candletool application to configure and test your MD-based actuators. You can find the detailed instructions on how to use candletool in the [candletool directory readme file](https://github.com/mabrobotics/CANdle-SDK/tree/main/candletool).

To test if the candletool installed correctly try running `candletool --version` and with a candle connected `candletool candle version`.

```{tip}
To get detailed information on usage you can run each `candletool` command with `-h` flag to display help.
```

## With MD

### Prerequisites

To get started with MAB Driver (MD) systems you will need the following:

> - MDxx or MAB pre-assembled drive
> - \> 25W 24V capable power supply
> - CANdle or CANdle HAT

### Installation

Connect the MD with the power supply and CANdle class device according to the documentation provided in the MD section using cabeling that was sent by MAB along with the driver.

```{note}
Connection details can be found in the [hardware setup section](hardware_setup).


For connecting the MD to your BLDC motor checkout the correct MD section of the document for driver specific soldering connections and magnet placement. [MD80](md80) [MD20](md20)
```

When the cabeling is connected turn the power on. The green LED on top of the board shoudl be light on and the green LED shoudl flash periodically.

```{note}
Red LED on the bottom indicates an error in board operation and is normal for unconfigured drives. You can use `candletool md --id 'id' info` for more details on the errors present.

When both red and green LEDs flash rapidly it means the board is in its bootloader phase. This is normal for the first few seconds of operation but if it does not stop it means that the firmware is corrupted and needs to be recovered via `candletool md --id 'id' update latest -r` where `-r` is a recovery flag.
```

When the power is on make sure that the CAN line is properly terminated. CANdle class devices have a switch that enables/disables internal 120 Ohm termination resistor. On the other end of CAN chain there shoudl either be a resistor plugin provided by MAB or PDS control board CAN input which has a CAN termination builtin.

```{note}
The rest of this section will not work for the CANopen protocol. Currently only FDCAN MAB protocol is supported by the CANdle devices. The drives shoudl be configured in accordance of CiA 402 specification which is not provided by MAB. The .eds files can be found in the [Downloads](downloads) section.
```

To make sure that the installation proces went correctly please try running

```bash
candletool md discover
```

and see if the drive responds with its ID on the network.

```{important}
For troubleshooting please checkout the [FAQ](faq) section of this document.
```

### First Steps

#### For the preassebled drive

The MAB motors with MDxx preassebled into them come preconfigured. Their **CAN ID** is set to the **last 3 digits of the warranty sticker** in case of FDCAN MAB protocol and **10** node ID in case of CANopen protocol.

```{note}
Although MAB motors are preconfigured, they still need their PID controlers adjusted for their final operation. Head to [motion modes](motion_modes) section to learn more.
```

To checkout the configuration of your motor run the command:

```bash
candletool md --id 'id' info
```

If there are no errors present you should be able to test the drives movement using this command:

```bash
candletool md --id 'id' test relative 'angle in radians from -10.0 to 10.0'
```

The motor shoudl than move using [impedance control mode](impedance-pd).

#### For the standalone MDxx

The standalone MDxx procedure comes in a form of a configuration and calibration steps.

Standalone MDs that use FDCAN protocol always come with **CAN ID** set to **100**.

In order to configure the driver we need a configuration file for this particular model. Some of the motors have MAB provided configuration files which can be used as a reference in creating your own. They can be found in the installation directory of candletool. For windows `C://Program Files/candletool/config/motors/` and for Linux `/etc/candletool/config/motors`. They are not ment to be modified so it is best to copy the one you need into your working directory and use that copy.

```{seealso}
For more details on configuring your own drive see [Configuration file description](config)
```

When you either created your own config or chosen config file made by MAB you need to run the following command:

```bash
candletool md --id 100 config upload 'path to your configuration file or name of the premade config like AK60-6.cfg'
```

You can verify your config by running:

```bash
candletool md --id 100 info
```

In the output there shoudl be no CONFIGURATION_ERROR and the values provided from the driver should match your configuration.

Next step is to calibrate the motor. This can be done via this command:

```bash
candletool md --id 100 calibrate
```

The prompt will provide the information on power rquirements and await confirmation. Once the calibration is done all of the errors should be gone and the driver should be ready to work.

```{seealso}
For more in depth explanation of calibration procedure head to [calibration section](calibration)
```

Run test to verify that the driver is able to operate:

```bash
candletool md --id 100 test relative 'angle in radians from -10.0 to 10.0'
```

Once it is verified you can than change your drive id to be able to connect it to the CAN network in chain. The valid ids range from 9 to 1999. You can change it using this command.

```bash
candletool md --id 100 can --new_id 'new id'
```

Than you can run save command to make the new id permament

```bash
candletool md --id 'new id' save
```

## With PDS

### Prerequisites

### Installation

### First Steps
