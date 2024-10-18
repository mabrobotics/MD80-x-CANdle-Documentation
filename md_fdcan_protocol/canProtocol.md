# MD FDCAN communication
The easiest way to communicate with MD controllers is to use a CANdle device connected to a PC. Even though we are aware some customers want to integrate the MD controllers in their product with minimal setup to reduce the costs and the system’s complexity. This manual will guide you through the process of communicating with MD actuators from your custom FDCAN-capable master controller.

## Hardware requirements
The main requirement for the host system is to be equipped with an FDCAN peripheral (either a built-in one or an external one) and an FDCAN transceiver capable of speeds up to 8Mbps. Lower maximum speed transceivers can be used as well, however for the cost of limited update rates. Depending on your custom setup you should be able to integrate a 120 ohm terminating resistor on both ends of your CAN bus.

```{note}
 MD controllers from version 2.0 can be upgraded to software controlled termination. Please contact us for more information
 ```

## Communication Structure

The communication stack is based on a register access using two frames - register read and register write. The list of available registers can be found at the end of this chapter. All fields are little-endian - least significant byte first, and all float fields are 4 bytes long encoded in IEEE-754 standard. 

### Default response

The default response is sent by the drive in case a register write operation was successful. 

<p></p>
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b></b></td>
			<td> <b>BYTE 0</b></td>
			<td> <b>BYTE 1-2</b></td>
			<td> <b>BYTE 3</b></td>
      <td> <b>BYTE 4-7</b></td>
      <td> <b>BYTE 8-11</b></td>
      <td> <b>BYTE 12-15</b></td>
      <td> <b>BYTE 16-19</b></td>
      <td> <b>BYTE 20-23</b></td>
		</tr>
		<tr>
			<td>NAME </td>
			<td>FRAME ID </td>
			<td>QUICK STATUS</td>
			<td>MOTOR TEMPERATURE </td>
      <td>MAIN ENCODER POSITION </td>
      <td>MAIN ENCODER VELOCITY </td>
      <td>MOTOR TORQUE </td>
      <td>OUTPUT ENCODER POSITION </td>
      <td>OUTPUT ENCODER VELOCITY </td>
		</tr>
    <tr>
			<td>TYPE </td>
			<td>uint8_t </td>
			<td>uint16_t </td>
			<td>uint8_t [*C] </td>
      <td>float [rad] </td>
      <td>float [rad/s] </td>
      <td>float [Nm] </td>
      <td>float [rad] </td>
      <td>float [rad/s] </td>
		</tr>
        <tr>
			<td>VALUE </td>
			<td>0x0A </td>
			<td>0x0000 - 0xFFFF </td>
			<td>0 - 255 </td>
      <td>- </td>
      <td>- </td>
      <td>- </td>
      <td>- </td>
      <td>- </td>
		</tr>
	</tbody>
</table>
<p></p>

In case the operation initiated by a frame was unsuccessful the MDxx will not respond. 

### Write register frame

Write register frame is used to modify values of the user-modifiable registers. Only registers with write access can be modified.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td> 
			<td> <b>DRIVE ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-3 </b></td>
      <td> <b>BYTE 4-X </b></td>
      <td> <b>BYTE X+1-X+2 </b></td>
      <td> <b>BYTE X+4-X+Y </b></td>
		</tr>
		<tr>
			<td>WRITE_REGISTER</td>
			<td>10-999</td>
			<td>X (64 max)</td>
			<td>0x40</td>
      <td>0x00</td>
      <td>reg ID</td>
      <td>value</td>
      <td>reg ID</td>
      <td>value</td>
		</tr>
	</tbody>
</table>
<p></p>

Params:
- regID (uint16_t) - first register ID (please see the end of this section)
- value (uint8_t/uint16_t/uint32_t/float/char[]) - first register value to be written
- regID (uint16_t) - second register ID (please see the end of this section)
- value (uint8_t/uint16_t/uint32_t/float/char[]) - second register value to be written
- ... (up to 64 bytes total)

When all registers write operations succeed the drive will respond with default response.

### Read Register Frame

