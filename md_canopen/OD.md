# Object Dictionary

Object dictionary holds CAN objects that can be accessed using SDOs and in some cases by PDOs. There are three main groups in which the address space is divided into: 

1. Communication Area
2. Manufacturer Specific Area
3. Profile Specific Area

## 1. Communication Area

The communication area describes the CANopen objects compliant with CiA301 standard.
### 0x1000 - Device type

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x1000</td>
			<td>0x00</td>
			<td>Device type</td>
     		<td>UINT32</td>
			<td>RO</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0x00020192</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>



### 0x1001 - Error Register

Indicates whether an error has occured. Currently, only the 0th bit is implemented, that indicates a general error. For a more verbose error and warning status, please see 0x2004 System Status. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x1001</td>
			<td>0x00</td>
			<td>Error Register</td>
     		<td>UINT8</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>


<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Bit</b></td>
			<td> <b>Meaning</b></td>
		</tr>
		<tr>
      		<td>0</td>
			<td>General Error</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x1008 - Manufacturer Device Name

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x1008</td>
			<td>0x00</td>
			<td>Manufacturer Device Name</td>
     		<td>STR</td>
			<td>RO</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>"MD80"</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

(store_parameters)=
### 0x1010 - Store Parameters

Use this object for saving parameters in non-volatile memory. Works only in "switch on disabled" state. To avoid saving parameters by mistake a value of 0x65766173 has to be explicitly written to 0x1010:1.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x1010</td>
			<td>0x01</td>
			<td>Store Parameters</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>-</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1017 - Producer Heartbeat Time

Defines the period of heartbeat message sent by the MD80.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x1017</td>
			<td>0x00</td>
			<td>Producer Heartbeat Time</td>
     		<td>UINT16</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>-</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x1600 - Receive PDO1 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1600</td>
			<td>-</td>
			<td>Receive PDO1 mapping</td>
		</tr>
		<tr>
      		<td>0x1600:1</td>
			<td>0x6040</td>
			<td>ControlWord</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1601 - Receive PDO2 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1601</td>
			<td>-</td>
			<td>Receive PDO2 mapping</td>
		</tr>
		<tr>
      		<td>0x1601:1</td>
			<td>0x6040</td>
			<td>ControlWord</td>
		</tr>
		<tr>
      		<td>0x1601:2</td>
			<td>0x6060</td>
			<td>Modes Of Operation</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1602 - Receive PDO3 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1602</td>
			<td>-</td>
			<td>Receive PDO3 mapping</td>
		</tr>
		<tr>
      		<td>0x1602:1</td>
			<td>0x6040</td>
			<td>ControlWord</td>
		</tr>
		<tr>
      		<td>0x1602:2</td>
			<td>0x607A</td>
			<td>Target Position</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1603 - Receive PDO4 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1603</td>
			<td>-</td>
			<td>Receive PDO4 mapping</td>
		</tr>
		<tr>
      		<td>0x1603:1</td>
			<td>0x6040</td>
			<td>ControlWord</td>
		</tr>
		<tr>
      		<td>0x1603:2</td>
			<td>0x60FF</td>
			<td>Target Velocity</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1A00 - Transmit PDO1 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1A00</td>
			<td>-</td>
			<td>Transmit PDO1 mapping</td>
		</tr>
		<tr>
      		<td>0x1A00:1</td>
			<td>0x6041</td>
			<td>StatusWord</td>
		</tr>
		<tr>
      		<td>0x1A00:2</td>
			<td>0x6061</td>
			<td>Modes Of Operation Display</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1A01 - Transmit PDO2 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1A01</td>
			<td>-</td>
			<td>Transmit PDO2 mapping</td>
		</tr>
		<tr>
      		<td>0x1A01:1</td>
			<td>0x6041</td>
			<td>StatusWord</td>
		</tr>
		<tr>
      		<td>0x1A01:2</td>
			<td>0x6064</td>
			<td>Position Actual Value</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1A02 - Transmit PDO3 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1A02</td>
			<td>-</td>
			<td>Transmit PDO3 mapping</td>
		</tr>
		<tr>
      		<td>0x1A02:1</td>
			<td>0x6041</td>
			<td>StatusWord</td>
		</tr>
		<tr>
      		<td>0x1A02:2</td>
			<td>0x606C</td>
			<td>Velocity Actual Value</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x1A03 - Transmit PDO4 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1A03</td>
			<td>-</td>
			<td>Transmit PDO4 mapping</td>
		</tr>
		<tr>
      		<td>0x1A03:1</td>
			<td>0x6041</td>
			<td>StatusWord</td>
		</tr>
		<tr>
      		<td>0x1A03:2</td>
			<td>0x6077</td>
			<td>Torque Actual Value</td>
		</tr>
	</tbody>
