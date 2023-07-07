(status)=
# Status

When an abnormal situation takes place the controller sets an error bit indicating a particular error or warning. The table below lists all available error and warning codes and their descriptions. The easiest way to check all statuses is to use mdtool. Another way could be to use the CANdle lib register access and read the statuses, or decode the general "Quick Status" using the CANdle lib getQuickStatus() function.

## Quick Status 

Quick status provides a general info about errors in each category of statuses. No warnings are indicated here. Last bit indicatest whether the current target (position or velocity) has been reached.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
		</tr>
		<tr>
			<td>0</td>
			<td>Main encoder error</td>
		</tr>
		<tr>
			<td>1</td>
			<td>Output encoder error</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Calibration encoder error</td>
		</tr>
		<tr>
			<td>3</td>
			<td>MOSFET bridge error</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Hardware errors</td>
		</tr>
    	<tr>
			<td>5</td>
			<td>Communication errors</td>
		</tr>
   		 <tr>
			<td>6</td>
			<td>Motion errors</td>
		</tr>
       	<tr>
			<td>7-14</td>
			<td>RESERVED</td>
		</tr>
		</tr>
			<tr>
			<td>15</td>
			<td>Target position (in Position PID / Profile position mode) or velocity ( in Velocity PID / Velocity profile mode) reached within position or velocity window <td>
		</tr>
	</tbody>
</table>
<p></p>

## Main / Output Encoder Errors

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error name</b></td>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
      		<td> <b>Action to clear it</b></td>
		</tr>
		<tr>
			<td>ERROR_COMMUNICATION </td>
			<td>0</td>
			<td>MD80 could not communicate with the encoder </td>
      		<td>Check connections </td>
		</tr>
    	<tr>
			<td>ERROR_WRONG_DIRECTION</td>
			<td>1</td>
			<td>Indicates the calibrated output encoder direction is different from the main encoder direction</td>
      		<td>Recalibrate</td>
		</tr>
   		 <tr>
			<td>ERROR_EMPTY_LUT</td>
			<td>2</td>
			<td>Indicates the encoder eccentricity table is empty</td>
      		<td>Recalibrate</td>
		</tr>
    	<tr>
			<td>ERROR_FAULTY_LUT</td>
			<td>3</td>
			<td>Indicates the encoder eccentricity table is faulty (contains too large corrections)</td>
    		<td>Check the setup and recalibrate</td>
		</tr>
    	<tr>
			<td>ERROR_CALIBRATION_FAILED</td>
			<td>4</td>
			<td>Calibration failed due to wrong motor <> encoder setup</td>
			<td>Check setup, recalibrate in case of problems contact MABRobotics</td>
		</tr>
    	<tr>
			<td>ERROR_POSITION_INVALID</td>
			<td>5</td>
			<td>Position reading is invalid</td>
			<td>Check endcoder physical setup, in case of problems contact MABRobotics</td>
		</tr>
		<tr>
			<td>ERROR_INIT</td>
			<td>6</td>
			<td>Encoder initialization failed</td>
			<td>Check endcoder setup and connection, in case of problems contact MABRobotics</td>
		</tr>
		<tr>
			<td>WARNING_LOW_ACCURACY</td>
			<td>30</td>
			<td>Encoder position readout accuracy may be lower than specified</td>
			<td>Check endcoder physical setup and reboot the MD80</td>
		</tr>
	</tbody>
</table>
<p></p>


## Calibration Errors

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error name</b></td>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
      		<td> <b>Action to clear it</b></td>
		</tr>
		<tr>
			<td>ERROR_OFFSET_CAL </td>
			<td>0</td>
			<td>Problem with the offset determination during calibration </td>
      		<td>Try recalibrating</td>
		</tr>
    	<tr>
			<td>ERROR_RESISTANCE_IDENT</td>
			<td>1</td>
			<td>Problem with resistance identification</td>
    		<td>Try recalibrating or running the `mdtool config bandwidth` command</td>
		</tr>
    	<tr>
			<td>ERROR_INDUCTANCE_IDENT</td>
			<td>2</td>
			<td>Problem with inductance identification</td>
      		<td>Try recalibrating or running the `mdtool config bandwidth` command</td>
		</tr>
    	<tr>
			<td>ERROR_POLE_PAIR_CAL</td>
			<td>3</td>
			<td>Problem with pole pair detection routine</td>
      		<td>Try recalibrating</td>
		</tr>
    	<tr>
			<td>ERROR_SETUP</td>
			<td>4</td>
			<td>Problem with motor config file download, or the setup parameters themselves</td>
      		<td>Check the config file again and try to upload one more time</td>
		</tr>
	</tbody>
