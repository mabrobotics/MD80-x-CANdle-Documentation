# Configuration Files

Every PDS and MD device has a certain configuration that is dependent on the hardware application
intended to be used. MAB Robotics uses .cfg files written in TOML format to store the configuration
of the devices. These files can be used to configure the devices using the `candletool` command line
interface.

## Configuration files for MD devices

Exemplary MD configuration files can be found
[here](https://github.com/mabrobotics/CANdle-SDK/tree/main/candletool/template_package/etc/candletool/config/motors).
Shown bellow is an example of a configuration file for AK10-9 with MD80:

```
[motor]
name = AK10-9
pole pairs = 21.0
kv = 100.0
torque constant = 0.095
gear ratio = 0.11111
max current = 22.0
torque bandwidth = 500.0
shutdown temp = 80.0

[limits]
max torque = 10.0
max velocity = 20.0
max position = 100.0
min position = -100.0
max acceleration = 100.0
max deceleration = 100.0

[profile]
acceleration = 10.0
deceleration = 10.0
velocity = 20.0

[output encoder]
output encoder = 0
output encoder mode = 0

[position pid]
kp = 30.0
ki = 0.5
kd = 0.0
windup = 1.0

[velocity pid]
kp = 2.0
ki = 0.5
kd = 0.0
windup = 0.1

[impedance pd]
kp = 3.5
kd = 0.25
```

The `[motor]` section represent hardware motor that the MD is connected to. The rest of the
parameters depend on the application and can be set to different values. The configuration file can
be used to configure the MD device using the `candletool md config upload` command.

## Configuration files for PDS device

PDS devices configuration depends on the modules that they are equipped with.

Exemplary configuration files can be found below:

```
[control_board]
can id = 120
can baud = 1M
shutdown time = 5000  ; Shutdown time [ ms ]
battery level 1 = 20000  ; Battery monitor lvl 1 [ mV ]
battery level 2 = 24000  ; Battery monitor lvl 2 [ mV ]
br socket = 0  ; Socket index where corresponding Brake Resistor is connected
br trigger voltage = 100000  ; Brake resistor trigger voltage [ mV ]
[socket 1]
type = ISOLATED_CONVERTER
temperature limit = 80.0  ; Temperature limit [ ^C ]
ocd level = 45000  ; Over-current detection level [ mA ]
ocd delay = 1000  ; Over-current detection delay [ ms ]
[socket 2]
type = POWER_STAGE
temperature limit = 80.0  ; Temperature limit [ ^C ]
ocd level = 45000  ; Over-current detection level [ mA ]
ocd delay = 1000  ; Over-current detection delay [ ms ]
br socket = 0  ; Socket index where corresponding Brake Resistor is connected
br trigger voltage = 100000  ; Brake resistor trigger voltage [ mV ]
autostart = OFF
[socket 3]
type = BRAKE_RESISTOR
temperature limit = 80.0  ; Temperature limit [ ^C ]
[socket 4]
type = NO MODULE
[socket 5]
type = NO MODULE
[socket 6]
type = NO MODULE
```

A template configuration file can be created using the `candletool pds read_cfg` command. The
modified configuration file can be used to configure the PDS device using the
`candletool pds setup_cfg` command.

## Configuration files for MD device with CANOpen communication

MD using can open communication need to have special config file.

Exemplary configuration files can be found below:

```
[motor]
name = AK10-9
pole pairs = 21.0
kv = 100.0
torque constant = 0.095
gear ratio = 0.11111
torque bandwidth = 500.0
shutdown temp = 80.0

[limits]
rated torque = 1000
max torque = 10000
rated current = 1000
max current = 22000
max velocity = 20
max position = 2147483647
min position = -2147483648
max acceleration = 100.0
max deceleration = 100.0

[profile]
acceleration = 10.0
deceleration = 10.0
velocity = 20.0

[output encoder]
output encoder = 0
output encoder mode = 0

[position pid]
kp = 30.0
ki = 0.5
kd = 0.0
windup = 1.0

[velocity pid]
kp = 2.0
ki = 0.5
kd = 0.0
windup = 0.1

[impedance pd]
kp = 3.5
kd = 0.25
```
