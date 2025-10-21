# Communication FDCAN

There are two FDCAN communication connections, that have to be described. To control the PDS stack,
one must connect to [PDS_CTRL](pds_ctrl) module, using 3-pin connector. 

There are also 6-pin connectors available on [PDS_PS](pds_ps) module, that allow for connecting MD 
series motor controllers and other FDCAN devices. However:
```{warning}
PDS_CTRL FDCAN is not internally connected to PDS_PS modules. They are independent signal lines, that
can be connected externally. To allow a single CANdle communicate with PDS and MD on a single string.
```


## PDS_PS module connectors

By default all connectors on [PDS_PS](pds_ps) module, have their CAN_H and CAN_L lines disconnected from 
each other, to provide only power though 6-pin connectors, allowing for up to 3 independent communication
strings, to exist on the bus. There are however, bridge pads, located below 6-pin connectors to allow 
for connecting these buses together.

In order to connect using architecture please solder correct bridges underneath the Micro-Fit molex connector.
These bridges connect CAN-L and CAN-H to another CAN-L/H of neighbor connector so the connection is transmitted without any adapters.

```{figure} images/power_stage/pds_ps_bridges.jpg
:alt: pds_power_stage_bridges
:align: center

FDCAN bridge placement

```


Also control board has its own built-in CAN termination. 
If possible CAN termination should be placed on each ends of CAN circuit as shown below in recommended architecture examples.

### **Example 1**

In this example there are: CANdle, Control board, two Power Stage modules, six MD actuators (two per Micro-Fit molex connector) and CAN termination. In this example, termination on the CANdle is disabled.

```{figure} images/control_board/PDS_CAN.png
:alt: PDS_CAN_architecture_example_1
:align: center

FDCAN architecture with 2 Power Stage modules

```

### **Example 2**

In this example there are: CANdle, Control board, one Power Stage module and six MD actuators (two per Micro-Fit molex connector).This is the type of example that shows how to use all ports of single Power Stage without additional CAN termination. In this example, termination on CANdle is set to ON.


```{figure} images/control_board/PDS_CAN_3port.png
:alt: PDS_CAN_architecture_example_2
:align: center

FDCAN architecture with 1 Power Stage module

```

## Communication Protocol 

Communication with a PDS device is done with the use of the “properties” concept. Each data or
setting is a property of a module that forms a PDS device stack. Each property has its own underlying
data type and access rights. Each property data occupies 4 bytes on the CAN frame. When
communicating with the PDS, the host controller has to form a request frame that contains:
- Message type ( which indicates what the host device is about to achieve ),
- Type of the module that the message is addressed to,
- Socket index where the particular module is connected,
- Number of properties that it is going to read or write,
- A set of properties (when reading) or a property/value pairs (when writing).

```{note}
As in all MAB CAN-based devices, the CAN ID is used to target specific devices. PSD is not an exception.
When the frame is successfully received and processed by the PDS device, its response body depends
on the message type.
```

When the host sends a write request to a module, the module responds with a frame containing the
protocol status, the number of properties received, and a status code for each property. If some 
properties are read-only, they will return a status of ‘NO ACCESS’, while successfully written ones will
return ‘OK’. To standardize communication, Control Board is considered as a module with a socket index 0.
When the host sends a request to read properties the PDS device responds in similar fashion, the protocol
status code, number of properties and a set of property status / value that corresponds to the
properties set in the request.


### Commands

The message frame body depends on the command code that is always placed at the beginning of the
frame. For simplicity, there are only two command codes supported by the PDS device:

  Read properties from the PDS module
  Write properties to the PDS module

<style>
  body {
    font-family: Arial, sans-serif;
    padding: 10px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    table-layout: auto;
    min-width: 600px;
    margin: 0 auto;
  }

  th, td {
    padding: 10px;
    font-size: 10px;
  }
</style>
<table>
  <tr>
    <th>Command name</th>
    <th>Command code [HEX]</th>
    <th>Description</th>
  </tr>

  <tr>
    <td>Read properties</td>
    <td>0x20</td>
    <td>Read properties from the PDS module</td>
  </tr>

  <tr>
    <td>Write properties</td>
    <td>0x21</td>
    <td>Write properties to the PDS module</td>
  </tr>
</table>


### Properties

