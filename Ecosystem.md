# Ecosystem overview 

MD80 x CANdle is a system of brushless actuator controllers (MD80) and translator devices (CANdle) used for interfacing with them. MD80-based actuators can be used in advanced robotic projects like quadrupedal robots, robotic manipulators, exoskeletons, gimbals, and many more. 

## MD80

MD80 is a highly integrated brushless motor controller. It can be interfaced with a great variety of motors to turn them into advanced servo actuators. MD80 can work with both direct drive (no gearbox) and geared motors.

```{image} images/md80.jpg
:alt: MD80
:class: bg-primary mb-1
:width: 400px
:align: center
:class: no-scaled-link
```

## CANdle and CANdle HAT

CANdle (CAN + dongle) is a translator device between the host controller and the MD80 drivers. It is possible to interface CANdle with a regular PC over USB bus or CANdle HAT with SBCs (such as Raspberry PI) over USB, SPI or UART bus. 

```{image} images/candle.jpg
:alt: candle
:class: bg-primary mb-1
:width: 400px
:align: center
:class: no-scaled-link
```

## Safety information 

Even though the MD80 is a small brushless controller it can push a substantial amount of current through the motor windings. This means there are many hazards related to the high torques that the actuator is able to produce as well as elevated temperatures that may occur close to the MD80 controller or the motor. Always make sure the actuator is mounted firmly and does not pose a threat to its surroundings. Make sure the power supply current limits are set to low values (~1A) as an additional safety measure when you are unsure about the tested behavior of the system. 


## Operating conditions (MD80 and CANdle)

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

CAN bus topology is a single-line network structure. A typical hardware connection/wiring scheme for CANdle x MD80 ecosystem is presented in the picture below:

```{image} images/hardware_setup.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
```{hint} In case you’d like to read more about the recommended lengths of the bus segments we suggest the elektormotus guide. 
```

The CAN bus termination is a single Molex connector with an embedded 120Ohm resistor for MD80 versions older than HW V2.0.For MD80 HW V2.0 and newer, the termination resistor is built-in and can be turned on and off using software (`mdtool config can` command) on each controller. Termination should be always turned on or attached to the last controller in a string. 

```{figure} images/hardware_setup_candle.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

CANdle MD80-actuator string (USB bus)
```

```{figure} images/hardware_setup_candleHAT.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link

CANdle HAT MD80-actuator string (SPI/UART bus using Raspberry Pi 4)
```
