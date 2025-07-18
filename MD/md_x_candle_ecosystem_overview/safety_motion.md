(watchdog)=
# FDCAN Watchdog

MD drivers feature an FDCAN Watchdog Timer. This timer will shut down the drive stage when no FDCAN frame has been received in a specified time. This is to protect the drive and its surroundings in an event of loss of communications, for example by physical damage to the wiring. By default, the watchdog is set to 250ms. This time can be set to any value in the range of 1 to 2000ms using [`mdtool config can`](mdtool_config_can) command. When the watchdog is set to 0, it will disable the timer, however, this can lead to dangerous situations, and it is not a recommended way of operating MDxx.

```{warning}
We do not recommend disabling the CAN watchdog timer.
```

(safety_limits)=
# Safety limits

Safety limits are implemented to limit the actuator parameters, to protect the controller or motor from overheating, as well as the surrounding environment from too-powerful actuator movements. Limits apply to: position, velocity, torque, phase current, and temperature of the MOSFETs and the motor.

```{warning}
Setting the max current limit to above the maximum continuous current may damage the MDxx controller if the maximum torque is commanded for a prolonged period.
```

## Current Limit
Let’s start with the max current limit:

```{figure} ./images/current_limit.png
:width: 1000px
:align: center
```

This setting limits the maximum current (and thus torque) the motor controller can output. It is the last user-configurable limit in the control scheme. The maximum current is set using the [`mdtool config current`](mdtool_config_current) command, and by default, it is usually set to 10A. This setting can be saved in the non-volatile memory so that it is always loaded on the actuator power-up. To estimate the maximum current setting for a particular motor, you should use the following formula:

$$I [A] = \frac{\tau [Nm] \frac{1}{G_r}}{K_t[\frac{Nm}{A}]}$$

where
* $ I[A] $ - calculated current in Amps
* $ \tau $ - desired maximum torque
* $ G_r $ - gear ratio
* $ K_t $ - motor’s torque constant

for example let’s calculate the max current limit for AK80-9 motor, for a 2Nm max torque:

$\tau = 2 Nm$

$G_r = 9:1 -> 9$

$K_t = 0.091 Nm/A$

$ I [A] = \frac{2[Nm] \cdot \frac{1}{9}}{0.091[\frac{Nm}{A}]} $

$ I [A] \approx  2.44A $

```{note}
Usually this limit should be set to the highest peak torque that is allowed in the system so that it doesn't limit the actuator performance.
```

Now, to save this value into the MDxx please refer to [`mdtool config current`](mdtool_config_current) command. Don’t forget to save it with the [`mdtool config save`](mdtool_config_save) command.

## Torque Limit

The next limit is the max torque limit which can be set using the CANdle script. This limit applies to maximum torque and is expressed in Nm. It is respected in all motion modes. When target torque, set either by either of the controllers, exceeds the `max torque` param the target torque is limited and a [motion warning](motion_status) is generated.

```{figure} ./images/torque_limit.png
:width: 1000px
:align: center
```

```{note}
if the torque bandwidth is set to a low value it is possible to read torque values that are above limits when external torque is applied (for example during impacts). This is only true in transition states - when the load is constant the limits will work as expected. This is because with low torque bandwidth the internal torque PI controllers may be too slow to compensate for rapidly changing torque setpoint when hitting the torque/current limit. If you care about accurate torque readout be sure to play with the torque bandwidth parameter and possibly increase it from the default level.
```

## Velocity Limit

Velocity limit is respected only in Velocity PID / Profile Velocity and Impedance / Position PID / Profile Position modes. When target velocity, set either by the user or the Position PID, exceeds the `max velocity` param the target is limited, and a [motion warning](motion_status) is generated.

```{figure} ./images/velocity_limit.png
:width: 1000px
:align: center
```

## Position Limit

Position limit is respected only in Impedance / Position PID / Profile Position modes. When target position, set by the user, exceeds the `<position limit min : position limit max>` param range the target is limited to that range, and a [motion warning](motion_status) is generated. Attempt to start the motor outside the range will generate a motion error.

