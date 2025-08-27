# Measurements

MD drivers are equipped with sensors that allow for measuring the motor position, velocity, and
torque. Whether the motor has an integrated gearbox or not, **the position, velocity, and torque**
are in the output shaft reference frame. This means that changing the position from 0.0 to 2$\\pi$
radians, will result in approximately one rotation of the motor for direct-drive (gearless) servos
and approximately one rotation of the gearbox output shaft for geared motors.

## Position

To measure the position of the rotor the MD driver uses an internal magnetic encoder. The resolution
of the encoder is 14 bits (16384 counts per rotation). The drive aggregates all the measurements to
provide **multi-rotation positional feedback**. The reference position (0.0 rad) is set by the user
and stored in the non-volatile memory. Please see [`candletool md zero`](candletool_commands)
command for more information on how to set the desired zero position.

```{note}
When using geared actuators with gear ratios above 1:1 it is not possible to determine the position after startup unambiguously, since the motor completes multiple rotations per single rotation of the output shaft. For example, for a 2:1 gearbox, there are two sections within a single output shaft rotation where the motor shaft is in the same position. Unless the motor is placed in the wrong “section” during startup the absolute encoder functionality will work. To deal with this issue please see the [axu encoder](aux_encoders).
```

## Velocity

The velocity is estimated by measuring position change in time, at a frequency of 40kHz. The
measurements are then filtered using a low-pass filter with a cut-off frequency of 5 kHz since the
position differentiation method introduces noise.

## Torque

Actuator torque is estimated by measuring motor phase currents. This method can be used on low-gear
ratio actuators (preferably below 9:1), that are easily back-drivable, to get an estimate of the
torque applied by the motor. In applications with higher gear ratios, the torque readout might be
less accurate due to excessive friction in the gearbox.
