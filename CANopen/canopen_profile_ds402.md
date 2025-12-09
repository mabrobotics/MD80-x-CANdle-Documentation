
#  Object Dictionary

## Communication Area

## Manufacturer Specific Area

### 0x2001 – Firmware Info
| Name                        | Index:Sub | Type              | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ----------------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2001:0  | UNSIGNED8         |    8     |     0x03     |    —     |    —     |   —   |  RO   |   —   |
| Commit Hash                 | 0x2001:1  | VISIBLE_STRING(8) |    64    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Build Date                  | 0x2001:2  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Version                     | 0x2001:3  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |

### 0x2002 – Bootloader Info
| Name                        | Index:Sub | Type              | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ----------------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2002:0  | UNSIGNED8         |    8     |     0x04     |    —     |    —     |   —   |  RO   |   —   |
| Bootloader Fixed            | 0x2002:1  | BOOLEAN           |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Commit Hash                 | 0x2002:2  | VISIBLE_STRING(8) |    64    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Build Date                  | 0x2002:3  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Version                     | 0x2002:4  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |

### 0x2003 – Hardware Info
| Name                        | Index:Sub | Type               | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ------------------ | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2003:0  | UNSIGNED8          |    8     |     0x05     |    —     |    —     |   —   |  RO   |   —   |
| Bridge Type                 | 0x2003:1  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Legacy Version              | 0x2003:2  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Device Type                 | 0x2003:3  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Device Revision             | 0x2003:4  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Core ID                     | 0x2003:5  | VISIBLE_STRING(12) |    96    |      0       |    —     |    —     |   —   |  RO   |   —   |

### 0x2004 – System Command
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2004:0  | UNSIGNED8 |    8     |     0x0D     |   —   |   —   |   —   |  RO   |   —   |
| Blink                       | 0x2004:1  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Reset                       | 0x2004:2  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Calibrate                   | 0x2004:3  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Calibrate Aux               | 0x2004:4  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Zero                        | 0x2004:5  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Calibrate Current           | 0x2004:6  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Test Main Encoder           | 0x2004:7  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Test Aux Encoder            | 0x2004:8  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Save                        | 0x2004:9  | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Revert Factory Settings     | 0x2004:10 | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Clear Errors                | 0x2004:11 | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| Clear Warnings              | 0x2004:12 | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |
| CAN Reinit                  | 0x2004:13 | BOOLEAN   |    8     |      0       |   —   |   —   |   —   |  WO   |   —   |

### 0x2005 – System Status
| Name                        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2005:0  | UNSIGNED8  |    8     |     0x09     |    —     |    —     |   —   |  RO   |   —   |
| Main Encoder Status         | 0x2005:1  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Aux Encoder Status          | 0x2005:2  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Calibration Status          | 0x2005:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Bridge Status               | 0x2005:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Hardware Status             | 0x2005:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Homing Status               | 0x2005:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Motion Status               | 0x2005:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Communication Status        | 0x2005:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Misc Status                 | 0x2005:9  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x2006 – Motor Settings
| Name                        | Index:Sub | Type               | Bit Size | Default Data | Min Data | Max Data |  Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ------------------ | :------: | :----------: | :------: | :------: | :----: | :---: | :---: |
| Highest sub-index supported | 0x2006:0  | UNSIGNED8          |    8     |     0x14     |    —     |    —     |   —    |  RO   |   —   |
| Pole Pairs                  | 0x2006:1  | UNSIGNED32         |    32    |      0       |    —     |    —     |   —    |  RW   |   —   |
| Torque Constant             | 0x2006:2  | REAL32             |    32    |      0       |    —     |    —     |  Nm/A  |  RW   |   —   |
| Inductance                  | 0x2006:3  | REAL32             |    32    |      0       |    —     |    —     |   H    |  RO   |   —   |
| Resistance                  | 0x2006:4  | REAL32             |    32    |      0       |    —     |    —     |  Ohm   |  RO   |   —   |
| Torque Bandwidth            | 0x2006:5  | UNSIGNED16         |    16    |      0       |    —     |    —     |   Hz   |  RW   |   —   |
| Name                        | 0x2006:6  | VISIBLE_STRING(24) |   192    |      MD      |    —     |    —     |   —    |  RW   |   —   |
| Motor Shutdown Temp         | 0x2006:7  | UNSIGNED8          |    8     |      80      |    —     |    —     | &deg;C |  RW   |   —   |
| Calibration Mode            | 0x2006:8  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —    |  RW   |   —   |
| CAN ID                      | 0x2006:9  | UNSIGNED32         |    32    |      10      |    —     |    —     |   —    |  RW   |   —   |
| CAN Datarate                | 0x2006:10 | UNSIGNED32         |    32    |   1000000    |    —     |    —     |   Hz   |  RW   |   —   |
| CAN Timeout                 | 0x2006:11 | UNSIGNED16         |    16    |     200      |    —     |    —     |   ms   |  RW   |   —   |
| CAN Termination             | 0x2006:12 | UNSIGNED8          |    8     |      0       |    —     |    —     |   —    |  RW   |   —   |
| KV                          | 0x2006:13 | UNSIGNED16         |    16    |      0       |    —     |    —     | rpm/V  |  RW   |   —   |
| Torque Constant A           | 0x2006:14 | REAL32             |    32    |      0       |    —     |    —     |  Nm/A  |  RW   |   —   |
| Torque Constant B           | 0x2006:15 | REAL32             |    32    |      0       |    —     |    —     |  Nm/A  |  RW   |   —   |
| Torque Constant C           | 0x2006:16 | REAL32             |    32    |      0       |    —     |    —     |  Nm/A  |  RW   |   —   |
| Friction Dynamic            | 0x2006:17 | REAL32             |    32    |      0       |    —     |    —     |   Nm   |  RW   |   —   |
| Friction Static             | 0x2006:18 | REAL32             |    32    |      0       |    —     |    —     |   Nm   |  RW   |   —   |
| Shunt Resistance            | 0x2006:19 | REAL32             |    32    |      0       |    —     |    —     |  Ohm   |  RW   |   —   |
| Thermistor Type             | 0x2006:20 | UNSIGNED8          |    8     |      0       |    —     |    —     |   —    |  RW   |   —   |