Properties are the values representing some state or parameter of the module like temperature,
voltage, CAN Baudrade, or module type connected to socket number 5. Obviously, not all properties are
available on each module and also there are some common properties that each module must have.

<table>
  <tr>
    <th rowspan = "2"> NAME</th>
    <th rowspan = "2"> ID</th>
    <th rowspan = "2"> ACCESS RIGHTS</th>
    <th rowspan = "2"> TYPE</th>
    <th rowspan = "2"> DESCRIPTION </th>
    <th colspan = "4"> AVAILABILITY ON MODULES</th>
  </tr>
  <tr>
    <th> CB</th>
    <th> PS</th>
    <th> BR</th>
    <th> IC</th>
  </tr>
  <tr>
    <td> STATUS WORD</td>
    <td> 0x00</td>
    <td> R</td>
    <td> U32 - btiwise</td>
    <td> A register were each bit represent different state of the module</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td> STATUS CLEAR</td>
    <td> 0x01</td>
    <td> W</td>
    <td> U32 - bitwise</td>
    <td> A register used to clear status bits in the STATUS WORD</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td> ENABLE</td>
    <td> 0x02</td>
    <td> RW</td>
    <td> Boolean</td>
    <td> Used to enable / disable particular module ( when write ) or simply check if it is enabled / disabled (when read )</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> TEMPERATURE</td>
    <td> 0x03</td>
    <td> R</td>
    <td> Float</td>
    <td> Module temperature</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> TEMPERATURE LIMIT</td>
    <td> 0x04</td>
    <td> RW</td>
    <td> Float</td>
    <td> Temperature limit. When module temperature exceeds this value it will become disabled and unable to be enabled back until cooldown</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> BUS VOLTAGE</td>
    <td> 0x05</td>
    <td> R</td>
    <td> U32</td>
    <td> Power supply input bus voltage on control board / Power output voltage on power stage and Isolated converter</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> LOAD CURRENT</td>
    <td> 0x10</td>
    <td> R</td>
    <td> S32</td>
    <td> Output current of the module</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> LOAD POWER</td>
    <td> 0x11</td>
    <td> R</td>
    <td> S32 </td>
    <td> Output power of the module</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> TOTAL DELIVERED ENERGY</td>
    <td> 0x12</td>
    <td> R</td>
    <td> U32</td>
    <td> Total amount of energy ( in WH ) that was consumed by device connected to the module</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> TOTAL RECUPERATED ENERGY</td>
    <td> 0x13</td>
    <td> R</td>
    <td> U32</td>
    <td> Total amount of energy ( in WH ) that was generated by the device connected to the module</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> CAN ID</td>
    <td> 0x20</td>
    <td> RW</td>
    <td> U16</td>
    <td> CAN ID</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> CAN BAUDRATE</td>
    <td> 0x21</td>
    <td> RW</td>
    <td> ENUM*</td>
    <td> CAN Baudrate ( 1M / 2M / 5M / 8M )</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SOCKET 1 MODULE</td>
    <td> 0x22</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> The type of the module that is connected to socket number 1</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SOCKET 2 MODULE</td>
    <td> 0x23</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> The type of the module that is connected to socket number 2</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SOCKET 3 MODULE</td>
    <td> 0x24</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> The type of the module that is connected to socket number 3</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SOCKET 4 MODULE</td>
    <td> 0x25</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> The type of the module that is connected to socket number 4</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SOCKET 5 MODULE</td>
    <td> 0x26</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> The type of the module that is connected to socket number 5</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SOCKET 6 MODULE</td>
    <td> 0x27</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> The type of the module that is connected to socket number 6</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> SHUTDOWN_TIME</td>
    <td> 0x28</td>
    <td> RW</td>
    <td> U32</td>
    <td> The time ( in mS ) that PDS device waits before it turns off after receiving shutdown request (either from power button or from host device )</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> BATTERY_LEVEL_1</td>
    <td> 0x29</td>
    <td> RW</td>
    <td> U32</td>
    <td rowspan = "2"> Levels ( in mV ) that defines ranges of battery energy available: 0 - L1 :: Almost discharged ( RED indication ), L1 - L2 :: Nominal charge ( YELLOW indication ), L2 < :: Fully charged ( GREEN indication )</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> BATTERY_LEVEL_2</td>
    <td> 0x2A</td>
    <td> RW</td>
    <td> U32</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> BR SOCKET INDEX</td>
    <td> 0x30</td>
    <td> RW</td>
    <td> ENUM*</td>
    <td> Socket index of the brake resistor that we are going to bind with the power stage</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> BR TRIGGER VOLTAGE</td>
    <td> 0x31</td>
    <td> RW</td>
    <td> U32</td>
    <td> The value of the power stage output voltage above which the brake resistor will be triggered (in mV)</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> OCD_LEVEL</td>
    <td> 0x40</td>
    <td> RW</td>
    <td> U32</td>
    <td> The value of current ( in mA ) above which the module will enter OCD state if this value is exceeded for a time equal or grater than the "OCD Delay" time of the same module.</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> OCD_DELAY</td>
    <td> 0x41</td>
    <td> RW</td>
    <td> U32</td>
    <td> The time ( in mS ) that the OCD level has to be exceedeed for to turn the module into OCD state</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> HW_VERSION</td>
    <td> 0xFD</td>
    <td> R</td>
    <td> ENUM*</td>
    <td> Hardware version of the module</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> FW_VERSION</td>
    <td> 0xFE</td>
    <td> R</td>
    <td> U32 - bytewise</td>
    <td> Firmware version of the Control board MCU</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> COMMAND</td>
    <td> 0xFF</td>
    <td> W</td>
    <td> ENUM*</td>
    <td> Property used to send various commands to the PDS device like ( power off, reboot, etc... ).</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
