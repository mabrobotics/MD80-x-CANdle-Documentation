# MAB Ecosystem

```{figure} images/md80_actuators.jpg
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

**CANdle Ecosystem** is a system of brushless actuator controllers (MD series motor controller) and
translator devices (CANdle) used for interfacing with them. MD series controller actuators can be
used in advanced robotic projects like quadrupedal robots, robotic manipulators, exoskeletons,
gimbals, and many more.

## MD series motor controller

MD series motor controller is a highly integrated brushless motor controller. It can be interfaced
with a great variety of motors to turn them into advanced servo actuators. MD series motor
controller can work with both direct drive (no gearbox) and geared motors. All MD series motor
controllers, feature built-in absolute encoder, FOC based control algorithm and variety of motion
control modes. MDs can also be equipped with additional encoders and brakes, for many application
scenarios.

```{image} images/mds.jpg
:alt: MDs
:class: bg-primary mb-1
:width: 700px
:align: center
:class: no-scaled-link
```

## PDS - Power Distribution System

PDS is a highly modular power management system, that aims to provide everything that a mobile robot
needs. It allows for safe and reliable power distribution with diagnostics, and can be easily
accessed via CANFD bus and CANdle.

```{image} images/pds.jpg
:alt: PDS
:class: bg-primary mb-1
:width: 700px
:align: center
:class: no-scaled-link
```

## CANdle and CANdle HAT

CANdle (CAN + dongle) is a translator device between the host controller (PC or SBC) and the MD
series motor controller drivers. It is possible to interface CANdle with a regular PC over USB bus
or CANdle HAT with SBCs (such as Raspberry PI) over USB, SPI or UART bus. The latest CANdle and
CANdle HAT devices are fitted with a switch for enabling and disabling the built-in termination
resistor. CANdle provides easy to use interface via C++, Python or ROS2 APIs, check
[CANdle-SDK](candle-sdk) for more info.

```{image} CANdle/images/CANdle_joined.webp
:alt: CANdles
:class: bg-primary mb-1
:width: 700px
:align: center
:class: no-scaled-link
```

```{note}
We officially support Linux x86-64, Windows 11 and ARM64 architecture hosts via CANdleSDK.
```

(hardware_setup)=

## Hardware setup

CAN bus topology is a single-line network structure. A typical hardware connection/wiring scheme for
CANdle x MD ecosystem is presented in the picture below:

```{image} images/ecosystem_diagram.jpg
:alt: ecosystem_diagram 
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{hint} In case you’d like to read more about the recommended lengths of the bus segments we suggest the [elektormotus guide](https://emusbms.com/files/bms/docs/Elektromotus_CAN_bus_recommendations_v0.2_rc3.pdf).
```

The CAN bus termination is a single Molex connector with an embedded 120Ohm resistor. Termination
should be always be attached to the first and last device in a string. CAN bus is very robust
protocol, and can usually work on low speeds with just one terminator, however if you are
experiencing any problems, we recommend you use a full terminator setup.

```{hint} Both CANdle and CANdleHAT feature a termination circuit, that can be enabled with a switch.
```

Here is an example setup of CANdle Ecosystem, with PDS, two MD based actuators, CANdle, and NVidia
Jetson as host computer, all connected in a single communication string.

```{image} images/ecosystem.jpg
:alt: ecosystem
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

To learn more about MAB Ecosystem, check out one of the categories below:

# Table of contents

```{tableofcontents}
```
