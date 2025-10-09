# Brake resistor

The PDS_BR module is a low-profile, high-power resistor with an integrated control and monitoring
system. It simplifies the management of overvoltage situations in the system, typically caused by
regenerative braking in motors. 
Key features include:
- onboard power resistors with a peak nominal power of 420W,
- built-in temperature monitoring for system safety,
- transient protection to prevent electrical surges,
- braking control through a MOSFET switch,
- adjustable trigger voltage via soware, providing flexibility.


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
    <td> Input protection</td>
    <td> transients, over temperature.</td>
  </tr>
  <tr>
    <td> Maximum dissipated power</td>
    <td> 420W</td>
  </tr>
  <tr>
    <td> Current consumption on standby(resistors disabled)</td>
    <td> 2,7 mA</td>
  </tr>
  <tr>
    <td> Mass</td>
    <td> 42g</td>
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
    <td> up to 95%, non-condensing at 40 ºC</td>
  </tr>
  <tr>
    <td> Maximum Humidity (Non-Operating)</td>
    <td> up to 95%, non-condensing at 60 ºC</td>
  </tr>
  <tr>
    <td> Altitude (Operating)</td>
    <td> -400 m to 2000 m</td>
  </tr>
</table>

The BRAKE_ENABLE is triggered when an overvoltage condition occurs on the PS module connected to the BR module. In such cases, excess energy is dissipated through the braking resistors. Proper cooling of the BR module is essential to prevent overheating and potential thermal shutdown. 
<!-- The module includes built-in hardware thermal protection and can automatically disable itself if it exceeds safe operating temperatures.-->

```{figure} ./images/brake_resistor/brv10.png
:alt: PDS_CTRL
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Brake resistor with highlighted ports
```

This port is designed for connecting the PDS_PS output. In the event of overvoltage caused by
regenerative braking, this port allows excess energy to be safely dissipated through an external brake
resistor or redirected to energy recovery systems. This ensures the system operates within safe voltage
limits, protecting components from potential damage.
