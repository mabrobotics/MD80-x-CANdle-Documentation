# Object Dictionary

Object dictionary holds CAN objects that can be accessed using SDOs and in some cases by PDOs. There are three main groups in which the address space is divided into: 

1. Communication Area
2. Manufacturer Specific Area
3. Profile Specific Area

## 0x1000 - Device type

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



## 0x1001 - Error Register

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


## 0x1008 - Manufacturer Device Name

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

## 0x1010 - Store Parameters

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

## 0x1017 - Producer Heartbeat Time

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


## 0x1600 - Receive PDO1 mapping

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

## 0x1601 - Receive PDO2 mapping

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

## 0x1602 - Receive PDO3 mapping

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
			<td>0x6060</td>
			<td>Target Position</td>
		</tr>
	</tbody>
</table>
<p></p>

## 0x1603 - Receive PDO4 mapping

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
			<td>0x6060</td>
			<td>Target Velocity</td>
		</tr>
	</tbody>
</table>
<p></p>

## 0x1A00 - Transmit PDO1 mapping

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
	</tbody>
</table>
<p></p>

## 0x1A01 - Transmit PDO2 mapping

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
      		<td>0x1A01:1</td>
			<td>0x6061</td>
			<td>Modes Of Operation Display</td>
		</tr>
	</tbody>
</table>
<p></p>

## 0x1A02 - Transmit PDO3 mapping

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
      		<td>0x1A02:1</td>
			<td>0x6064</td>
			<td>Position Actual Value</td>
		</tr>
	</tbody>
</table>
<p></p>

## 0x1A03 - Transmit PDO4 mapping

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
      		<td>0x1A03:1</td>
			<td>0x606C</td>
			<td>Velocity Actual Value</td>
		</tr>
	</tbody>
</table>
<p></p>

## 0x1A04 - Transmit PDO5 mapping

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
      		<td> <b>Index</b></td>
			<td> <b>PDO Index</b></td>
			<td> <b>Name</b></td>
		</tr>
		<tr>
      		<td>0x1A04</td>
			<td>-</td>
			<td>Transmit PDO5 mapping</td>
		</tr>
		<tr>
      		<td>0x1A04:1</td>
			<td>0x6041</td>
			<td>StatusWord</td>
		</tr>
		<tr>
      		<td>0x1A04:1</td>
			<td>0x6077</td>
			<td>Torqur Actual Value</td>
		</tr>
	</tbody>
</table>
<p></p>



## 0x6040 - Control Word

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
			<td>None</td>
		</tr>
        <tr>
            <td>5</td>
      		<td>Disable operation command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>6</td>
      		<td>Shutdown command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>7</td>
      		<td>Quick stop command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>8</td>
      		<td>Shutdown command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>9</td>
      		<td>Disable voltage command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>10</td>
      		<td>Disable voltage / Quick stop command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>11</td>
      		<td>Quick stop command received</td>
			<td>None</td>
		</tr>
        <tr>
            <td>12</td>
      		<td>Automatic transition when quick stop is completed </td>
			<td>None</td>
		</tr>
        <tr>
            <td>13</td>
      		<td>Fault ocurred</td>
			<td>None</td>
		</tr>
        <tr>
            <td>14</td>
      		<td>Automatic transition to fault state </td>
			<td>None</td>
		</tr>
        <tr>
            <td>15</td>
      		<td>Fault reset command received</td>
			<td>None</td>
		</tr>
	</tbody>
</table>
<p></p>


## 0x6041 - Status Word

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


## 0x6060 - Modes Of Operation 

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
			<td>Calibration</td>
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

## 0x6061 - Modes Of Operation 

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
      		<td>0x6060</td>
			<td>0x00</td>
			<td>Modes Of Operation</td>
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
			<td>Calibration</td>
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

## 0x6062 - Position Demand Value

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

## 0x6064 - Position Actual Value

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


## 0x6067 - Position Window

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


## 0x606B - Velocity Demand Value

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

## 0x606C - Velocity Actual Value

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

## 0x606D - Velocity Window

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

## 0x6072 - Max Torque

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

## 0x6073 - Max Current

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

## 0x6075 - Motor Rated Current

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

## 0x6072 - Motor Rated Torque

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
      		<td>0x6072</td>
			<td>0x00</td>
			<td>Motor Rated Torque</td>
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

## 0x6077 - Torque Actual Value

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

## 0x6079 - DC Link Circuit Voltage

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


## 0x607A - Target Position

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

## 0x607D - Software Position Limit

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
	</tDody>
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
	</tDody>
</table>
<p></p>


## 0x6080 - Max Motor Speed

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

## 0x6081 - Profile Velocity

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


## 0x6083 - Profile Acceleration

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

## 0x6084 - Profile Deceleration

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

## 0x60FF - Target Velocity

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

## 0x6502 - Supported Drive Modes

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
      		<td>0x60FF</td>
			<td>0x00</td>
			<td>Target Velocity</td>
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