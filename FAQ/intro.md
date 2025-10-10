# Common Issues and FAQ

## How to check if my motor is operating properly

First thing to check is the [`candletool md info`](/CANdle-SDK/candletool/Commands.md) command
output. If there are no errors (meaning the error field are empty or show 'ALL OK" message) the
drive did not detect any issues by itself. The other thing is to make sure that the actuator runs
smoothly - such that there is no excessive cogging torque when rotating. You can check it using
[`candletool md test relative`](/CANdle-SDK/candletool/Commands.md) command - for example by
commanding 0 position and moving the rotor by hand - such test makes easy to determine if there is
excessive cogging torque. You can also use the Python/C++ examples to rotate the motor. The last
thing to check is the motion parameters - position velocity and torque. If any of these quantities
look suspicious feel free to contact us using:
[support@mabrobotics.pl](https://www.mabrobotics.pl/contact).

## Motor terminals not soldered properly

In case you have ordered the MD controllers without the MAB assembly option you will have to make
sure the controller is soldered correctly to the motor. Usually, hobby motors have multiple wires
wound in parallel on each motor phase, and it is crucial to solder ALL wires to the controller.
Leaving a single string of wire can lead to an imbalance between the phases, which in the best
scenario will cause the calibration to fail and in the worst will cause large torque variations
(large cogging torque).

```{warning}
Operating such an improperly configured motor can lead to hazardous situations for both the operator and the driver. 
```

## Failed calibration

The calibration can fail for several reasons, yet the most common one is just improperly soldered
motor wires. In this case, you’ll see the ERROR_CALIBRATION general error or ERROR_CALIBRATION and
ERROR_PARAM_IDENT. These two errors will also show up when automatic parameter identification fails.
In this case, rerunning the calibration should fix the issue. ERROR_POLE_PAIR_DET error is shown in
case the automatic pole pair detection algorithm detected a different pole pair number (compared to
the one form the \*.cfg file) or it failed due to high rotor friction/external load, which stopped
the rotor during the process.

The other most common reason is that the eccentricity calibration is interrupted by either a large
load on the motor shaft or the encoder placed non-axially in regard to the magnet mounted on the
motor shaft. In this case, you'll see the ERROR_CALIBRATION general error. To fix it be sure to
unload the motor shaft completely, make it run smoothly, and make sure the controller is placed
axially with respect to the magnet placed on the motor shaft.

## Lack of FDCAN termination

Proper termination on the FDCAN bus is crucial, especially when the string of actuators is long or
selected datarate high. In case you see some communication errors, or the drives connected to your
FDCAN bus string are not discovered correctly using CANdleTool, be sure to check if the termination
is present and working (the resistance between CANH and CANL lines should be 60 Ohms - two 120 Ohm
resistors in parallel, on ends of the bus). The termination resistor is embedded in the CANdle
device, and can be turned on/off with a physical switch.

## MD is not detected on "candletool discover" command

There might be several reasons why MD controllers are not showing up during the discovery. Please
ensure you've check the things listed below:

1. Check the power supply - when powered the MD's onboard LEDs should be blinking. The LEDs are
   located under the connectors near the PCB edge.
1. Check the LED blink pattern - if red and green LEDs are blinking very quickly, this means your MD
   firmware is corrupted and, you need to update/repair it using [candletool md update](downloads).
   If red led is on and the green one is blinking in 1s intervals this means there is an error in
   the setup that can be checked using [candletool md info](/CANdle-SDK/candletool/Commands.md). If
   only the green LED is blinking in 1s intervals the MD should operate and be discovered without
   issues. In case it's not please check the cabling one more time.

## Different FDCAN speeds between actuators

MAB Ecosystem is not adopted for working with actuators of different FDCAN baudrates. Trying to
control actuators with different baud rates on a common FDCAN bus can cause the communication to
fail or not start at all. If that’s the case, use the
[`candletool md can`](/CANdle-SDK/candletool/Commands.md) command to fix it. It may be required to
set up all the driver one by one.

## Can MD FD Protocol and CANOpen work on single bus?

No, they cannot. Both protocols are fundamentally different, and will interfere with each other.

## Too-low torque bandwidth setting

When the torque bandwidth is set to a too low value it can cause the motor to behave improperly in
highly dynamic scenarios, for example, impacts. Because with low torque bandwidth, the torque
controller gains are set so that the controller is slow, it might not be able to keep up with the
changing setpoint value. This can be done by changing the bandwidth in motor .cfg file, or via
register, and recalibrating. This has a disadvantage connected to it - the higher the bandwidth the
more audible noise (hissing) you will hear coming from the motor.

## Should I use FDCAN Protocol or CANOpen?

While CANOpen is well estabilished industry standard protocol, we generally recommend using FDCAN
protocol. CANOpen provides a lot of robustness, it is more complicated and lacks flexibility and
bandwidth, for many modern control systems. If you dont already use CANOpen, FDCAN protocol will
likely be a better option.