```{figure} ./images/position_limit.png
:width: 1000px
:align: center
```

(motion_modes)=
# Motion modes

```{hint}
TL;DR: [MD x CANdle - motion modes](https://www.youtube.com/watch?v=XnD8sG22zro&t=0s)
```

To control the motor shaft with the user’s command MDxx is equipped with multiple control loops. All controllers are based on a regular PID controller design with an anti-windup block. The saturator (anti-windup) is an additional module that acts as a limiter to the ‘I’ part of the controller, as in many systems, the error integration may grow to very large numbers, completely overwhelming ‘P’ and ‘D’ parts of the controller.


```{figure} ./images/limiters.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## Velocity PID

Velocity PID controller calculates velocity error based on target velocity (set by user) and estimated velocity read from the encoder. Its output is a torque command for the internal current/torque controller. The parameters of the controller are:
* Velocity Target (in [rad/s])
* kP (proportional gain)
* kI (integral gain)
* kD (derivative gain)
* I windup (maximal output of an integral part in[Nm])

```{figure} ./images/velocity_pid.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## Position PID

Position PID mode is the most common controller mode used in industrial servo applications. In MDxx, it is implemented as a cascaded PID controller. This means that the controller is working in two stages, firstly the position error is calculated, and it is then passed to the Position PID, which outputs the target velocity. This value is then passed as an input to the Velocity PID controller, which outputs commanded torque. This mode uses both Position PID and Velocity PID and thus needs the following parameters:

For Position PID:

* Position Target (in [rad])
* kP (proportional gain)
* kI (integral gain)
* kD (derivative gain)
* I windup (maximal output of an integral part in [rad/s])

For Velocity PID:

* Velocity Target (in [rad/s])
* kP (proportional gain)
* kI (integral gain)
* kD (derivative gain)
* I windup (maximal output of an integral part in[Nm])

To properly tune the controller, it is recommended to first tune the velocity controller (in velocity PID mode), and then the position PID. The controller can be described with a diagram:

```{figure} ./images/position_pid.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## Impedance PD

Impedance Control mode is a popular choice for mobile or legged robots, as well as for any compliant mechanism. The main idea behind it is to mimic the behavior of a torsional spring with variable stiffness and damping. The parameters of the controller are:
* Position Target
* Velocity Target
* kP (position gain)
* kD (velocity gain)
* Torque Feed Forward (Torque FF) 

The torque output is proportional to the position error and velocity error and additionally supplemented with a torque command from the user. Here are some of the most common applications for this control mode:
* <b>Spring-damper mechanism</b> - when velocity target is set to 0, impedance controllers kP gain acts as the virtual spring stiffness and kD as its damping coefficient. 
Example use case: a variable suspension for a wheeled robot, where suspension stiffness can be regulated by kP, damping by kD, and height (clearance) by changing the target position;
* <b>High-frequency torque controller</b>, where its targets and gains can act as stabilizing agents to the torque command.
Example use case: In legged robots, force control can be achieved by advanced control algorithms, which usually operate at rates below 100 Hz. It is usually enough to stabilize the robot but too slow to avoid vibrations. Knowing desired robot's joint positions, velocities, and torques, drives can be set to produce the proper torque and hold the position/velocity with small gains. This would compensate for any high-frequency oscillations (vibrations) that may occur, as the impedance controller works at 40kHz (much faster than <100 Hz).
* <b>Raw torque controller</b> - when kP and kD are set to zero, the torque_ff command is equal to the output controller torque. 
* <b>Idle</b> - when kP and kD are set to zero, and the torque_ff command is equal to zero, the motor shaft will be free to rotate. When the drive is disabled it connects all the windings together for safety. This mode can be useful for enabling free rotation of the shaft, but the rotational energy shoudl not be too high as the voltages induced in the motor windings coudl break the driver. 

The impedance controller is relatively simple and works according to the schematic below:

```{figure} ./images/impedance.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

# Velocity Profile 