</table>
<p></p>


## 2. Manufacturer Specific Area

The manufacturer specific area describes the custom CANopen objects, valid only for MD80s.


### 0x2000 - Motor Settings

Configures the most important motor settings. This object is especially useful when you want to configure or reconfigure an MD80 for a particular motor. Be sure to save after modification using 0x1010 Store Parameters. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x01</td>
			<td>Pole Pairs</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>[2;255]</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x02</td>
			<td>Torque constant</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>Nm/A</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x03</td>
			<td>Phase Inductance</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>[5nH-100mH]</td>
            <td>0</td>
            <td>H</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x04</td>
			<td>Phase Resistance</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>[5mOhm-20Ohm]</td>
            <td>0</td>
            <td>Ohm</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x05</td>
			<td>Torque Bandwidth</td>
     		<td>UINT16</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>50-2500</td>
            <td>0</td>
            <td>Hz</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x06</td>
			<td>Motor Name</td>
     		<td>STR(20)</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x07</td>
			<td>Motor Shutdown Temperature</td>
     		<td>UINT8</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>10-80</td>
            <td>0</td>
            <td>*C</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x08</td>
			<td>Gear Ratio</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>1</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x09</td>
			<td>Calibration Mode</td>
     		<td>UINT8</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>FULL = 0, NOPPDET = 1</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2000</td>
			<td>0x0A</td>
			<td>Can ID</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>1 - 31</td>
            <td>1</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

(velocity_pid_controller)=
### 0x2001 - Velocity PID Controller

Configures the Velocity PID controller gains. Be sure to save after modification using 0x1010 Store Parameters. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2001</td>
			<td>0x01</td>
			<td>Kp</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2001</td>
			<td>0x02</td>
			<td>Ki</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2001</td>
			<td>0x03</td>
			<td>Kd</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2001</td>
			<td>0x04</td>
			<td>Integral Limit</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>Nm</td>
		</tr>
	</tbody>
</table>
<p></p>

```{figure} images/velocity_pid_CANopen.png
:align: center
:width: 1000px
```
(position_pid_controller)=
### 0x2002 - Position PID Controller

Configures the Position PID controller gains. Be sure to save after modification using 0x1010 Store Parameters. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2002</td>
			<td>0x01</td>
			<td>Kp</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2002</td>
			<td>0x02</td>
			<td>Ki</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2002</td>
			<td>0x03</td>
			<td>Kd</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2002</td>
			<td>0x04</td>
			<td>Integral Limit</td>
     		<td>FLOAT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>rad/s</td>
		</tr>
	</tbody>
</table>
<p></p>

```{image} images/position_pid_CANopen.png
:class: bg-primary mb-1
:width: 1000px
:align: center
```

(system_command)=
### 0x2003 - System Command

Allows to issue a system command. Write a non-zero value to start a specific action. Actions work only in "switch on disabled" state and "service" (-2) operation mode. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x01</td>
			<td>Blink LEDs</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x02</td>
			<td>Reset Controller</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x03</td>
			<td>Run Calibration</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x04</td>
			<td>Run Output Encoder Calibration</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x05</td>
			<td>Set Zero</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x06</td>
			<td>Calibrate Current PI Gains</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<!-- <tr>
      		<td>0x2003</td>
			<td>0x07</td>
			<td>Test Output Encoder</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x08</td>
			<td>Test Main Encoder</td>
     		<td>BOOL</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr> -->
	</tbody>
</table>
<p></p>

### 0x2004 - System Status

