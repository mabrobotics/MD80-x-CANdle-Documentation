
# CiA 402 Profile Specific Area

## 0x603F – Error Code
| Name       | Index:Sub | Type      | Bit Size | Min Data | Max Data | Default Data | Unit | Access | PDO Mapping |
| ---------- | --------- | --------- | -------- | -------- | -------- | ------------ | ---- | ------ | ----------- |
| Error Code | 0x603F:0  | INTEGER16 | 16       |          |          | 0            |      | ro     | Yes         |

## 0x6040 – Controlword
| Name        | Index:Sub | Type      | Bit Size | Min Data | Max Data | Default Data | Unit | Access | PDO Mapping |
| ----------- | --------- | --------- | -------- | -------- | -------- | ------------ | ---- | ------ | ----------- |
| Controlword | 0x6040:0  | INTEGER16 | 16       |          |          | 0            |      | rw     | Yes         |

## 0x6041 – Statusword
| Name       | Index:Sub | Type      | Bit Size | Min Data | Max Data | Default Data | Unit | Access | PDO Mapping |
| ---------- | --------- | --------- | -------- | -------- | -------- | ------------ | ---- | ------ | ----------- |
| Statusword | 0x6041:0  | INTEGER16 | 16       |          |          | 0            |      | ro     | Yes         |

## 0x6060 – Modes Of Operation
| Name               | Index:Sub | Type     | Bit Size | Min Data | Max Data | Default Data | Unit | Access | PDO Mapping |
| ------------------ | --------- | -------- | -------- | -------- | -------- | ------------ | ---- | ------ | ----------- |
| Modes Of Operation | 0x6060:0  | INTEGER8 | 8        |          |          | 0            |      | rw     | Yes         |

## 0x6061 – Modes Of Operation Display
| Name                       | Index:Sub | Type     | Bit Size | Min Data | Max Data | Default Data | Unit | Access | PDO Mapping |
| -------------------------- | --------- | -------- | -------- | -------- | -------- | ------------ | ---- | ------ | ----------- |
| Modes Of Operation Display | 0x6061:0  | INTEGER8 | 8        |          |          | 0            |      | ro     | Yes         |

## 0x6062 – Position Demand Value
| Name                  | Index:Sub | Type      | Bit Size | Min Data | Max Data | Default Data | Unit | Access | PDO Mapping |
| --------------------- | --------- | --------- | -------- | -------- | -------- | ------------ | ---- | ------ | ----------- |
| Position Demand Value | 0x6062:0  | INTEGER16 | 16       |          |          | 0            |      | ro     | Yes         |
