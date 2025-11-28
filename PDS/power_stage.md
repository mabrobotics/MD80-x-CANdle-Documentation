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

| **Parameter**                                                                 | **Value**                                                                                     |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Input voltage                                                                  | 10–54 V                                                                                       |
| Input protection                                                               | Reverse polarity down to –54 V, overvoltage, overcurrent (no fuse on the board, based on current monitoring), transients |
| Output current                                                                 | up to 50 A                                                                                    |
| Delivered power                                                                | up to 2500 W                                                                                  |
| Total internal resistance                                                      | 1.35 mΩ                                                                                       |
| Conduction losses at 50 A current (excluding connector resistance)             | 3.375 W                                                                                       |
| Power transfer efficiency                                                      | up to 99.8%                                                                                   |
| Output protection                                                              | Over-current, over-voltage, over-temperature, transient                                        |
| Internal bus capacitance                                                       | 376 µF (low ESR Aluminum Hybrid Polymer Capacitors)                                           |
| Current consumption on standby (no load)                                       | 11.56 mA                                                                                      |
| Quiescent current in shutdown                                                  | 1.97 µA                                                                                       |
| Mass                                                                          | 43 g                                                                                          |
| Ambient Temperature (Operating)                                                | 0–40 ℃                                                                                        |
| Ambient Temperature (Non-operating)                                            | 0–60 ℃                                                                                        |
| Maximum Humidity (Operating)                                                   | up to 95%, non-condensing at 40 ℃                                                             |
| Maximum Humidity (Non-operating)                                               | up to 95%, non-condensing at 60 ℃                                                             |
| Altitude (Operating)                                                           | –400 m to 2000 m                                                                              |

```{figure} ./images/power_stage/PSv11.png
:alt: PDS_PS
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
:width: 600px
Power stage with highlighted ports
```

| **Connector Name**                  | **Included Cable Specification** | **Wiring Details**                                                                                                       |
|------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| MASTER MODULE                      | 10-pin Molex PicoBlade           | Connect to control board                                                                                                |
| POWER OUTPUT PORT 1/2/3            | No cables included               | Connect the actuators to Molex Micro-Fit ports                                                                          |
| BRAKE RESISTOR / AUXILIARY POWER SUPPLY | 691340500006 included without cables | Power output port for brake or actuators. Recommended connectors: 691340500006 or 691343510006. |

The module includes built-in hardware thermal protection and can automatically disable itself if it exceeds safe operating temperatures.

```{important}
POWER OUTPUT PORTS 1, 2, and 3 are dedicated to supplying power to actuators and do not support FDCAN communication to the PDS. However, FDCAN connectivity can be shared between MOLEX ports, as illustrated in [FDCAN Architecture](architecture) section.
```
