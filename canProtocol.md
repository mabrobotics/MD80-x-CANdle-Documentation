# MD80 FDCAN communication
The easiest way to communicate with an MD80 controller is to use a CANdle device connected to a PC. Even though we are aware some customers want to integrate the MD80 controllers in their product with minimal setup to reduce the costs and the system’s complexity. This manual will guide you through the process of communicating with MD80 actuators from your custom FDCAN-capable master controller.

## Hardware requirements
The main requirement for the host system is to be equipped with an FDCAN peripheral (either a built-in one or an external one) and an FDCAN transceiver capable of speeds up to 8Mbps. Lower maximum speed transceivers can be used as well, however for the cost of limited update rates. Currently, the differential side of the transceiver (the CANH and CANL lines) is supplied with 5V. Depending on your custom setup you should be able to integrate a 120 ohm terminating resistor on both ends of your CAN bus (MD80 controllers from version 2.0 have a built-in resistor that can be controlled by software).

## Communication overview
MD80 controllers are programed to receive a frame that takes the following structure:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b> </b></td>
			<td> <b>BYTE 0 </b></td>
			<td> <b>BYTE 1 </b></td>
			<td> <b>BYTE 2 </b></td>
      <td> <b>BYTE 3 </b></td>
      <td> <b>BYTE 4 </b></td>
      <td> <b>BYTE 5 </b></td>
      <td> <b>BYTE x </b></td>
		</tr>
		<tr>
			<td> NAME </td>
			<td>FRAME ID </td>
			<td> 0x00 </td>
			<td>FRAME BYTE 0 </td>
      <td>FRAME BYTE 1 </td>
      <td>FRAME BYTE 2 </td>
      <td>FRAME BYTE 3 </td>
      <td>FRAME BYTE 4 </td>
		</tr>
	</tbody>
</table>
<p></p>
and in most cases they respond with a default response frame (in case of operation success): 
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
			<td>ERROR VECTOR </td>
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

Table below  shows the possible CAN frame IDs that can be recognised by MD80:
<p></p>
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME TYPE </b></td>
			<td> <b>ID: </b></td>
			<td> <b>WATCHDOG </b></td>
			<td> <b>DEFAULT RESPONSE </b></td>
		</tr>
		<tr>
			<td> FLASH LED </td>
			<td> 0x00 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> MOTOR ENABLE </td>
			<td> 0x01 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> CONTROL SELECT </td>
			<td> 0x02 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> ZERO ENCODER </td>
			<td> 0x03 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> SET MAX CURRENT </td>
			<td> 0x04 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> GET_INFO </td>
			<td> 0x05 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> SET TORQUE BANDWIDTH </td>
			<td> 0x06 </td>
			<td> NO </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> POS_CONTROL </td>
			<td> 0x10 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> VEL_CONTROL </td>
			<td> 0x11 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> IMP_CONTROL </td>
			<td> 0x12 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> RESTART </td>
			<td> 0x13 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> SET_MOTION_TARGETS </td>
			<td> 0x14 </td>
			<td> YES </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> STOP_WDG </td>
			<td> 0x19 </td>
			<td> NO </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> SET_CAN_CONFIG </td>
			<td> 0x20 </td>
			<td> NO </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> SAVE_CONFIG </td>
			<td> 0x21 </td>
			<td> NO </td>
			<td> YES </td>
		</tr>
		<tr>
			<td> WRITE_REGISTER </td>
			<td> 0x40 </td>
			<td> NO </td>
			<td> NO </td>
		</tr>
		<tr>
			<td> READ_REGISTER </td>
			<td> 0x41 </td>
			<td> NO </td>
			<td> NO </td>
		</tr>
		<tr>
			<td> CALIBRATION </td>
			<td> 0x70 </td>
			<td> NO </td>
			<td> YES </td>
		</tr>
	</tbody>
</table>


The watchdog column indicates whether a particular frame initializes and starts the CAN communication watchdog that will disable the actuator in case it hasn’t received a message in a preset period of time. This safety feature ensures the communication is ongoing and any hazardous situations are avoided (like a nonzero torque target with a sudden FDCAN bus malfunction). In case the can watchdog safety feature is unwanted it can be shut down (although it is highly advised against). The watchdog is only started if the actuator was enabled using MOTOR ENABLE frame prior to the current message. 
The default response column indicates whether the response is a default one, or a more complex response. These responses will be described in detail in the next chapter.  

## Frame details

FDCAN frames are described in detail in the following section. **Frame ID and length are for reference only, FDCAN frame data section should be populated with bytes starting from BYTE 0.**

### 1. Flash onboard LEDs

This frame is used to flash the onboard MD80 leds. It can be useful when trying to find a particular MD80 in a long FDCAN bus string. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
		</tr>
		<tr>
			<td>FLASH LED</td>
			<td>0x00</td>
			<td>2</td>
			<td>0x00</td>
      <td>0x00 </td>
		</tr>
	</tbody>
</table>
<p></p>

Example: 
- data[0] = 0x00 (FRAME ID)
- data[1] = 0x00 (Not Important)

### 2. Enable 

Enable frame is used to turn on the drive and begin the operation. After enabling the actuator, it is in IDLE motion mode. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2 </b></td>
		</tr>
		<tr>
			<td>ENABLE</td>
			<td>0x01</td>
			<td>3</td>
			<td>0x01</td>
      <td>0x00</td>
      <td>enable</td>
		</tr>
	</tbody>
</table>
<p></p>

Params:
- enable (uint8_t) - send 0 to disable, 1 to enable

Example:
- data[0] = 0x01 (FRAME ID)
- data[1] = 0x00 (Not Important)
- data[2] = 0x01 (enable) / 0x00 (disable)

### 3. Control select

