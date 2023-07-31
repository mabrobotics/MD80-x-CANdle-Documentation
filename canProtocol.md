# MD80 FDCAN communication
The easiest way to communicate with an MD80 controller is to use a CANdle device connected to a PC. Even though we are aware some customers want to integrate the MD80 controllers in their product with minimal setup to reduce the costs and the system’s complexity. This manual will guide you through the process of communicating with MD80 actuators from your custom FDCAN-capable master controller.

## Hardware requirements
The main requirement for the host system is to be equipped with an FDCAN peripheral (either a built-in one or an external one) and an FDCAN transceiver capable of speeds up to 8Mbps. Lower maximum speed transceivers can be used as well, however for the cost of limited update rates. Currently, the differential side of the transceiver (the CANH and CANL lines) is supplied with 5V. Depending on your custom setup you should be able to integrate a 120 ohm terminating resistor on both ends of your CAN bus (MD80 controllers from version 2.0 can be upgraded to software controlled termination. Please contact us for more information).

## Communication Structure

The communication stack is based on a register access using two frames - register read and register write. The list of available registers can be found at the end of this chapter. 

## Default response

The default response is sent by the drive in case a register write operation was successfull. 

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

In case the operation initiated by a frame was unsuccessful the MD80 will not respond. 

### WRITE REGISTER FRAME

Write register frame is used to modify values of the user-modifiable registers. Only registers with write access can be modified.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td> 
			<td> <b>ID</b></td>
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
			<td>0x40</td>
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

### READ REGISTER FRAME

Read register command is used to retrieve certain register values. The actuator will respond with a frame consisting of the addresses and values of the registers issued in the master request. The master request should have the following form: 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
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
			<td>0x41</td>
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

When all read operations succeed the 0x00 fields will be filled with appropriate register data when transmitted back to master by the MD80 controller. Maximum payload should not exceed 64 bytes. 

