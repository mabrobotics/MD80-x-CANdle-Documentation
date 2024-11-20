# Utilities
(GPIO)=
## GPIO

All of the MD controllers have two multi-purpose GPIO pins. Currently they have two functionalities:

- Auto Brake - in this mode MDxx will automatically engage MAB Robotics's provided braking systems via GPIO A pin, please contact us for more information in that regard
- GPIO input - in this mode MDxx will output GPIO pin states to state register (*userGpioState 0x161*)

```{important}

The GPIO are connected directly to board's MCU. **DO NOT** drive this pins higher than +5V or lower than 0V as this **WILL** damage the board.

Also the GPIO pins are floating so if you want to use those pins as an external function switches, do so with proper pull-up/down resistor or push-pull circuitry.

```