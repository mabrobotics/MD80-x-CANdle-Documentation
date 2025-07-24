(status)=

# Status

When an abnormal situation takes place the controller sets an error bit indicating a particular
error or warning. The table below lists all available error and warning codes and their
descriptions. The easiest way to check all statuses is to use mdtool. Another way could be to use
the CANdle lib register access and read the statuses, or decode the general "Quick Status" using the
CANdle lib getQuickStatus() function.

Errors and warnings can be cleared by register access, or using `mdtool clear` command. Please note
that all warnings and only non-critical errors can be cleared.

(quick_status)=

### Quick Status

Quick status provides a general info about errors in each category of statuses. No warnings are
indicated here. Last bit indicatest whether the current target (position or velocity) has been
reached.

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
			<td>8-14</td>
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

### Main / Output Encoder Errors

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
			<td>MDxx could not communicate with the encoder </td>
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
			<td>Check endcoder physical setup and reboot the MDxx</td>
		</tr>
	</tbody>
</table>
<p></p>

### Calibration Errors

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

### Bridge errors

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
      		<td>Lower the current limit, clear the error or restart the drives</td>
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

### Hardware errors

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
      		<td>Lower the current limit, clear the error or restart the drive</td>
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
			<td>MDxx power side exceeded the limit of 100*C</td>
      		<td>wait for the MDxx to cool down</td>
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

### Comunication errors

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
      		<td>make sure candle.end() is called in your script, clear using mdtool</td>
		</tr>
  </tbody>
</table>
<p></p>

(motion_status)=

### Motion status

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
      		<td>Re-home the actuator, set a temporary zero to move it back into the limits, or increase the limit range, clear using mdtool</td>
		</tr>
		<tr>
			<td>ERROR_VELOCITY_OUTSIDE_LIMITS</td>
			<td>1</td>
			<td>Velocity exceeded the max velocty param</td>
      		<td>Ensure the velocity limit is set to a proper value, clear using mdtool</td>
		</tr>
		<tr>
			<td>WARNING_ACCELERATION_CLIPPED</td>
			<td>24</td>
			<td>Acceleration command was clipped to max acceleration at least once</td>
      		<td>Check acceleration limits, clear using mdtool</td>
		</tr>
    	<tr>
			<td>WARNING_TORQUE_CLIPPED</td>
			<td>25</td>
			<td>Torque command was clipped to max torque at least once</td>
      		<td>Check torque limits, clear using mdtool</td>
		</tr>
    	<tr>
			<td>WARNING_VELOCITY_CLIPPED</td>
			<td>26</td>
			<td>Velocity command was clipped to max velocity at least once</td>
      		<td>Check velocity limits, clear using mdtool</td>
		</tr>
    	<tr>
			<td>WARNING_POSITON_CLIPPED</td>
			<td>27</td>
			<td>Position command was clipped to either max or min position at least once</td>
      		<td>Check position limits, clear using mdtool</td>
		</tr>
  </tbody>
</table>
<p></p>

The following table shows when warnings and errors are issued based on the mode the controller is
currently in:

```{figure} images/Status/status_vs_motion_mode.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

## Utilities

(GPIO)=

### GPIO

All of the MD controllers have two multi-purpose GPIO pins. Currently they have two functionalities:

- Auto Brake - in this mode MDxx will automatically engage MAB Robotics's provided braking systems
  via GPIO A pin, see [brake systems](brake_systems) and [registers section](registers) for more
  details.
- GPIO input - in this mode MDxx will output GPIO pin states to state register (*userGpioState
  0x161*)

```{important}

The GPIO are connected directly to board's MCU. **DO NOT** drive this pins higher than +5V or lower than 0V as this **WILL** damage the board.

Also the GPIO pins are floating so if you want to use those pins as an external function switches, do so with proper pull-up/down resistor or push-pull circuitry.

```
