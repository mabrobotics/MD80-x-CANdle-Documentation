(pds_ctrl)=
# Control board

## General specification
The PDS_CTRL module serves as the central controller in the system. 
Its main functions include:
- managing and acquiring data from up to six connected modules,
- facilitating communication over CAN FD with support for integration into the CANdle
ecosystem,
- handling the RGB switch for powering the system on and off, with status reporting via the RGB
diodes,
- the monitoring input voltage,
- tracking temperature across the system,
- managing Safe Turn Off (STO) inputs ensures safe operation in critical situations.

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
    font-size: 14px;
  }
</style>

<table>
  <tr>
    <th> Parameter</th>
    <th> Value</th>
  </tr>
  <tr>
    <td> Input voltage</td>
    <td> 12-54V</td>
  </tr>
  <tr>
    <td> Max number of slave modules</td>
    <td> 6</td>
  </tr>
  <tr>
    <td> FDCAN Baudrate (adjustable)</td>
    <td> 1/2/5/8 Mbps</td>
  </tr>
  <tr>
    <td> Current consumption on standby (without slave modules)</td>
    <td> 37.5 mA</td>
  </tr>
  <tr>
    <td> The quiescent current in the shutdown</td>
    <td> 11.63 uA</td>
  </tr>
  <tr>
    <td> Mass</td>
    <td> 36g</td>
  </tr>
  <tr>
    <td> Ambient Temperature (Operating)</td>
    <td> 0-40℃</td>
  </tr>
  <tr>
    <td> Ambient Temperature (non-operating)</td>
    <td> 0-60℃</td>
  </tr>
  <tr>
    <td> Maximum Humidity (Operating)</td>
    <td> up to 95%</td>
  </tr>
  <tr>
    <td> Maximum Humidity (Non-Operating)</td>
    <td> up to 95%</td>
  </tr>
  <tr>
    <td> Altitude (Operating)</td>
    <td> -400 m to 2000 m</td>
  </tr>
</table>

<br>

## Ports and communication

```{figure} ./images/control_board/PDS_CTRL.drawio.png
:alt: PDS_CTRL
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Control board with highlighted ports
```

<br>

<table>
  <tr>
    <th> Connector name</th>
    <th> Included cable specification</th>
    <th> Wiring details</th>
  </tr>
  <tr>
    <td> SLAVE MODULES CONNECTORS</td>
    <td> 10-pin Molex PicoBlade</td>
    <td> Connect to each submodule</td>
  </tr>
  <tr>
    <td> STO1/2</td>
    <td> 2-pin Molex Microlock 1m</td>
    <td> Connect normally closed switch to safe supply (12-30V).</td>
  </tr>
  <tr>
    <td> FDCAN</td>
    <td> 3-pin Molex Microlock 1m</td>
    <td> Non-isolated FDCAN port for communication via CANdle or custom FDCAN.</td>
  </tr>
  <tr>
    <td> CHARGER DETECTION</td>
    <td> Optional</td>
    <td> Port to detect charging. Connect to charging add-on module.</td>
  </tr>
  <tr>
    <td> RS422</td>
    <td> Optional</td>
    <td> RS422 port with isolated power included on request.</td>
  </tr>
  <tr>
    <td> RGB SWITCH</td>
    <td> 6-pin Molex Microlock</td>
    <td> RGB switch port. Switch enables PDS and indidates states.</td>
  </tr>
</table>
<br>

The CAN FD interface in the PDS is designed to provide essential telemetry data, including information
on currents, voltages, and temperature, as well as to facilitate the configuration and control of the
system. Its transceiver is non-isolated with split termination on board and operates up to 8-Mbps. In order to connect FDCAN with PDS system user needs to connect FDCAN directly to Control Board. Please take a look at examples of [recommended architecture](architecture.md).

## Safety Turn Off
The PDS includes a safety mechanism for controlled power shut-off, similar to those found in standard motor controllers. It features two input channels, each capable of independently disconnecting power from the connected loads, ensuring safe operation. The inputs are protected against reverse polarity.

Each slave module can be integrated into the safety mechanism by setting the STO configuration switch accordingly.

```{figure} ./images/control_board/sto.drawio.png
:alt: PDS_CTRL_STO
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
STO1/2 logic circuit
```
Truth table for STO1/2 logic:
<table>
  <tr>
    <th> STO1_FB</th>
    <th> STO2_FB</th>
    <th> ENABLE_X_MCU</th>
    <th> STO_CONFIG_SWITCH</th>
    <th> ENABLE_X_CONNECTOR MODULE ENABLE INPUT STATE</th>
  </tr>
  <tr>
    <td> X</td>
    <td> X</td>
    <td> 0</td>
    <td> X</td>
    <td> 0</td>
  </tr>
  <tr>
    <td> X</td>
    <td> X</td>
    <td> 1</td>
    <td> 0</td>
    <td> 1</td>
  </tr>
  <tr>
    <td> 0</td>
    <td> 0</td>
    <td rowspan = "4"> 1</td>
    <td rowspan = "4"> 1</td>
    <td> 0</td>
  </tr>
  <tr>
    <td> 1</td>
    <td> 0</td>
    <td> 0</td>
  </tr>
  <tr>
    <td> 0</td>
    <td> 1</td>
    <td> 0</td>
  </tr>
  <tr>
    <td> 1</td>
    <td> 1</td>
    <td> 1</td>
  </tr>
</table>
<br>

Summarizing:
1. If STO_CONFIG_SWITCH is in position 0, the ENABLE state set by MCU is passed directly to the
output, regardless of the status of STO1_FB and STO2_FB
2. If STO_CONFIG_SWITCH is in position 1, the ENABLE state set by MCU is passed to the output
only when the STOx_FB signals state is 1

## RGB SWITCH
This port is dedicated to connecting the RGB switch which enables the PDS and reports the system state
with the RGB diodes.

```{figure} ./images/control_board/rgb_switch_states.drawio.png
:alt: PDS_CTRL_RGB_SWITCH
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
States and transitions on RGB switch
```
<table>
  <tr>
    <th> State</th>
    <th> Description</th>
  </tr>
  <tr>
    <td> Shutdown</td>
    <td> PDS is turned off with a quiescent current ~20uA.</td>
  </tr>
  <tr>
    <td> Battery monitor</td>
    <td> PDS shows the battery charge level with respect to the user-predefined voltage levels. In this state, all slave modules are turned off.</td>
  </tr>
  <tr>
    <td> Charging</td>
    <td> PDS slave modules are turned off. The CTRL module is enabled. The battery is charging. RGB button blinks slowly with color dependent on the battery voltage.</td>
  </tr>
  <tr>
    <td> Operating</td>
    <td> Normal operation. RGB switch indicates battery level same way as in battery monitor state. If the charger is connected the RGB switch additionally blinks slowly with BLUE/BAT_LEVEL color alternately.</td>
  </tr>
  <tr>
    <td> STO</td>
    <td> Device generally works as in operating state but RGB Led is indicating STO event by blinking RED / YELLOW.</td>
  </tr>
  <tr>
    <td> Shutdown ongoing</td>
    <td> All submodules except Isolated converters are disabled. RGB switch turns solid WHITE.</td>
  </tr>
</table>

<br>

Battery Level can be set in software using Candletool or CANdle-SDK (`setBatteryVoltageLevels(u32 batteryLvl1, u32 batteryLvl2)`).

```{figure} ./images/control_board/ind_bar.png
:alt: PDS_CTRL_BATTERY_LEVELS
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Battery levels and according color of RGB switch
```
