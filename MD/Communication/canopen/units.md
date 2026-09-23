(canopen_units)=
# System Units

CANopen carries integers, not physical quantities. Every object in the MD object dictionary uses one
of the scalings below. Getting this wrong is the most common cause of a drive that moves a thousand
times too far, so read this page before writing any setpoint.

## Position, velocity and acceleration

The drive works in **micro-revolutions of the output shaft**. One full output revolution is
1 000 000 increments.

| Quantity     | Unit                          | Objects                                              |
| ------------ | ----------------------------- | ---------------------------------------------------- |
| Position     | micro-revolutions             | 0x6064, 0x607A, 0x6067, 0x607B, 0x607D, 0x2002:5     |
| Velocity     | micro-revolutions per second  | 0x606C, 0x60FF, 0x6080, 0x2002:6                     |
| Acceleration | micro-revolutions per second squared | 0x6083, 0x6084, 0x6085                        |

The drive publishes these scalings through the CiA 402 SI unit objects, which are read-only:

| Object | Name                | Value      |
| ------ | ------------------- | ---------- |
| 0x60A8 | SI Unit Position    | 0xFAB40000 |
| 0x60A9 | SI Unit Velocity    | 0xFAB40300 |
| 0x60AA | SI Unit Acceleration | 0xFAB45700 |

Converting to and from radians, which is what the MD Protocol and the CANdle SDK use:

```
increments = radians * 1000000 / (2 * pi)
radians    = increments * (2 * pi) / 1000000
```

Some worked values:

| Physical value      | Object value |
| ------------------- | ------------ |
| 1 revolution        | 1 000 000    |
| 90 degrees          | 250 000      |
| 1 rad               | 159 155      |
| 1 rev/s (60 rpm)    | 1 000 000    |
| 1 rad/s             | 159 155      |

Position is multi-turn and signed. The full INT32 range covers roughly plus or minus 2147 output
revolutions before the counter wraps.

```{note}
All of these are **output shaft** quantities. The gear ratio in 0x6091 is applied by the drive, so
you never convert for the gearbox yourself.
```

## Torque and current

Torque and current setpoints are expressed in **thousandths of the corresponding rated value**, as
CiA 402 requires. The rated values themselves are absolute.

| Object | Name                 | Unit                              |
| ------ | -------------------- | --------------------------------- |
| 0x6076 | Motor Rated Torque   | mNm                               |
| 0x6071 | Target Torque        | 1/1000 of Motor Rated Torque      |
| 0x6072 | Max Torque           | 1/1000 of Motor Rated Torque      |
| 0x6077 | Torque Actual Value  | 1/1000 of Motor Rated Torque      |
| 0x6075 | Motor Rated Current  | mA                                |
| 0x6073 | Max Current          | 1/1000 of Motor Rated Current     |

For example, with Motor Rated Torque set to 1000 (1 Nm), a Target Torque of 250 commands 0.25 Nm,
and a Max Torque of 2000 allows twice the rated torque.

```{important}
Motor Rated Torque and Motor Rated Current must be written **before** any of the per-mille objects.
While either rated value is still zero the drive cannot compute the scaling and aborts the transfer
with code 0x08000020, *data cannot be transferred or stored to the application*.
```

## Other quantities

| Object   | Name                       | Unit                                   |
| -------- | -------------------------- | -------------------------------------- |
| 0x6079   | DC Link Circuit Voltage    | mV                                     |
| 0x2004:1 | Power Stage Temperature    | degrees Celsius                        |
| 0x2004:2 | Motor Temperature          | degrees Celsius                        |
| 0x2000:3 | Phase Inductance           | H, IEEE-754 single precision           |
| 0x2000:4 | Phase Resistance           | ohm, IEEE-754 single precision         |
| 0x2000:5 | Torque Bandwidth           | Hz                                     |
| 0x2000:7 | Motor Shutdown Temperature | degrees Celsius                        |
| 0x2000:9 | Motor Torque Constant      | Nm/A, IEEE-754 single precision        |
| 0x2000:A | Motor KV Rating            | RPM/V, IEEE-754 single precision       |
| 0x2003:2 | Torque Sensor Value        | Nm, IEEE-754 single precision          |
| 0x1017   | Producer Heartbeat Time    | ms                                     |
| 0x6091:1 | Motor Revolutions          | dimensionless                          |
| 0x6091:2 | Shaft Revolutions          | dimensionless                          |

Controller gains in 0x2010, 0x2011 and 0x2012 are IEEE-754 single precision values and are not
scaled. They operate on the shaft quantities described above.

```{note}
Every multi-byte value, including the floating point ones, is transferred little endian. Some
CANopen configuration tools display REAL32 objects as raw integers. If a gain reads back as a large
meaningless number, the tool is showing you the bit pattern rather than the float.
```
