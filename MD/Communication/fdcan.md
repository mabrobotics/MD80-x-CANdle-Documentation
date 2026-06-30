<style>
.small-table table {
  font-size: 12px;
}
</style>

(md_protocol)=

# MD communication

The easiest way to communicate with MD controllers is to use a CANdle device connected to a PC. Even
though we are aware some customers want to integrate the MD controllers in their product with
minimal setup to reduce the costs and the system’s complexity. This manual will guide you through
the process of communicating with MD actuators from your custom CAN master controller.

## Hardware requirements

From firmware version 2.5.0 upwards, MDs are capable of either FDCAN mode communication or CAN2.0
compatible mode. FDCAN is a preferred protocol to use, as it allows for far greater flexibility and
bandwidth. CAN2.0 is supported but not recommended, as the protocol was not optimized for it, and
basic operations and control may require multiple CAN frames to be exchanged, significantly reducing
the bandwidth, especially with multiple actuators on a single bus.

### FDCAN

The main requirement for the host system is to be equipped with an FDCAN peripheral (either a
built-in one or an external one) and an FDCAN transceiver capable of speeds up to 8Mbps. Lower
maximum speed transceivers can be used as well, however for the cost of limited update rates.
Depending on your custom setup you should be able to integrate a 120 ohm terminating resistor on
both ends of your CAN bus.

### CAN2.0

While MD was designed with FDCAN protocol in mind, CAN2.0 compatibility was introduced. In CAN2.0
mode, the driver can only operate in 1M baudrate, and some registers (that are more than 4 bytes in
size) are not available for modification, i.e motorName register. Additionally only some of the
[Frame Types](frame-types) are supported in this mode - **READ_REGISTER_CAN2.0** and
**WRITE_REGISTER_CAN2.0**. In most cases, access in 2.0 mode has to happen 1 register at a time (one
register per can frame), with an exception of accessing two U8 type registers. Apart from maximum
frame length, the contents of the frames will be the same as in FDCAN version of protocol.

```{note}
 MD controllers can be upgraded to software controlled termination on demand. Please contact us for more information before placing your order.
```

## Communication Structure

Communication with MD, happen is a strict Master-Slave structure. **The MD will never produce a
CAN frame by itself**, it will only respond to direct commands from a host. Each MD device has
configurable **CAN ID**, that serves as its unique identifier on the CAN bus. There may never be
more than one MD with the same CAN ID, as this will lead to conflicts and errors.

All communication with the particular drive will happen only via messages with particular ID. For
example:

```{note}
Host sends a request (command) to drive with Id *100*, the drive will execute the command and respond 
with a CAN frame that also has the ID of *100*
```

The communication stack is based on a register access using two frames - **register read and
register write**. The list of [available registers](registers) can be found at the end of this
chapter. All fields are little-endian - least significant byte first, and all float fields are 4
bytes long (32 bit) encoded in IEEE-754 standard.

The MD will response with one of the three possible frame types, based on the hosts' command:
- Register Data frame,
- Quick Data frame,
- Error frame.

```{warning} 
**For pre 3.0.0 firmware versions (v2.5.x)**, 

wrong access, incorrect data values or other communication errors are not reported explicitly.  
**Command that failed (regardless of the reason), will result in the drive not producing any response.** 
Generally if the drive does not start producing a CAN frame with 100us of the the last bit of the command,
the host may consider the command has failed.
```

### Frame Structure

All frames (FDCAN and CAN2.0) are composed in the same fashion. The first byte is a
[Frame Type](frame-types), then a padding byte, followed by the contents of a message.

Message contents are similar in both read and write operations. They follow a pattern of repeating
sequence: register id (2 bytes) and register value (1-24 bytes depending on a register). The number
of registers to be accessed is only limited by a size of message - 64 bytes for FDCAN, and 8 bytes
for CAN2.0.

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

