(canopen_setup)=
# Setting Up a New Motor

This is the commissioning order for a drive that has never been configured. The order matters: some
objects are rejected until others hold sensible values, and calibration needs the motor parameters
to already be in place.

Everything here is done with SDO writes. Read [System Units](canopen_units) first, because most of
these objects are scaled integers.

## 1. Establish communication

A factory drive answers on node ID 100 at 1 Mbit/s. Read Device Type 0x1000 and confirm it returns
0x00020192. If you need a different node ID, write it to 0x2000:1 and be aware the drive switches
identifiers immediately.

| Object   | Name   | Range    |
| -------- | ------ | -------- |
| 0x2000:1 | CAN ID | 10 to 127 |

## 2. Motor parameters

| Object   | Name                       | Unit and range                    |
| -------- | -------------------------- | --------------------------------- |
| 0x2000:2 | Pole Pairs                 | 2 to 42                           |
| 0x2000:3 | Phase Inductance           | H, 5e-9 to 0.1                    |
| 0x2000:4 | Phase Resistance           | ohm, 0.005 to 20                  |
| 0x2000:5 | Torque Bandwidth           | Hz, 10 to 2500                    |
| 0x2000:6 | Motor Name                 | up to 24 characters               |
| 0x2000:7 | Motor Shutdown Temperature | degrees Celsius, 10 to 120        |
| 0x2000:9 | Motor Torque Constant      | Nm/A, greater than 0              |
| 0x2000:A | Motor KV Rating            | RPM/V, greater than 0             |

Motor Name is longer than 4 bytes, so it needs a segmented SDO write. An expedited write is
rejected.

```{important}
The torque constant and the KV rating describe the same property, so the order you write them in
decides which one wins. Writing KV recomputes the torque constant from it, as 60 divided by 2 pi
times KV. Writing the torque constant afterwards leaves KV untouched.

Write KV first and let the drive derive the torque constant, or write the torque constant last if
your motor data sheet gives a measured value you trust more. KV is stored as a whole number, so a
fractional value reads back rounded down.
```

## 3. Gear ratio

| Object   | Name              |
| -------- | ----------------- |
| 0x6091:1 | Motor Revolutions |
| 0x6091:2 | Shaft Revolutions |

A 1:9 gearbox is Motor Revolutions 9 and Shaft Revolutions 1. Set this before the limits, because
every position, velocity and torque object refers to the output shaft.

## 4. Ratings, then limits

```{important}
Write Motor Rated Torque and Motor Rated Current **before** any of the objects scaled against them.
While either is zero, writes to 0x6071, 0x6072, 0x6073 and 0x6077 abort with 0x08000020.
```

| Object | Name                | Unit                          |
| ------ | ------------------- | ----------------------------- |
| 0x6076 | Motor Rated Torque  | mNm                           |
| 0x6075 | Motor Rated Current | mA                            |

Then the limits:

| Object   | Name               | Unit                                |
| -------- | ------------------ | ----------------------------------- |
| 0x6072   | Max Torque         | 1/1000 of rated torque              |
| 0x6073   | Max Current        | 1/1000 of rated current             |
| 0x6080   | Max Motor Speed    | micro-revolutions per second        |
| 0x607D:1 | Min Position Limit | micro-revolutions                   |
| 0x607D:2 | Max Position Limit | micro-revolutions                   |

Setting both software position limits to the same value disables position limiting.

## 5. Encoders

The main encoder is onboard. The auxiliary encoder is optional and mounted on the output shaft. Both
take a type identifier:

| Value | Encoder              |
| ----- | -------------------- |
| 0     | None                 |
| 1     | AMS5047, on axis     |
| 2     | AMS5047, off axis    |
| 3     | RLS 17-bit, RS422    |
| 4     | TLI, off axis        |
| 5     | iC-TW39, on axis     |
| 6     | iC-TW39, off axis    |
| 8     | AMS5047, onboard     |
| 9     | RLS 17-bit, SPI      |
| 10    | RLS Orbis, RS422     |
| 11    | CE300                |

See [Encoders](aux_encoders) for which physical part each identifier refers to and how to mount it.
A type the drive cannot use on that port is rejected with abort 0x06090030.