### 0x2008 – Main Encoder
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2008:0  | UNSIGNED8 |    8     |     0x0A     |   —   |   —   |   —   |  RO   |   —   |
| Type                        | 0x2008:1  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Calibration Mode            | 0x2008:2  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Mode                        | 0x2008:3  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Direction                   | 0x2008:4  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Position                    | 0x2008:5  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RO   |  Tx   |
| Velocity                    | 0x2008:6  | REAL32    |    32    |      0       |   —   |   —   | rad/s |  RO   |  Tx   |
| Standard Deviation          | 0x2008:7  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Max Error                   | 0x2008:8  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Min Error                   | 0x2008:9  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Zero Offset                 | 0x2008:10 | INTEGER32 |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |

### 0x200A – Auxiliary Encoder
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x200A:0  | UNSIGNED8 |    8     |     0x0A     |   —   |   —   |   —   |  RO   |   —   |
| Type                        | 0x200A:1  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Calibration Mode            | 0x200A:2  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Mode                        | 0x200A:3  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Direction                   | 0x200A:4  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Position                    | 0x200A:5  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RO   |  Tx   |
| Velocity                    | 0x200A:6  | REAL32    |    32    |      0       |   —   |   —   | rad/s |  RO   |  Tx   |
| Standard Deviation          | 0x200A:7  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Max Error                   | 0x200A:8  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Min Error                   | 0x200A:9  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Zero Offset                 | 0x200A:10 | INTEGER32 |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |

### 0x200F – Velocity PID Controller
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x200F:0  | UNSIGNED8 |    8     |     0x05     |   —   |   —   |   —   |  RO   |   —   |
| Kp                          | 0x200F:1  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |  Rx   |
| Ki                          | 0x200F:2  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |  Rx   |
| Kd                          | 0x200F:3  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |  Rx   |
| Integral Limit              | 0x200F:4  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Output Max                  | 0x200F:5  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |

### 0x2010 – Position PID Controller
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2010:0  | UNSIGNED8 |    8     |     0x05     |   —   |   —   |   —   |  RO   |   —   |
| Kp                          | 0x2010:1  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Ki                          | 0x2010:2  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Kd                          | 0x2010:3  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Integral Limit              | 0x2010:4  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Output Max                  | 0x2010:5  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |

### 0x2011 – Impedance PD Controller
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2011:0  | UNSIGNED8 |    8     |     0x03     |   —   |   —   |   —   |  RO   |   —   |
| Kp                          | 0x2011:1  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Kd                          | 0x2011:2  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Output Max                  | 0x2011:3  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |

### 0x2012 – Temperature
| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  |  Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :----: | :---: | :---: |
| Highest sub-index supported | 0x2012:0  | UNSIGNED8 |    8     |     0x02     |   —   |   —   |   —    |  RO   |   —   |
| Motor Temperature           | 0x2012:1  | REAL32    |    32    |      0       |   —   |   —   | &deg;C |  RO   |  Tx   |
| Driver Temperature          | 0x2012:2  | REAL32    |    32    |      0       |   —   |   —   | &deg;C |  RO   |  Tx   |