</table>

### Status and status clear words
The terms 'Status' and 'Status Clear' indicate basic binary states or events within a module, such as whether it is enabled or a limit has been exceeded. The U32 bitwise type means that each bit in the value represents a different purpose rather than a singular numerical value. Like properties, status bits are module-specific—each module defines its own set, which may or may not align with those of othermodules.


<table>
  <tr>
    <th rowspan = "2"> NAME</th>
    <th rowspan = "2"> BIT POSITION</th>
    <th rowspan = "2"> DESCRIPTION</th>
    <th colspan = "4"> AVAILABILITY ON MODULES</th>
  </tr>
  <tr>
    <th> CB</th>
    <th> PS</th>
    <th> BR</th>
    <th> IC</th>
  </tr>
  <tr>
    <td> Enabled</td>
    <td> 0</td>
    <td> Indicates whenever the module is enabled or not. Note that in case of Control board it indicates entire device power on status.</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> Over temperature</td>
    <td> 1</td>
    <td> The temperature limit of the module has been exceeded</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> Over current</td>
    <td> 2</td>
    <td> The current limit of the module has been exceeded (OCD state )</td>
    <td> ❌</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ✅</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
  <tr>
    <td> STO1</td>
    <td> 10</td>
    <td> Safe Turn Off at input 1 has been triggered</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> STO2</td>
    <td> 11</td>
    <td> Safe Turn Off at input 2 has been triggered</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> FDCAN Timeout</td>
    <td> 12</td>
    <td> CAN message processing timeout</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 1 error</td>
    <td> 13</td>
    <td rowspan = "6"> Some error occurs on the module connected to the socket ( 1 - 6 ). Refer to the particular module status word for more details about the issue</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 2 error</td>
    <td> 14</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 3 error</td>
    <td> 15</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 4 error</td>
    <td> 16</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 5 error</td>
    <td> 17</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Submodule 6 error</td>
    <td> 18</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Charger detection</td>
    <td> 19</td>
    <td> Indicates whenever charger has been connected to the device</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> Shutdown schedule</td>
    <td> 20</td>
    <td> Indicates that the PDS device shutdown has been scheduled and the PDS device is about to be turned off within the time specified in the "Shutdown time" property of the control board.</td>
    <td> ✅</td>
    <td> ❌</td>
    <td> ❌</td>
    <td> ❌</td>
  </tr>
  <tr>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
    <td> ...</td>
  </tr>
</table>

### Communication frames
Generic frame body of the “Write property” ( 0x21 ) message:
<table>
  <tr>
    <td> nBytes</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 4</td>
    <td> …</td>
    <td> 1</td>
    <td> 4</td>
    <td> 1</td>
    <td> 4</td>
  </tr>
  <tr>
    <td> Frame field</td>
    <td> Write property command code [0x21]</td>
    <td> Module type</td> 
    <td> Socket index</td>
    <td> Number of properties</td>
    <td> Property 1 type</td>
    <td> Property 1 value</td>
    <td> Property 2 type</td>
    <td> Property 2 value</td>
    <td> ...</td>
    <td> Property N-1 type</td>
    <td> Property N-1 value</td>
    <td> Property N type</td>
    <td> Property N value</td>
  </tr>