Read register command is used to retrieve certain register values. The actuator will respond with a frame consisting of the addresses and values of the registers issued in the master request. The master request should have the following form: 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>DRIVE ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-3 </b></td>
      <td> <b>BYTE 4-X </b></td>
      <td> <b>BYTE X+1-X+2 </b></td>
      <td> <b>BYTE X+4-X+Y </b></td>
		</tr>
		<tr>
			<td>READ_REGISTER</td>
			<td>10-999</td>
			<td>X (64 max)</td>
			<td>0x41</td>
      <td>0x00</td>
      <td>reg ID</td>
      <td>0x00</td>
      <td>reg ID</td>
      <td>0x00</td>
		</tr>
	</tbody>
</table>
<p></p>

When all read operations succeed the 0x00 fields will be filled with appropriate register data when transmitted back to master by the MDxx controller.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>DRIVE ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-3 </b></td>
      <td> <b>BYTE 4-X </b></td>
      <td> <b>BYTE X+1-X+2 </b></td>
      <td> <b>BYTE X+4-X+Y </b></td>
		</tr>
    <tr>
      <td>Response to register read</td>
      <td>10-999</td>
      <td>X (64 max)</td>
      <td>0x41</td>
      <td>0x00</td>
      <td>reg ID</td>
      <td>reg value</td>
      <td>reg ID</td>
      <td>reg value</td>
    </tr>
	</tbody>
</table>
<p></p>


```{warning}
Frame payload length must not exceed 64 bytes. 
```

