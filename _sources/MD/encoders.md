(aux_encoders)=

# Encoders
Encoders are rotary position sensors, used for measuring motor/actuator rotor angle with respect to the stator. 
Encoders can be either incremental or absolute - MD only work with selected absolute encoders.

MD motor controllers can work with up to 2 rotary position encoders at a time. There are two roles, the encoder can have:
- **Main Encoder** - used for __motor commutation__ and motion control by default,
- **Auxiliary (Aux) Encoder** - used mostly getting absolute actuator position (after gearbox), optionally can
    be used for motion control, or not used by driver (can be read via register by host).

**Main Encoder** is required for operation. The MD does not currently support sensorless control mode.


# Supported Encoders

| Encoder&nbsp;type | Supported Role | Notes |
| --------------|------------|----------|
| `ONBOARD` | **Main** / Aux | Mounted on every MD |
| [ME_AM On-axis](https://www.mabrobotics.pl/product-page/me-am) | **Main** / Aux | Present in some of MA-x actuators |
| [ME_AM Off-axis](https://www.mabrobotics.pl/product-page/me-am) | Aux |  Present in some of MA-x actuators |
| [RLS_17B_RS422](https://www.mabrobotics.pl/product-page/rls-aksim-2) | **Main** / Aux | High precision position sensor. Present in some of MA-x actuators, mainly hollow shaft (HS) series. |
| `CM_OFFAXIS` | Aux | Present in some of the CubeMars actuators |
| [RLS_17B_SPI](https://www.mabrobotics.pl/product-page/rls-aksim-2) | **Main** / Aux | High precision position sensor variant. Present in some MA-x actuators |
| `RLS_ORBIS_RS422` | **Main** / Aux | - |
| `CE300` | Aux | - |

```{Note}
Custom encoder support.

If you would like to use specific position sensor that is not currently supported, we are open to introducing
it to MD Ecosystem. Please contact us at: `contact@mabrobotics.pl`.
```

### Onboard Encoder
Each MD unit, features a 14-bit absolute encoder on the PCB. The Encoder is mounted on the bottom layer 
in the middle of the driver - in the center point of all mounting holes. This allows for mounting the 
driver right behind the motor, creating a compact and power-dense actuator with minimal moving parts.

# Auxiliary (Aux) Encoders

```{figure} ./images/encoder/encoders.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link/
```
If actuator has a gearbox, **Main encoder** (measuring motors' rotor angle) cannot determine output shaft
position on startup. This is where **Aux Encoder** can be used to supplement the driver with absolute
angle measurement *after* gearbox. 
Thanks to this, the actuators can keep track of its position between startups, which is especially 
useful while starting up mobile robots.


## ME-am

**ME-am** is a simple, reliable and cost-effective solution for adding additional position sensor to 
MD based actuators. ME-am can work in one of two placement configurations:

- ME-am placed axially on the output shaft with a regular diametrically magnetized magnet

```{figure} ./images/encoder/output_encoder_axial.jpg
:width: 300px
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

- ME-am placed non-axially together with a __diametrically magnetized__ ring magnet

```{figure} ./images/encoder/output_encoder_offaxis.jpg
:width: 300px
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{note}
**ME-am** encoder can be connected to MD20 and MD80 using AUX1 (6-pin) connector. 
```

### CM encoder

MD drivers can also work with encoders supplied in many CubeMars actuators (such as AK10-9). These
encoders are usually already mounted inside of the actuator. These encoders are perfectly fine to
determine actuator on startup, but due to their noisy nature, are not recommended to be used for
motion control.
```{note}
**CM encoder** can be connected to MD20 and MD80 using AUX1 (6-pin) connector. 
```

## [RLS](https://www.rls.si/) Precision Encoders
```{figure} ./images/encoder/rls.jpg
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

While Onboard and ME-am encoders provide sufficient precision for most general-purpose applications, 
there are situations where high-precision, through hole (hollow shaft) encoder is required. For those
cases we worked together with [RLS](https://www.rls.si/) to provide easy way to connect MD to a few of
https://www.mabrobotics.pl/product-page/rls-aksim-2 and RLS Orbis encoders.
We support [RLS AksIM 2](https://www.mabrobotics.pl/product-page/rls-aksim-2) with RS-422 interface
with the sizes ranging from 22 to 80mm.
```{warning}
**RLS AksIM2 and Orbis with RS-422 interface** can be connected to MD20 and MD80 using AUX2 (10-pin) connector.

<b><font color="#AA0000">RS-422 is on-demand feature of MD drivers, and by default it is not available 
on the board. </font></b>
Contact MAB Robotics support at `support@mabrobotics.pl`, for more information.
```

# Aux Encoder Modes

With Aux encoder connected, MD can use its data in a few different ways. For most applications,
where the encoder is used to determine absolute position of the shaft after a gearbox, STARTUP mode
is the most suitable.

| Encoder&nbsp;Mode | Description |
|--------------|-------------|
| `STARTUP` | Initial position from <b><font color="#FF6900">aux encoder</font></b>, report <b><font color="#008000">main encoder</font></b> values, motion based on <b><font color="#008000">main encoder</font></b>. |
| `MOTION` | Initial position from <b><font color="#FF6900">aux encoder</font></b>, report <b><font color="#FF6900">aux encoder</font></b> values, motion based on <b><font color="#FF6900">aux encoder</font></b>. |
| `REPORT` | Initial position from <b><font color="#008000">aux encoder</font></b>, report <b><font color="#FF6900">aux encoder</font></b> values, motion based on <b><font color="#008000">main encoder</font></b>. Calibration of the <b><font color="#FF6900">aux encoder</font></b> is impossible. |
| `MAIN` (legacy) | Position from <b><font color="#008000">aux encoder</font></b>, is mapped as <b><font color="#008000">main encoder</font></b>, and used for both control and commutation. Note: This is only applicable for drivers with firmware 2.x.x. For v3.0.0+ firmware, the main/aux encoder is set though `mainEncoder` and `auxEncoder` registers. |

```{warning}
The non-axial configuration outputs a nonlinear position values. This means it requires a 
[full calibration](aux_encoder_calibration) (your setup should be able to rotate by at least one full rotation), and in case of the report mode it will output nonlinear position and velocity readings that will have to be compensated in the host's software
```

Not all modes are recommended for every encoder. The off-axis placed CM or ME-am encoder is inherently
more noisy and less accurate and thus we recommend using it only in STARTUP mode. Please refer to
the table below:

| Encoder type | Supported modes | Recommended |
|--------------|------------|-------------|
| `ME_AM_CENTER` | `STARTUP` / `MOTION` / `REPORT` | `STARTUP` / `MOTION` / `REPORT` |
| `ME_AM_OFFAXIS` |`STARTUP` / `MOTION` / `REPORT` | `STARTUP` / `REPORT` |
| [RLS_17B_RS422](https://www.mabrobotics.pl/product-page/rls-aksim-2) | ALL | ALL |
| `CM_OFFAXIS` | `STARTUP` | Only off-axis configuration is supported. |
| [RLS_17B_SPI](https://www.mabrobotics.pl/product-page/rls-aksim-2) | ALL | ALL |
| `RLS_ORBIS_RS422` | ALL | ALL |
| `CE300` | `STARTUP` | `STARTUP` |

# ME-am - Mechanical mounting

How to add an encoder to the driver setup:

- make sure the encoder sensor is placed correctly:

```{figure} ./images/encoder/output_encoder_cross.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

- - in case of axially placed sensors make sure they are placed in center at correct height above
    the magnet (1 mm is usually optimal),
  - in case of non-axial configuration make sure the magnet is close to the ring magnet (\<0.5mm)
    and the sensor IC is at least 2mm above or below the ring magnet horizontal plane.

- Connect the MD with the encoder using a picoblade series cable assembly and connect power to the
  MD,

- Modify the motor config file, or directly access registers, according to your setup and save it to
  the MD,

- Calibrate the MD using `candletool md calibration` command,

- (if applicable) Calibrate the output encoder using `candletool md calibration -e aux` command

- Test the encoders using `candletool test encoder` command.

- Use the `candletool md info` command to make sure there are no errors and the test results (min,
  max and stddev errors) are within your expectations.

- The external encoder is ready to use!

```{warning}
Most of the auxialary encoder require sum-millimeter mounting for conitnous and reliable operation.
It is recommended to use CNC-machined mounting brackets for attaching the encoder. 3D printed enclosures
often do not provide sufficient precision and stiffnes (especially after heating up), and can lead to 
more noisy and reliable readings.
```

