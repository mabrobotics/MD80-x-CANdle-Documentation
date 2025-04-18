# Ecosystem overview 

MD x CANdle is a system of brushless actuator controllers (MD series motor controller) and translator devices (CANdle) used for interfacing with them. MD series controller actuators can be used in advanced robotic projects like quadrupedal robots, robotic manipulators, exoskeletons, gimbals, and many more. 

## MD series motor controller

MD series motor controller is a highly integrated brushless motor controller. It can be interfaced with a great variety of motors to turn them into advanced servo actuators. MD series motor controller can work with both direct drive (no gearbox) and geared motors.

```{image} images/md80.webp
:alt: MD80
:class: bg-primary mb-1
:width: 400px
:align: center
:class: no-scaled-link
```

## CANdle and CANdle HAT

CANdle (CAN + dongle) is a translator device between the host controller and the MD series motor controller drivers. It is possible to interface CANdle with a regular PC over USB bus or CANdle HAT with SBCs (such as Raspberry PI) over USB, SPI or UART bus. The latest CANdle and CANdle HAT devices are fitted with a switch for enabling and disabling the built-in termination resistor.


```{note}
We officially support Linux x86-64 and ARMv8-A architecture hosts.
```

```{image} images/candle.webp
:alt: candle
:class: bg-primary mb-1
:width: 400px
:align: center
:class: no-scaled-link
```

## Safety information 

Even though the MD series motor controller is a small brushless controller it can push a substantial amount of current through the motor windings. This means there are many hazards related to the high torques that the actuator is able to produce as well as elevated temperatures that may occur close to the MD series motor controller controller or the motor. Always make sure the actuator is mounted firmly and does not pose a threat to its surroundings. Make sure the power supply current limits are set to low values (~1A) as an additional safety measure when you are unsure about the tested behavior of the system. 


## Operating conditions (MD series motor controller and CANdle)

```{list-table}

* - Ambient Temperature (Operating)
  - 0°C - 40°C
* - Ambient Temperature (non-operating)
  - 0°C - 60°C
* - Maximum Humidity (Operating)
  - up to 95%, non-condensing at 40 ºC
* - Maximum Humidity (Non-Operating)
  - up to 95%, non-condensing at 60 ºC
* - Altitude (Operating)
  - -400 m to 2000 m
```
(hardware_setup)=
## Hardware setup 

CAN bus topology is a single-line network structure. A typical hardware connection/wiring scheme for CANdle x MD ecosystem is presented in the picture below:

```{image} images/hardware_setup.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
```{hint} In case you’d like to read more about the recommended lengths of the bus segments we suggest the [elektormotus guide](https://emusbms.com/files/bms/docs/Elektromotus_CAN_bus_recommendations_v0.2_rc3.pdf). 
```

The CAN bus termination is a single Molex connector with an embedded 120Ohm resistor. Termination should be always be attached to the last controller in a string. 

```{figure} images/hardware_setup_candle.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

CANdle MD-actuator string (USB bus)
```

```{figure} images/hardware_setup_candleHAT.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

CANdle HAT MD-actuator string (SPI/UART bus using Raspberry Pi 4)
```
