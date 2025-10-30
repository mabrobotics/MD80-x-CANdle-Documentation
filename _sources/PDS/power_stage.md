(pds_ps)=
# Power Stage

The PDS_PS module is a high-power power path designed to provide a safe and reliable power source
for robot actuators. 
Its features include:
- continuous current capacity of up to 50A,
- isolated voltage and current measurements for precise monitoring,
- bus-controlled with an electronic high-side switch for efficient power management
- inrush current limitation to prevent damage from startup surges,
- high-quality bulk capacitance for stable operation,
- protection against reverse polarity, over-voltage and over-current to ensure safety,
- transient protection for resilience against voltage spikes,
- thermal monitoring and safe operation.

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
    <td> 10-54V</td>
  </tr>
  <tr>
    <td> Input protection</td>
    <td> reverse polarity down to -54V, overvoltage, overcurrent (no fuse on the board, based on current monitoring), transients.</td>
  </tr>
  <tr>
    <td> Output current</td>
    <td> up to 50A</td>
  </tr>
  <tr>
    <td> Delivered power</td>
    <td> up to 2500W</td>
  </tr>
  <tr>
    <td> Total internal resistance</td>
    <td> 1.35 mohm</td>
  </tr>
  <tr>
    <td> Conduction losses at 50A current(excluding losses on the connectors' resistance)</td>
    <td> 3.375 W</td>
  </tr>
  <tr>
    <td> Power transfer efficiency</td>
    <td> up to 99.8%</td>
  </tr>
  <tr>
    <td> Output protection</td>
    <td> Over-current, over-voltage, over temperature, transient.</td>
  </tr>
  <tr>
    <td> Internal bus capacitance</td>
    <td> 376uF(low ESR Aluminum Hybrid Polymer Capacitors)</td>
  </tr>
  <tr>
    <td> Current consumption on standby(no load)</td>
    <td> 11.56 mA</td>
  </tr>
  <tr>
    <td> The quiescent current in the shutdown</td>
    <td> 1.97 uA</td>
  </tr>
  <tr>
    <td> Mass</td>
    <td> 43g</td>
  </tr>
  <tr>
    <td> Ambient Temperature (operating)</td>
    <td> 0-40℃</td>
  </tr>
  <tr>
    <td> Ambient Temperature (non-operating)</td>
    <td> 0-60℃</td>
  </tr>
  <tr>
    <td> Maximum Humidity (operating)</td>
    <td> up to 95%, non-condensing at 40℃</td>
  </tr>
  <tr>
    <td> Maximum Humidity (non-operating)</td>
    <td> up to 95%, non-condensing at 60℃</td>
  </tr>
  <tr>
    <td> Altitude (operating)</td>
    <td> -400 m to 2000 m</td>
  </tr>
</table>

<br>

```{figure} ./images/power_stage/PSv11.png
:alt: PDS_PS
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Power stage with highlighted ports
```

<br>

<table>
  <tr>
    <th> Connector name</th>
    <th> Included cable specification</th>
    <th> Wiring details</th>
  </tr>
  <tr>
    <td> MASTER MODULE</td>
    <td> 10-pin Molex PicoBlade</td>
    <td> Connect to control board</td>
  </tr>
  <tr>
    <td> POWER OUTPUT PORT 1/2/3</td>
    <td> No cables included</td>
    <td> Connect the actuators to Molex Micro-Fit ports</td>
  </tr>
  <tr>
    <td> BRAKE RESISTOR/AUXILLARY POWER SUPPLY</td>
    <td> 691340500006 included without cables</td>
    <td> Power output port for brake or actuators. Recommended connectors: 691340500006 or 691343510006.</td>
  </tr>
</table>

<!-- The module includes built-in hardware thermal protection and can automatically disable itself if it exceeds safe operating temperatures.-->

```{important}
POWER OUTPUT PORTS 1, 2, and 3 are dedicated to supplying power to actuators and do not support FDCAN communication to the PDS. However, FDCAN connectivity can be shared between MOLEX ports, as illustrated in [FDCAN Architecture](architecture) section.
```