For example, a frame that would read a value of the current position, velocity and torque from a
drive, would, have a length of 20 bytes, and look like the following:

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
            <td> 0x0063 </td>
            <td> 0x00 00 00 00 </td>
            <td> 0x0062 </td>
            <td> 0x00 00 00 00 </td>
            <td> 0x0064 </td>
            <td> 0x00 00 00 00 </td>
		</tr>
	</tbody>
</table>
<p></p>

(frame-types)=

### Frame Types

Although there are basically only two possible genres of frames - read and write register - the
frames can trigger different behaviours, apart of reading and writing. Here is a brief description
of the frame behaviours by their id:

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
            <td> performs write operation, and makes the drive respond with <a href="#legacy-response">legacy response</a>. This is sometimes useful in high frequency control loops, to minimize number of frames exchanged. For frame contents, refer to <a href="write-register"> Write Register Frame </a>. </td>
		</tr>
		<tr>
			<td> 0x41 </td>
            <td> READ_REGISTER</td>
            <td> performs read operation, and responds with state of the registers. Refer to  <a href="read-register"> Read Register Frame </a> </td>
		</tr>
		<tr>
			<td> 0x42 </td>
            <td> WRITE_REGISTER</td>
            <td> performs write operation, and responds with state of the registers AFTER operation. Useful for verification of write operation. For more info, refer to <a href="write-register"> Write Register Frame </a> </td>
		</tr>
		<tr>
			<td> 0x43 </td>
            <td> READ_REGISTER_CAN2.0 </td>
            <td> performs read operation, and responds with state of the registers. Works same as <a href="read-register"> Read Register Frame </a>, but is limited to 8 bytes and produces CAN2.0 compatible response. </td>
		</tr>
		<tr>
			<td> 0x44 </td>
            <td> WRITE_REGISTER_CAN2.0 </td>
            <td> performs write operation, and responds with state of the registers AFTER operation. Useful for verification of write operation. Works same as <a href="write-register"> Write Register Frame </a>, but is limited to 8 bytes and produces CAN2.0 compatible response.</td>
		</tr>
        <tr></tr>
		<tr>
			<td> 0xA0 </td>
            <td> QUICK DATA (LEGACY Response) </td>
            <td> RESPONSE ONLY. A response produced as a result of some frames. Contains data, most commonly required in fast control loops - <a href="#legacy-response">more info here.</a> </td>
		</tr>
		<tr>
			<td> 0xA1 </td>
            <td> ERROR RESPONSE </td>
            <td> RESPONSE ONLY. A response produced as a result of failed register write or read attempt. Contains an error code and failed register id.</td>
		</tr>
	</tbody>
</table>
<p></p>

(write-register)=

### Write register frame

Write register frame is used to modify values of the user-modifiable registers. Only registers with
write access can be modified.

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

Read register command is used to retrieve certain register values. The actuator will respond with a
frame consisting of the addresses and values of the registers issued in the master request. The
master request should have the following form:

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

When all read operations succeed the 0x00 fields will be filled with appropriate register data when
transmitted back to master by the MDxx controller.

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

### Error response

Error response is present in MD firmware v3.0.0 and newer. For older versions (v2.x.x), when the error occurs, no
response is produced at all, and error handling must happen via timeout handling.

<p></p>
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b></b></td>
			<td> <b>BYTE 0</b></td>
			<td> <b>BYTE 1</b></td>
			<td> <b>BYTE 2-3</b></td>
		</tr>
		<tr>
			<td>NAME </td>
			<td>FRAME ID </td>
			<td>ERROR CODE</td>
			<td>REGISTER ID </td>
		</tr>
    <tr>
			<td>TYPE </td>
			<td>uint8_t </td>
			<td>int8_t </td>
			<td>uint16_t [*C] </td>
		</tr>
        <tr>
			<td>VALUE </td>
			<td>0xA1 </td>
			<td>-255 - 0 </td>
			<td>0x0000 - 0xFFFF</td>
		</tr>
	</tbody>
</table>
<p></p>

