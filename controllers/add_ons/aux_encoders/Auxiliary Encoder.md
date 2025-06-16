(output_encoder)=
# Auxiliary Encoder

Output encoder is a position sensor that can be attached to the output shaft of the actuator. It is usually useful for geared motors where the output shaft position after startup cannot be determined unambiguously using the MD’s onboard encoder due to the gearbox. By using an output encoder one can make sure that the output shaft position is always known at startup. 

```{figure} ./images/output_encoders.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

Currently we support one encoder type with two placement configurations: 
* ME AS placed axially on the output shaft with a regular diametrically magnetized magnet

```{figure} ./images/output_encoder_axial.jpg
:width: 300px
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

* ME AS placed non-axially together with a diametrically magnetized ring magnet 

```{figure} ./images/output_encoder_offaxis.jpg
:width: 300px
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## Configuration

The output encoder configuration is performed in the motor config files and saved to the MD series motor controller using the [`mdtool setup motor`](mdtool_setup_motor) command. There are only two parameters used in output encoder setup: 

```
[output encoder]
output encoder = <encoder type>
output encoder mode = <encoder mode>
```

where:

```{list-table}
:header-rows: 1

* - \<encoder type\> 
  - Description
* - ME_AS_CENTER 
  - for axially placed ME AS encoder
* - ME_AS_OFFAXIS
  - for non-axially placed ME AS
* - MB053SFA17BENT00
  - Renishaw RS422 17-bit RLS encoder
* - CM_OFFAXIS
  - CubeMars motors offaxis encoder
```

```{list-table}
:header-rows: 1

* - \<encoder mode\> 
  - Description
* - STARTUP
  - initial position from <b><font color="#FFBF00">output encoder</font></b>, 
    report <b><font color="#008000">main encoder</font></b> values, 
    motion based on <b><font color="#008000">main encoder</font></b>
* - MOTION
  - initial position from <b><font color="#FFBF00">output encoder</font></b>,
    report <b><font color="#FFBF00">output encoder</font></b> values,
    motion based on <b><font color="#FFBF00">output encoder</font></b>
* - REPORT
  - initial position from <b><font color="#008000">main encoder</font></b>,
    report <b><font color="#FFBF00">output encoder</font></b> values,
    motion based on <b><font color="#008000">main encoder</font></b>,
    calibration of the <b><font color="#FFBF00">output encoder</font></b>  is impossible
* - MAIN
  - <b><font color="#FFBF00">output encoder</font></b> is used as the <b><font color="#008000">main encoder</font></b>. All <b><font color="#FFBF00">output encoder</font></b> measurements are mapped as <b><font color="#008000">main encoder</font></b> values. 
* - CALIBRATED_REPORT
  - initial position from <b><font color="#008000">main encoder</font></b>,
    report <b><font color="#FFBF00">output encoder</font></b> values,
    motion based on <b><font color="#008000">main encoder</font></b>,
    calibration of the <b><font color="#FFBF00">output encoder</font></b> is possible
```

```{warning}
The non-axial configuration outputs a nonlinear position values. This means it requires a [full calibration](output_encoder_calibration) (your setup should be able to rotate by at least one full rotation), and in case of the report mode it will output nonlinear position and velocity readings that will have to be compensated in the host's software
```

Not all modes are recommended for every encoder. The non-axially placed ME AS encoder is inherently more noisy and less accurate and thus we recommend using it only in STARTUP mode. Please refer to the table below: 

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

Steps to add an external encoder to the driver setup:

* make sure the encoder sensor is placed correctly: 

```{figure} ./images/output_encoder_cross.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
*
  * in case of axially placed sensors make sure they are placed in center at correct height above the magnet (1 mm is usually optimal)
  * in case of non-axial configuration make sure the magnet is close to the ring magnet (<0.5mm) and the sensor IC is at least 2mm above or below the ring magnet horizontal plane.

* Connect the MDxx with the encoder using a picoblade series cable assembly and connect power to the MDxx. 
* Modify the motor config file according to your setup and save it to the MDxx using [mdtool](mdtool)

```{figure} ./images/setup_output_encoder.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

You can confirm the setup using the [`mdtool setup info`](mdtool_setup_info) command to make sure all parameters are correct: 

```{figure} ./images/mdtool_setup_info_errors.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
```{note}
At this point some errors will be present as the setup is not yet calibrated. 
```

* Calibrate the MDxx using [`mdtool setup calibration`](mdtool_setup_calibration) command 
* Calibrate the output encoder using [`mdtool setup calibration_out`](mdtool_setup_calibration_out) command
* Test the encoders using [`mdtool test encoder`](mdtool_test_encoder) command.
* Use the [`mdtool setup info all`](mdtool_setup_info) command to make sure there are no errors and the test results (min, max and stddev errors) are within your expectations.
* The external encoder is ready to use! For more information on external encoder parameters please see the [output encoder calibration](output_encoder_calibration) section.