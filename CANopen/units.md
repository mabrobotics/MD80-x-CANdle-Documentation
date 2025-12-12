# System units

This file describes the SI units and their definitions used in MD CANopen devices compliant with the CiA 402 profile.

SI Units are defined in the objects:
 
- Position Unit — **0x60A8**
- Velocity Unit — **0x60A9**
- Acceleration Unit — **0x60AA**

SI object structure looks like this:

| **Bit 31...24** | **Bit 23...16** | **Bit 15...8** | **Bit 7...0** |
| --------------- | --------------- | -------------- | ------------- |
| Prefix          | Numerator       | Denominator    | Reserved (0)  |

**Table 1**: SI Units – Parameter Structure


Listed in the following table are the possible exponents (prefixes) and their values:

### Prefixes

| **Prefix** |   **Factor**    | **Symbol** | **Notation Index** |
| :--------: | :-------------: | :--------: | :----------------: |
|    Mega    | 10<sup>6</sup>  |     M      |        0x06        |
|    Kilo    | 10<sup>3</sup>  |     k      |        0x03        |
|     —      | 10<sup>0</sup>  |     —      |        0x00        |
|   Milli    | 10<sup>-3</sup> |     m      |        0xFD        |
|   Micro    | 10<sup>3</sup>  |     µ      |        0xFA        |

**Table 2**: SI unit prefixes – Notation index

### Numerators

|           **Name**            |     **Symbol**     | **Notation Index** |
| :---------------------------: | :----------------: | :----------------: |
|         Dimensionless         |         —          |        0x00        |
|            Meters             |         m          |        0x01        |
|            Radians            |        rad         |        0x10        |
|            Degrees            |        deg         |        0x41        |
|             Steps             |       steps        |        0xAC        |
|          Revolutions          |        rev         |        0xB4        |
|          Increments           |        inc         |        0xB5        |
| Revolutions per minute **\*** | rpm **or** rev/min |        0xC0        |

**Table 3**: SI unit numerators – Notation index

**\*** *Manufacturer specific unit*

### Denominators

|   **Name**    |  **Symbol**   | **Notation Index** |
| :-----------: | :-----------: | :----------------: |
|    second     |       s       |        0x03        |
|    minute     |      min      |        0x47        |
| square second | s<sup>2</sup> |        0x57        |
| cubic second  | s<sup>3</sup> |        0xA0        |

**Table 4**: SI unit denominators – Notation index