The velocity profile motion mode uses trapezoidal velocity profiles to achieve smooth velocity changes with predefined acceleration and deceleration. The trajectory generator module interpolates between two velocity setpoints to achieve constant acceleration.

```{figure} ./images/velocity_profile_generator_CANdle.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

# Position Profile

The position profile motion mode uses trapezoidal velocity profiles to achieve smooth position changes with predefined acceleration, deceleration, and velocity. The trajectory generator module interpolates between two position setpoints to achieve constant acceleration, and linearly changing velocity.

```{figure} ./images/position_profile_generator_CANdle.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```


## Controller implementation

Controller implementation can be useful for simulating the actuators in virtual environments. Please find the PID and impedance C/C++ language implementations below:

```
float mab_controller_performPid(PID_controller *c, float act_value)
{
	c->error_last = c->error;
	c->error = c->target - act_value;
	c->integrator += c->error*c->dt;
	c->integrator = mab_commons_range(c->integrator, -c->integrator_windup, c->integrator_windup);
	c->de = (c->error - c->error_last)/c->dt;
	c->output = mab_commons_range( (c->kp * c->error + c->ki * c->integrator + c->kd * c->de) , -c->output_max, c->output_max);
	return c->output;
}
```

```
float mab_controller_performImpedanceController(Impedance_controller *c, float position, float velocity)
{
	c->output = c->setTorque + c->kp * (c->positionTarget - position) + c->kd * (c->velocityTarget - velocity);
	c->output = mab_commons_range(c->output, -c->outputMax, c->outputMax);
	return c->output;
}
```
(Motion_controller_tuning)=
# Motion controller tuning

```{hint}
The best way to get started with tuning is to copy the [default gains](https://2d033567-d193-42c8-9e42-4931131b206f.usrfiles.com/ugd/2d0335_4f52c3bdab9e4b1cbd2cec68e48b7e14.pdf) and tweak them. You can treat this section as our recommendation for tuning the controllers, but [online articles](https://www.motioncontroltips.com/how-are-servo-system-velocity-control-loops-tuned/) can be useful as well 
```

The first step to correctly set up the gains is to start with our [default gains](https://2d033567-d193-42c8-9e42-4931131b206f.usrfiles.com/ugd/2d0335_4f52c3bdab9e4b1cbd2cec68e48b7e14.pdf). There are three sets of default gains that are set on each motor power up and thus they allow for restoring the actuator to a default state in case some gains were set incorrectly by the user. These gains are also a great starting point for user modifications when the actuator has to be used in a specific application requiring high positioning accuracy or very dynamic movements.

```{note}
Default gains are set to work with CANdle examples. This way they can be assumed to be universal but it does not have to always be the case
```

```{hint}
When something does go wrong during the tuning process just power-cycle the actuator - the default gains will be restored. 
```

```{warning}
Always keep your safety limits low when experimenting with gains. Gains not suitable for your system may cause oscillations and unstable operation of the MD-based actuators
```

## Velocity PID / Velocity Profile 

1. Start by slowly increasing kp gain of the controller keeping ki kd and iWindup set to zero
2. increase set iWindup to 1.0 and try increasing ki to see if it helps to reach the setpoint velocity
3. Generally try to avoid using kd

## Position PID / Position Profile

1. Tune the Velocity PID first - make sure in Velocity PID mode the actuator is able to follow the setpoints
2. Start by slowly increasing kp gain of the position controller keeping ki kd and iWindup set to zero
3. Increase set iWindup to 1.0 and try increasing ki to see if it helps to reach the setpoint velocity
4. Generally try to avoid using kd

## Impedance PD

1. Increase kp to the point you're satisfied with the stiffnes of the output shaft (the spring coefficient)
2. Increase kd to the point youre satified with the damping of the output shaft (the damping coeficient)
3. Avoid setting kd too high - it may cause severe vibrations.

## Current PI 

Current/torque PI is the lowest-level controller. Its gains are not directly user-configurable, however, they can be modified using the bandwidth parameter. Please see the calibration section for more insight on the topic. 
