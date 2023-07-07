(homing)=
# Homing

Homing can be used to find the zero position in case there is no external encoder. 

Currently only sensorless homing is supported, meaning a collision of the limit and the load has to occur on each end of the allowed.

```{note}
In order for homing to work the actuator's Velocity PID and Position PID loops have to be tuned correctly. 
```