<div class="small-table">
Error codes are int8 based **negative** values.
| Error Code | Error Name | Description |
| --- | --- | -------|
|  0 (0x00) | NONE | No error |  
| -1 (0xFF) | DEPRECATED | Register deprecated - can be treated as warning. The call had no effect | 
| -2 (0xFE) | INVALID | Frame composition invalid - usually incorrecy size of frame layout |  
| -3 (0xFD) | UNKNOWN | Register ID unknown - The call has no effect |  
| -4 (0xFC) | OUT_OF_RANGE | Register value was parsed, but was out of acceptable range. Refer to register table below. |  
| -5 (0xFB) | ACCESS | Trying to write to read-only register, or read write-only register |  
</div>

```{dropdown} **EXAMPLE** Write invalid motor kv
Command, send from host to MD:

<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
            <td> <b>BYTE 4-5 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> PADDING (0x00) </td>
            <td> regId - motorKv </td>
            <td> (u16) 65001 </td>
		</tr>
		<tr>
			<td> 0x42 </td>
            <td> 0x00 </td>
            <td> 0x001D </td>
            <td> 0xFDE9 </td>
		</tr>
	</tbody>
</table>
<p></p>
Which in raw HEX is: 0x42 00 1D 00 E9 FD

Acceptable range here is 1 - 65000, so value `65001` is out of range, producing error response.

Response, send from MD to Host:
<table border="1" cellpadding="2" cellspacing="0"  class="gridlines sheet0" id="sheet0" style="float:center;text-align:center;font-size:11px ;width:100%">
	<tbody>
		<tr>
			<td> <b>BYTE 0</b></td>
            <td> <b>BYTE 1 </b></td>
            <td> <b>BYTE 2-3 </b></td>
		</tr>
		<tr>
			<td> FRAME ID </td>
            <td> Error Code </td>
            <td> RegisterId </td>
		</tr>
		<tr>
			<td> 0xA1 </td>
            <td> 0xFC </td>
            <td> 0x001D </td>
		</tr>
	</tbody>
</table>
<p></p>
Which in raw HEX is: 0xA1 FC 1D 00 
```

(registers)=

## Register Table

Below is full register list supported by MD drives. The list is being updated regularely as MD firmware
releases introduce new features. 



<div class="small-table">

### Communications

| Register | Addr | R/W | Type | Value | Description | Status |
|:---------|:----:|:---:|:-----|:-------|:------------|:-----------------|
| canId | `0x001` | RW | `uint32` | 10–2000 | FDCAN bus ID number | **Active** |
| canBaudrate | `0x002` | RW | `uint32` | 1M, 2M, 5M, 8M | FDCAN bus baudrate | **Active** |
| canWatchdog | `0x003` | RW | `uint16` | 0–2500 [ms] | FDCAN watchdog timeout | **Active** |
| canTermination | `0x004` | RW | `uint8` | 0–1 | Toggle CAN bus termination (only on selected HW revisions) | Deprecated |


### Actuator Parameters
| Register | Addr | R/W | Type | Value | Description | Status |
|:---------|:----:|:---:|:-----|:-------|:------------|:-------|
| motorName | `0x010` | RW | `char[24]` | – | User-defined motor name. | **Active** |
| motorPolePairs | `0x011` | RW | `uint32` | 2–225 | Number of motor pole pairs. | **Active** |
| motorKt | `0x012` | RW | `float` | > 0 | Motor torque constant (Nm/A). | **Active** |
| motorIMax | `0x016` | RW | `float` | 1–controller peak current | Maximum allowable phase current. | **Active** |
| motorGearRatio | `0x017` | RW | `float` | – | Gear ratio. Values < 1 indicate a reducer, values > 1 indicate a multiplier (e.g. 2:1 reduction → 0.5). | **Active** ||
| motorTorqueBandwidth | `0x018` | RW | `uint16` | 50–2500 Hz | Desired torque control bandwidth. | **Active** |
| motorResistance | `0x01B` | RO | `float` | 5 mΩ–20 Ω | Measured motor phase resistance (d-axis). | **Active** |
| motorInductance | `0x01C` | RO | `float` | 5 nH–100 mH | Measured motor phase inductance (d-axis). | **Active** |
| motorKV | `0x01D` | RW | `uint16` | 0 - 65000 | Motor speed constant (RPM/V). | **Active** |
| motorCalibrationMode | `0x01E` | RW | `uint8` | `0`, `1` | Calibration mode (`FULL = 0`, `NOPPDET = 1`). | **Active** |
| motorThermistorType | `0x01F` | RW | `uint8` | – | Connected motor thermistor type. | **Active** |

