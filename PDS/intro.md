(pds)=

# PDS - Power Distribution System

![PDS_stack_image](../images/pds.jpg)

## Overview

For robots, particularly mobile ones, it’s crucial to have robust power distribution systems that
ensure reliable, safe operation, energy efficiency, and seamless integration with components like
motors, sensors, onboard computers, and subsystems. Additionally, the challenge is to make these
systems compact and lightweight. MAB PDS addresses all these requirements, offering a comprehensive,
integrated solution that simplifies the construction of robots while meeting all essential power
management needs in a small, efficient form factor.

With the MAB PDS, robotic researchers, engineers, and system integrators can focus on higher-level
development instead of being limited by hardware and embedded firmware design, which can be
time-consuming and complex.

The MAB PDS is built on a modular philosophy designed to meet the core needs of every robot:

- High-power bus for motors with on/off control,
- Safe power bus for the computers and sensors with on/off control,
- Handling regenerative energy from motors,
- Monitoring all the parameters related to power supplies and energy consumption,
- Power switch to enable/disable the robot,
- Fast and reliable handling of safety triggers,
- Fast telemetry and control from a higher-level controller,
- Scalability for flexible system expansion.

## Modules

To handle all these features, the MAB PDS is split into four different types of modules:

### Control (CTRL)

Master module of the system.

```{image} ./images/CTRL.JPG
:alt: CRTL
:class: bg-primary mb-1
:width: 300px
:align: center
```

### Isolated DC/DC converter (IC)

A module with an isolated DC/DC converter for peripherals like computers and sensors.

```{image} ./images/IC.JPG
:alt: IC
:class: bg-primary mb-1
:width: 300px
:align: center
```

### Power stage (PS)

A module that handles high-power delivery to the motors.

```{image} ./images/PS.JPG
:alt: PS
:class: bg-primary mb-1
:width: 300px
:align: center
```

### Brake resistor (BR)

Complementary subsystem with the Power Stage module.

```{image} ./images/BR.JPG
:alt: BR
:class: bg-primary mb-1
:width: 300px
:align: center
```

The overview of what exactly the PDS slave modules do is presented in the simple scheme below:

![PDS_system_scheme](images/PDS_modules_scheme.png)

The master (CTRL) module manages ENABLE signals, acquires current/voltage measurements, and
communicates with external systems.

```{important}
For detailed description refer to <a href = ../docs/pds_guide_1.0.pdf>PDS Guide</a>
```
