(config)=
# Config

MDxx's config allows for configuring the controller for a specific motor and the application it is used in. This section will cover the parameters that are used in config files. 

## [motor] section

- `name` - actuator name. Max 20 characters
- `pole pairs` - the number of rotor magnets divided by 2. If you are unsure type zero here - during calibration it will be autodetected. Later on it is advised to retype it after the calibration to the config file. It can be accessed using mdtool setup info or by register access.
- `KV` - declated KV of the motor - its used when torque constant is set to zero. 
- `torque constant` - motor torque constant in Nm/A
- `gear ratio` - gear ratio -> example 6:1 reductor is 0.166666 whereas 1:2 multiplicator is 2
- `max current` - maximum allowable phase (not power supply) current
- `torque bandwidth` - [torque bandwidth](torque_bandwidth) setting
- `shutdown temp` - temperature threshold in [*C] of the motor that will cause a overtemperature stop. Note: this safety limit works only with a motor thermistor connected. If motor temp is 0*C when mdtool setup info is called, the thremistor is not populated or is not working.

## [limits] section
Global limits used to issue warnings or errors.

- `max torque` - maximum allowed torque in Nm
- `max velocity` - maximum allowed velocity in rad/s
- `max position` - maximum position limit in rad 
- `min position` - minimum position limit in rad 
- `max acceleration` - max acceleration in rad/s^2 
- `max deceleration` - max deceleration in rad/s^2 

## [profile] section
These settings are respected in POSITION PROFILE and VELOCITY PROFILE modes.

- `acceleration` - profile acceleration in rad/s^2 
- `deceleration` - profile deceleration in rad/s^2
- `velocity` - profile velocity in rad/s

## [output encoder] section
For more information please refer to [output encoder](output_encoder) section. 

- `output encoder` - valid types: AS5047_CENTER, AS5047_OFFAXIS, MB053SFA17BENT00, CM_OFFAXIS
- `output encoder mode` - valid modes: STARTUP, MOTION, REPORT, CALIBRATED_REPORT

## [position PID] section
Position PID default gains (used at every startup, then can be modified using the C++/Python script, or register access)
- `kp` - proportional gain
- `ki` - integral gain
- `kd` - derivative gain
- `windup` - integral limit 

## [velocity PID] section
Velocity PID default gains (used at every startup, then can be modified using the C++/Python script, or register access)
- `kp` - proportional gain
- `ki` - integral gain
- `kd` - derivative gain
- `windup` - integral limit 

## [impedance PD] section
Impedance PID default gains (used at every startup, then can be modified using the C++/Python script, or register access)
- `kp` - proportional gain
- `kd` - derivative gain
