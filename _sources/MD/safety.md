# Safety

(watchdog)=

## Communication Watchdog

MD drivers feature an Communication Watchdog Timer. This timer will shut down the drive stage when
no FDCAN frame has been received in a specified time. This is to protect the drive and its
surroundings in an event of loss of communications, for example by physical damage to the wiring. By
default, the watchdog is set to 250ms. This time can be set to any value in the range of 1 to 2000ms
using `candletool md config can` command. When the watchdog is set to 0, it will disable the timer,
however, this can lead to dangerous situations, and it is not a recommended way of operating MD.

```{warning}
We do not recommend disabling the CAN watchdog timer!
```

(safety_limits)=

## Current Limit

Let’s start with the max current limit:

```{figure} ./images/current_limit.png
:width: 1000px
:align: center
```

This setting limits the maximum current (and thus torque) the motor controller can output. It is the
last user-configurable limit in the control scheme. The maximum current is set using the `motorIMax`
register. This setting can be saved in the non-volatile memory so that it is always loaded on the
actuator power-up. To estimate the maximum current setting for a particular motor, you should use
the following formula:

$$ I [A] = \frac{\tau [Nm] \frac{1}{G_r}}{K_t[\frac{Nm}{A}]} $$

where

- $ I[A] $ - calculated current in Amps
- $ \tau $ - desired maximum torque
- $ G_r $ - gear ratio
- $ K_t $ - motor’s torque constant

for example let’s calculate the max current limit for AK80-9 motor, for a 2Nm max torque:

$\tau = 2 Nm$

$G_r = 9:1 -> 9$

$K_t = 0.091 Nm/A$

$ I [A] = \frac{2[Nm] \cdot \frac{1}{9}}{0.091[\frac{Nm}{A}]} $

$ I [A] \approx 2.44A $

```{note}
Usually this limit should be set to the highest peak torque that is allowed in the system so that it doesn't limit the actuator performance.
```

## Safety limits

Safety limits are implemented to limit the actuator parameters, to protect the controller or motor
from overheating, as well as the surrounding environment from too-powerful actuator movements.
Limits apply to: position, velocity, torque, phase current, and temperature of the MOSFETs and the
motor.

## Torque Limit

The next limit is the max torque limit which can be set using the CANdle script. This limit applies
to maximum torque and is expressed in Nm. It is respected in all motion modes. When target torque,
set either by either of the controllers, exceeds the `max torque` param the target torque is limited
and a [motion warning](motion_status) is generated.

```{figure} ./images/torque_limit.png
:width: 1000px
:align: center
```

```{note}
if the torque bandwidth is set to a low value it is possible to read torque values that are above limits when external torque is applied (for example during impacts). This is only true in transition states - when the load is constant the limits will work as expected. This is because with low torque bandwidth the internal torque PI controllers may be too slow to compensate for rapidly changing torque setpoint when hitting the torque/current limit. If you care about accurate torque readout be sure to play with the torque bandwidth parameter and possibly increase it from the default level.
```

## Velocity Limit

Velocity limit is respected only in Velocity PID / Profile Velocity and Impedance / Position PID /
Profile Position modes. When target velocity, set either by the user or the Position PID, exceeds
the `max velocity` param the target is limited, and a [motion warning](motion_status) is generated.

```{figure} ./images/velocity_limit.png
:width: 1000px
:align: center
```

## Position Limit

Position limit is respected only in Impedance / Position PID / Profile Position modes. When target
position, set by the user, exceeds the `<position limit min : position limit max>` param range the
target is limited to that range, and a [motion warning](motion_status) is generated. Attempt to
start the motor outside the range will generate a motion error.

```{figure} ./images/position_limit.png
:width: 1000px
:align: center
```

```{note}
Setting both Position limit min and max, to 0.0, will disable the limiters completely.
```