| Object   | Name                       | Values                                  |
| -------- | -------------------------- | --------------------------------------- |
| 0x2001:1 | Main Encoder Type          | see table above                         |
| 0x2001:2 | Main Encoder Direction     | -1.0 or 1.0 only                        |
| 0x2002:1 | Auxiliary Encoder Type     | see table above                         |
| 0x2002:2 | Auxiliary Encoder Direction | -1.0 or 1.0 only                       |
| 0x2002:3 | Auxiliary Encoder Mode     | 0 none, 1 startup, 2 motion, 3 report   |
| 0x2002:4 | Calibration Mode           | 0 full, 1 direction only                |

[Aux Encoder Modes](aux_encoders) explains what each mode does. Changing 0x2002:3 sets the restart
required warning in Misc Status; the new mode takes effect after the next reboot.

## 6. Controller gains

| Object | Controller             | Sub-indices                    |
| ------ | ---------------------- | ------------------------------ |
| 0x2010 | Position PID           | 1 Kp, 2 Ki, 3 Kd, 4 Integral Limit |
| 0x2011 | Velocity PID           | 1 Kp, 2 Ki, 3 Kd, 4 Integral Limit |
| 0x2012 | Impedance PD           | 1 Kp, 2 Kd                     |

All gains are IEEE-754 single precision and must be zero or positive. Negative values abort with
0x06090030. [Motion controller tuning](motion_modes) covers how to choose them.

## 7. Profile settings

| Object | Name                    | Unit                                     |
| ------ | ----------------------- | ---------------------------------------- |
| 0x6083 | Profile Acceleration    | micro-revolutions per second squared     |
| 0x6084 | Profile Deceleration    | micro-revolutions per second squared     |
| 0x6085 | Quick Stop Deceleration | micro-revolutions per second squared     |
| 0x6067 | Position Window         | micro-revolutions                        |
| 0x606D | Velocity Window         | micro-revolutions per second             |

Profile Acceleration defaults to 0, which means a drive straight out of the box will not move in
either profile mode. Set it before trying Profile Position or Profile Velocity.

Quick Stop Deceleration is also the rate used when the
[heartbeat consumer](canopen_nmt) detects a lost master, so give it a value you are happy with as an
emergency stop.

## 8. Save

Write 1 to Save Config 0x2023:1, or write the signature 0x65766173 to the standard
[Store Parameters](canopen_diagnostics) object 0x1010:1. The two do the same thing. The drive writes
flash and reboots, so expect it to disappear from the bus for a moment. Everything up to this point
lives in RAM only.

## 9. Calibrate

Run these in order, each by writing 1, and wait for the routine in progress bit in Misc Status
0x2022:9 to clear between them. Each routine saves and reboots on success.

1. **0x2023:6 Calibrate Current PI Gains.** Computes the current loop from the resistance,
   inductance and torque bandwidth you entered.
2. **0x2023:4 Run Calibration.** Calibrates the motor and main encoder. The shaft moves, so make
   sure it is free to turn.
3. **0x2023:5 Run Auxiliary Encoder Calibration.** Only if an auxiliary encoder is fitted. It is
   skipped silently when the type is None or the mode is report.

```{warning}
Calibration drives the motor. Clear the workspace and make sure nothing is attached that could be
damaged by unexpected motion.
```

## 10. Verify

- Read Config Status 0x2022:10. The saving required bit should be clear.
- Read the encoder status registers 0x2022:2 and 0x2022:3, and Calibration Status 0x2022:4. All
  should be zero.
- Optionally run Test Main Encoder 0x2023:2 and Test Auxiliary Encoder 0x2023:3.

## 11. First move

1. Select a mode, for example write 3 to 0x6060 for Profile Velocity, and read 0x6061 back.
2. Write a small Target Velocity to 0x60FF.
3. Write 0x0006 then 0x000F to Controlword 0x6040 and confirm Statusword 0x6041 reads 0x0027.
4. Stop by writing 0x0002 for quick stop, then 0x0000.

See [State Machine](canopen_state_machine) and [Modes of Operation](canopen_modes) for the detail.

```{note}
`candletool` can do all of this for you over a CANdle device, including reading and writing whole
configuration files. See the [CANdle SDK](mdco) documentation for the `candletool mdco` commands.
```