### Aux (Output) Encoder
| Register                        | Addr | R/W | Type    | Value   | Description | Status |
|---------------------------------|------:|-----|---------|-------------------|-------------| ---- |
| outputEncoder                   | 0x020 | RW  | uint8     | [0 - 11]      | NONE=0,<br>ME_AS_CENTER=1,<br>ME_AS_OFFAXIS=2,<br>RLS_RS422_17B=3,<br>CM_OFFAXIS=4,<br>M24B_CENTER=5,<br>M24B_OFFAXIS=6, <br>ONBOARD=8,<br>RLS_SPI_17B=9, <br>RLS_ORBIS_14B=10,<br>CE300=11 | **Active** |
| outputEncoderDir                | 0x021 | RW  | float32   | -1 or 1       | Aux encoder direction, CCW or CW - automatically set during calibration | **Active** |
| *outputEncoderDir (legacy)*     | 0x021 | RW  | int8      | -1 or 1       | Aux encoder direction, CCW or CW - automatically set during calibration | up to v2.5.4 |
| outputEncoderVelocity           | 0x023 | RO  | float32   | -             | Aux encoder velocity [rad/s], computed @ 5kHz | **Active** |
| outputEncoderPosition           | 0x024 | RO  | float32   | -             | Aux encoder position [rad], read @ 5kHz | **Active** |
| outputEncoderMode               | 0x025 | RW  | uint8     | [0;1;2;3;4]   | NONE=0,<br> STARTUP=1,<br>MOTION=2,<br>REPORT=3,<br>MAIN=4 (legacy - valid up to v2.5.4) | **Active** |
| outputEncoderCalibrationMode    | 0x026 | RW  | uint8     | [0;1]         | FULL=0,<br> DIRONLY=1 | **Active** |

### Main Encoder
| Register                        | Addr | R/W | Type    | Value   | Description | Status |
|---------------------------------|------:|-----|---------|-------------------|-------------| ---- |
| mainEncoder (new)               | 0x02A | RW  | uint8     | [0; 1; 3; 8; 9; 10;] | NONE=0,<br>ME_AS_CENTER=1,<br>RLS_RS422_17B=3,<br>ONBOARD=8,<br>RLS_SPI_17B=9, <br>RLS_ORBIS_14B=10| **Active**<br>from&nbsp;v3.0.0 |
| mainEncoderDir (new)            | 0x02B | RW  | float32   | -1 or 1       | Main encoder direction, CCW or CW - automatically set during calibration | **Active**<br>from&nbsp;v3.0.0 |

### Motion Control
| Register               | Addr  | R/W | Type  | Value | Description | Status |
|------------------------|------:|-----|-------|--------|-------------| ------ |
| motorPosPidKp         | 0x030 | RW  | float | -      | Position PID proportional gain | **Active** |
| motorPosPidKi         | 0x031 | RW  | float | -      | Position PID integral gain | **Active** |
| motorPosPidKd         | 0x032 | RW  | float | -      | Position PID derivative gain | **Active** |
| motorPosPidWindup     | 0x034 | RW  | float | -      | Position PID integral windup limit | **Active** |
| | | | | | | |
| motorVelPidKp         | 0x040 | RW  | float | -      | Velocity PID proportional gain | **Active** |
| motorVelPidKi         | 0x041 | RW  | float | -      | Velocity PID integral gain | **Active** |
| motorVelPidKd         | 0x042 | RW  | float | -      | Velocity PID derivative gain | **Active** |
| motorVelPidWindup     | 0x044 | RW  | float | -      | Velocity PID integral windup limit | **Active** |
| | | | | | | |
| motorImpPidKp         | 0x050 | RW  | float | -      | Impedance PD proportional gain | **Active** |
| motorImpPidKd         | 0x051 | RW  | float | -      | Impedance PD derivative gain | **Active** |
| | | | | | | |
| velocity *(was mainEncoderVelocity)* | 0x062 | RO  | float | -      | Actuator velocity in rad/s | Active |
| position *(was mainEncoderPosition)* | 0x063 | RO  | float | -      | Actuator position in rad | Active |
| torque *(was motorTorque)*           | 0x064 | RO  | float | -      | Actuator torque in Nm | Active |
| | | | | | | |
| targetPosition  | 0x150 | RW  | float | -      | Sets target position in rad | Active |
| targetVelocity  | 0x151 | RW  | float | -      | Sets target velocity in rad/s | Active |
| targetTorque    | 0x152 | RW  | float | -      | Sets target torque in Nm | Active |

