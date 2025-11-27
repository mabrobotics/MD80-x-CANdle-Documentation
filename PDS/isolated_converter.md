(pds_ic)=

# Isolated converter

The PDS_IC module features an isolated DC/DC converter, providing a secure and stable power supply
for sensitive electronic systems, such as computers and subsystems.
Key characteristics include:

- isolated power line with a configurable output voltage,
- isolated voltage and current measurements on the isolated bus,
- temperature monitoring for reliable operation,
- reverse polarity, over-voltage and over-current protection for safety,
- integrated EMC filter to reduce electromagnetic interference,
- transient protection to guard against sudden voltage spikes.

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
    <td> reverse polarity down to -54V, overvoltage, overcurrent(with fuse), transients.</td>
  </tr>
  <tr>
    <td> Power</td>
    <td> 60W</td>
  </tr>
  <tr>
    <td> DC/DC converter output</td>
    <td> Available options: 3.3VDC 12A, 5VDC 12A, 12VDC 5A, 15VDC 4A, 24VDC 2.5A</td>
  </tr>
  <tr>
    <td> Output protection</td>
    <td> Short circuit (Continuous), overload, over-voltage, over temperature, input undervoltage lockout.</td>
  </tr>
  <tr>
    <td> Current consumption on standby(no load)</td>
    <td> 7,8 mA</td>
  </tr>
  <tr>
    <td> The quiescent current in the shutdown</td>
    <td> 6,57 uA</td>
  </tr>
  <tr>
    <td> Mass</td>
    <td> 74g</td>
  </tr>
  <tr>
    <td> Ambient</td>
    <td> Temperature (Operating) 0-40℃</td>
  </tr>
  <tr>
    <td> Ambient Temperature</td>
    <td> (non-operating) 0-60℃</td>
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

```{figure} ./images/isolated_converter/ICv10.png
:alt: PDS_CTRL
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Isolated converter with highlighted ports
```

The PDS_IC comes with a factory-assembled thermistor mounted on DC/DC converter. It also includes 2 pcs of 691340500002 without cables.
