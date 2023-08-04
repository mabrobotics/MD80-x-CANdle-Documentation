(homing)=
# Homing

Homing can be used to find the zero position in case there is no external encoder. 

Currently only sensorless homing is supported, meaning a collision of the limit and the load has to occur on each end of the allowed range.

```{note}
In order for homing to work the actuator's Velocity PID and Position PID loops have to be tuned correctly. 
```

## Homing settings

Homing can be performed after a certain setup is complete. The setup is done using motor config file and `mdtool setup motor` command. For more information refer to [homing config](homing_config) section.