### Available registers

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
  <thead>
    <tr style="text-align: center;">
      <th>reg name</th>
      <th>address</th>
      <th>read/write</th>
      <th>size</th>
      <th>limits</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>canId</td>
      <td>0x001</td>
      <td>RW</td>
      <td>uint32_t</td>
      <td>[10-2000]</td>
      <td>FDCAN bus id number</td>
    </tr>
    <tr>
      <td>canBaudrate</td>
      <td>0x002</td>
      <td>RW</td>
      <td>uint32_t</td>
      <td>[1e6;2e6;5e6;8e6]</td>
      <td>FDCAN bus baudrate</td>
    </tr>
    <tr>
      <td>canWatchdog</td>
      <td>0x003</td>
      <td>RW</td>
      <td>uint16_t</td>
      <td>[0-2500]</td>
      <td>FDCAN bus watchdog period in ms</td>
    </tr>
    <tr>
      <td>canTermination</td>
      <td>0x004</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>[0-1]</td>
      <td>CAN termination (available upon request)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>motorName</td>
      <td>0x010</td>
      <td>RW</td>
      <td>char[24]</td>
      <td>-</td>
      <td>motor name</td>
    </tr>
    <tr>
      <td>motorPolePairs</td>
      <td>0x011</td>
      <td>RW</td>
      <td>uint32_t</td>
      <td>[2;225]</td>
      <td>motor pole pair count</td>
    </tr>
    <tr>
      <td>motorKt</td>
      <td>0x012</td>
      <td>RW</td>
      <td>float</td>
      <td>>0</td>
      <td>motor torque constant</td>
    </tr>
    <tr>
      <td>motorKt_a</td>
      <td>0x013</td>
      <td>RW</td>
      <td>float</td>
      <td>>0</td>
      <td>optional parameter for phase specific torque constant</td>
    </tr>
    <tr>
      <td>motorKt_b</td>
      <td>0x014</td>
      <td>RW</td>
      <td>float</td>
      <td>>0</td>
      <td>optional parameter for phase specific torque constant</td>
    </tr>
    <tr>
      <td>motorKt_c</td>
      <td>0x015</td>
      <td>RW</td>
      <td>float</td>
      <td>>0</td>
      <td>optional parameter for phase specific torque constant</td>
    </tr>
    <tr>
      <td>motorIMax</td>
      <td>0x016</td>
      <td>RW</td>
      <td>float</td>
      <td>[1 - peak controller current]</td>
      <td>maximum phase current</td>
    </tr>
    <tr>
      <td>motorGearRatio</td>
      <td>0x017</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>actuator gear ratio (ex 2:1 should be 0.5) <1 - reducer >1 - multiplier</td>
    </tr>
    <tr>
      <td>motorTorqueBandwidth</td>
      <td>0x018</td>
      <td>RW</td>
      <td>uint16_t</td>
      <td>[50-2500]</td>
      <td>torque bandwidth in Hz</td>
    </tr>
    <tr>
      <td>motorFriction</td>
      <td>0x019</td>
      <td>RO</td>
      <td>float32</td>
      <td>-</td>
      <td>UNUSED</td>
    </tr>
    <tr>
      <td>motorStiction</td>
      <td>0x01A</td>
      <td>RO</td>
      <td>float32</td>
      <td>-</td>
      <td>UNUSED</td>
    </tr>
    <tr>
      <td>motorResistance</td>
      <td>0x01B</td>
      <td>RO</td>
      <td>float</td>
      <td>[5mOhm-20Ohm]</td>
      <td>motor resistance in d axis</td>
    </tr>
    <tr>
      <td>motorInductance</td>
      <td>0x01C</td>
      <td>RO</td>
      <td>float</td>
      <td>[5nH-100mH]</td>
      <td>motor inductance in d axis</td>
    </tr>
    <tr>
      <td>motorKV</td>
      <td>0x01D</td>
      <td>RW</td>
      <td>uint16_t</td>
      <td>-</td>
      <td>motor KV rating [RPM/V]</td>
    </tr>
    <tr>
      <td>motorCalibrationMode</td>
      <td>0x01E</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>[0;1]</td>
      <td>FULL = 0, NOPPDET = 1</td>
    </tr>
    <tr>
      <td>motorThermistorType</td>
      <td>0x01F</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>outputEncoder</td>
      <td>0x020</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>[0;1;2;3]</td>
      <td>NONE = 0, AS5047_CENTER = 1, AS5047_OFFAXIS = 2, MB053SFA17BENT00 = 3, CM_OFFAXIS = 4, M24B_CENTER = 5, M24B_OFFAXIS = 6</td>
    </tr>
    <tr>
      <td>outputEncoderDir</td>
      <td>0x021</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>0</td>
      <td>RESERVED</td>
    </tr>
    <tr>
      <td>outputEncoderDefaultBaud</td>
      <td>0x022</td>
      <td>RW</td>
      <td>uint32_t</td>
      <td>115200</td>
      <td>optional parameter for setting default output encoder baudrate</td>
    </tr>
    <tr>
      <td>outputEncoderVelocity</td>
      <td>0x023</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>output encoder velocity in rad/s (calculated in a 5kHz loop)</td>
    </tr>
    <tr>
      <td>outputEncoderPosition</td>
      <td>0x024</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>output encoder position in rad (read in 5kHz loop)</td>
    </tr>
    <tr>
      <td>outputEncoderMode</td>
      <td>0x025</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>[0;1;2;3;4]</td>
      <td>NONE = 0, STARTUP = 1, MOTION = 2, REPORT = 3, MAIN = 4</td>
    </tr>
    <tr>
      <td>outputEncoderCalibrationMode</td>
      <td>0x026</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>[0;1]</td>
      <td>FULL = 0, DIRONLY = 1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>motorPosPidKp</td>
      <td>0x030</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>position PID proportional gain</td>
    </tr>
    <tr>
      <td>motorPosPidKi</td>
      <td>0x031</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>position PID integral gain</td>
    </tr>
    <tr>
      <td>motorPosPidKd</td>
      <td>0x032</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>position PID derivative gain</td>
    </tr>
    <tr>
      <td>motorPosPidWindup</td>
      <td>0x034</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>position PID integral windup limit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>motorVelPidKp</td>
      <td>0x040</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>velocity PID proportional gain</td>
    </tr>
    <tr>
      <td>motorVelPidKi</td>
      <td>0x041</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>velocity PID integral gain</td>
    </tr>
    <tr>
      <td>motorVelPidKd</td>
      <td>0x042</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>velocity PID derivative gain</td>
    </tr>
    <tr>
      <td>motorVelPidWindup</td>
      <td>0x044</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>velocity PID integral windup limit</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>motorImpPidKp</td>
      <td>0x050</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>impedance PD proportional gain</td>
    </tr>
    <tr>
      <td>motorImpPidKd</td>
      <td>0x051</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>impedance PD derivative gain</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>mainEncoderVelocity</td>
      <td>0x062</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>main encoder velocity in rad/s (calculated in a 40kHz loop)</td>
    </tr>
    <tr>
      <td>mainEncoderPosition</td>
      <td>0x063</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>main encoder position in rad (read in 40kHz loop)</td>
    </tr>
    <tr>
      <td>motorTorque</td>
      <td>0x064</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td> motor output shaft torque in Nm (read in 40kHz loop)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>runSaveCmd</td>
      <td>0x080</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>save non-volatile memory</td>
    </tr>
    <tr>
      <td>runTestMainEncoderCmd</td>
      <td>0x081</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>runs main encoder test routine</td>
    </tr>
    <tr>
      <td>runTestOutputEncoderCmd</td>
      <td>0x082</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>runs output encoder test routine</td>
    </tr>
    <tr>
      <td>runCalibrateCmd</td>
      <td>0x083</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>runs main calibration routine</td>
    </tr>
    <tr>
      <td>runCalibrateOutputEncoderCmd</td>
      <td>0x084</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>runs output encoder calibration routine</td>
    </tr>
    <tr>
      <td>runCalibratePiGains</td>
      <td>0x085</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>runs current PI loop calibration routine</td>
    </tr>
    <tr>
      <td>runRestoreFactoryConfig</td>
      <td>0x087</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>reverts config to factory state</td>
    </tr>
    <tr>
      <td>runReset</td>
      <td>0x088</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>resets the controller</td>
    </tr>
    <tr>
      <td>runClearWarnings</td>
      <td>0x089</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>clears all warnings</td>
    </tr>
    <tr>
      <td>runClearErrors</td>
      <td>0x08A</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>clears non-critical errors</td>
    </tr>
    <tr>
      <td>runBlink</td>
      <td>0x08B</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>blinks onboard LEDs</td>
    </tr>
    <tr>
      <td>runZero</td>
      <td>0x08C</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>sets new zero position</td>
    </tr>
    <tr>
      <td>runCanReinit</td>
      <td>0x08D</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>other than 0 to run</td>
      <td>reinitializes can peripheral</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>calOutputEncoderStdDev</td>
      <td>0x100</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>output encoder test result (standard deviation)</td>
    </tr>
    <tr>
      <td>calOutputEncoderMinE</td>
      <td>0x101</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>output encoder test result (min error)</td>
    </tr>
    <tr>
      <td>calOutputEncoderMaxE</td>
      <td>0x102</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>output encoder test result (max error)</td>
    </tr>
    <tr>
      <td>calMainEncoderStdDev</td>
      <td>0x103</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>main encoder test result (standard deviation)</td>
    </tr>
    <tr>
      <td>calMainEncoderMinE</td>
      <td>0x104</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>	main encoder test result (min error)</td>
    </tr>
    <tr>
      <td>calMainEncoderMaxE</td>
      <td>0x105</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>	main encoder test result (max error)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>positionLimitMax</td>
      <td>0x110</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>maximum valid position</td>
    </tr>
    <tr>
      <td>positionLimitMin</td>
      <td>0x111</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>minimum valid position</td>
    </tr>
    <tr>
      <td>maxTorque</td>
      <td>0x112</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>maximum torque</td>
    </tr>
    <tr>
      <td>maxVelocity</td>
      <td>0x113</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>maximum velocity</td>
    </tr>
    <tr>
      <td>maxAcceleration</td>
      <td>0x114</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>maximum acceleration</td>
    </tr>
    <tr>
      <td>maxDeceleration</td>
      <td>0x115</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>maximum deceleration</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>profileVelocity</td>
      <td>0x120</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>profile velocity</td>
    </tr>
    <tr>
      <td>profileAcceleration</td>
      <td>0x121</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>profile acceleration</td>
    </tr>
    <tr>
      <td>profileDeceleration</td>
      <td>0x122</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>profile deceleration</td>
    </tr>
    <tr>
      <td>quickStopDeceleration</td>
      <td>0x123</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>quick stop deceleration in case of a non-critical error</td>
    </tr>
    <tr>
      <td>positionWindow</td>
      <td>0x124</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>position window within position is considered to be reached</td>
    </tr>
    <tr>
      <td>velocityWindow</td>
      <td>0x125</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>velocity window within velocity is considered to be reached</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>motionModeCommand</td>
      <td>0x140</td>
      <td>WO</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>commands a motion mode change: IDLE = 0x00,
          POSITION_PID = 0x01,
          VELOCITY_PID = 0x02,
          RAW_TORQUE = 0x03,
          IMPEDANCE = 0x04,
          POSITION_PROFILE = 0x07,
          VELOCITY_PROFILE = 0x08</td>
    </tr>
    <tr>
      <td>motionModeStatus</td>
      <td>0x141</td>
      <td>RO</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>shows the currently set motion mode</td>
    </tr>
    <tr>
      <td>state</td>
      <td>0x142</td>
      <td>RW</td>
      <td>uint16_t</td>
      <td>-</td>
      <td>returns the internal <a href=../md80_canopen/OD.html#x6040-control-word>state machine</a> state of the controller </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>targetPosition</td>
      <td>0x150</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>sets target position in rad</td>
    </tr>
    <tr>
      <td>targetVelocity</td>
      <td>0x151</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>sets target velocity in rad/s</td>
    </tr>
    <tr>
      <td>targetTorque</td>
      <td>0x152</td>
      <td>RW</td>
      <td>float</td>
      <td>-</td>
      <td>sets target torque in Nm</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>userGpioConfiguration</td>
      <td>0x160</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>0 - OFF, 1 - AUTO-BRAKE, 2 - GPIO INPUT</td>
    </tr>
    <tr>
      <td>userGpioState</td>
      <td>0x161</td>
      <td>RO</td>
      <td>uint16_t</td>
      <td>-</td>
      <td>GPIO input state</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>reverseDirection</td>
      <td>0x600</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>used to change the direction of the main encoder when using other encoders than the onboard one. Always recalibrate after changing this setting</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>shuntResistance</td>
      <td>0x700</td>
      <td>RO</td>
      <td>float</td>
      <td>[0.001 - 0.01]</td>
      <td>Current sense resistor value. Setting this register to a value that is not coherent with the hardware may damage the controller. In this cases warranty is not respected.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>buildDate</td>
      <td>0x800</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>software build date</td>
    </tr>
    <tr>
      <td>commitHash</td>
      <td>0x801</td>
      <td>RO</td>
      <td>char[8]</td>
      <td>-</td>
      <td>commit hash</td>
    </tr>
    <tr>
      <td>firmwareVersion</td>
      <td>0x802</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>hardwareVersion</td>
      <td>0x803</td>
      <td>RO</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>bridgeType</td>
      <td>0x804</td>
      <td>RO</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>type of the mosfet driver</td>
    </tr>
    <tr>
      <td>quickStatus</td>
      <td>0x805</td>
      <td>RO</td>
      <td>uint16_t</td>
      <td>-</td>
      <td>quick status vector</td>
    </tr>
    <tr>
      <td>mosfetTemperature</td>
      <td>0x806</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>power stage temperature</td>
    </tr>
    <tr>
      <td>motorTemperature</td>
      <td>0x807</td>
      <td>RO</td>
      <td>float</td>
      <td>-</td>
      <td>motor temperature (if thermistor is mounted)</td>
    </tr>
    <tr>
      <td>motorShutdownTemp</td>
      <td>0x808</td>
      <td>RW</td>
      <td>uint8_t</td>
      <td>-</td>
      <td>temperature at which the MD series motor controller will enter IDLE mode</td>
    </tr>
    <tr>
      <td>mainEncoderErrors</td>
      <td>0x809</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>main encoder errors</td>
    </tr>
    <tr>
      <td>outputEncoderErrors</td>
      <td>0x80A</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>output encoder errors</td>
    </tr>
    <tr>
      <td>calibrationErrors</td>
      <td>0x80B</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>calibration errors</td>
    </tr>
    <tr>
      <td>bridgeErrors</td>
      <td>0x80C</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>bridge errors</td>
    </tr>
    <tr>
      <td>hardwareErrors</td>
      <td>0x80D</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>hardware errors</td>
    </tr>
    <tr>
      <td>communicationErrors</td>
      <td>0x80E</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>communication errors</td>
    </tr>
    <tr>
      <td>motionErrors</td>
      <td>0x810</td>
      <td>RO</td>
      <td>uint32_t</td>
      <td>-</td>
      <td>motion errors</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>