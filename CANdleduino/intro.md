# CANdleduino

[Candleduino](https://github.com/mabrobotics/Candleduino) is a ibrary for communication with drives for Arduino (AVR and Renesas) and Teensy >4.0.

```{note} 
AVR based Arduino boards don't support native CAN, therefore Candleduino supports MCP2515 via SPI.
```

## Functionalities

Main features of MD module include:

- Creating MD and PDS assigned to instance with unique IDs
- Managing internal registers of MD and properties of PDS
- Provides helper functions for managing MD and PDS, for example: 
`getPosition()`, `zero()`, `getVoltage(PDSmodule module, &voltage)`, `enable(PDSmodule module)`

## MD library
```cpp
#include "MD_arduino.hpp"
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
Error_t readRegister<T>(Message<T> &registerData)
Error_t writeRegister<T>(Message<T> registerData)

Error_t readRegister<T>(uint16_t registerId, T &registerData)
Error_t writeRegister<T>(uint16_t registerId, T registerData)
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

### Examples

[Read and write](https://github.com/mabrobotics/Candleduino/blob/main/examples/MD_read_write/MD_read_write.ino)
This example shows basic usage of all possible communication functionalities.

[Impedance control](https://github.com/mabrobotics/Candleduino/blob/main/examples/MD_impedance_control/MD_impedance_control.ino)
This example demonstrates how to control MD drive using Arduino or Teensy.

## PDS library

```{note} 
PDS library works only with Teensy boards with native CANFD compatibility.
```

```cpp
#include "PDS_arduino.hpp"
uint16_t ID = 100; //ID of the PDS

FlexCAN_T4FD<CAN3, RX_SIZE_256, TX_SIZE_16> CANbus; //CANFD

PDS pds(ID, &CANbus);

pds.init(); //initialize PDS object
```
For simplicity, there is a structure called PDSmodule:

Example:
```cpp
PDSmodule IC = {ISOLATED_CONVERTER, 2}; // {NAME, SOCKET_INDEX}
```
For basic communication there are predefined commands like:
```cpp
pds.enable(PDSmodule module);
pds.getTemperature(PDSmodule module, float &temperature);
...
```
Some functions are dedicated to only Power Stage or Isolated like `setOCDlevel(<PS> or <IC>, <OCDlevel>)` or `bindBrakeResistor(<PS>, <BR index>)`

Similarly to MD, PDS uses the same Message structure to send data as properties.
```cpp
Error_t readProperty(PDSmodule module, Message<T> &propertyData)
Error_t readProperty(PDSmodule module, uint8_t propertyId, T &propertyData)
Error_t readProperties(PDSmodule module, T &...message)

Error_t writeProperty(PDSmodule module, Message<T> propertyData)
Error_t writeProperty(PDSmodule module, uint8_t propertyId, T propertyData)
Error_t writeProperties(PDSmodule module, T... message)
```

For multiple PDS stacks simply use multiple instances:

Example:
```cpp
PDS pds1(100, &canBus);
PDS pds2(120, &canBus);
```

### Examples
[Read and write](https://github.com/mabrobotics/Candleduino/blob/main/examples/PDS_read_write/PDS_read_write.ino)
This example shows basic usage of all possible communication functionalities.

[PDS modules](https://github.com/mabrobotics/Candleduino/blob/main/examples/PDS_modules/PDS_modules.ino)
This example configures Isolated Converter, Power Stage and Brake Resistor, enables them and reads the data.


Please look at [register table](../MD/Communication/fdcan.md#register-table) and [properties table](https://mabrobotics.github.io/MD80-x-CANdle-Documentation/PDS/communication.html#properties) to find more details about registers/properites and their types.