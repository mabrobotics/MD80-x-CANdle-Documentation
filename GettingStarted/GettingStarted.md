(getting_started)=

# Getting Started

## Important Notes

Before you start working with the MAB ecosystem, here are some key precautions to keep in mind:

1. **Safety with Actuators**: Unintentional movement can cause serious injury. Always ensure they are securely fixed to a workbench during operation and have enough space to not damage people or goods.

1. **Safety Limits**: Familiarize yourself with the [safety limits](md_safety) section in this document. Keep safety limits low during development, and only increase them once you are confident in your understanding and control of the system.

1. **Electrical Safety**: Though our systems are designed to work with safe voltages it is adviced to be cautious and not touch powered on systems as well as watch out for any shorts which might cause an explosion at high currents present in the devices.

1. **Power Supply Recommendations**: Choose power supply sources that can operate in two quadrants. These supplies should be capable of both supplying and dissipating energy from the motor when it functions as a generator. Avoid using older transformer-based power supplies, as they may block current, leading to dangerous overvoltage events. SMPS power supplies are ideal.

```{danger}
Before operating the system, be sure to read the full documentation to understand all safety precautions and avoid potential damage to both the system and yourself.
```

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
> - Installed candletool

### Installation

Connect the MD with the power supply and CANdle class device according to the documentation provided in the MD section using cabeling that was sent by MAB along with the driver.

```{note}
Connection details can be found in the [hardware setup section](hardware_setup).


For connecting the MD to your BLDC motor checkout the correct MD section of the document for driver specific soldering connections and magnet placement. [MD80](md80_mechanical_data) [MD20](md20_mechanical_data)
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
For more details on configuring your own drive see [configuration file description](config) and [configuration files in CANdle-SDK](config_md).
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

```{seealso}
For more commands see [candletool commands section](md_commands)
```

```{dropdown} **Deprecated video tutorials**
Tutorials listed here are old and some of the things might not work but they still can give you a concept of how the system shoudl operate. Full video tutorials will come soon.
1. Guide on how to set up a new MD series motor controller to work with a motor of your choice:
   [MD x CANdle - Brushless Motor Setup Guide](https://www.youtube.com/watch?v=74zTUlJ2hmo&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=5)
1. Quick startup guide - watch when your motor is already configured and you'd like to try the
   examples:
   [MD x CANdle - Getting Started Tutorial](https://www.youtube.com/watch?v=bIZuhFpFtus&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=1)
1. MDtool guide - a short introduction to MDtool and its basic commands (at this point the MDtool
   has evolved, however, the main principles are the same)
   [MD x CANdle - MDtool](https://www.youtube.com/watch?v=BrojxsU8oD8&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=2)
1. Motion modes guide - an introduction to motion modes available on MD series motor controller
   [MD x CANdle - motion modes](https://www.youtube.com/watch?v=XnD8sG22zro&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=3)
1. ROS/ROS2 startup guide - an introduction to ROS/ROS2 drivers for MD series motor controller
   [MD x CANdle - ROS/ROS2 startup guide](https://www.youtube.com/watch?v=6sLQNaJKuJY&list=PLYKmGVZotGRoMR8eV5AuC2XP_qJsL6Bu6&index=4)


```

## With PDS

### Prerequisites

> - Assembled PDS stack
> - \> 25W 24V capable power supply
> - CANdle or CANdle HAT
> - Installed candletool
> - PDS accessories provided by MAB

### Installation

PDS is a modular system that requires diffrent assemblies depending on the modules present in the stack.

```{important}
For more details on how to assemble the PDS you are using please head to the [PDS overview section](pds_overview).
```

Following sections describe connections for each of the modules:

> - [Control module (CTRL)](pds_ctrl)
> - [Power stage module (PS)](pds_ps)
> - [Isolated converted module (IC)](pds_ic)
> - [Brake resistor module (BR)](pds_br)

```{seealso}
<a href = ../docs/pds_guide_1.0.pdf>PDS User Manual</a>
```

When the PDS has all the connections done turn on the powersupply and hold the power button for 4 seconds. It shoudl light green and stay lit. Than and run the following command:

```bash
candletool pds discover
```

In the command output the connected PDS's id shoudl be present.

```{seealso}
[PDS CLI](pds_commands)
```

### First Steps

Below you can find the basic functionalities presentation for your particular module.

```{important}
All modules asside from CTRL can have diffrent sockets they are connected to. When running module specific commands it is required to provide the socket number of the module. More info on that can be found inside <a href = ../docs/pds_guide_1.0.pdf>PDS User Manual</a>.
```

#### CTRL module

Run the command bellow for basic status of the module

```bash
candletool pds --id 'id' info
```

#### IC module

Run the command bellow for basic status of the module

```bash
candletool pds --id 'id' ic 'socket id' info
```

To enable power on the isolated converter's output use:

```bash
candletool pds --id 'id' ic 'socket id' enable
```

To disable power on the isolated converter's output use:

```bash
candletool pds --id 'id' ic 'socket id' disable
```

#### PS module

Run the command bellow for basic status of the module

```bash
candletool pds --id 'id' ps 'socket id' info
```

To enable power on power stage outputs use:

```bash
candletool pds --id 'id' ps 'socket id' enable
```

To disable power on the power stage outputs use:

```bash
candletool pds --id 'id' ps 'socket id' disable
```

#### BR module

Run the command bellow for basic status of the module

```bash
candletool pds --id 'id' br 'socket id' info
```

To check at what temperature the BR module will shutdown use

```bash
candletool pds --id 'id' br 'socket id' get_temp_limit
```
