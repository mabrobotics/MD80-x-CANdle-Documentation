# Common Issues and FAQ

## MDxx is not detected on "mdtool ping all" command

There might be several reasons why MD controllers are not showing up in the mdtool ping all command output. Please ensure you've check the things listed below: 

1. Check the power supply - when powered the MDxx's onboard LEDs should be blinking. The LEDs are located under the connectors near the PCB edge.
2. Check the LED blink pattern - if red and green LEDs are blinking one after another quickly in 4s intervals this means you need to download the firmware using [MAB_CAN_Flasher](mab_can_flasher) program with `id 9` and `wait` flag, ex.: `./MAB_CAN_Flasher --id 9 --baud 1M --wait`. If the red led is on and the green one is blinking in 1s intervals this means there is an error in the setup that can be checked using [mdtool setup info](mdtool_setup_info). If only the green LED is blinking in 1s intervals the MD8xx should operate and be discovered without issues. In case it's not please check the cabling one more time. 

## How to check if my motor is operating properly

First thing to check is the [`mdtool setup info`](mdtool_setup_info) command output. If there are no errors (meaning the error field are empty or show 'ALL OK" message) the drive did not detect any issues by itself. The other thing is to make sure that the actuator runs smoothly - such that there is no excessive cogging torque when rotating. You can check it using [`mdtool test move`](mdtool_test_move) command - for example by commanding 0 position and moving the rotor by hand - such test makes easy to determine if there is excessive cogging torque. You can also use the Python/C++ examples to rotate the motor. The last thing to check is the motion parameters - position velocity and torque. You can check them by looking at the [`mdtool encoder`](mdtool_encoder) command output. If any of these quantities look suspicious feel free to contact us using: [contact@mabrobotics.pl](https://www.mabrobotics.pl/contact).

## Motor terminals not soldered properly

In case you have ordered the MDxx controllers without the MAB assembly option you will have to make sure the controller is soldered correctly to the motor. Usually, hobby motors have multiple wires wound in parallel on each motor phase, and it is crucial to solder ALL wires to the controller. Leaving a single string of wire can lead to an imbalance between the phases, which in the best scenario will cause the calibration to fail and in the worst will cause large torque variations (large cogging torque). 

```{warning}
Operating such an improperly configured motor can lead to hazardous situations for both the operator and the driver. 
```

##  Failed calibration

The calibration can fail for several reasons, yet the most common one is just improperly soldered motor wires. In this case, you’ll see the ERROR_CALIBRATION general error or ERROR_CALIBRATION and ERROR_PARAM_IDENT. These two errors will also show up when automatic parameter identification fails. In this case, rerunning the calibration should fix the issue. ERROR_POLE_PAIR_DET error is shown in case the automatic pole pair detection algorithm detected a different pole pair number (compared to the one form the *.cfg file) or it failed due to high rotor friction/external load, which stopped the rotor during the process. 

The other most common reason is that the eccentricity calibration is interrupted by either a large load on the motor shaft or the encoder placed non-axially in regard to the magnet mounted on the motor shaft. In this case, you'll see the ERROR_CALIBRATION general error. To fix it be sure to unload the motor shaft completely, make it run smoothly, and make sure the controller is placed axially with respect to the magnet placed on the motor shaft. 

##  Lack of FDCAN termination

Proper termination on the FDCAN bus is crucial, especially when the string of actuators is long. In case you see some communication errors, or the drives connected to your FDCAN bus string are not discovered correctly using MDtool be sure to check if the termination is present and working (the resistance between CANH and CANL lines should be 60 Ohms - two 120 Ohm resistors in parallel). The termination resistor is embedded in the CANdle device, and can be turned on/off with a physical switch. 

```{hint}
Since version HW2.0 the termination resistor can be mounted on demand on the MD controllers. Please check out the [`mdtool config can`](mdtool_config_can) command for more information.
```

##  Different FDCAN speeds between actuators

MD x CANdle ecosystem is not adopted for working with actuators of different FDCAN baudrates. Trying to control actuators with different baud rates on a common FDCAN bus can cause the communication to fail or not start at all. This is why it is crucial to make sure when you call the [`mdtool ping all`](mdtool_ping) command, all discovered MD controllers lie in a single baudrate category. If that’s not the case, use the [`mdtool config can`](mdtool_config_can) command to fix it. 

##  Too-low torque bandwidth setting

When the torque bandwidth is set to a too low value it can cause the motor to behave improperly in highly dynamic scenarios, for example, impacts. Because with low torque bandwidth, the torque controller gains are set so that the controller is slow, it might not be able to keep up with the changing setpoint value. In order to fix this issue, you can calibrate the motor for a higher torque bandwidth frequency using [`mdtool config bandwidth`](mdtool_config_bandwidth) command. This has a disadvantage connected to it - the higher the bandwidth the more audible noise you will hear coming from the motor.
