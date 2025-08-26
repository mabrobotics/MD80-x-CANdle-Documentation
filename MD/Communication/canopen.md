# CANopen

MD controllers are capable of supporting CANopen communication protocol according the CiA402 device
profile. For further details, please examine the Object Dictionary chapter that contains the
communication objects that are used to exchange data.

```{note}
Make sure you've contacted MABRobotics for the appropriate software update, as the default MD flasher
only supports CANdle protocol. 
```

## [Object Dictionary](./canopen_od.md)

MD controllers follow an object dictionary, that is consistent with CIA402 device profile. You can
see full documentation, along with corresponding .eds files in the
[Object Dictionary section of the documentation](./canopen.md)

## Setting up a new motor

To set up a new motor make sure the drive is in the "switch on disabled" state. After that make sure
you set up the following registers:

**1. Motor Parameters:**

- 0x6075:0 - Rated Current
- 0x6076:0 - Rated Torque
- 0x6072:0 - Max Torque
- 0x6072:0 - Max Current
- 0x6080:0 - Max Speed
- 0x2000:1 - Pole Pairs
- 0x2000:2 - Torque Constant
- 0x2000:5 - Torque Bandwidth
- 0x2000:7 - Motor Shutdown Temp
- 0x2000:8 - Gear Ratio

**2. Velocity PID gains:**

- 0x2001:1 - Kp
- 0x2001:2 - Ki
- 0x2001:3 - Kd
- 0x2001:4 - Integral Limit

**3. Position PID gains:**

- 0x2002:1 - Kp
- 0x2002:2 - Ki
- 0x2002:3 - Kd
- 0x2002:4 - Integral Limit

**4. Profile velocity/position settings:**

- 0x6081 - Profile Velocity
- 0x6083 - Profile Acceleration
- 0x6084 - Profile Deceleration
- 0x6085 - Quick Stop Deceleration

```{note}
Remember to save the parameters - please see the last chapter 
```

## Setting up an external encoder

Setup of the external encoder should be done after the motor has been configured, as suggested in
previous paragraph. To setup the output encoder the following fields need to be filled:

- 0x2005:1 - Output Encoder Type (please see [output encoder](output_encoder))
- 0x2005:2 - Calibration Mode (please see [output encoder calibration](output_encoder_calibration))
- 0x2005:3 - Mode (please see [output encoder](output_encoder))

```{note}
Remember to save the parameters - please see the last chapter 
```

## Saving and Calibrating

After the parameters have been filled there are two more steps to follow - save to non-volatile
memory and calibrate:

1. Run [store parameters](store_parameters) routine using 0x1010:1:

   - make sure the state machine is in "switch on disabled" state (write 0x8 to controlword 0x6040)
   - write 0x65766173 to 0x1010:1
   - wait for the drive to reboot

1. Run [calibration routine](system_command) using 0x2003:3 (and output encoder calibration routine
   0x2003:4 if output encoder is present)

   - make sure the state machine is in "operational" state (write sequentially 0x8, 0x6, 0xf to
     controlword 0x6040, and check if the statusword 0x6041 is 0x39)
   - make sure the drive is in "service" operation mode (write -2 to Modes Of Operation 0x6060)
   - write 1 to 0x2003:3 to start the calibration
   - wait for the drive to reboot