### System Commands
| Register                     | Addr  | R/W | Type   | Value               | Description | Status |
|-----------------------------|------:|-----|--------|----------------------|-------------| ----    |
| runSaveCmd                  | 0x080 | WO  | uint8 | 1 to run  | Save non-volatile memory | **Active** |
| runTestMainEncoderCmd       | 0x081 | WO  | uint8 | 1 to run  | Runs main encoder test routine | **Active** |
| runTestOutputEncoderCmd     | 0x082 | WO  | uint8 | 1 to run  | Runs output encoder test routine | **Active** |
| runCalibrateCmd             | 0x083 | WO  | uint8 | 1 to run  | Runs main calibration routine | **Active** |
| runCalibrateOutputEncoderCmd| 0x084 | WO  | uint8 | 1 to run  | Runs output encoder calibration routine | **Active** |
| runCalibratePiGains         | 0x085 | WO  | uint8 | 1 to run  | Runs current PI loop calibration routine | **Active** |
| runRestoreFactoryConfig     | 0x087 | WO  | uint8 | 1 to run  | Reverts config to factory state | **Active** |
| runReset                    | 0x088 | WO  | uint8 | 1 to run  | Resets the controller | **Active** |
| runClearWarnings            | 0x089 | WO  | uint8 | 1 to run  | Clears all warnings | **Active** |
| runClearErrors              | 0x08A | WO  | uint8 | 1 to run  | Clears non-critical errors | **Active** |
| runBlink                    | 0x08B | WO  | uint8 | 1 to run  | Blinks onboard LEDs | **Active** |
| runZero                     | 0x08C | WO  | uint8 | 1 to run  | Sets new zero position | **Active** |
| runCanReinit                | 0x08D | WO  | uint8 | 1 to run  | Reinitializes CAN peripheral | **Active** |

### Test Results
| Register                | Addr  | R/W | Type  | Value | Description | Status |
|-------------------------|------:|-----|-------|--------|-------------| ------ |
| calOutputEncoderStdDev  | 0x100 | RO  | float | -      | Aux encoder test result (standard deviation) | **Active** |
| calOutputEncoderMinE    | 0x101 | RO  | float | -      | Aux encoder test result (min error) | **Active** |
| calOutputEncoderMaxE    | 0x102 | RO  | float | -      | Aux encoder test result (max error) | **Active** |
| calMainEncoderStdDev    | 0x103 | RO  | float | -      | Main encoder test result (standard deviation) | **Active** |
| calMainEncoderMinE      | 0x104 | RO  | float | -      | Main encoder test result (min error) | **Active** |
| calMainEncoderMaxE      | 0x105 | RO  | float | -      | Main encoder test result (max error) | **Active** |

### Limits 
| Register           | Addr  | R/W | Type  | Value | Description | Status |
|--------------------|------:|-----|-------|--------|-------------| ------ |
| maxPosition *(was positionLimitMax)* | 0x110 | RW  | float | > 0    | Maximum valid position | **Active** |
| minPosition *(was positionLimitMin)* | 0x111 | RW  | float | < 0    | Minimum valid position | **Active** |
| maxTorque          | 0x112 | RW  | float | > 0    | Maximum torque | **Active** |
| maxVelocity        | 0x113 | RW  | float | > 0    | Maximum velocity | **Active** |
| maxAcceleration    | 0x114 | RW  | float | > 0    | Maximum acceleration | **Active** |
| maxDeceleration    | 0x115 | RW  | float | > 0    | Maximum deceleration | **Active** |

