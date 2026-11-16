(canopen_state_machine)=
# State Machine

The drive implements the CiA 402 state machine. It decides whether the power stage is energised and
whether setpoints are acted on. It is driven entirely by the Controlword 0x6040 and observed through
the Statusword 0x6041.

This is separate from [network management](canopen_nmt). NMT decides whether the drive talks; the
CiA 402 state machine decides whether it moves.

## States

| State                 | Statusword & 0x006F | Typical raw value | Power stage | Setpoints followed |
| --------------------- | ------------------- | ----------------- | ----------- | ------------------ |
| Not ready to switch on | 0x0000             | 0x0200            | off         | no                 |
| Switch on disabled    | 0x0040              | 0x0240            | off         | no                 |
| Ready to switch on    | 0x0021              | 0x0221            | off         | no                 |
| Switched on           | 0x0023              | 0x0223            | on          | no                 |
| Operation enabled     | 0x0027              | 0x0237 or higher  | on          | yes                |
| Quick stop active     | 0x0007              | 0x0217            | on          | no, decelerating   |
| Fault reaction active | 0x000F              | 0x020F            | stopping    | no                 |
| Fault                 | 0x0008              | 0x0208            | off         | no                 |

```{important}
The statusword carries more than the state bits, so always mask it with 0x006F before comparing it to
a state. Comparing the raw value against 0x0027 never matches.
```

## Statusword bits

| Bit | Name                | Meaning                                                              |
| --- | ------------------- | -------------------------------------------------------------------- |
| 0-3, 5, 6 | State         | See the table above                                                  |
| 4   | Voltage enabled     | Set in Operation enabled and Quick stop active, while the power stage drives the motor |
| 9   | Remote              | Always set, the controlword is always processed                      |
| 10  | Target reached      | Profile Position: within Position Window 0x6067 of the target. Profile Velocity: within Velocity Window 0x606D of the target |
| 11  | Internal limit active | A velocity, torque or, in position modes, position target is being clipped by a limit |
| 12  | Mode specific       | Profile Position: set-point acknowledge. Profile Velocity: speed zero, the speed is within 0x606D of zero. Cyclic Synchronous Position and Velocity: drive follows the command |

Bits 10, 11 and 12 are only set in Operation enabled. Bits 7, 8, 13, 14 and 15 are always 0.

Bit 15 of Quick Status 0x2022:1 also reports target reached, using the same windows, and is mapped
into TPDO1 by default.

Not ready to switch on is transient. The drive leaves it for Switch on disabled on its own as soon
as the state machine runs, so in practice the first state a master observes is Switch on disabled,
raw value 0x0240.

## Controlword commands

Each command is recognised by masking the controlword and comparing it to a fixed value, so bits
outside the mask are ignored.

| Command                       | Mask   | Value  | Common controlword |
| ----------------------------- | ------ | ------ | ------------------ |
| Shutdown                      | 0x0087 | 0x0006 | 0x0006             |
| Switch on                     | 0x0087 | 0x0007 | 0x0007             |
| Switch on and enable operation | 0x008F | 0x000F | 0x000F            |
| Disable voltage               | 0x0082 | 0x0000 | 0x0000             |
| Quick stop                    | 0x0086 | 0x0002 | 0x0002             |
| Disable operation             | 0x008F | 0x0007 | 0x0007             |
| Enable operation              | 0x008F | 0x000F | 0x000F             |
| Fault reset                   | 0x0080 | 0x0080 | 0x0080             |

## Transitions

| From                  | Controlword       | To                    |
| --------------------- | ----------------- | --------------------- |
| Not ready to switch on | automatic        | Switch on disabled    |
| Switch on disabled    | Shutdown          | Ready to switch on    |
| Ready to switch on    | Switch on         | Switched on           |
| Ready to switch on    | Switch on and enable operation | Operation enabled |
| Ready to switch on    | Disable voltage or Quick stop | Switch on disabled |
| Switched on           | Enable operation  | Operation enabled     |
| Switched on           | Shutdown          | Ready to switch on    |
| Switched on           | Disable voltage   | Switch on disabled    |
| Operation enabled     | Disable operation | Switched on           |
| Operation enabled     | Shutdown          | Ready to switch on    |
| Operation enabled     | Disable voltage   | Switch on disabled    |
| Operation enabled     | Quick stop        | Quick stop active     |
| Quick stop active     | Disable voltage   | Switch on disabled    |
| Fault reaction active | automatic         | Fault                 |
| Fault                 | Fault reset       | Switch on disabled    |

## Enabling the drive

From a freshly powered drive the sequence is two writes to 0x6040:

1. Write 0x0006. The drive moves to Ready to switch on, statusword & 0x006F = 0x0021.
2. Write 0x000F. The drive moves through Switched on to Operation enabled, statusword & 0x006F =
   0x0027.

Writing 0x000F on its own does nothing, because Switch on disabled only responds to Shutdown. Always
read the statusword back, mask it with 0x006F and confirm 0x0027 before sending setpoints.

```{note}
Select the [mode of operation](canopen_modes) and write a sensible setpoint before enabling. The
drive starts following whatever is already in the target objects the moment it reaches Operation
enabled.
```

## Quick stop

Quick stop brings the shaft to rest at the rate in Quick Stop Deceleration 0x6085 while the power
stage stays energised. Enter it by writing 0x0002 from Operation enabled.

The drive stays in Quick stop active until you write Disable voltage, 0x0000, which returns it to
Switch on disabled. It does not release on its own once the shaft has stopped. From there, re-enable
with the ordinary 0x0006 then 0x000F sequence.

The [heartbeat consumer](canopen_nmt) triggers the same quick stop automatically when a monitored
master falls silent.

## Faults

An internal fault, meaning any error bit in the [status registers](canopen_diagnostics), forces the
state machine to Fault reaction active regardless of the controlword. The drive stops the motor,
then moves to Fault on its own and de-energises.

Recovery takes two steps, and the order matters:

1. Clear the underlying condition, then clear the error bits by writing 1 to Clear Errors 0x2023:10.
2. Write Fault reset, 0x0080, to 0x6040 to move from Fault back to Switch on disabled.

Resetting the state machine while the error bit is still set puts the drive straight back into
Fault. Read 0x2022 to find out what actually failed before attempting recovery.
