(pds_ic)=

# Isolated converter

The PDS_IC module features an isolated DC/DC converter, providing a secure and stable power supply
for sensitive electronic systems, such as computers and subsystems.
The DC/DC converter modules are available in power ratings ranging from 60 W to 300 W, allowing them to support a wide variety of power requirements.
Key characteristics include:

- isolated power line with a configurable output voltage,
- isolated voltage and current measurements on the isolated bus,
- temperature monitoring for reliable operation,
- reverse polarity, over-voltage and over-current protection for safety,
- integrated EMC filter to reduce electromagnetic interference,
- transient protection to guard against sudden voltage spikes.

|**Parameter**|**Value**|
|-------------|---------|
| Input voltage| 16-54V (60W, 150W) <br> 36-54V (300W)|
| Input protection| Reverse polarity down to –54 V, overvoltage, overcurrent (with fuse), transients|
| Power and DC/DC converter output| **60W**: 3.3V/12A, 5V/12A, 12V/5A, 15V/4A, 24V/2.5A <br> **150W**:12V/13A, 24V/6.5A <br> **300W**: 28V/9.4A|
| Output protection| Short circuit (continuous), overload, over-voltage, over-temperature, input undervoltage lockout|
| Current consumption on enabled (no load) | 7.8 mA (60W) <br> 160mA (24V, 150W) <br> 300mA (12V, 150W) <br> 100mA (28V, 300W)|
| Quiescent current in shutdown | 6.57 µA|
| Mass| 74 g (60W) <br> 90g (150W, 300W)|
| Ambient Temperature (Operating) | 0–40 ℃ |
| Ambient Temperature (Non-operating)| 0–60 ℃|
| Maximum Humidity (Operating)| up to 95%, non-condensing at 40 ℃|
| Maximum Humidity (Non-operating)| up to 95%, non-condensing at 60 ℃|
| Altitude (Operating)| –400 m to 2000 m|

```{important}
Higher power IC like 150W and 300W are expected to generate increased heat; therefore, adequate cooling is recommended.
```

```{figure} ./images/isolated_converter/ICv10.png
:alt: PDS_CTRL
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Isolated converter with highlighted ports
```

The PDS_IC comes with a factory-assembled thermistor mounted on DC/DC converter. It also includes 2 pcs of 691340500002 without cables.

To operate IC and configure its parameters such as OCD level or temperature limit use commands in [CANdle-SDK PDS commands](../CANdle-SDK/candlelib/PDSModule.md) and [candletool for PDS](../CANdle-SDK/candletool/Commands.md#candletool-pds)