### Motion Profiles
| Register                 | Addr  | R/W | Type  | Value | Description | Status |
|--------------------------|------:|-----|-------|--------|-------------| ------ |
| profileVelocity         | 0x120 | RW  | float | -      | up to v2.5.4 - profile velocity<br>**from v3.0.0 - replaced by targetVelocity** | *Discontinued*<br>from&nbsp;v3.0.0 |
| profileAcceleration     | 0x121 | RW  | float | -      | Profile acceleration | **Active** |
| profileDeceleration     | 0x122 | RW  | float | -      | Profile deceleration | **Active** |
| quickStopDeceleration   | 0x123 | RW  | float | -      | Quick stop deceleration in case of a non-critical error | **Active** |
| positionWindow          | 0x124 | RW  | float | -      | Position window within position is considered to be reached | **Active** |
| velocityWindow          | 0x125 | RW  | float | -      | Velocity window within velocity is considered to be reached | **Active** |

### State
| Register             | Addr  | R/W | Type   | Value | Description | Status |
|----------------------|------:|-----|--------|--------|-------------| ------ |
| motionModeCommand    | 0x140 | WO  | uint8 | -      | IDLE=0x00,<br>POSITION_PID=0x01,<br>VELOCITY_PID=0x02,<br>RAW_TORQUE=0x03,<br>IMPEDANCE=0x04,<br>POSITION_PROFILE=0x07,<br>VELOCITY_PROFILE=0x08 | **Active** |
| motionModeStatus     | 0x141 | RO  | uint8 | -      | Shows the currently set motion mode | **Active** |
| state                | 0x142 | RW  | uint16 | -     | Returns the internal state machine state of the controller | **Active** |

### GPIO / Add-ons
| Register               | Addr  | R/W | Type    | Value | Description | Status |
|------------------------|------:|-----|---------|--------|-------------| ------ |
| userGpioConfiguration  | 0x160 | RW  | uint8  | -      | 0 - OFF,<br>1 - BRAKE,<br>2 - GPIO INPUT | **Active** |
| userGpioState          | 0x161 | RO  | uint16 | 0 or 1 | GPIO input state | **Active** |

### Driver Info
| Register          | Addr  | R/W | Type  | Value      | Description | Status |
|-------------------|------:|-----|-------|-------------|-------------| ------ |
| shuntResistance   | 0x700 | RW  | float | > 0 | Current sense resistor value. Setting this register to a value that is not coherent with the hardware may damage the controller. In this cases warranty is not respected. | *Outdated*<br>from&nbsp;v3.0.0|
| shuntResistance   | 0x700 | **RO**  | float  | > 0 | Current sense resistance. | **Active**<br>from&nbsp;v3.0.0 |
| maxDriverCurrent  | 0x701 | **RO**  | float  | > 0 | Max measurable (peak) current. | **Active**<br>from&nbsp;v3.0.0 |
| productionDate    | 0x7FB | **RO**  | uint32 | > 0 | Production date encoded in ddmmyy format  | **Active**<br>from&nbsp;v3.0.0 |
| productionBatch   | 0x7FC | **RO**  | uint32 | > 0 | Production batch code  | **Active**<br>from&nbsp;v3.0.0 |
| productionUID     | 0x7FD | **RO**  | uint32 | > 0 | Unique Identifier of MD  | **Active**<br>from&nbsp;v3.0.0 |
| hardwareRevision  | 0x7FE | **RO**  | uint32 | > 0 | Hardware revision  | **Active**<br>from&nbsp;v3.0.0 |
| hardwareType      | 0x7FF | **RO**  | uint32 | > 0 | Hardware yype id  | **Active**<br>from&nbsp;v3.0.0 |
| firmwareBuildDate *(was buildDate)* | 0x800 | RO  | uint32  | - | Firmware build date, as ddmmyy number | **Active** |
| firmwareHash *(was commitHash)*     | 0x801 | RO  | char[8] | - | Firmware hash | **Active** |
| firmwareVersion      | 0x802 | RO  | uint32 | -      | Firmware Version | **Active** |
| hardwareVersion      | 0x803 | RO  | uint8  | -      | Hardware Version | **Active** |
| dcBusVoltage         | 0x811 | RO  | float32  | 0 - 100V | Voltage measured on the DC bus | **Active** |

