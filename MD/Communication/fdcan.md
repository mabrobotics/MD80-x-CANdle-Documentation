(md_protocol)=
# MD communication
The easiest way to communicate with MD controllers is to use a CANdle device connected to a PC. Even though we are aware some customers want to integrate the MD controllers in their product with minimal setup to reduce the costs and the system’s complexity. This manual will guide you through the process of communicating with MD actuators from your custom CAN master controller.

## Hardware requirements
From firmware version 2.5.0 upwards, MDs are capable of either FDCAN mode communication or CAN2.0 compatibile mode. FDCAN is a preffered protocol to use, as it allows for far greater flexibility and bandwidth. CAN2.0 is supported but not recommended, as the protocol was not optimized for it, and basic operations and control may require multiple CAN frames to be exchanged, significantly reducing the bandwidth, especially with multiple actuators on a single bus.

### FDCAN
The main requirement for the host system is to be equipped with an FDCAN peripheral (either a built-in one or an external one) and an FDCAN transceiver capable of speeds up to 8Mbps. Lower maximum speed transceivers can be used as well, however for the cost of limited update rates. Depending on your custom setup you should be able to integrate a 120 ohm terminating resistor on both ends of your CAN bus.

### CAN2.0
While MD was designed with FDCAN protocol in mind, CAN2.0 compability was introduced. In CAN2.0 mode, the driver can only operate in 1M baudrate, and some registers (that are more than 4 bytes in size) are not available for modification, i.e motorName register. Additionally only some of the [Frame Types](frame-types) are supported in this mode - **READ_REGISTER_CAN2.0** and **WRITE_REGISTER_CAN2.0**. In most cases, access in 2.0 mode has to happen 1 register at a time (one register per can frame), with an exception of accessing two U8 type registers. Apart from maximum frame length, the contents of the frames will be the same as in FDCAN version of protocol. 

```{note}
 MD controllers can be upgraded to software controlled termination on demand. Please contact us for more information before placing your order.
 ```

## Communication Structure

Comminication with MD, happen is a strict Master-Slave structure. The MD itself will never produce a CAN frame by itself, it will only respond to direct commands from a host. Each MD device has configurable **CAN ID**, that serves as its unique identifier on the CAN bus. There may never be more than one MD with the same CAN ID, as this will lead to conflicts and errors. 

All communication with the particular drive will happen only via messeges with particular ID. For example:

```{note}
Host sends a request (command) to drive with Id *100*, the drive will execute the command and respond with a CAN frame that also has the ID of *100*
```

The communication stack is based on a register access using two frames - **register read and register write**. The list of [available registers](registers) can be found at the end of this chapter. All fields are little-endian - least significant byte first, and all float fields are 4 bytes long (32 bit) encoded in IEEE-754 standard. 

```{warning}
Wrong access, incorrect data values or other communication errors are not reported explicitly. **Command that failed (regardless of the reason), will result in the drive not producing any response.** Generally if the drive does not start producing a CAN frame with 100us of the the last bit of the command, the host may consider the command has failed.
```

### Frame Structure
All frames (FDCAN and CAN2.0) are composed in the same fasion. The first byte is a [Frame Type](frame-types), then a padding byte, followed by the contents of a message.

Message contents are similar in both read and write operations. They follow a pattern of repeating sequence: register id (2 bytes) and register value (1-24 bytes depending on a register). The number of registers to be accessed is only limited by a size of message - 64 bytes for FDCAN, and 8 bytes for CAN2.0. 

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-X </b></td>
            <td> <b>BYTE X+1-X+2 </b></td>
            <td> <b>BYTE X+4-X+Y </b></td>
            <td> <b> ... </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> REG ID 1 </td>
            <td> VALUE 1  </td>
            <td> REG ID 2 </td>
            <td> VALUE 2  </td>
            <td> ...      </td>
		</tr>
	</tbody>
</table>
<p></p>

For example, a frame that would read a value of the current position, velocity and torque from a drive, would, have a length of 20 bytes, and look like the following:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-7 </b></td>
            <td> <b>BYTE 8-9 </b></td>
            <td> <b>BYTE 10-13 </b></td>
            <td> <b>BYTE 14-15 </b></td>
            <td> <b>BYTE 16-19 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> regId - mainEncoderPosition </td>
            <td> PADDING </td>
            <td> regId - mainEncoderVelocity </td>
            <td> PADDING </td>
            <td> regId - motorTorque </td>
            <td> PADDING </td>
		</tr>
		<tr>
			<td> 0x41 </td>
            <td> 0x00 </td>
            <td> 0x0062 </td>
            <td> 0x00 00 00 00 </td>
            <td> 0x0063 </td>
            <td> 0x00 00 00 00 </td>
            <td> 0x0064 </td>
            <td> 0x00 00 00 00 </td>
		</tr>
	</tbody>
</table>
<p></p>

