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


| **Parameter**                                 | **Value**                                                                                  |
|-----------------------------------------------|--------------------------------------------------------------------------------------------|
| Input voltage                                 | 12–54 V                                                                                   |
| Input protection                              | Transients, over temperature                                                              |
| Maximum dissipated power                       | 420 W                                                                                     |
| Current consumption on standby (resistors disabled) | 2.7 mA                                                                                  |
| Mass                                          | 42 g                                                                                       |
| Ambient Temperature (Operating)               | 0–40 ℃                                                                                     |
| Ambient Temperature (Non-operating)           | 0–60 ℃                                                                                     |
| Maximum Humidity (Operating)                  | up to 95%, non-condensing at 40 ℃                                                         |
| Maximum Humidity (Non-operating)              | up to 95%, non-condensing at 60 ℃                                                         |
| Altitude (Operating)                          | –400 m to 2000 m                                                                          |

The BRAKE_ENABLE is triggered when an overvoltage condition occurs on the PS module connected to the BR module. In such cases, excess energy is dissipated through the braking resistors. Proper cooling of the BR module is essential to prevent overheating and potential thermal shutdown. 
<!-- The module includes built-in hardware thermal protection and can automatically disable itself if it exceeds safe operating temperatures. -->

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