Allows to read System status. Each specific status is a UINT32, where lower bits (0-15) indicate errors, and higher bits (16-31) indicate warnings. Please see the [Status ](status) section to see how to decode the status to individual fields. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2004</td>
			<td>0x01</td>
			<td>Main Encoder Status</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x02</td>
			<td>Output Encoder Status</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x03</td>
			<td>Calibration Status</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x04</td>
			<td>Bridge Status</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x05</td>
			<td>Hardware Status</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x02</td>
			<td>Motion Status</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x2005 - Output Encoder

Output encoder related record.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2005</td>
			<td>0x01</td>
			<td>Type</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>1 (AS5047_CENTER), 2 (AS5047_OFFAXIS), 3 (MB053SFA17BENT00)</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x02</td>
			<td>Calibration Mode</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>FULL = 0, DIRONLY = 1</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x03</td>
			<td>Mode</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>NONE = 0, STARTUP = 1, MOTION = 2, REPORT = 3</td>
            <td>0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x04</td>
			<td>Position</td>
     		<td>FLOAT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0.0</td>
            <td>rad</td>
		</tr>
		<tr>
      		<td>0x2003</td>
			<td>0x05</td>
			<td>Velocity</td>
     		<td>FLOAT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0.0</td>
            <td>rad/s</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x2006 - Temperature 

Motor and mosfet temperature readout record.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x2006</td>
			<td>0x01</td>
			<td>Motor Temperature</td>
     		<td>FLOAT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0.0</td>
            <td>-</td>
		</tr>
		<tr>
      		<td>0x2006</td>
			<td>0x02</td>
			<td>Mosfet Temperature</td>
     		<td>FLOAT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0.0</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

## 3. Profile Specific Area

The profile specific area describes the CANopen objects compliant with CiA402 standard.
### 0x6040 - Control Word

Control word is used to change the state of the internal CiA402 state machine implemented on the drive.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6040</td>
			<td>0x00</td>
			<td>Control Word</td>
     		<td>UINT16</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

The state machine is defined as follows: 