(frame-types)=
### Frame Types
Although there are basically only two possible genres of frames - read and write register - the frames can trigger different behaviours, apart of reading and writing. Here is a brief description of the frame behaviours by their id:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
            <td> Frame ID </td>
            <td> Name </td>
            <td> Description </td>
		</tr>
		<tr>
			<td> 0x40 </td>
            <td> WRITE_REGISTER_LEGACY</td>
            <td> performs write operation, and makes the drive respond with <a href="#legacy-response">legacy response</a>. This is sometimes usefull in high frequency control loops, to minimize number of frames exchanged. For frame contents, refer to <a href="write-register"> Write Register Frame </a>. </td>
		</tr>
		<tr>
			<td> 0x41 </td>
            <td> READ_REGISTER</td>
            <td> performs read operation, and responds with state of the registers. Refer to  <a href="read-register"> Read Register Frame </a> </td>
		</tr>
		<tr>
			<td> 0x42 </td>
            <td> WRITE_REGISTER</td>
            <td> performs write operation, and responds with state of the registers AFTER operation. Usefull for verification of write operation. For more info, refer to <a href="write-register"> Write Register Frame </a> </td>
		</tr>
		<tr>
			<td> 0x43 </td>
            <td> READ_REGISTER_CAN2.0 </td>
            <td> performs read operation, and responds with state of the registers. Works same as <a href="read-register"> Read Register Frame </a>, but is limited to 8 bytes and produces CAN2.0 compatibile response. </td>
		</tr>
		<tr>
			<td> 0x44 </td>
            <td> WRITE_REGISTER_CAN2.0 </td>
            <td> performs write operation, and responds with state of the registers AFTER operation. Usefull for verification of write operation. Works same as <a href="write-register"> Write Register Frame </a>, but is limited to 8 bytes and produces CAN2.0 compatibile response.</td>
		</tr>
		<tr>
			<td> 0x0A </td>
            <td> LEGACY_RESPONE </td>
            <td> RESPONSE ONLY. A response produced as a result of some frames. Contains data, most commonly required in fast control loops - <a href="#legacy-response">more info here.</a> </td>
		</tr>
	</tbody>
</table>
<p></p>

(write-register)=
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
			<td>10-1000</td>
			<td>X (64 max)</td>
			<td>0x42</td>
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

```{dropdown} **EXAMPLE** Write target position and velocity
Command, send from host to MD:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-7 </b></td>
            <td> <b>BYTE 8-9 </b></td>
            <td> <b>BYTE 10-13 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> regId - targetPosition </td>
            <td> (float) 0.25 </td>
            <td> regId - targetVelocity </td>
            <td> (float) -7.4 </td>
		</tr>
		<tr>
			<td> 0x42 </td>
            <td> 0x00 </td>
            <td> 0x0150 </td>
            <td> 0x3E 80 00 00 </td>
            <td> 0x0151 </td>
            <td> 0xC0 EC CC CD </td>
		</tr>
	</tbody>
</table>
<p></p>
Which in raw HEX is: 0x42 00 01 50 3E 80 00 00 01 51 C0 EC CC CD

Response, send from MD to Host:
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-7 </b></td>
            <td> <b>BYTE 8-9 </b></td>
            <td> <b>BYTE 10-13 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> regId - targetPosition </td>
            <td> (float) 0.25 </td>
            <td> regId - targetVelocity </td>
            <td> (float) -7.4 </td>
		</tr>
		<tr>
			<td> 0x42 </td>
            <td> 0x00 </td>
            <td> 0x0150 </td>
            <td> 0x3E 80 00 00 </td>
            <td> 0x0151 </td>
            <td> 0xC0 EC CC CD </td>
		</tr>
	</tbody>
</table>
<p></p>
Which in raw HEX is: 0x42 00 01 50 3E 80 00 00 01 51 C0 EC CC CD
```

(read-register)=
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
			<td>10-2000</td>
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
      <td>10-2000</td>
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

```{dropdown} **EXAMPLE** Read MD status and position
Command, send from host to MD:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-5 </b></td>
            <td> <b>BYTE 6-7 </b></td>
            <td> <b>BYTE 8-11 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> regId - quickStatus </td>
            <td> PADDING (2 bytes) </td>
            <td> regId - mainEncoderPosition </td>
            <td> PADDING (4 bytes) </td>
		</tr>
		<tr>
			<td> 0x41 </td>
            <td> 0x00 </td>
            <td> 0x0805 </td>
            <td> 0x00 00  </td>
            <td> 0x0062 </td>
            <td> 0x00 00 00 00 </td>
		</tr>
	</tbody>
</table>
<p></p>
Which in raw HEX is: 0x41 00 08 05 00 00 00 62 00 00 00 00

Response, send from MD to Host:
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-5 </b></td>
            <td> <b>BYTE 6-7 </b></td>
            <td> <b>BYTE 8-11 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> regId - quickStatus </td>
            <td> status (u16) </td>
            <td> regId - mainEncoderPosition </td>
            <td> 16.74 (float) </td>
		</tr>
		<tr>
			<td> 0x41 </td>
            <td> 0x00 </td>
            <td> 0x0805 </td>
            <td> 0x80 00  </td>
            <td> 0x0062 </td>
            <td> 0x41 85 EB 85 </td>
		</tr>
	</tbody>
</table>
<p></p>
Which in raw HEX is: 0x41 00 08 05 80 00 00 62 41 85 EB 85
```
### Legacy response

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

(registers)=
## Register Table

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
      <td>NONE = 0, ME_AS_CENTER = 1, ME_AS_OFFAXIS = 2, MB053SFA17BENT00 = 3, CM_OFFAXIS = 4, M24B_CENTER = 5, M24B_OFFAXIS = 6</td>
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
      <td>returns the internal <a href=../md_canopen/OD.html#x6040-control-word>state machine</a> state of the controller </td>
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