</table>
Generic response to properties writes frame body:
<table>
  <tr>
    <td> nBytes</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> …</td>
    <td> 1</td>
    <td> 1</td>
  </tr>
  <tr>
    <td> Frame field</td>
    <td> STATUS</td>
    <td> Number of properties</td>
    <td> Property 1 Status</td>
    <td> Property 2 Status</td>
    <td> ...</td>
    <td> Property N-1 Status</td>
    <td> Property N Status</td>
  </tr>
</table>
Generic frame body of the “Read properties” ( 0x20 ) message:
<table>
  <tr>
    <td> nBytes</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> …</td>
    <td> 1</td>
    <td> 1</td>
  </tr>
  <tr>
    <td> Frame field</td>
    <td> Write property command code [0x20]</td>
    <td> Module type</td> 
    <td> Socket index</td>
    <td> Number of properties</td>
    <td> Property 1 type</td>
    <td> Property 2 type</td>
    <td> ...</td>
    <td> Property N-1 type</td>
    <td> Property N type</td>
  </tr>
</table>
Generic response to properties read frame body:
<table>
  <tr>
    <td> nBytes</td>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
    <td> 4</td>
    <td> 1</td>
    <td> 4</td>
    <td> …</td>
    <td> 1</td>
    <td> 4</td>
    <td> 1</td>
    <td> 4</td>
  </tr>
  <tr>
    <td> Frame field</td>
    <td> STATUS</td>
    <td> Number of properties</td>
    <td> Property 1 Status</td>
    <td> Property 1 value</td>
    <td> Property 2 Status</td>
    <td> Property 2 value</td>
    <td> ...</td>
    <td> Property N-1 Status</td>
    <td> Property N-1 value</td>
    <td> Property N Status</td>
    <td> Property N value</td>
  </tr>
</table>

### Response status codes

Response to correct read or write request frames contains two different status code types. The overall
message status code ( protocol status ) and per property status code ( property status ).

Overall message status codes:
<table>
  <tr>
    <th> Status</th>
    <th> Code [ HEX ]</th>
    <th> Description</th>
  </tr>
  <tr>
    <td> OK</td>
    <td> 0x00</td>
    <td> Request frame parsed correctly</td>
  </tr>
  <tr>
    <td> Invalid message length</td>
    <td> 0x01</td>
    <td> The received request frame length is incorrect. For example when the number of properties byte indicates 4 properties but only 3 types are provided. Or if the received frame length is less than the expected header.</td>
  </tr>
  <tr>
    <td> Invalid module type</td>
    <td> 0x02</td>
    <td> Module type code is out of range</td>
  </tr>
  <tr>
    <td> Invalid socket index</td>
    <td> 0x03</td>
    <td> Socket index code is out of range</td>
  </tr>
  <tr>
    <td> No module at socket</td>
    <td> 0x04</td>
    <td> There is no module connected to the desired socket index</td>
  </tr>
  <tr>
    <td> Wrong module at the socket</td>
    <td> 0x05</td>
    <td> The desired module type does not match the one actually connected to the desired socket</td>
  </tr>
</table>

Properties status codes:

<table>
  <tr>
    <th> Status</th>
    <th> Code [ HEX ]</th>
    <th> Description</th>
  </tr>
  <tr>
    <td> OK</td>
    <td> 0x00</td>
    <td> Property read/write operation success</td>
  </tr>
  <tr>
    <td> No property</td>
    <td> 0x01</td>
    <td> The addressed module does not support the requested property</td>
  </tr>
  <tr>
    <td> Invalid access rights</td>
    <td> 0x02</td>
    <td> Requested read operation from write-only property or write operation to read-only property</td>
  </tr>
  <tr>
    <td> Invalid data argument</td>
    <td> 0x03</td>
    <td> Given data value during the write operation is invalid. For example when the user is trying to exceed some limit or pass some value that is out of valid enumeration range.</td>
  </tr>
</table>
