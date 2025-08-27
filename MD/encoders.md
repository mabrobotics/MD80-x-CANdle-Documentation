(aux_encoders)=

# Auxiliary Encoders

```{figure} ./images/encoder/encoders.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link/
```

Encoder is a position sensor that can be attached to the output shaft of the actuator. It is usually
useful for geared motors where the output shaft position after startup cannot be determined
unambiguously using the MD’s onboard encoder due to the gearbox. By using an output encoder one can
make sure that the output shaft position is always known at startup.

Currently we support one encoder type with two placement configurations:

- ME AS placed axially on the output shaft with a regular diametrically magnetized magnet

```{figure} ./images/encoder/output_encoder_axial.jpg
:width: 300px
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

- ME AS placed non-axially together with a diametrically magnetized ring magnet

```{figure} ./images/encoder/output_encoder_offaxis.jpg
:width: 300px
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

```{note}
MD can also work with encoders supplied in most CubeMars motors (such as AK10-9) and be paired with custom encoder such as RLS Aksim2 series on demand. Many of MABs MA series actuators use these for high precision applications.

If you want to pair an encoder other than MA AS, please contact us support@mabrobotics.pl.
```

## Encoder Modes

With Aux encoder connected, MD can use its data in a few different ways. For most applications,
where the encoder is used to determine absolute position of the shaft after a gearbox, STARTUP mode
is the most suitable.

```{list-table}
:header-rows: 1

* - \<encoder mode\> 
  - Description
* - STARTUP
  - initial position from <b><font color="#FF6900">output encoder</font></b>, 
    report <b><font color="#008000">main encoder</font></b> values, 
    motion based on <b><font color="#008000">main encoder</font></b>
* - MOTION
  - initial position from <b><font color="#FF6900">output encoder</font></b>,
    report <b><font color="#FF6900">output encoder</font></b> values,
    motion based on <b><font color="#FF6900">output encoder</font></b>
* - REPORT
  - initial position from <b><font color="#008000">main encoder</font></b>,
    report <b><font color="#FF6900">output encoder</font></b> values,
    motion based on <b><font color="#008000">main encoder</font></b>,
    calibration of the <b><font color="#FF6900">output encoder</font></b>  is impossible
* - MAIN
  - <b><font color="#FF6900">output encoder</font></b> is used as the <b><font color="#008000">main encoder</font></b>. All <b><font color="#FF6900">output encoder</font></b> measurements are mapped as <b><font color="#008000">main encoder</font></b> values. 
* - CALIBRATED_REPORT
  - initial position from <b><font color="#008000">main encoder</font></b>,
    report <b><font color="#FF6900">output encoder</font></b> values,
    motion based on <b><font color="#008000">main encoder</font></b>,
    calibration of the <b><font color="#FF6900">output encoder</font></b> is possible
```

```{warning}
The non-axial configuration outputs a nonlinear position values. This means it requires a [full calibration](aux_encoder_calibration) (your setup should be able to rotate by at least one full rotation), and in case of the report mode it will output nonlinear position and velocity readings that will have to be compensated in the host's software
```

Not all modes are recommended for every encoder. The non-axially placed ME AS encoder is inherently
more noisy and less accurate and thus we recommend using it only in STARTUP mode. Please refer to
the table below:

```{list-table}
:header-rows: 1

* - \<encoder type\> 
  - Valid modes
  - Description
* - ME_AS_CENTER 
  - STARTUP / MOTION / REPORT / MAIN / CALIBRATED_REPORT
  - \-
* - ME_AS_OFFAXIS
  - STARTUP
  - This configuration is much more noisy than the axial placement
* - MB053SFA17BENT00 
  - STARTUP / MOTION / REPORT / MAIN / CALIBRATED_REPORT
  - \-
* - CM_OFFAXIS
  - STARTUP
  - Only offaxis configuration is supported
```

## Attaching an encoder

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