### 0x2013 – User GPIO
| Name                        | Index:Sub | Type       | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2013:0  | UNSIGNED8  |    8     |     0x02     |   —   |   —   |   —   |  RO   |   —   |
| GPIO Configuration          | 0x2013:1  | UNSIGNED8  |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| GPIO State                  | 0x2013:2  | UNSIGNED16 |    16    |      0       |   —   |   —   |   —   |  RO   |   —   |

## Profile Specific Area

### 0x603F – Error Code
| Name       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Error Code | 0x603F:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x6040 – Controlword
| Name        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Controlword | 0x6040:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6041 – Statusword
| Name       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Statusword | 0x6041:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x6060 – Modes Of Operation
| Name               | Index:Sub | Type     | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------ | --------- | -------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Modes Of Operation | 0x6060:0  | INTEGER8 |    8     |      0       |    —     |    —     |   —   |  RW   |  Rx   |

| Value |           Mode of Operation            |
| :---: | :------------------------------------: |
|  -3   |          Impedance Mode (IMP)          |
|  -2   |           Service Mode (SRV)           |
|   0   |                  Idle                  |
|   1   |      Profile Position Mode (PPM)       |
|   3   |      Profile Velocity Mode (PVM)       |
|   8   | Cyclic Synchronous Position Mode (CSP) |
|   9   |           Velocity Mode (VM)           |
|  10   |  Cyclic Synchronous Torque Mode (CST)  |

### 0x6061 – Modes Of Operation Display
| Name                       | Index:Sub | Type     | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------------- | --------- | -------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Modes Of Operation Display | 0x6061:0  | INTEGER8 |    8     |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x6062 – Position Demand Value
| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Position Demand Value | 0x6062:0  | INTEGER32 |    32    |      0       |    —     |    —     |  inc  |  RO   |  Tx   |

### 0x6064 – Position Actual Value
| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Position Actual Value | 0x6064:0  | INTEGER32 |    32    |      0       |    —     |    —     |  inc  |  RO   |  Tx   |

### 0x6067 – Position Window
| Name            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Position Window | 0x6067:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |  inc  |  RW   |  Rx   |

### 0x606B – Velocity Demand Value
| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data |   Unit   |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :------: | :---: | :---: |
| Velocity Demand Value | 0x606B:0  | INTEGER32 |    32    |      0       |    —     |    —     | mrev/min |  RO   |  Tx   |

### 0x606C – Velocity Actual Value
| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data |   Unit   |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :------: | :---: | :---: |
| Velocity Actual Value | 0x606C:0  | INTEGER32 |    32    |      0       |    —     |    —     | mrev/min |  RO   |  Tx   |

### 0x606D – Velocity Window
| Name            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data |   Unit   |  SDO  |  PDO  |
| --------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :------: | :---: | :---: |
| Velocity Window | 0x606D:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrev/min |  RW   |  Rx   |

### 0x6071 – Target Torque
| Name          | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Target Torque | 0x6071:0  | INTEGER16 |    16    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6072 – Max Torque
| Name       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Torque | 0x6072:0  | UNSIGNED16 |    16    |     1000     |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6073 – Max Current
| Name        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Current | 0x6073:0  | UNSIGNED16 |    16    |     1000     |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6074 – Torque Demand Value
| Name                | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Torque Demand Value | 0x6074:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x6075 – Motor Rated Current
| Name                | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Motor Rated Current | 0x6075:0  | UNSIGNED32 |    32    |      1       |    1     | 1000000  |  mA   |  RW   |   —   |

### 0x6076 – Motor Rated Torque
| Name               | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Motor Rated Torque | 0x6076:0  | UNSIGNED32 |    32    |      1       |    —     |    —     |  mNm  |  RW   |   —   |

### 0x6077 – Torque Actual Value
| Name                | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Torque Actual Value | 0x6077:0  | INTEGER16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x6079 – DC Link Circuit Voltage
| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| DC Link Circuit Voltage | 0x6079:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

### 0x607A – Target Position
| Name            | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Target Position | 0x607A:0  | INTEGER32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x607B – Position Range Limit
| Name                        | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x607B:0  | UNSIGNED8 |    8     |     0x02     |    —     |    —     |   —   |  RO   |   —   |
| Min Position Range Limit    | 0x607B:1  | INTEGER32 |    32    | -2147483648  |    —     |    —     |   —   |  RW   |  Rx   |
| Max Position Range Limit    | 0x607B:2  | INTEGER32 |    32    |  2147483647  |    —     |    —     |   —   |  RW   |  Rx   |

