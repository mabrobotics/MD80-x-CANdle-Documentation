# CANopen
MD80 controllers are capable of supporting CANopen communication protocol accoriding the CiA402 device profile. For further details, please examine the Object Dictionary chapter that contains the communication objects that are used to exchange data. 

```{note}
Make sure you've contacted MABRobotics for the aproperiate software update, as the default MD80 flasher only supports CANdle protocol. 
```

## Setting up a new motor

To set up a new motor make sure the drive is in the "switch on disabled" state. After that make sure you set up the following registers: 

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

**5. (Optional) Output encoder setup:**
- 0x2005:1 - Output Encoder Type
- 0x2005:2 - Calibration Mode
- 0x2005:3 - Mode

**After filling up the registers listed above there are two crucial steps:**

1. Run [store parameters](store_parameters) routine using 0x1010:1
2. Run [calibration routine](system_command) using 0x2003:3 (and output encoder calibration routine 0x2003:4 if output encoder is present)