### 16. Available registers

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
        <tbody>
          <tr class="row0">
            <td  ><b>reg name</b></td>
            <td  ><b>address</b></td>
            <td  ><b>read/write</b></td>
            <td  ><b>size</b></td>
            <td  ><b>limits</b></td>
            <td  ><b>info</b></td>
          </tr>
          <tr class="row1">
            <td  >canId</td>
            <td  >0x001</td>
            <td  >RW</td>
            <td  >uint32</td>
            <td  >[10-2000]</td>
            <td  >FDCAN bus id number</td>
          </tr>
          <tr class="row2">
            <td  >canBaudrate</td>
            <td  >0x002</td>
            <td  >RW</td>
            <td  >uint32</td>
            <td  >[1e6;2e6;5e6;8e6]</td>
            <td  >FDCAN bus baudrate</td>
          </tr>
          <tr class="row3">
            <td  >canWatchdog</td>
            <td  >0x003</td>
            <td  >RW</td>
            <td  >uint16</td>
            <td  >[0-2500]</td>
            <td  >FDCAN bus watchdog period in ms</td>
          </tr>
          <tr class="row4">
            <td  >canTermination</td>
            <td  >0x004</td>
            <td  >RW</td>
            <td  >uint8_t</td>
            <td  >[0-1]</td>
            <td  >CAN termination (available in MD80 v2.0)</td>
          </tr>
          <tr class="row5">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row6">
            <td  >motorName</td>
            <td  >0x010</td>
            <td  >RW</td>
            <td  >char[24]</td>
            <td  >-</td>
            <td  >motor name</td>
          </tr>
          <tr class="row7">
            <td  >motorPolePairs</td>
            <td  >0x011</td>
            <td  >RW</td>
            <td  >uint32</td>
            <td  >[2;255]</td>
            <td  >motor pole pair count</td>
          </tr>
          <tr class="row8">
            <td  >motorKt</td>
            <td  >0x012</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >&gt;0</td>
            <td  >motor torque constant</td>
          </tr>
          <tr class="row9">
            <td  >motorKt_a</td>
            <td  >0x013</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >motor polynomial torque constant a coefficient</td>
          </tr>
          <tr class="row10">
            <td  >motorKt_b</td>
            <td  >0x014</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >motor polynomial torque constant b coefficient</td>
          </tr>
          <tr class="row11">
            <td  >motorKt_c</td>
            <td  >0x015</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >motor polynomial torque constant c coefficient</td>
          </tr>
          <tr class="row12">
            <td  >motorIMax</td>
            <td  >0x016</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >[1 - peak controller current]</td>
            <td  >maximum phase current</td>
          </tr>
          <tr class="row13">
            <td  >motorGearRatio</td>
            <td  >0x017</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >actuator gear ratio (ex 2:1 should be 0.5) &lt;1 - reductors &gt;1 - multiplicators</td>
          </tr>
          <tr class="row14">
            <td  >motorTorgueBandwidth</td>
            <td  >0x018</td>
            <td  >RW</td>
            <td  >uint16</td>
            <td  >[50-2500]</td>
            <td  >torque bandwidth in Hz</td>
          </tr>
          <tr class="row15">
            <td  >motorFriction</td>
            <td  >0x019</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >dynamic friction in Nm (not yet implemented)</td>
          </tr>
          <tr class="row16">
            <td  >motorStiction</td>
            <td  >0x01A</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >static friction in Nm (not yet implemented)</td>
          </tr>
          <tr class="row17">
            <td  >motorResistance</td>
            <td  >0x01B</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >[5mOhm-20Ohm]</td>
            <td  >motor resistance in d axis</td>
          </tr>
          <tr class="row18">
            <td  >motorInductance</td>
            <td  >0x01C</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >[5nH-100mH]</td>
            <td  >motor inductance in d axis</td>
          </tr>
          <tr class="row19">
            <td  >motorKV</td>
            <td  >0x01D</td>
            <td  >RW</td>
            <td  >uint16</td>
            <td  >-</td>
            <td  >motor KV rating [RPM/V]</td>
          </tr>
          <tr class="row20">
            <td  >motorCalibrationMode</td>
            <td  >0x01E</td>
            <td  >RW</td>
            <td  >uint8_t</td>
            <td  >[0;1]</td>
            <td  >FULL = 0, NOPPDET = 1</td>
          </tr>
          <tr class="row22">
            <td  >motorThermistorType</td>
            <td  >0x01F</td>
            <td  >RW</td>
            <td  >uint8_t</td>
            <td  >&nbsp;</td>
            <td  >thermistor type (not yet implemented)</td>
          </tr>
          <tr class="row23">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row24">
            <td  >outputEncoder</td>
            <td  >0x020</td>
            <td  >RW</td>
            <td  >uint8</td>
            <td  >[0;1;2]</td>
            <td  >NONE = 0, AMS5047_CENTER = 1, AMS5047_OFFAXIS = 2</td>
          </tr>
          <tr class="row25">
            <td  >outputEncoderDefaultBaud</td>
            <td  >0x022</td>
            <td  >RW</td>
            <td  >uint32_T</td>
            <td  >-</td>
            <td  >output encoder default baudrate</td>
          </tr>
          <tr class="row26">
            <td  >outputEncoderVelocity</td>
            <td  >0x023</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >output encoder velocity in rad/s (calculated in a 5kHz loop)</td>
          </tr>
          <tr class="row27">
            <td  >outputEncoderPosition</td>
            <td  >0x024</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >output encoder velocity in rad/s (read in 5kHz loop)</td>
          </tr>
          <tr class="row28">
            <td  >outputEncoderMode</td>
            <td  >0x025</td>
            <td  >RW</td>
            <td  >uint8_t</td>
            <td  >[0;1;2;3]</td>
            <td  >NONE = 0, STARTUP = 1, MOTION = 2, REPORT = 3</td>
          </tr>
          <tr class="row32">
            <td  >outputEncoderCalibrationMode</td>
            <td  >0x026</td>
            <td  >RW</td>
            <td  >uint8_t</td>
            <td  >[0;1]</td>
            <td  >FULL = 0, DIRONLY = 1</td>
          </tr>
          <tr class="row34">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row35">
            <td  >motorPosPidKp</td>
            <td  >0x030</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >position PID proportional gain</td>
          </tr>
          <tr class="row36">
            <td  >motorPosPidKi</td>
            <td  >0x031</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >position PID integral gain</td>
          </tr>
          <tr class="row37">
            <td  >motorPosPidKd</td>
            <td  >0x032</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >position PID derivative gain</td>
          </tr>
          <tr class="row38">
            <td  >motorPosPidOutMax</td>
            <td  >0x033</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >position PID out max (max velocity)</td>
          </tr>
          <tr class="row39">
            <td  >motorPosPidWindup</td>
            <td  >0x034</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >position PID integral windup limit</td>
          </tr>
          <tr class="row40">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row41">
            <td  >motorVelPidKp</td>
            <td  >0x040</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >velocity PID proportional gain</td>
          </tr>
          <tr class="row42">
            <td  >motorVelPidKi</td>
            <td  >0x041</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >velocity PID integral gain</td>
          </tr>
          <tr class="row43">
            <td  >motorVelPidKd</td>
            <td  >0x042</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >velocity PID derivative gain</td>
          </tr>
          <tr class="row44">
            <td  >motorVelPidOutMax</td>
            <td  >0x043</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >velocity PID out max (max torque)</td>
          </tr>
          <tr class="row45">
            <td  >motorVelPidWindup</td>
            <td  >0x044</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >velocity PID integral windup limit</td>
          </tr>
          <tr class="row46">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row47">
            <td  >motorImpPidKp</td>
            <td  >0x050</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >impedance PD proportional gain</td>
          </tr>
          <tr class="row48">
            <td  >motorImpPidKd</td>
            <td  >0x051</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >impedance PD derivative gain</td>
          </tr>
          <tr class="row49">
            <td  >motorImpPidOutMax</td>
            <td  >0x052</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >-</td>
            <td  >impedance PD max out (torque)</td>
          </tr>
          <tr class="row50">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row51">
            <td  >mainEncoderVelocity</td>
            <td  >0x062</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >&nbsp;</td>
            <td  >main encoder velocity in rad/s (calculated in a 40kHz loop)</td>
          </tr>
          <tr class="row52">
            <td  >mainEncoderPosition</td>
            <td  >0x063</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >&nbsp;</td>
            <td  >main encoder velocity in rad/s (read in 40kHz loop)</td>
          </tr>
          <tr class="row53">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row54">
            <td  >runSaveCmd</td>
            <td  >0x080</td>
            <td  >WO</td>
            <td  >uint8_t</td>
            <td  >any value to run</td>
            <td  >runs save flash command</td>
          </tr>
          <tr class="row55">
            <td  >runTestMainEncoderCmd</td>
            <td  >0x081</td>
            <td  >WO</td>
            <td  >uint8_t</td>
            <td  >any value to run</td>
            <td  >runs main encoder test routine</td>
          </tr>
          <tr class="row56">
            <td  >runTestOutputEncoderCmd</td>
            <td  >0x082</td>
            <td  >WO</td>
            <td  >uint8_t</td>
            <td  >any value to run</td>
            <td  >runs output encoder test routine</td>
          </tr>
          <tr class="row57">
            <td  >runCalibrateCmd</td>
            <td  >0x083</td>
            <td  >WO</td>
            <td  >uint8_t</td>
            <td  >any value to run</td>
            <td  >runs main calibration routine</td>
          </tr>
          <tr class="row58">
            <td  >runCalibrateOutpuEncoderCmd</td>
            <td  >0x084</td>
            <td  >WO</td>
            <td  >uint8_t</td>
            <td  >any value to run</td>
            <td  >runs output encoder calibration routine</td>
          </tr>
          <tr class="row59">
            <td  >runCalibratePiGains</td>
            <td  >0x085</td>
            <td  >WO</td>
            <td  >uint8_t</td>
            <td  >any value to run</td>
            <td  >runs current PI loop calibration routine</td>
          </tr>
          <tr class="row60">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row61">
            <td  >calOutputEncoderStdDev</td>
            <td  >0x100</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >output encoder test result (standard deviation)</td>
          </tr>
          <tr class="row62">
            <td  >calOutputEncoderMinE</td>
            <td  >0x101</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >output encoder test result (min error)</td>
          </tr>
          <tr class="row63">
            <td  >calOutputEncoderMaxE</td>
            <td  >0x102</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >output encoder test result (max error)</td>
          </tr>
          <tr class="row64">
            <td  >calMainEncoderStdDev</td>
            <td  >0x103</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >main encoder test result (standard deviation)</td>
          </tr>
          <tr class="row65">
            <td  >calMainEncoderMinE</td>
            <td  >0x104</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >main encoder test result (min error)</td>
          </tr>
          <tr class="row66">
            <td  >calMainEncoderMaxE</td>
            <td  >0x105</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  >main encoder test result (max error)</td>
          </tr>
          <tr class="row67">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row68">
            <td  >shuntResistance</td>
            <td  >0x700</td>
            <td  >RW</td>
            <td  >float</td>
            <td  >[0.001 - 0.01]</td>
            <td  >Current sense resistor value. Setting this register to a value that is not coherent with the hardware may damage the controller. In this cases warranty is not respected.</td>
          </tr>
          <tr class="row69">
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
            <td  >&nbsp;</td>
          </tr>
          <tr class="row70">
            <td  >buildDate</td>
            <td  >0x800</td>
            <td  >RO</td>
            <td  >uint32</td>
            <td  >-</td>
            <td  >software build date</td>
          </tr>
          <tr class="row71">
            <td  >commitHash</td>
            <td  >0x801</td>
            <td  >RO</td>
            <td  >char [8]</td>
            <td  >-</td>
            <td  >commit hash</td>
          </tr>
          <tr class="row72">
            <td  >firmwareVersion</td>
            <td  >0x802</td>
            <td  >RO</td>
            <td  >uint32</td>
            <td  >-</td>
            <td  >firmware version</td>
          </tr>
          <tr class="row73">
            <td  >hardwareVersion</td>
            <td  >0x803</td>
            <td  >RO</td>
            <td  >uint32</td>
            <td  >-</td>
            <td  >hardware version</td>
          </tr>
          <tr class="row74">
            <td  >bridgeType</td>
            <td  >0x804</td>
            <td  >RO</td>
            <td  >uint8</td>
            <td  >-</td>
            <td  >type of the mosfet driver</td>
          </tr>
          <tr class="row75">
            <td  >errorVector</td>
            <td  >0x805</td>
            <td  >RO</td>
            <td  >uint16</td>
            <td  >-</td>
            <td  >error vector</td>
          </tr>
          <tr class="row76">
            <td  >mosfetTemperature</td>
            <td  >0x806</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td  > power stage temperature</td>
          </tr>
          <tr class="row77">
            <td  >motorTemperature</td>
            <td  >0x807</td>
            <td  >RO</td>
            <td  >float</td>
            <td  >-</td>
            <td > motor temperature (if thermistor is mounted)</td>
          </tr>
          <tr class="row78">
            <td  >motorShutdownTemp</td>
            <td  >0x808</td>
            <td  >RW</td>
            <td  >uint8_t</td>
            <td  >-</td>
            <td  >temperature at which the md80 will enter IDLE mode</td>
          </tr>
          <tr class="row79">
            <td  >mainEncoderErrors</td>
            <td  >0x809</td>
            <td  >RO</td>
            <td  >uint32_t</td>
            <td  >-</td>
            <td  >main encoder errors</td>
          </tr>
          <tr class="row80">
            <td  >outputEncoderErrors</td>
            <td  >0x80A</td>
            <td  >RO</td>
            <td  >uint32_t</td>
            <td  >-</td>
            <td  >output encoder errors</td>
          </tr>
          <tr class="row81">
            <td  >calibrationErrors</td>
            <td  >0x80B</td>
            <td  >RO</td>
            <td  >uint32_t</td>
            <td  >-</td>
            <td  >calibration errors</td>
          </tr>
          <tr class="row82">
            <td  >bridgeErrors</td>
            <td  >0x80C</td>
            <td  >RO</td>
            <td  >uint32_t</td>
            <td  >-</td>
            <td  >mosfet driver errors</td>
          </tr>
          <tr class="row83">
            <td  >hardwareErrors</td>
            <td  >0x80D</td>
            <td  >RO</td>
            <td  >uint32_t</td>
            <td  >-</td>
            <td  >hardware errors</td>
          </tr>
          <tr class="row84">
            <td  >communicationErrors</td>
            <td  >0x80E</td>
            <td  >RO</td>
            <td  >uint32_t</td>
            <td  >-</td>
            <td  >communication errors</td>
          </tr>
        </tbody>
    </table>