### Status
| Register              | Addr  | R/W | Type     | Value | Description | Status |
|----------------------|------:|-----|----------|--------|-------------| ------  |
| quickStatus          | 0x805 | RO  | uint16_t | -      | Quick status vector | **Active** |
| mosfetTemperature    | 0x806 | RO  | float    | -      | Driver temperature | **Active** |
| motorTemperature     | 0x807 | RO  | float    | -      | Motor temperature (if thermistor is mounted) | **Active** |
| motorShutdownTemp    | 0x808 | RW  | uint8_t  | -      | Temperature at which the MD will enter IDLE mode | **Active** |
| | | | | | | |
| mainEncoderStatus *(was mainEncoderErrors)*       | 0x809 | RO  | uint32 | - | Main encoder status | **Active** |
| auxEncoderStatus *(was outputEncoderErrors)*      | 0x80A | RO  | uint32 | - | Aux encoder status | **Active** |
| calibrationStatus *(was calibrationErrors)*       | 0x80B | RO  | uint32 | - | Calibration status | **Active** |
| bridgeStatus *(was bridgeErrors)*                 | 0x80C | RO  | uint32 | - | Bridge status | **Active** |
| hardwareStatus *(was hardwareErrors)*             | 0x80D | RO  | uint32 | - | Hardware status | **Active** |
| communicationStatus *(was communicationErrors)*   | 0x80E | RO  | uint32 | - | Communication status | **Active** |
| motionStatus *(was motionErrors)*                 | 0x810 | RO  | uint32 | - | Motion status | **Active** |
| miscStatus           | 0x812 | RO  | uint32_t | -      | Misc status | **Active** <br>from&nbsp;v3.0.0 |
| configStatus         | 0x813 | RO  | uint32_t | -      | Config status | **Active** <br>from&nbsp;v3.0.0|

### Deprecated
These registers have been used in some points in the past, but are now not used or replaced. 

| Register | Addr | R/W | Type | Value | Description | Status |
|:---------|:----:|:---:|:-----|:-------|:------------|:-------|
| motorKt_a | `0x013` | RW | `float` | > 0 | Optional phase A torque constant. | **Deprecated** |
| motorKt_b | `0x014` | RW | `float` | > 0 | Optional phase B torque constant. | **Deprecated** |
| motorKt_c | `0x015` | RW | `float` | > 0 | Optional phase C torque constant. | **Deprecated** |
| motorFriction | `0x019` | RO | `float32` | – | Actuator dynamic friction| **Temporarily disabled** |
| motorStiction | `0x01A` | RO | `float32` | – | Actuator static friction | **Temporarily disabled** |
| outputEncoderDefaultBaud        | 0x022 | RW  | uint32| 115200            | optional parameter for default output encoder baudrate | **Deprecated** |
| bridgeType        | 0x070 | RO  | uint8 | - | type of the mosfet driver | **Deprecated** |
| homingMode        | 0x071 | RW  | uint8 | - | Homing Mode | **Temporarily disabled** |
| homingMaxTravel   | 0x072 | RW  | float | - | Max distance to travel looking for homing point| **Temporarily disabled** |
| homingVelocity    | 0x073 | RW  | float | - | Target velocity during homing | **Temporarily disabled** |
| homingTorque      | 0x074 | RW  | float | - | Max torque during homing | **Temporarily disabled** |
| homingStatus      | 0x80F | RO  | uint32| - | Homing status bitfield| **Temporarily disabled** |

</div>

