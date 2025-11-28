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

| **Parameter**                            | **Value**                                                                                                         |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Input voltage                            | 10–54 V                                                                                                          |
| Input protection                         | Reverse polarity down to –54 V, overvoltage, overcurrent (with fuse), transients                                 |
| Power                                    | 60 W                                                                                                             |
| DC/DC converter output                   | Available options: 3.3 VDC 12 A, 5 VDC 12 A, 12 VDC 5 A, 15 VDC 4 A, 24 VDC 2.5 A                               |
| Output protection                        | Short circuit (continuous), overload, over-voltage, over-temperature, input undervoltage lockout                 |
| Current consumption on standby (no load) | 7.8 mA                                                                                                           |
| Quiescent current in shutdown            | 6.57 µA                                                                                                          |
| Mass                                     | 74 g                                                                                                             |
| Ambient Temperature (Operating)          | 0–40 ℃                                                                                                           |
| Ambient Temperature (Non-operating)      | 0–60 ℃                                                                                                           |
| Maximum Humidity (Operating)             | up to 95%, non-condensing at 40 ℃                                                                                |
| Maximum Humidity (Non-operating)         | up to 95%, non-condensing at 60 ℃                                                                                |
| Altitude (Operating)                     | –400 m to 2000 m                                                                                                 |

```{figure} ./images/isolated_converter/ICv10.png
:alt: PDS_CTRL
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Isolated converter with highlighted ports
```

The PDS_IC comes with a factory-assembled thermistor mounted on DC/DC converter. It also includes 2 pcs of 691340500002 without cables.
