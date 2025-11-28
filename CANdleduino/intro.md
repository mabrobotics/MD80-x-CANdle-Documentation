# CANdleduino

Library for communication with drives for Arduino (AVR and Renesas) and Teensy >4.0.

```{note} 
AVR based Arduino boards don't support native CAN, therefore Candleduino supports MCP2515 via SPI.
```

It can be included into a project via header-file:

```
#include "Candleduino.hpp"
```

## Functionalities

Main features of MD module include:

- Creating MDs assigned to instance with unique IDs
- Managing internal registers of MDs
- Provides helper functions for managing MDs, for example: `getPosition()`, `zero()`,
  `setTargetPosition()`

## Usage
```cpp
uint16_t ID = 100; //ID of the MD drive

MD md(ID); 
// MD md(ID, CS_PIN); for custom CS_PIN (Arduino AVR and MCP2515), default is 9

// FlexCAN_T4FD<CAN3, RX_SIZE_256, TX_SIZE_16> CANbus; //CANFD
//or
// FlexCAN_T4<CAN3, RX_SIZE_256, TX_SIZE_16> CANbus; //CAN2.0
// MD md(ID, &CANbus); for Teensy

md.init(); //initialize MD object
```

For basic communication there are predefined commands like:
```cpp
md.blink();

md.getMosfetTemperature(float &temperature);

md.setPositionPIDparam(float kp, float ki, float kd, float integralMax);

...
```
For other registers it is recommended to use:

```cpp
MD::Error_t MD::readRegister<T>(MD::Message<T> &registerData)
MD::Error_t MD::writeRegister<T>(MD::Message<T> registerData)

MD::Error_t MD::readRegister<T>(uint16_t registerId, T &registerData)
MD::Error_t MD::writeRegister<T>(uint16_t registerId, T registerData)
```

Or CANFD only use readRegisters or writeRegisters for multiple data frame

```cpp
MD::Error_t MD::readRegisters<T>(MD::Message<T> registerData, ...)
MD::Error_t MD::writeRegisters<T>(MD::Message<T> registerData, ...)
```

For multiple MD drives user can create multiple MD object with unique ID's.

Example:
```cpp
MD md1(100);
MD md2(120);

md1.init();
md2.init();

md1.blink();
md2.blink();
```

Pleace look at [register table](../MD/Communication/fdcan.md#register-table) to find more details about registers and their types.