```{figure} images/CIA402_state_machine_docs.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

All the transitions are based on the control word. The current state can be read using the status word (0x6041).

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Command</b></td>
			<td> <b>Reset Fault (bit 7)</b></td>
     		<td> <b>Enable Operation (bit 3)</b></td>
			<td> <b>Quick Stop (bit 2)</b></td>
			<td> <b>Disable Voltage (bit 1)</b></td>
			<td> <b>Switch On (bit 0)</b></td>
			<td> <b>Decimal value</b></td>
		</tr>
		<tr>
            <td>Shutdown</td>
      		<td>0</td>
			<td>X</td>
     		<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>6</td>
		</tr>
        <tr>
            <td>Switch on</td>
      		<td>0</td>
			<td>0</td>
     		<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>7</td>
		</tr>
        <tr>
            <td>Switch on and Enable Operation</td>
      		<td>0</td>
			<td>1</td>
     		<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>15</td>
		</tr>
        <tr>
            <td>Disable Voltage</td>
      		<td>0</td>
			<td>X</td>
     		<td>X</td>
			<td>0</td>
			<td>X</td>
			<td>0</td>
		</tr>
        <tr>
            <td>Quick Stop</td>
      		<td>0</td>
			<td>X</td>
     		<td>0</td>
			<td>1</td>
			<td>X</td>
			<td>2</td>
		</tr>
        <tr>
            <td>Disable operation</td>
      		<td>0</td>
			<td>0</td>
     		<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>7</td>
		</tr>
        <tr>
            <td>Enable operation</td>
      		<td>0</td>
			<td>1</td>
     		<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>15</td>
		</tr>
        <tr>
            <td>Fault reset</td>
      		<td>0->1</td>
			<td>X</td>
     		<td>X</td>
			<td>X</td>
			<td>X</td>
			<td>128</td>
		</tr>
	</tbody>
</table>
<p></p>

X means "do not care"

Example: 

To put the drive into operational mode set: 
1. Control word = 6 (dec) (Shutdown cmd)
2. Control word = 15 (dec) (Switch on and Enable Operation cmds)


The events and respective transitions are gathered in the table below: 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Transition</b></td>
			<td> <b>Event</b></td>
     		<td> <b>Internal action</b></td>
		</tr>
		<tr>
            <td>0</td>
      		<td>Automatic transition after power up</td>
			<td>Drive internal initialization</td>
		</tr>
        <tr>
            <td>1</td>
      		<td>Automatic transition after drives internal initialization</td>
			<td>Object dictionary is initalized with NVM data</td>
		</tr>
        <tr>
            <td>2</td>
      		<td>Shutdown command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>3</td>
      		<td>Switch on command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>4</td>
      		<td>Enable operation command received</td>
			<td>Current controllers are on, power is applied to the motor</td>
		</tr>
        <tr>
            <td>5</td>
      		<td>Disable operation command received</td>
			<td>Current controllers are off, power is not applied to the motor</td>
		</tr>
        <tr>
            <td>6</td>
      		<td>Shutdown command received</td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>7</td>
      		<td>Quick stop command received</td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>8</td>
      		<td>Shutdown command received</td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>9</td>
      		<td>Disable voltage command received</td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>10</td>
      		<td>Disable voltage / Quick stop command received</td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>11</td>
      		<td>Quick stop command received</td>
			<td>Quick stop action is enabled. The drive decelerates and transits to SWITCH ON DISABLED</td>
		</tr>
        <tr>
            <td>12</td>
      		<td>Automatic transition when quick stop is completed </td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>13</td>
      		<td>Fault ocurred</td>
			<td>Current controllers are turned off</td>
		</tr>
        <tr>
            <td>14</td>
      		<td>Automatic transition to fault state </td>
			<td>None</td>
		</tr>
        <tr>
            <td>15</td>
      		<td>Fault reset command received</td>
			<td>Fault is cleared if not critical</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x6041 - Status Word

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6041</td>
			<td>0x00</td>
			<td>Status Word</td>
     		<td>UINT16</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Status Word</b></td>
			<td> <b>State Machine State</b></td>
		</tr>
		<tr>
      		<td>xxxx xxxx x0xx 0000</td>
			<td>Not ready to switch on</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x1xx 0000</td>
			<td>Switch on disabled</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x01x 0001</td>
			<td>Ready to switch on</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x01x 0011</td>
			<td>Switched on</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x01x 0111</td>
			<td>Operation Enabled</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x00x 0111</td>
			<td>Quick stop active</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x0xx 1111</td>
			<td>Fault reaction active</td>
		</tr>
		<tr>
      		<td>xxxx xxxx x0xx 1000</td>
			<td>Quick stop active</td>
		</tr>
	</tbody>
</table>
<p></p>

bit 10 of the statusword indicates the current target has been reached (1) or not (0). This bit is motion mode - dependent, meaning for example in position mode it indicates the position has been reached (within a 0x6067 Position Window margin), and in velocity mode that a velocity target has been reached (within 0x606D Velocity Window).

bit 11 of the statusword indicates whether any of the internal limits was active during current power up - for more information on which limit is active, check the 0x2004:7 Motion Status. 


### 0x6060 - Modes Of Operation 

Use this object to request a motion mode change. The actual mode is reflected in 0x6061 Modes Of Operation Display.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6060</td>
			<td>0x00</td>
			<td>Modes Of Operation</td>
     		<td>INT8</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Value</b></td>
			<td> <b>Mode</b></td>
		</tr>
		<tr>
      		<td>-2</td>
			<td>Service</td>
		</tr>
		<tr>
      		<td>0</td>
			<td>Idle</td>
		</tr>
		<tr>
      		<td>1</td>
			<td>Profile Position</td>
		</tr>
		<tr>
      		<td>3</td>
			<td>Profile Velocity</td>
		</tr>
		<tr>
      		<td>8</td>
			<td>Cyclic Sync Position</td>
		</tr>
		<tr>
      		<td>9</td>
			<td>Cyclic Sync Velocity</td>
		</tr>
	</tbody>
</table>
<p></p>

#### Service

Mode in which [System Commands](system_command) can be issued. 

#### Idle 

Default state of the drive. No torque is produced, motor phases are shorted to GND which causes a damping sensation on the shaft.

#### Profile position 

Profile position mode uses a trapeziodal trajectory generator on top of the [Position PID controller](position_pid_controller). Allows to perform smooth point-to-point movements. 

```{figure} images/position_profile_generator_CANopen.png
```

#### Profile velocity

Profile velocity mode uses a trapeziodal trajectory generator on top of the [Velocity PID controller](velocity_pid_controller). Allows to reach a certain velocity with a constant acceleration / deceleration. 

```{figure} images/velocity_profile_generator_CANopen.png
```

#### Cyclic Sync Position

Raw position PID controller. Target position is reached as fast as possible, respecting the position range limits, max velocity, and max torque limit. To achieve smooth trajectories new setpoints need to be sent with high frequency.

#### Cyclic Sync Velocity

Raw velocity PID controller. Target velocity is reached as fast as possible, respecting the max velocity limit, and max torque limit. To achieve smooth acceleration new velocity setpoints need to be sent with high frequency. 


### 0x6061 - Modes Of Operation Display

Use this object to read current motion mode

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6061</td>
			<td>0x00</td>
			<td>Modes Of Operation Display</td>
     		<td>INT8</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Value</b></td>
			<td> <b>Mode</b></td>
		</tr>
		<tr>
      		<td>-2</td>
			<td>Service</td>
		</tr>
		<tr>
      		<td>0</td>
			<td>Idle</td>
		</tr>
		<tr>
      		<td>1</td>
			<td>Profile Position</td>
		</tr>
		<tr>
      		<td>3</td>
			<td>Profile Velocity</td>
		</tr>
		<tr>
      		<td>8</td>
			<td>Cyclic Sync Position</td>
		</tr>
		<tr>
      		<td>9</td>
			<td>Cyclic Sync Velocity</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6062 - Position Demand Value

This object provides the target position for Position PID controller, after the limits have been applied. Expressed in encoder increments. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6062</td>
			<td>0x00</td>
			<td>Position Demand Value</td>
     		<td>INT32</td>
			<td>RO</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>INC</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6064 - Position Actual Value

Provides the actual position value read from the encoder, expressed in the output shaft reference frame. Expressed in encoder increments. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6064</td>
			<td>0x00</td>
			<td>Position Actual Value</td>
     		<td>INT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>INC</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x6067 - Position Window

Sets the size of the position window within which the target position is considered to have been reached. This value is symmetrically added to both sides of the target position value. Expressed in encoder increments.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6067</td>
			<td>0x00</td>
			<td>Position Window</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>INC</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x606B - Velocity Demand Value

Provides the target velocity value for the Velocity PID controller, after the limits have been applied. Expressed in RPM.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x606B</td>
			<td>0x00</td>
			<td>Velocity Demand Value</td>
     		<td>INT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>RPM</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x606C - Velocity Actual Value

Provides the actual velocity value read from the encoder, expressed in the output shaft reference frame. Expressed in RPM.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x606C</td>
			<td>0x00</td>
			<td>Velocity Actual Value</td>
     		<td>INT32</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>RPM</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x606D - Velocity Window

Sets the size of the velocity window within which the target velocity is considered to have been reached. This value is symmetrically added to both sides of the target velocity value. Expressed in RPM.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x606D</td>
			<td>0x00</td>
			<td>Velocity Window</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>RPM</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6072 - Max Torque

Configures the maximum allowed torque in the motor. The value is expressed in permille of rated torque. Example: rated torque of the motor is 1Nm, and the maximum is 2Nm. The Max Torque object should equal to 2000.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6072</td>
			<td>0x00</td>
			<td>Max Torque</td>
     		<td>UNT16</td>
			<td>RW</td>
			<td>RX</td>
			<td>yes</td>
			<td>32767</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6073 - Max Current

Configures the maximum allowed phase current in the motor. The value is expressed in permille of rated current. Example: rated current of the motor is 15A, and the maximum is 30A. The Max Current object should equal to 2000.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6073</td>
			<td>0x00</td>
			<td>Max Current</td>
     		<td>UNT16</td>
			<td>RW</td>
			<td>RX</td>
			<td>yes</td>
			<td>50000</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6075 - Motor Rated Current

Configures the motor rated current expressed in mA. This object is a reference for parameters such as 0x6073 Max Current. The value should be taken from the motor's datasheet. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6075</td>
			<td>0x00</td>
			<td>Motor Rated Current</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>1000000</td>
            <td>0x00</td>
            <td>mA</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6076 - Motor Rated Torque

Configures the motor rated torque expressed in mNm. This object is a reference for parameters such as 0x6072 Max Torque. The value should be taken from the motor's datasheet. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6076</td>
			<td>0x00</td>
			<td>Motor Rated Torque</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>-</td>
			<td>yes</td>
			<td>1000000</td>
            <td>0x00</td>
            <td>mNm</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6077 - Torque Actual Value

Provides the actual velocity value read from the encoder, expressed in the output shaft reference frame. Expressed in permille of 0x6076 Motor Rated Torque. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6077</td>
			<td>0x00</td>
			<td>Torque Actual Value</td>
     		<td>INT16</td>
			<td>RO</td>
			<td>TX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6079 - DC Link Circuit Voltage

Provides the bus voltage measured by the motor controller in mV.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6079</td>
			<td>0x00</td>
			<td>DC Link Circuit Voltage</td>
     		<td>UNT32</td>
			<td>RO</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>mV</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x607A - Target Position

Sets the target position for all motion modes.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x607A</td>
			<td>0x00</td>
			<td>Target Position</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0x00</td>
            <td>inc</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x607D - Software Position Limit

Configures software limits that each new target position is checked against, and clipped if needed. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x607D</td>
			<td>0x01</td>
			<td>Min Position Limit</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>yes</td>
			<td>-</td>
            <td>0x00</td>
            <td>inc</td>
		</tr>
	</tbody>
</table>
<p></p>

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x607D</td>
			<td>0x02</td>
			<td>Max Position Limit</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>yes</td>
			<td>-</td>
            <td>0x00</td>
            <td>inc</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x6080 - Max Motor Speed

Sets the maximum allowed velocity of the actuator's output shaft in both directions.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6080</td>
			<td>0x00</td>
			<td>Max Motor Speed</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>1000</td>
            <td>RPM</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6081 - Profile Velocity

Configures the target velocity for the profile position mode. If this value is greater than 0x6080 Max Motor Speed, it will be limited to Max Motor Speed.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6081</td>
			<td>0x00</td>
			<td>Profile Velocity</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>yes</td>
			<td>-</td>
            <td>0</td>
            <td>RPM</td>
		</tr>
	</tbody>
</table>
<p></p>


### 0x6083 - Profile Acceleration

Configures the acceleration for profile position and profile velocity modes. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6083</td>
			<td>0x00</td>
			<td>Profile Acceleration</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>RPM/s</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6084 - Profile Deceleration

Configures the deceleration for profile position and profile velocity modes. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6084</td>
			<td>0x00</td>
			<td>Profile Deceleration</td>
     		<td>UINT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>RPM/s</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x60FF - Target Velocity

Sets the target velocity for all motion modes.

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x60FF</td>
			<td>0x00</td>
			<td>Target Velocity</td>
     		<td>INT32</td>
			<td>RW</td>
			<td>RX</td>
			<td>-</td>
			<td>-</td>
            <td>0</td>
            <td>RPM</td>
		</tr>
	</tbody>
</table>
<p></p>

### 0x6502 - Supported Drive Modes

Indicates the supported drive modes (binary value).

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>Sub Index</b></td>
			<td> <b>Name</b></td>
     		<td> <b>Data Type</b></td>
			<td> <b>SDO</b></td>
			<td> <b>PDO</b></td>
			<td> <b>NVM</b></td>
			<td> <b>Range</b></td>
            <td> <b>Default</b></td>
            <td> <b>Units</b></td>
		</tr>
		<tr>
      		<td>0x6502</td>
			<td>0x00</td>
			<td>Supported Drive Modes</td>
     		<td>INT32</td>
			<td>RO</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
            <td>647</td>
            <td>-</td>
		</tr>
	</tbody>
</table>
<p></p>