</table>
<p></p>

## Bridge errors

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error name</b></td>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
      		<td> <b>Action to clear it</b></td>
		</tr>
		<tr>
			<td>ERROR_BRIDGE_COM</td>
			<td>0</td>
			<td>Communication problem with the bridge</td>
      		<td>Contact MABRobotics</td>
		</tr>
    	<tr>
			<td>ERROR_BRIDGE_OC</td>
			<td>1</td>
			<td>The bridge detected overcurrent</td>
      		<td>Lower the current limit, restart the drives</td>
		</tr>
    	<tr>
			<td>ERROR_BRIDGE_GENERAL_FAULT</td>
			<td>2</td>
			<td>Usually indicates a hardware issue</td>
      		<td>Contact MABRobotics</td>
		</tr>
	</tbody>
</table>
<p></p>

## Hardware errors
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error name</b></td>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
      		<td> <b>Action to clear it</b></td>
		</tr>
   		<tr>
			<td>ERROR_OVER_CURRENT</td>
			<td>0</td>
			<td>Overcurrent detected</td>
      		<td>Lower the current limit, restart the drives</td>
		</tr>
    	<tr>
			<td>ERROR_OVER_VOLTAGE</td>
			<td>1</td>
			<td>Overvoltage detected</td>
      		<td>Lower the system voltage, avoid rapid braking in the system, use a modern PSU, or a LiPo battery</td>
		</tr>
    	<tr>
			<td>ERROR_UNDER_VOLTAGE</td>
			<td>2</td>
			<td>Undervoltage detected</td>
      		<td>Ensure your power supply has enough current capability for your system</td>
		</tr>
    	<tr>
			<td>ERROR_MOTOR_TEMP</td>
			<td>3</td>
			<td>Motor temperature exceeded the limit set in the config file</td>
      		<td>Wait for the motor to cool down</td>
		</tr>
    	<tr>
			<td>ERROR_MOSFET_TEMP</td>
			<td>4</td>
			<td>MD80 power side exceeded the limit of 100*C</td>
      		<td>wait for the MD80 to cool down</td>
		</tr>
     	<tr>
			<td>ERROR_ADC_CURRENT_OFFSETS</td>
			<td>5</td>
			<td>Error during adc current offsets calibration</td>
      		<td>Usually indicates a hardware error - contact MABRobotics</td>
		</tr> 
  </tbody>
</table>
<p></p>

## Comunication errors

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error name</b></td>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
      		<td> <b>Action to clear it</b></td>
		</tr>
    	<tr>
			<td>WARNING_CAN_WD</td>
			<td>30</td>
			<td>Indicates the communication with the host was ended by the watchdog</td>
      		<td>make sure candle.end() is called in your script</td>
		</tr>
  </tbody>
</table>
<p></p>

(motion_status)=
## Motion status

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>Error name</b></td>
			<td> <b>Error bit</b></td>
			<td> <b>Error description</b></td>
      		<td> <b>Action to clear it</b></td>
		</tr>
		<tr>
			<td>ERROR_POSITION_OUTSIDE_LIMITS</td>
			<td>0</td>
			<td>Current shaft position is outside the <min position : max position> limits from the config file</td>
      		<td>Re-home the actuator, set a temporary zero to move it back into the limits, or increase the limit range</td>
		</tr>
    	<tr>
			<td>WARNING_TORQUE_CLIPPED</td>
			<td>25</td>
			<td>Torque command was clipped to max torque at least once</td>
      		<td>Check torque limits</td>
		</tr>
    	<tr>
			<td>WARNING_VELOCITY_CLIPPED</td>
			<td>26</td>
			<td>Velocity command was clipped to max velocity at least once</td>
      		<td>Check velocity limits</td>
		</tr>
    	<tr>
			<td>WARNING_POSITON_CLIPPED</td>
			<td>27</td>
			<td>Position command was clipped to either max or min position at least once</td>
      		<td>Check position limits</td>
		</tr>
  </tbody>
</table>
<p></p>