### 0x607D – Software Position Limit
| Name                        | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x607D:0  | UNSIGNED8 |    8     |     0x02     |    —     |    —     |   —   |  RO   |   —   |
| Min Position Limit          | 0x607D:1  | INTEGER32 |    32    | -2147483648  |    —     |    —     |   —   |  RW   |  Rx   |
| Max Position Limit          | 0x607D:2  | INTEGER32 |    32    |  2147483647  |    —     |    —     |   —   |  RW   |  Rx   |

### 0x607E – Polarity
| Name     | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Polarity | 0x607E:0  | UNSIGNED8 |    8     |     0x00     |    —     |    —     |   —   |  RW   |   —   |

### 0x6080 – Max Motor Speed
| Name            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Motor Speed | 0x6080:0  | UNSIGNED32 |    32    |     1000     |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6081 – Profile Velocity
| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Profile Velocity | 0x6081:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6083 – Profile Acceleration
| Name                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Profile Acceleration | 0x6083:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6084 – Profile Deceleration
| Name                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Profile Deceleration | 0x6084:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6085 – Quick Stop Deceleration
| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Quick Stop Deceleration | 0x6085:0  | UNSIGNED32 |    32    |    10000     |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6091 – Gear Ratio
| Name                        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x6091:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RO   |   —   |
| Motor Revolutions           | 0x6091:1  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |  Rx   |
| Shaft  Revolutions          | 0x6091:2  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x60A8 – SI Unit Position

Default position units are encoder increments.

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| SI Unit Position | 0x60A8:0  | UNSIGNED32 |    32    |  0x00B50000  |    —     |    —     |   —   |  RO   |   —   |

### 0x60A9 – SI Unit Velocity

Default velocity units are milli revolutions per minute.

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| SI Unit Velocity | 0x60A9:0  | UNSIGNED32 |    32    |  0xFDB44700  |    —     |    —     |   —   |  RO   |   —   |

### 0x60A9 – SI Unit Acceleration

Default acceleration units are milli revolutions per minute per second.

| Name                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| SI Unit Acceleration | 0x60A9:0  | UNSIGNED32 |    32    |  0xFDC00300  |    —     |    —     |   —   |  RO   |   —   |

### 0x60C5 – Max Acceleration
| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Acceleration | 0x60C5:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x60C6 – Max Deceleration
| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Deceleration | 0x60C6:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x60C6 – Target Velocity
| Name            | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Target Velocity | 0x60C6:0  | INTEGER32 |    32    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

### 0x6502 – Supported Drive Modes

MD controllers support following standard CiA 402 drive modes:

- Cyclic Synchronous Torque Mode (CST)
- Cyclic Synchronous Position Mode (CSP)
- Velocity Mode (VM)
- Profile Position Mode (PPM)
- Profile Velocity Mode (PVM)

And two manufacturer specific modes:

- Impedance Mode (IMP)
- Service Mode (SRV)

| Name                  | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Supported Drive Modes | 0x6502:0  | UNSIGNED32 |    32    |  0x00030287  |    —     |    —     |   —   |  RO   |   —   |

|         Bit 31...16         | Bit 15...10 |   Bit 9...0    |
| :-------------------------: | :---------: | :------------: |
| Manufacturer-specific Modes |  Reserved   | Standard Modes |

|   Bit   | Value |               Drive Mode                |
| :-----: | :---: | :-------------------------------------: |
| 31...18 |   0   |          Manufacturer-specific          |
|   17    |   1   | Impedance (IMP — Manufacturer-specific) |
|   16    |   1   |  Service (SRV — Manufacturer-specific)  |
| 15...10 |   0   |                Reserved                 |
|    9    |   1   |  Cyclic Synchronous Torque Mode (CST)   |
|    8    |   0   | Cyclic Synchronous Velocity Mode (CSV)  |
|    7    |   1   | Cyclic Synchronous Position Mode (CSP)  |
|    6    |   0   |     Interpolated Position Mode (IP)     |
|    5    |   0   |            Homing Mode (HM)             |
|    4    |   0   |                Reserved                 |
|    3    |   0   |            Torque Mode (TQ)             |
|    2    |   1   |       Profile Velocity Mode (PV)        |
|    1    |   1   |           Velocity Mode (VL)            |
|    0    |   1   |       Profile Position Mode (PP)        |