Control select frame is used to select the current motion mode.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2 </b></td>
		</tr>
		<tr>
			<td>CONTROL SELECT</td>
			<td>0x02</td>
			<td>3</td>
			<td>0x02</td>
      <td>0x00</td>
      <td>mode</td>
		</tr>
	</tbody>
</table>
<p></p>

Params:
- mode = 0 - IDLE - motor phases are shorted to gnd, the motor is braking
- mode = 1 - position PID
- mode = 2 - velocity PID
- mode = 3 - deprecated 
- mode = 4 - impedance PD

Example:
- data[0] = 0x02 (FRAME ID)
- data[1] = 0x00 (Not Important)
- data[2] = 0x04 (impedance PD mode)

### 4. Set zero position

Set zero position frame is used to set the current shaft position to be the new zero position. Sending this frame zeroes the output encoder as well if it is in STARTUP or MOTION modes. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
		</tr>
		<tr>
			<td>SET ZERO POSITON</td>
			<td>0x03</td>
			<td>2</td>
			<td>0x03</td>
      <td>0x00</td>
		</tr>
	</tbody>
</table>
<p></p>

```{note}
This command needs to be saved using the `SAVE CONFIG` command to be preserved after power-up. 
```
### 5. Set max current

Set max current frame is used to set the max current limit. This limit is imposed on q-axis current, thus it applies to phase currents, not source current. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-5 </b></td>
		</tr>
		<tr>
			<td>SET MAX CURRENT</td>
			<td>0x04</td>
			<td>6</td>
			<td>0x04</td>
      <td>0x00</td>
      <td>current</td>
		</tr>
	</tbody>
</table>
<p></p>

Example (10.0f amps):
- data[0] = 0x04 (FRAME ID)
- data[1] = 0x00 (Not Important)
- data[2] = 0x00 (float byte 0)
- data[3] = 0x00 (float byte 1)
- data[4] = 0x20 (float byte 2)
- data[5] = 0x41 (float byte 3)


```{note}
This command needs to be saved using the `SAVE CONFIG` command to be preserved after power-up. 
```

### 6. SET POSITION PID 

Set position PID frame is used to set custom position PID gains. These are temporary gains that will overwrite the defaults until next power up. To change default gains please refer to the read/write register section of this document. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-5 </b></td>
      <td> <b>BYTE 6-9 </b></td>
		</tr>
		<tr>
			<td>SET POSITION PID</td>
			<td>0x10</td>
			<td>32</td>
			<td>0x10</td>
      <td>0x00</td>
      <td>kp</td>
      <td>ki</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 10-13</b></td>
			<td> <b>BYTE 14-17</b></td>
			<td> <b>BYTE 18-21</b></td>
			<td> <b>BYTE 22-25</b></td>
		</tr>
		<tr>
			<td>kd</td>
			<td>i windup</td>
			<td>max output</td>
      <td>target position</td>
		</tr>
	</tbody>
</table>
<p></p>

Params:
- kp (float) - proportional gain
- ki (float) - integral gain
- kd (float) - derivative gain
- i windup (float) - integral windup limit 
- max output (float) - maximum output limit (maximum velocity)
- target position (float) - target position (rad)


### 6. SET VELOCITY PID 

Set velocity PID frame is used to set custom velocity PID gains. These are temporary gains that will overwrite the defaults until next power up. To change default gains please refer to the read/write register section of this document. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-5 </b></td>
      <td> <b>BYTE 6-9 </b></td>
		</tr>
		<tr>
			<td>SET VELOCITY PID</td>
			<td>0x11</td>
			<td>32</td>
			<td>0x11</td>
      <td>0x00</td>
      <td>kp</td>
      <td>ki</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 10-13</b></td>
			<td> <b>BYTE 14-17</b></td>
			<td> <b>BYTE 18-21</b></td>
			<td> <b>BYTE 22-25</b></td>
		</tr>
		<tr>
			<td>kd</td>
			<td>i windup</td>
			<td>max output</td>
      <td>target velocity</td>
		</tr>
	</tbody>
</table>
<p></p>

Params:
- kp (float) - proportional gain
- ki (float) - integral gain
- kd (float) - derivative gain
- i windup (float) - integral windup limit 
- max output (float) - maximum output limit (maximum torque)
- target velocity (float) - target velocity (rad/s)

### 6. SET IMPEDANCE PD  

Set impedance PID frame is used to set custom impedance PID gains. These are temporary gains that will overwrite the defaults until next power up. To change default gains please refer to the read/write register section of this document. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>FRAME NAME</b></td>
			<td> <b>ID</b></td>
			<td> <b>LENGTH</b></td>
			<td> <b>BYTE 0 [ID]</b></td>
      <td> <b>BYTE 1 </b></td>
      <td> <b>BYTE 2-5 </b></td>
      <td> <b>BYTE 6-9 </b></td>
		</tr>
		<tr>
			<td>SET IMPEDANCE PD</td>
			<td>0x12</td>
			<td>32</td>
			<td>0x12</td>
      <td>0x00</td>
      <td>kp</td>
      <td>kd</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 10-13</b></td>
			<td> <b>BYTE 14-17</b></td>
			<td> <b>BYTE 18-21</b></td>
			<td> <b>BYTE 22-25</b></td>
		</tr>
		<tr>
			<td>target position</td>
			<td>target velocity</td>
			<td>feedforward torque</td>
      <td>max output</td>
		</tr>
	</tbody>
</table>
<p></p>

Params:
- kp (float) - proportional gain
- kd (float) - derivative gain
- target position (float) - Position target 
- target velocity (float) - Velocity target
- feedforward torque (float) - torque to be added at the controller output
- max output (float) - maximum output limit (maximum torque) 

### 9. Reset

