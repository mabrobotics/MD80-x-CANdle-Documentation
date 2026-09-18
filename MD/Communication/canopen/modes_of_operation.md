(canopen_modes)=
# Modes of Operation

The mode of operation selects which controller runs inside the drive and therefore which target
objects have any effect. Write it to Modes of Operation 0x6060 and read it back from Modes of
Operation Display 0x6061.

The underlying controllers are the same ones the MD Protocol exposes. For the control theory, tuning
advice and block diagrams, see [Motion Control](motion_modes). This page covers only how to reach
them over CANopen.

## Supported modes

| Value | Mode                   | Controller             | Setpoint objects                  |
| ----- | ---------------------- | ---------------------- | ---------------------------------- |
| -3    | Impedance              | [Impedance PD](impedance-pd) | 0x607A, 0x60FF, 0x6071      |
| -2    | Service                | none, motor idle       | none                               |
| 0     | Idle                   | none, motor idle       | none                               |
| 1     | Profile Position       | trajectory into [Velocity PID](velocity-pid) | 0x607A, 0x60FF     |
| 3     | Profile Velocity       | trajectory into [Velocity PID](velocity-pid) | 0x60FF             |
| 8     | Cyclic Sync Position   | [Position PID](position-pid) cascade | 0x607A                     |
| 9     | Cyclic Sync Velocity   | [Velocity PID](velocity-pid) | 0x60FF                             |

Supported Drive Modes 0x6502 reads 0x00000185, which advertises Profile Position, Profile Velocity,
Cyclic Synchronous Position and Cyclic Synchronous Velocity. The two manufacturer specific modes,
Impedance and Service, are negative values and are not represented in that bit field.

```{warning}
Writing a value that is not in the table above does not produce an SDO abort. The drive accepts the
write and falls back to Idle, which stops the motor. Always read 0x6061 back to confirm the mode you
asked for is the mode you got.
```

```{note}
Reading 0x6060 returns the mode the drive is currently running, not the last value written. It gives
the same answer as 0x6061.
```

## Profile Position, mode 1

The drive runs an internal trajectory generator from the current position to Target Position 0x607A
and feeds the result to the velocity controller.

| Object | Role                               |
| ------ | ---------------------------------- |
| 0x607A | Destination                        |
| 0x60FF | Cruise velocity of the profile     |
| 0x6083 | Acceleration                       |
| 0x6084 | Deceleration                       |
| 0x2011 | Velocity PID gains                 |

```{important}
The cruise velocity comes from Target Velocity 0x60FF, not from Profile Velocity 0x6081. There is no
0x6081 in this object dictionary. A profile position move with 0x60FF left at zero will not move.
```

Completion is reported through bit 15 of Quick Status 0x2022:1, using Position Window 0x6067 as the
tolerance. The statusword does not carry a target reached bit.

## Profile Velocity, mode 3

The trajectory generator ramps from the current velocity to Target Velocity 0x60FF, respecting
0x6083 and 0x6084, and feeds the velocity controller. Position targets are ignored.

Completion is reported through bit 15 of Quick Status 0x2022:1, using Velocity Window 0x606D.

## Cyclic Synchronous Position, mode 8

Target Position 0x607A is applied directly to a cascaded position and velocity controller with no
trajectory generation. The master is responsible for feeding a smooth stream of positions, typically
one per SYNC through a receive PDO.

| Object | Role                  |
| ------ | --------------------- |
| 0x607A | Position setpoint     |
| 0x2010 | Position PID gains    |
| 0x2011 | Velocity PID gains    |
| 0x6080 | Max Motor Speed, clamps the position loop output |

## Cyclic Synchronous Velocity, mode 9

Target Velocity 0x60FF is applied directly to the velocity controller, again with no trajectory
generation. Only the Velocity PID gains in 0x2011 apply.

## Impedance, mode -3

A manufacturer specific mode that makes the drive behave like a spring and damper around a moving
setpoint, with a feed-forward torque. This is the mode to use for compliant and force controlled
applications.

| Object | Role                      |
| ------ | ------------------------- |
| 0x607A | Equilibrium position      |
| 0x60FF | Equilibrium velocity      |
| 0x6071 | Feed-forward torque       |
| 0x2012:1 | Stiffness, Kp           |
| 0x2012:2 | Damping, Kd             |

## Service and Idle

Both leave the motor un-driven. Service, mode -2, is what the drive reports while it is running an
internal routine such as a test or an open loop procedure.

```{note}
Unlike the legacy CANopen firmware, calibration does not require Service mode. The routines in
0x2023 run from whatever mode the drive is in. See [Setting Up a New Motor](canopen_setup).
```

## Changing mode safely

Switch modes with the drive in Switched on rather than Operation enabled, or write a setpoint that
matches the current state before enabling. Changing mode while the drive is following a setpoint
hands control to a different controller with a target that may be stale, which shows up as a jump on
the output shaft.
