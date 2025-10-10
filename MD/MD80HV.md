# MD80 60V

```{figure} ./images/md80hv.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## General parameters

MD80 60V is high voltage variant of MD80, designed to work well with 12S lithium batteries. It has
all functionalities and features of regular MD80, for more information, please refer to
[MD80](#md80)

**General parameters table for MD80 60V:**

```{list-table}
:header-rows: 1

* - Parameter
  - Value
* - Nominal Input Voltage Range
  - 48 VDC
* - Maximum Input Voltage Range
  - 12 - 60 VDC
* - Max Input Current (connector)
  - 10.0 A (RMS)
* - Max Continuous Phase Current w/o cooling
  - 12 A
* - Max Peak Phase Current (t = 2 s)
  - 40 A
* - Built-in software-controlled termination resistor
  - optional
* - FDCAN Baudrate (adjustable)
  - 1/2/5/8 Mbps
* - Position PID Controller Execution Frequency
  - 1 kHz
* - Velocity PID Controller Execution Frequency
  - 5 kHz
* - Impedance Controller Execution Frequency
  - 40 kHz
* - Torque Control Execution Frequency
  - 40 kHz
* - Torque Bandwidth (adjustable)
  - 50 Hz - 2.5 kHz
* - External encoder support
  - yes, SPI and RS422 (optional)
* - External 5V power supply max current
  - 150 mA
```

```{figure} ./images/MD80/mount_cross_section.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## Connectors pinout

The connectors used in the system on the CAN FD side are MOLEX Micro-Fit series 3.0. Both connectors
are connected in parallel for easy daisy-chaining. The connector pinout with respected color coding
is presented below:

```{figure} ./images/motor_connectors.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{warning}
<font color='red'> Always make sure CAN bus lines are not shorted to the positive power rail. Applying supply voltage to these pins will cause permanent damage to the controller! </font> 
```

### Thermistor connection

All MD80 versions have the capability to measure the MOSFET and motor temperature. This is to ensure
the safe operation of the driver and motor. The motor shutdown temperature is configurable up to
140°C max with a hysteresis of 20°C. The driver shutdown temperature is fixed at 100°C with a
hysteresis of 20°C.

In the case of the MD80 60V the MOSFET thermistor is built-in directly under the power stage and
only the motor thermistor connector is available:

```{figure} ./images/HW20_thermistor.png
:alt: candle
:scale: 100%
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{note}
We recommend using [NTCMHP10K thermistors](https://www.mabrobotics.pl/product-page/thermistor) . Using other thermistors may result in imprecise temperature readout.
```

### Aux connectors

MD80 60V feature two accessory connectors.

**Aux 1 connector** is dedicated to connect MABs
[ME_am](https://www.mabrobotics.pl/product-page/me-am) and other SPI based encoders. For external
encoder connection via the SPI *530480650 Molex PicoBlade* connectors is provided.

```{warning}
<font color='red'>The auxiliary connector pins are 3.3V tolerant. Applying 5V to these pins will cause permanent damage to the controller! </font> 
```

```{figure} ./images/MD80/aux1_connector_pinout_HW2.1.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

**Aux 2 connector** has two user-configurable GPIOs, and RS422 interface for connecting to RLS Axim2
encoder. AUX GPIO A pin can be used as an automatic brake control output signal. This signal when
amplified, can be used to control
[MAB SLIM](https://www.mabrobotics.pl/product-page/mab-slim-electromagnetic-brake) electromagnetic
brakes. Enabling of this mode is done via `userGpioConfiguration` register. When enabled driver will
automatically disengage the brake when enabled. For external encoder connection via the RS422 and
the GPIO pins utilization *530480810 Molex PicoBlade* connectors could be used.

```{figure} ./images/MD80/aux2_connector_pinout.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

We are able to integrate custom functions such as GPIOs for external sensors and indicators. For
more information please contact us: [contact@mabrobotics.pl](https://www.mabrobotics.pl/contact)

```{warning}
By default RS422 transciver is not soldered on the MD80 boards. If you plan to use RLS Axim2 encoder with MD80, let us know when ordering the board. This modification will be done free of charge.
```

## Thermal characteristics

**Test Conditions and Setup**

To cover all potential cases, three cooling scenarios have been performed:

- No additional cooling
- Passive cooling
- Active air cooling

MD80HV driver was tested using coupled inductors (each 22uH) - simulating a motor.

The circuit of the test station is visible below.

```{figure} images/thermal/MD_test.png
:alt: MD testing station
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In this way driver is set up for the worst case when there is no shaft and all the power is
converted to heat.

In each scenario, tests were conducted for a range of phase currents, varying from 2 A to 78 A in 4
A increments. For each current level, the setup was operated until the temperature stabilized, with
a target duration of 120 seconds.

All tests were performed in constant environment conditions, in still air at 25°C ambient
temperature.

The temperature was measured using an onboard thermistor placed on the bottom layer of the PCB,
directly below the MOSFETs.

Tests were performed using voltage levels of 14V, 24V, 36V, 48V and 60V.

**Test scenario I - no cooling**

```{figure} images/thermal/MD80HV/no_cooling/14V.png
:alt: MD80HV no cooling 14V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/no_cooling/24V.png
:alt: MD80HV no cooling 24V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/no_cooling/36V.png
:alt: MD80HV no cooling 36V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/no_cooling/48V.png
:alt: MD80HV no cooling 48V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/no_cooling/60V.png
:alt: MD80HV no cooling 60V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

**Test scenario II - passive cooling**

```{figure} images/thermal/MD80HV/passive_cooling/14V.png
:alt: MD80HV passive cooling 14V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/passive_cooling/24V.png
:alt: MD80HV passive cooling 24V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/passive_cooling/36V.png
:alt: MD80HV passive cooling 36V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/passive_cooling/48V.png
:alt: MD80HV passive cooling 48V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/passive_cooling/60V.png
:alt: MD80HV passive cooling 60V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

**Test scenario III - active air cooling**

```{figure} images/thermal/MD80HV/active_air_cooling/14V.png
:alt: MD80HV active air cooling 14V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/active_air_cooling/24V.png
:alt: MD80HV active air cooling 24V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/active_air_cooling/36V.png
:alt: MD80HV active air cooling 36V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/active_air_cooling/48V.png
:alt: MD80HV active air cooling 48V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{figure} images/thermal/MD80HV/active_air_cooling/60V.png
:alt: MD80HV active air cooling 60V
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
