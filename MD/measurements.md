# Measurements

MD drivers are equipped with sensors that allow for measuring the motor position, velocity, and
torque. Whether the motor has an integrated gearbox or not, **the position, velocity, and torque**
are in the output shaft reference frame. This means that changing the position from 0.0 to 2$\\pi$
radians, will result in approximately one rotation of the motor for direct-drive (gearless) servos
and approximately one rotation of the gearbox output shaft for geared motors.

## Position

To measure the position of the rotor the MD driver uses an internal magnetic encoder. The resolution
of the encoder is 14 bits (16384 counts per rotation). The drive aggregates all the measurements to
provide **multi-rotation positional feedback**. The reference position (0.0 rad) is set by the user
and stored in the non-volatile memory. Please see [`candletool md zero`](candletool_commands)
command for more information on how to set the desired zero position.

```{important}
When using geared actuators with gear ratios above 1:1 it is not possible to determine the position after startup unambiguously, since the motor completes multiple rotations per single rotation of the output shaft. For example, for a 2:1 gearbox, there are two sections within a single output shaft rotation where the motor shaft is in the same position. Unless the motor is placed in the wrong “section” during startup the absolute encoder functionality will work. To deal with this issue please see the [axu encoder](aux_encoders).
```

## Velocity

The velocity is estimated by measuring position change in time, at a frequency of 40kHz. The
measurements are then filtered using a low-pass filter with a cut-off frequency of 5 kHz since the
position differentiation method introduces noise.

## Torque

Actuator torque is estimated by measuring motor phase currents. This method can be used on low-gear
ratio actuators (preferably below 9:1), that are easily back-drivable, to get an estimate of the
torque applied by the motor. In applications with higher gear ratios, the torque readout might be
less accurate due to excessive friction in the gearbox.

## Energy, input current and motor phase current
The MD's come with cable set to connect it to power supply and CAN network, with usage of CANdle or to custom hardware. To avoid confusion during wiring it is important to understand the difference between motor phase current and input current from the power source. Input current depends strongly on the total mechanical power delivered by the actuator, so increasing the motor torque and velocity increases that quantity. In the case of motor phase current, it is produced by the motor controller, and the best way to imagine the relation is to think about the motor controller as a kind of three-phase rotating DC/DC converter - it sets the output current to the desired level by controlling the phase voltage with the PWM. This is achieved by the high frequency FOC loop that converts the desired torque into the voltage applied to the motor terminals. The generated torque is proportional to the motor phase current, but the input current depends on the power that transferred to the load. Relationship between output power, input current and motor phase current is presented below:

```{figure} ./images/md_motor_wiring_diag.jpg
:alt: candle
:scale: 70%
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```
```{figure} ./images/current_comp.png
:alt: candle
:scale: 70%
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

For simplicity only the linear operation region is presented. In case of FOC controlled actuator that means setting the reference value to Iq current regulator, while keeping the Id current at 0A - without field weakening - classic MTPA (maximum torque per amper). Relation between torque and Iq current is linear:

$$
\tau = K_t \cdot I_q
$$
where:
- $\tau$ — motor torque,
- $K_t$ — torque constant,
- $I_q$ — quadrature axis current, aligned 90° electrically with the rotor flux,
  directly proportional to the electromagnetic torque.

## Motor operating conditions: Case A vs Case B

To illustrate the difference between two distinct motor operating conditions, two points are marked on the graph: **A** and **B**.

### Case A — holding torque, zero speed

| Parameter | Value |
|---|---|
| Torque / current setpoint | 20 A |
| Motor state | Shaft blocked or heavily loaded (impedance mode control) |
| Speed | 0 RPM |
| Input current | ~2 A — covers only system power losses |

**Example scenarios:**
- Actuators in a heavy-loaded robotic arm that don't move,
- Actuators in a humanoid robot's arms during walking while holding heavy objects,
- Actuators in a quadruped robot's legs during standing with heavy load on the back,
- Actuators in an exoskeleton supporting a human during transport of heavy load in a fixed position.

> All these scenarios share the same load scheme — significant motor phase current, but no mechanical work done. Energy is lost as heat in the wires, motor controller, power supply, and primarily in the motor coil resistance. **Efficiency: 0%.**

### Case B — active work under load

| Parameter | Value |
|---|---|
| Torque / current setpoint | 20 A |
| Motor state | Heavy load, not blocked — producing torque |
| Speed | 50 RPM |
| Input current | ~10 A — covers losses **and** physical work |

**Example scenarios:**
- Actuators in a heavy-loaded robotic arm that move quickly,
- Actuators in a humanoid robot's arms during lifting heavy objects,
- Actuators in a quadruped robot's legs during running with heavy load on the back,
- Actuators in an exoskeleton supporting a human during lifting heavy objects.

### Why the same current means different power?

In these scenarios, the motor spins and moves the load, so physical work is done.
The efficiency depends on the quality of the motor, gearbox, motor controller,
motor control algorithm, temperature, and many other conditions.

To understand how the same torque/phase current can result in different power
levels, we need to examine the mathematical model of the BLDC motor.
The phase current equation is:

$$
I_{ph} = \frac{1}{R} \left( U_{ph} - L \frac{dI_{ph}}{dt} - K_e \, \omega \right)
$$

where:
- $I_{ph}$ — phase current [A],
- $R$ — phase winding resistance [Ω],
- $U_{ph}$ — phase voltage [V],
- $L$ — phase winding inductance [H]
- $K_e$ — back-EMF constant [V·s/rad],
- $\omega$ — angular velocity [rad/s].

Back-EMF ($K_e \, \omega$) is proportional to the motor velocity. When the motor
spins under load, the current regulator increases the applied voltage (higher
PWM duty cycle) to maintain the same phase current. As both voltage and current
are present, the electrical power delivered to the motor increases — represented
by the area under the voltage and current curves.

> **Power = $U_{ph} \times I_{ph}$**
>
> At zero speed, $U_{ph}$ is small (only covering resistive losses),
> so the power area is small despite the same current.
> At 50 RPM, $U_{ph}$ must increase to overcome back-EMF,
> expanding the power area significantly.

### Operating conditions in mobile robots

In mobile robots, operating conditions described above are usually mixed. For example:

- **Legged robots** alternate between running (high torque and power) and standing
  (low power, high torque),
- **Wheeled robots** don't always accelerate — steady-state cruising draws
  significantly less power than peak acceleration.

This dynamic range makes thermal management and current budgeting critical
across all actuator types.

### Losses and power scaling — MD Motor Controllers

For the MD motor controllers, switching and conduction losses are very similar
in both operating scenarios (Case A and Case B). This is because most of the
heat is dissipated in the MOSFETs themselves.

At higher power levels, additional losses appear in:

- **PCB power traces** — resistive heating scales with $I^2 R$
- **Connectors** — contact resistance becomes significant at higher currents

### Input current bottleneck

Beyond the maximum phase current — which is limited by MOSFET losses and cooling
efficiency — the **connector current rating** becomes the primary bottleneck in
scaling output mechanical power.

| Controller | Connector | Max Input Current | Limiting Factor |
|---|---|---|---|
| MD80 | Molex Micro Fit | 10 A | Connector rating |
| MD20 | Molex Micro Lock + | 3.1 A | Connector rating |

### Need more power?

For higher power requirements, alternative connector solutions are available:

- **Molex MicroFit Plus** for MD80 — higher current rating
- Custom connector configurations on request

Contact us to discuss your specific application requirements.