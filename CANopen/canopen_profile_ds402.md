
#  Object Dictionary

Object dictionary holds CAN objects that can be accessed using SDOs and in some cases by PDOs. There
are three main groups in which the address space is divided into:

1. [Communication Area](#communication-area)
2. [Manufacturer Specific Area](#manufacturer-specific-area)
3. [Profile Specific Area](#profile-specific-area)

## Communication Area

This section defines the Communication Area Object Dictionary entries for the device.

<details>

**<summary>Communication Area Object Dictionary entries</summary>**

### 0x1000 – Device Type

Describes the device type. The entry stands for the supported device profile number. The value
0x00000192 (decimal: 402) means that the device follows **CiA 402** — *Device Profile for Drives and Motion Control*.

<details>

**<summary>Entry table</summary>**

| Name        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Device Type | 0x1000:0  | UNSIGNED32 |    32    |  0x00000192  |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1001 – Error Register

Indicates whether an error has occurred. Currently, only the 0th bit is implemented, that indicates
a general error. For a more verbose error and warning status, please see **0x2003 — System Status**.

```{note}
This Entry works now similarly to the `0x603F` Error Code entry defined in the Profile Specific Area.
```

<details>

**<summary>Entry table</summary>**

| Name           | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Error Register | 0x1001:0  | UNSIGNED8 |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1005 – COB-ID SYNC Message

Defines the COB-ID of the synchronization object (SYNC).

<details>

**<summary>Entry table</summary>**

| Name                | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| COB-ID SYNC Message | 0x1005:0  | UNSIGNED32 |    32    |  0x00000080  |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1006 – Communication Cycle Period

Defines the communication cycle period (0 if not used).

<details>

**<summary>Entry table</summary>**

| Name                       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Communication Cycle Period | 0x1006:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |  µs   |  RW   |   —   |

</details>

### 0x1007 – Synchronous Window Length

Defines the length of the time window for synchronous messages (0 if not used).

<details>

**<summary>Entry table</summary>**

| Name                      | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Synchronous Window Length | 0x1007:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |  µs   |  RW   |   —   |

</details>

### 0x1008 – Manufacturer Device Name

Contains manufacturer's device name.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type              | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ----------------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Manufacturer Device Name | 0x1008:0  | VISIBLE_STRING(3) |    24    |      MD      |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1009 – Manufacturer Hardware Version

Contains manufacturer's hardware version code.

<details>

**<summary>Entry table</summary>**

| Name                          | Index:Sub | Type              | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------------- | --------- | ----------------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Manufacturer Hardware Version | 0x1009:0  | VISIBLE_STRING(1) |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1010 – Store Parameters

This entry saves parameters in non-volatile memory. Saving procedure is triggered by writing 0x65766173 (ASCII value of "save") to the *Save All Parameters* — `0x1010:1` sub-entry.

```{note}
For saving parameters to non-volatile memory you can also use the `0x2004` – *System Command* entry. Sub-index *Save* (`0x2004:9`) will have exact same effect as this entry.
```

<details>

**<summary>Entry table</summary>**

| Name                                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported          | 0x1010:0  | UNSIGNED8  |    8     |     0x04     |    —     |    —     |   —   |  RO   |   —   |
| Save All Parameters                  | 0x1010:1  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |
| Save Communication Parameters        | 0x1010:2  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |
| Save Application Parameters          | 0x1010:3  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |
| Save Manufacturer Defined Parameters | 0x1010:4  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1011 – Restore Default Parameters

This entry restore all parameters to the default states. Restoring procedure is triggered by writing 0x64616F6C (ASCII value of "load") to the *Restore All Default Parameters* — `0x1011:1` sub-entry.

```{note}
For restoring default parameters to non-volatile memory you can also use the `0x2004` – *System Command* entry. Sub-index *Revert Factory Settings* (`0x2004:10`) will have exact same effect as this entry.
```

<details>

**<summary>Entry table</summary>**

| Name                                            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported                     | 0x1011:0  | UNSIGNED8  |    8     |     0x04     |    —     |    —     |   —   |  RO   |   —   |
| Restore All Default Parameters                  | 0x1011:1  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |
| Restore Communication Default Parameters        | 0x1011:2  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |
| Restore Application Default Parameters          | 0x1011:3  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |
| Restore Manufacturer Defined Default Parameters | 0x1011:4  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1012 – COB-ID Time Stamp Object

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| COB-ID Time Stamp Object | 0x1012:0  | UNSIGNED32 |    32    |  0x00000100  |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1014 – COB-ID EMCY

<details>

**<summary>Entry table</summary>**

| Name        | Index:Sub | Type       | Bit Size |   Default Data   | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------- | --------- | ---------- | :------: | :--------------: | :------: | :------: | :---: | :---: | :---: |
| COB-ID EMCY | 0x1014:0  | UNSIGNED32 |    32    | 0x80 + `Node ID` |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1015 – Inhibit Time EMCY

<details>

**<summary>Entry table</summary>**

| Name              | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Inhibit Time EMCY | 0x1015:0  | UNSIGNED16 |    16    |      0       |    —     |    —     | 100ms |  RW   |   —   |

</details>

### 0x1016 – Consumer Heartbeat Time

The consumer heartbeat time specifies the expected interval between heartbeat messages and therefore must be set to a value greater than the producer heartbeat time configured on the device sending the heartbeat. Monitoring begins once the first heartbeat is received. If the consumer heartbeat time is set to 0, that entry is ignored.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x1016:0  | UNSIGNED8  |    8     |     0x08     |    —     |    —     |   —   |  RO   |   —   |
| Consumer Heartbeat Time     | 0x1016:1  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:2  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Consumer Heartbeat Time     | 0x1016:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1017 – Producer Heartbeat Time

Defines the period of heartbeat message sent by the device. It is 0 if not used.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Producer Heartbeat Time | 0x1017:0  | UNSIGNED16 |    16    |     1000     |    —     |    —     |  ms   |  RW   |   —   |

</details>

### 0x1018 – Identity Object

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x1018:0  | UNSIGNED8  |    8     |     0x04     |    —     |    —     |   —   |  RO   |   —   |
| Vendor ID                   | 0x1018:1  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Product Code                | 0x1018:2  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Revision Number             | 0x1018:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Serial Number               | 0x1018:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1019 – Synchronous Counter Overflow Value

<details>

**<summary>Entry table</summary>**

| Name                               | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Synchronous Counter Overflow Value | 0x1019:0  | UNSIGNED8 |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1200 – SDO Server Parameter

Holds the parameters for the SDOs in which the device acts as the server.

<details>

**<summary>Entry table</summary>**

| Name                         | Index:Sub | Type       | Bit Size |   Default Data    | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------------------- | --------- | ---------- | :------: | :---------------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported  | 0x1200:0  | UNSIGNED8  |    8     |       0x02        |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Client to Server (rx) | 0x1200:1  | UNSIGNED32 |    32    | 0x600 + `Node ID` |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Server to Client (tx) | 0x1200:2  | UNSIGNED32 |    32    | 0x580 + `Node ID` |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1201 – SDO Server Parameter

Holds the parameters for the SDOs in which the device acts as the server.

<details>

**<summary>Entry table</summary>**

| Name                         | Index:Sub | Type       | Bit Size |   Default Data    | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------------------- | --------- | ---------- | :------: | :---------------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported  | 0x1201:0  | UNSIGNED8  |    8     |       0x02        |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Client to Server (rx) | 0x1201:1  | UNSIGNED32 |    32    | 0x600 + `Node ID` |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Server to Client (tx) | 0x1201:2  | UNSIGNED32 |    32    | 0x580 + `Node ID` |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x1280 – SDO Client Parameter

<details>

**<summary>Entry table</summary>**

| Name                         | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported  | 0x1280:0  | UNSIGNED8  |    8     |     0x03     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Client to Server (tx) | 0x1280:1  | UNSIGNED32 |    32    |  0x80000000  |    —     |    —     |   —   |  RW   |   —   |
| COB-ID Server to Client (rx) | 0x1280:2  | UNSIGNED32 |    32    |  0x80000000  |    —     |    —     |   —   |  RW   |   —   |
| Node ID of the SDO Server    | 0x1280:3  | UNSIGNED8  |    8     |     0x01     |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1400 – RPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1400:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By RPDO     | 0x1400:1  | UNSIGNED32 |    32    |  0x00000200  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1400:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1401 – RPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1401:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By RPDO     | 0x1401:1  | UNSIGNED32 |    32    |  0x00000300  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1401:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1402 – RPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1402:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By RPDO     | 0x1402:1  | UNSIGNED32 |    32    |  0x00000400  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1402:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1403 – RPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1403:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By RPDO     | 0x1403:1  | UNSIGNED32 |    32    |  0x00000500  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1403:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1600 – RPDO Mapping Parameter

Provides the mapping for the PDOs that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1600:0  | UNSIGNED8  |    8     |     0x01     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1600:1  | UNSIGNED32 |    32    |  0x60FF0020  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1600:2  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 3          | 0x1600:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 4          | 0x1600:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 5          | 0x1600:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 6          | 0x1600:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 7          | 0x1600:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 8          | 0x1600:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1601 – RPDO Mapping Parameter

Provides the mapping for the PDOs that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1601:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1601:1  | UNSIGNED32 |    32    |  0x60400010  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1601:2  | UNSIGNED32 |    32    |  0x60600008  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 3          | 0x1601:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 4          | 0x1601:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 5          | 0x1601:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 6          | 0x1601:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 7          | 0x1601:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 8          | 0x1601:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1602 – RPDO Mapping Parameter

Provides the mapping for the PDOs that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1602:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1602:1  | UNSIGNED32 |    32    |  0x60400010  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1602:2  | UNSIGNED32 |    32    |  0x607A0020  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 3          | 0x1602:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 4          | 0x1602:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 5          | 0x1602:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 6          | 0x1602:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 7          | 0x1602:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 8          | 0x1602:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1603 – RPDO Mapping Parameter

Provides the mapping for the PDOs that the device can receive.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1603:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1603:1  | UNSIGNED32 |    32    |  0x60400010  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1603:2  | UNSIGNED32 |    32    |  0x60FF0020  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 3          | 0x1603:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 4          | 0x1603:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 5          | 0x1603:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 6          | 0x1603:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 7          | 0x1603:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 8          | 0x1603:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1800 – TPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1800:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By TPDO     | 0x1800:1  | UNSIGNED32 |    32    |  0x00000180  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1800:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |
| Inhibit Time            | 0x1800:3  | UNSIGNED16 |    16    |      0       |    —     |    —     | 100µs |  RW   |   —   |
| Compatibility Entry     | 0x1800:4  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |
| Event Timer             | 0x1800:5  | UNSIGNED16 |    16    |      0       |    —     |    —     |  ms   |  RW   |   —   |
| SYNC Start Value        | 0x1800:6  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1801 – TPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1801:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By TPDO     | 0x1801:1  | UNSIGNED32 |    32    |  0x00000280  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1801:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |
| Inhibit Time            | 0x1801:3  | UNSIGNED16 |    16    |      0       |    —     |    —     | 100µs |  RW   |   —   |
| Compatibility Entry     | 0x1801:4  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |
| Event Timer             | 0x1801:5  | UNSIGNED16 |    16    |      0       |    —     |    —     |  ms   |  RW   |   —   |
| SYNC Start Value        | 0x1801:6  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1802 – TPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1802:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By TPDO     | 0x1802:1  | UNSIGNED32 |    32    |  0x00000380  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1802:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |
| Inhibit Time            | 0x1802:3  | UNSIGNED16 |    16    |      0       |    —     |    —     | 100µs |  RW   |   —   |
| Compatibility Entry     | 0x1802:4  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |
| Event Timer             | 0x1802:5  | UNSIGNED16 |    16    |      0       |    —     |    —     |  ms   |  RW   |   —   |
| SYNC Start Value        | 0x1802:6  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1803 – TPDO Communication Parameter

Includes the communication parameters for the current PDO that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max sub-index supported | 0x1803:0  | UNSIGNED8  |    8     |     0x06     |    —     |    —     |   —   |  RO   |   —   |
| COB-ID Used By TPDO     | 0x1803:1  | UNSIGNED32 |    32    |  0x00000480  |    —     |    —     |   —   |  RW   |   —   |
| Transmission Type       | 0x1803:2  | UNSIGNED8  |    8     |     0xFE     |    —     |    —     |   —   |  RW   |   —   |
| Inhibit Time            | 0x1803:3  | UNSIGNED16 |    16    |      0       |    —     |    —     | 100µs |  RW   |   —   |
| Compatibility Entry     | 0x1803:4  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |
| Event Timer             | 0x1803:5  | UNSIGNED16 |    16    |      0       |    —     |    —     |  ms   |  RW   |   —   |
| SYNC Start Value        | 0x1803:6  | UNSIGNED8  |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1A00 – TPDO Mapping Parameter

Provides the mapping for the PDOs that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1A00:0  | UNSIGNED8  |    8     |     0x01     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1A00:1  | UNSIGNED32 |    32    |  0x6041001   |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1A00:2  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1A01 – TPDO Mapping Parameter

Provides the mapping for the PDOs that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1A01:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1A01:1  | UNSIGNED32 |    32    |  0x60410010  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1A01:2  | UNSIGNED32 |    32    |  0x60640020  |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1A02 – TPDO Mapping Parameter

Provides the mapping for the PDOs that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1A02:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1A02:1  | UNSIGNED32 |    32    |  0x60410010  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1A02:2  | UNSIGNED32 |    32    |  0x606C0020  |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x1A03 – TPDO Mapping Parameter

Provides the mapping for the PDOs that the device can transmit.

<details>

**<summary>Entry table</summary>**

| Name                     | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Number of Mapped Objects | 0x1A03:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 1          | 0x1A03:1  | UNSIGNED32 |    32    |  0x60410010  |    —     |    —     |   —   |  RW   |   —   |
| Mapped Object 2          | 0x1A03:2  | UNSIGNED32 |    32    |  0x60770010  |    —     |    —     |   —   |  RW   |   —   |

</details>

</details>

## Manufacturer Specific Area

This section defines the Manufacturer Specific Area Object Dictionary entries for the device.

<details>

**<summary>Manufacturer Specific Area Object Dictionary entries</summary>**

### 0x2000 – Firmware Info

Contains metadata describing the firmware running on the device, including version information, build date, and the commit hash used to generate the build.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type              | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ----------------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2000:0  | UNSIGNED8         |    8     |     0x03     |    —     |    —     |   —   |  RO   |   —   |
| Commit Hash                 | 0x2000:1  | VISIBLE_STRING(8) |    64    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Build Date                  | 0x2000:2  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Version                     | 0x2000:3  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x2001 – Bootloader Info

Provides information about the device’s bootloader, such as its version, build details, commit hash, and whether a fixed bootloader is present.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type              | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ----------------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2001:0  | UNSIGNED8         |    8     |     0x04     |    —     |    —     |   —   |  RO   |   —   |
| Bootloader Fixed            | 0x2001:1  | BOOLEAN           |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Commit Hash                 | 0x2001:2  | VISIBLE_STRING(8) |    64    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Build Date                  | 0x2001:3  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |
| Version                     | 0x2001:4  | UNSIGNED32        |    32    |      0       |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x2002 – Hardware Info

Includes hardware-related identifiers and configuration details for the device, such as bridge type, legacy revision data, device type, and core identification.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type               | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ------------------ | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2002:0  | UNSIGNED8          |    8     |     0x05     |    —     |    —     |   —   |  RO   |   —   |
| Bridge Type                 | 0x2002:1  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Legacy Version              | 0x2002:2  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Device Type                 | 0x2002:3  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Device Revision             | 0x2002:4  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RO   |   —   |
| Core ID                     | 0x2002:5  | VISIBLE_STRING(12) |    96    |      0       |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x2003 – System Status

Provides a set of real-time status indicators describing the current operating state of the device, as defined in the [status description](/MD/status_utility). All entries are read-only and can be transmitted via PDO for continuous monitoring.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2003:0  | UNSIGNED8  |    8     |     0x09     |    —     |    —     |   —   |  RO   |   —   |
| Main Encoder Status         | 0x2003:1  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Aux Encoder Status          | 0x2003:2  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Calibration Status          | 0x2003:3  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Bridge Status               | 0x2003:4  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Hardware Status             | 0x2003:5  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Homing Status               | 0x2003:6  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Motion Status               | 0x2003:7  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Communication Status        | 0x2003:8  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |
| Misc Status                 | 0x2003:9  | UNSIGNED32 |    32    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

</details>

### 0x2004 – System Command

Contains write-only command entries used to control system-level actions on the device.

<details>

**<summary>Entry table</summary>**

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

</details>

### 0x2005 – Motor Settings

Configures the most important motor settings. This object is especially useful when you want to
configure or reconfigure an MD series motor controller for a particular motor.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type               | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ------------------ | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2005:0  | UNSIGNED8          |    8     |     0x14     |    —     |    —     |   —   |  RO   |   —   |
| Pole Pairs                  | 0x2005:1  | UNSIGNED32         |    32    |      0       |    2     |   255    |   —   |  RW   |   —   |
| Torque Constant             | 0x2005:2  | REAL32             |    32    |      0       |    —     |    —     | Nm/A  |  RW   |   —   |
| Inductance                  | 0x2005:3  | REAL32             |    32    |      0       |    —     |    —     |   H   |  RO   |   —   |
| Resistance                  | 0x2005:4  | REAL32             |    32    |      0       |    —     |    —     |  Ohm  |  RO   |   —   |
| Torque Bandwidth            | 0x2005:5  | UNSIGNED16         |    16    |      0       |    50    |   2500   |  Hz   |  RW   |   —   |
| Name                        | 0x2005:6  | VISIBLE_STRING(24) |   192    |      MD      |    —     |    —     |   —   |  RW   |   —   |
| Motor Shutdown Temp         | 0x2005:7  | UNSIGNED8          |    8     |      80      |    —     |   140    |  °C   |  RW   |   —   |
| Calibration Mode            | 0x2005:8  | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |
| CAN ID                      | 0x2005:9  | UNSIGNED32         |    32    |      10      |    10    |    31    |   —   |  RW   |   —   |
| CAN Datarate                | 0x2005:10 | UNSIGNED32         |    32    |   1000000    |    —     |    —     |  Hz   |  RW   |   —   |
| CAN Timeout                 | 0x2005:11 | UNSIGNED16         |    16    |     200      |    —     |    —     |  ms   |  RW   |   —   |
| CAN Termination             | 0x2005:12 | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |
| KV                          | 0x2005:13 | UNSIGNED16         |    16    |      0       |    —     |    —     | rpm/V |  RW   |   —   |
| Torque Constant A           | 0x2005:14 | REAL32             |    32    |      0       |    —     |    —     | Nm/A  |  RW   |   —   |
| Torque Constant B           | 0x2005:15 | REAL32             |    32    |      0       |    —     |    —     | Nm/A  |  RW   |   —   |
| Torque Constant C           | 0x2005:16 | REAL32             |    32    |      0       |    —     |    —     | Nm/A  |  RW   |   —   |
| Friction Dynamic            | 0x2005:17 | REAL32             |    32    |      0       |    —     |    —     |  Nm   |  RW   |   —   |
| Friction Static             | 0x2005:18 | REAL32             |    32    |      0       |    —     |    —     |  Nm   |  RW   |   —   |
| Shunt Resistance            | 0x2005:19 | REAL32             |    32    |      0       |    —     |    —     |  Ohm  |  RW   |   —   |
| Thermistor Type             | 0x2005:20 | UNSIGNED8          |    8     |      0       |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x2006 – Velocity PID Controller

This entry configures the Velocity PID controller gains. 

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2006:0  | UNSIGNED8 |    8     |     0x05     |   —   |   —   |   —   |  RO   |   —   |
| Kp                          | 0x2006:1  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |  Rx   |
| Ki                          | 0x2006:2  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |  Rx   |
| Kd                          | 0x2006:3  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |  Rx   |
| Integral Limit              | 0x2006:4  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Output Max                  | 0x2006:5  | REAL32    |    32    |      0       |   —   |   —   | rad/s |  RW   |   —   |

</details>

Velocity PID Controller diagram:

```{figure} images/Velocity_PID_CANopen.png
:align: center
:width: 600px
:class: no-scaled-link
```


### 0x2007 – Position PID Controller

This entry configures the Position PID controller gains. 

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2007:0  | UNSIGNED8 |    8     |     0x05     |   —   |   —   |   —   |  RO   |   —   |
| Kp                          | 0x2007:1  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Ki                          | 0x2007:2  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Kd                          | 0x2007:3  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Integral Limit              | 0x2007:4  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Output Max                  | 0x2007:5  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |

</details>

Position PID Controller diagram:

```{figure} images/Position_PID_CANopen.png
:align: center
:width: 600px
:class: no-scaled-link
```

### 0x2008 – Impedance PD Controller

This entry configures the Impedance PD controller gains. 

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2008:0  | UNSIGNED8 |    8     |     0x03     |   —   |   —   |   —   |  RO   |   —   |
| Kp                          | 0x2008:1  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Kd                          | 0x2008:2  | REAL32    |    32    |      0       |   —   |   —   |   —   |  RW   |   —   |
| Output Max                  | 0x2008:3  | REAL32    |    32    |      0       |   —   |   —   |  Nm   |  RW   |   —   |

</details>

Impedance PD Controller diagram:

```{figure} images/Impedance_PD_CANopen.png
:align: center
:width: 600px
:class: no-scaled-link
```

### 0x2009 – Main Encoder

Main encoder related record.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x2009:0  | UNSIGNED8 |    8     |     0x0A     |   —   |   —   |   —   |  RO   |   —   |
| Type                        | 0x2009:1  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Calibration Mode            | 0x2009:2  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Mode                        | 0x2009:3  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Direction                   | 0x2009:4  | UNSIGNED8 |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| Position                    | 0x2009:5  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RO   |  Tx   |
| Velocity                    | 0x2009:6  | REAL32    |    32    |      0       |   —   |   —   | rad/s |  RO   |  Tx   |
| Standard Deviation          | 0x2009:7  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Max Error                   | 0x2009:8  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Min Error                   | 0x2009:9  | REAL32    |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |
| Zero Offset                 | 0x2009:10 | INTEGER32 |    32    |      0       |   —   |   —   |  rad  |  RW   |   —   |

</details>

### 0x200A – Auxiliary Encoder

Auxiliary encoder related record.

<details>

**<summary>Entry table</summary>**

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

</details>

### 0x200B – Temperature

Entry containing temperature readings from the device.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x200B:0  | UNSIGNED8 |    8     |     0x02     |   —   |   —   |   —   |  RO   |   —   |
| Motor Temperature           | 0x200B:1  | REAL32    |    32    |      0       |   —   |   —   |  °C   |  RO   |  Tx   |
| Driver Temperature          | 0x200B:2  | REAL32    |    32    |      0       |   —   |   —   |  °C   |  RO   |  Tx   |

</details>

### 0x200C – User GPIO

This entry provides access to user-configurable GPIO pins on the device and their states.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type       | Bit Size | Default Data |  Min  |  Max  | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :---: | :---: | :---: | :---: | :---: |
| Highest sub-index supported | 0x200C:0  | UNSIGNED8  |    8     |     0x02     |   —   |   —   |   —   |  RO   |   —   |
| GPIO Configuration          | 0x200C:1  | UNSIGNED8  |    8     |      0       |   —   |   —   |   —   |  RW   |   —   |
| GPIO State                  | 0x200C:2  | UNSIGNED16 |    16    |      0       |   —   |   —   |   —   |  RO   |   —   |

</details>

</details>

## Profile Specific Area

This section contains Object Dictionary entries that are specific to the CiA 402 profile for drives and motion control.

<details>

**<summary>Profile Specific Area Object Dictionary entries</summary>**

### 0x603F – Error Code

Indicates whether an error has occurred. Currently, only the 0th bit is implemented, that indicates
a general error. For a more verbose error and warning status, please see **0x2003 — System Status**.

<details>

**<summary>Entry table</summary>**

| Name       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Error Code | 0x603F:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

</details>

### 0x6040 – Controlword

Control word is used to change the state of the internal CiA402 state machine implemented on the drive.

<details>

**<summary>Entry table</summary>**

| Name        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Controlword | 0x6040:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

</details>

The state machine is defined as follows:

```{figure} images/CIA402_state_machine_docs.png
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

All the transitions are based on the control word. The current state can be read using the status
word (0x6041_legacy).

| Command                        | Reset Fault (bit 7) | Enable Operation (bit 3) | Quick Stop (bit 2) | Disable Voltage (bit 1) | Switch On (bit 0) | Decimal value |
| ------------------------------ | :-----------------: | :----------------------: | :----------------: | :---------------------: | :---------------: | :-----------: |
| Shutdown                       |          0          |            X             |         1          |            1            |         0         |       6       |
| Switch on                      |          0          |            0             |         1          |            1            |         1         |       7       |
| Switch on and Enable Operation |          0          |            1             |         1          |            1            |         1         |      15       |
| Disable Voltage                |          0          |            X             |         X          |            0            |         X         |       0       |
| Quick Stop                     |          0          |            X             |         0          |            1            |         X         |       2       |
| Disable operation              |          0          |            0             |         1          |            1            |         1         |       7       |
| Enable operation               |          0          |            1             |         1          |            1            |         1         |      15       |
| Fault reset                    |         0→1         |            X             |         X          |            X            |         X         |      128      |

X means "do not care"

#### Example:

To put the drive into operational mode set:

1. Control word = 6 (dec_legacy) (Shutdown cmd)
2. Control word = 15 (dec_legacy) (Switch on and Enable Operation cmds)

The events and respective transitions are gathered in the table below:

| Transition | Event                                                     | Internal action                                                                        |
| :--------: | --------------------------------------------------------- | -------------------------------------------------------------------------------------- |
|     0      | Automatic transition after power up                       | Drive internal initialization                                                          |
|     1      | Automatic transition after drives internal initialization | Object dictionary is initialized with NVM data                                         |
|     2      | Shutdown command received                                 | None                                                                                   |
|     3      | Switch on command received                                | None                                                                                   |
|     4      | Enable operation command received                         | Current controllers are on, power is applied to the motor                              |
|     5      | Disable operation command received                        | Current controllers are off, power is not applied to the motor                         |
|     6      | Shutdown command received                                 | Current controllers are turned off                                                     |
|     7      | Quick stop command received                               | Current controllers are turned off                                                     |
|     8      | Shutdown command received                                 | Current controllers are turned off                                                     |
|     9      | Disable voltage command received                          | Current controllers are turned off                                                     |
|     10     | Disable voltage / Quick stop command received             | Current controllers are turned off                                                     |
|     11     | Quick stop command received                               | Quick stop action is enabled. The drive decelerates and transits to SWITCH ON DISABLED |
|     12     | Automatic transition when quick stop is completed         | Current controllers are turned off                                                     |
|     13     | Fault occurred                                            | Current controllers are turned off                                                     |
|     14     | Automatic transition to fault state                       | None                                                                                   |
|     15     | Fault reset command received                              | Fault is cleared if not critical                                                       |


### 0x6041 – Statusword

Describes the current state of the internal CiA402 state machine implemented on the drive.

<details>

**<summary>Entry table</summary>**

| Name       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Statusword | 0x6041:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

</details>

|     Status Word     | State Machine State    |
| :-----------------: | ---------------------- |
| xxxx xxxx x0xx 0000 | Not ready to switch on |
| xxxx xxxx x1xx 0000 | Switch on disabled     |
| xxxx xxxx x01x 0001 | Ready to switch on     |
| xxxx xxxx x01x 0011 | Switched on            |
| xxxx xxxx x01x 0111 | Operation Enabled      |
| xxxx xxxx x00x 0111 | Quick stop active      |
| xxxx xxxx x0xx 1111 | Fault reaction active  |
| xxxx xxxx x0xx 1000 | Quick stop active      |

Bit 10 of the statusword indicates the current target has been reached (1) or not (0). This bit is motion mode - dependent, meaning for example in position mode it indicates the position has been reached (within a `0x6067` Position Window margin), and in velocity mode that a velocity target has been reached (within `0x606D` Velocity Window).

Bit 11 of the **Statusword** indicates whether any of the internal limits was active during current power up - for more information on which limit is active, check the `0x2003:7` Motion Status.


### 0x6060 – Modes Of Operation

Use this object to request a motion mode change. The actual mode is reflected in 0x6061 Modes Of
Operation Display.

<details>

**<summary>Entry table</summary>**

| Name               | Index:Sub | Type     | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------ | --------- | -------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Modes Of Operation | 0x6060:0  | INTEGER8 |    8     |      0       |    —     |    —     |   —   |  RW   |  Rx   |

</details>

The following mode values are valid:

| Value |           Mode of Operation            |
| :---: | :------------------------------------: |
|  -3   |          Impedance Mode (IMP)          |
|  -2   |           Service Mode (SRV)           |
|   0   |                  Idle                  |
|   1   |      Profile Position Mode (PPM)       |
|   3   |      Profile Velocity Mode (PVM)       |
|   8   | Cyclic Synchronous Position Mode (CSP) |
|   9   | Cyclic Synchronous Velocity Mode (CSV) |
|  10   |  Cyclic Synchronous Torque Mode (CST)  |

#### 1. Impedance Mode (IMP)

#### 2. Service Mode (SRV)

#### 3. Idle

#### 4. Profile Position Mode (PPM)

#### 5. Profile Velocity Mode (PVM)

#### 6. Cyclic Synchronous Position Mode (CSP)

Raw position PID controller. Target position is reached as fast as possible, respecting the position range limits, max velocity, and max torque limit. To achieve smooth trajectories new setpoints need to be sent with high frequency.

#### 7. Cyclic Synchronous Velocity Mode (CSV)

Raw velocity PID controller. Target velocity is reached as fast as possible, respecting the max velocity limit, and max torque limit. To achieve smooth acceleration new velocity setpoints need to be sent with high frequency.

#### 8. Cyclic Synchronous Torque Mode (CST)

### 0x6061 – Modes Of Operation Display

Indicates the actual operation mode.

<details>

**<summary>Entry table</summary>**

| Name                       | Index:Sub | Type     | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------------- | --------- | -------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Modes Of Operation Display | 0x6061:0  | INTEGER8 |    8     |      0       |    —     |    —     |   —   |  RO   |  Tx   |

</details>

### 0x6062 – Position Demand Value

Indicates the demanded position value.

<details>

**<summary>Entry table</summary>**

| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Position Demand Value | 0x6062:0  | INTEGER32 |    32    |      0       |    —     |    —     |  inc  |  RO   |  Tx   |

</details>

### 0x6064 – Position Actual Value

This entry represents the value of the position measurement device.

<details>

**<summary>Entry table</summary>**

| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Position Actual Value | 0x6064:0  | INTEGER32 |    32    |      0       |    —     |    —     |  inc  |  RO   |  Tx   |

</details>

### 0x6067 – Position Window

The *position window* defines a symmetrical range of accepted positions relative to the target position.

<details>

**<summary>Entry table</summary>**

| Name            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Position Window | 0x6067:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |  inc  |  RW   |  Rx   |

</details>

### 0x606B – Velocity Demand Value

Indicates the demanded velocity value.

<details>

**<summary>Entry table</summary>**

| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Velocity Demand Value | 0x606B:0  | INTEGER32 |    32    |      0       |    —     |    —     | mrpm  |  RO   |  Tx   |

</details>

### 0x606C – Velocity Actual Value

The actual velocity value derived either from the velocity sensor or the position sensor.

<details>

**<summary>Entry table</summary>**

| Name                  | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Velocity Actual Value | 0x606C:0  | INTEGER32 |    32    |      0       |    —     |    —     | mrpm  |  RO   |  Tx   |

</details>

### 0x606D – Velocity Window

The *velocity window* defines a symmetrical range of accepted velocities relative to the target velocity.

<details>

**<summary>Entry table</summary>**

| Name            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Velocity Window | 0x606D:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrpm  |  RW   |  Rx   |

</details>

### 0x6071 – Target Torque

Desired torque value to be applied by the motor.

<details>

**<summary>Entry table</summary>**

| Name          | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Target Torque | 0x6071:0  | INTEGER16 |    16    |      0       |    —     |    —     |   —   |  RW   |  Rx   |

</details>

### 0x6072 – Max Torque

Maximum allowable torque the drive can apply.

<details>

**<summary>Entry table</summary>**

| Name       | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Torque | 0x6072:0  | UNSIGNED16 |    16    |     1000     |    —     |    —     |   —   |  RW   |  Rx   |

</details>

### 0x6073 – Max Current

Maximum allowable current for the motor.

<details>

**<summary>Entry table</summary>**

| Name        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Current | 0x6073:0  | UNSIGNED16 |    16    |     1000     |    —     |    —     |   —   |  RW   |  Rx   |

</details>

### 0x6074 – Torque Demand Value

Current torque requested by the controller.

<details>

**<summary>Entry table</summary>**

| Name                | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Torque Demand Value | 0x6074:0  | UNSIGNED16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

</details>

### 0x6075 – Motor Rated Current

Nominal motor current rating in milliamperes.

<details>

**<summary>Entry table</summary>**

| Name                | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Motor Rated Current | 0x6075:0  | UNSIGNED32 |    32    |      1       |    1     | 1000000  |  mA   |  RW   |   —   |

</details>

### 0x6076 – Motor Rated Torque

Nominal motor torque rating in millinewton-meters.

<details>

**<summary>Entry table</summary>**

| Name               | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------ | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Motor Rated Torque | 0x6076:0  | UNSIGNED32 |    32    |      1       |    —     |    —     |  mNm  |  RW   |   —   |

</details>

### 0x6077 – Torque Actual Value

Measured motor torque.

<details>

**<summary>Entry table</summary>**

| Name                | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Torque Actual Value | 0x6077:0  | INTEGER16 |    16    |      0       |    —     |    —     |   —   |  RO   |  Tx   |

</details>

### 0x6079 – DC Link Circuit Voltage

Measured DC link voltage of the drive.

<details>

**<summary>Entry table</summary>** 

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| DC Link Circuit Voltage | 0x6079:0  | UNSIGNED32 |    32    |      0       |    —     |    —     |  mV   |  RO   |  Tx   |

</details>

### 0x607A – Target Position

Desired motor position in increments.

<details>

**<summary>Entry table</summary>**

| Name            | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Target Position | 0x607A:0  | INTEGER32 |    32    |      0       |    —     |    —     |  inc  |  RW   |  Rx   |

</details>

### 0x607B – Position Range Limit

Minimum and maximum allowed motor positions.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x607B:0  | UNSIGNED8 |    8     |     0x02     |    —     |    —     |   —   |  RO   |   —   |
| Min Position Range Limit    | 0x607B:1  | INTEGER32 |    32    | -2147483648  |    —     |    —     |  inc  |  RW   |  Rx   |
| Max Position Range Limit    | 0x607B:2  | INTEGER32 |    32    |  2147483647  |    —     |    —     |  inc  |  RW   |  Rx   |

</details>

### 0x607D – Software Position Limit

Software-configurable minimum and maximum position limits.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x607D:0  | UNSIGNED8 |    8     |     0x02     |    —     |    —     |   —   |  RO   |   —   |
| Min Position Limit          | 0x607D:1  | INTEGER32 |    32    | -2147483648  |    —     |    —     |  inc  |  RW   |  Rx   |
| Max Position Limit          | 0x607D:2  | INTEGER32 |    32    |  2147483647  |    —     |    —     |  inc  |  RW   |  Rx   |

</details>

### 0x607E – Polarity

Motor rotation direction setting.

<details>

**<summary>Entry table</summary>**

| Name     | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Polarity | 0x607E:0  | UNSIGNED8 |    8     |     0x00     |    —     |    —     |   —   |  RW   |   —   |

</details>

### 0x6080 – Max Motor Speed

Maximum allowed motor speed in millirevolutions per minute.

<details>

**<summary>Entry table</summary>**

| Name            | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Max Motor Speed | 0x6080:0  | UNSIGNED32 |    32    |     1000     |    —     |    —     | mrpm  |  RW   |  Rx   |

</details>

### 0x6081 – Profile Velocity

Velocity used in position profiles in millirevolutions per minute.

<details>

**<summary>Entry table</summary>**

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Profile Velocity | 0x6081:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrpm  |  RW   |  Rx   |

</details>

### 0x6083 – Profile Acceleration

Acceleration used in motion profiles in millirevolutions per minute per second.

<details>

**<summary>Entry table</summary>**

| Name                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data |  Unit  |  SDO  |  PDO  |
| -------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :----: | :---: | :---: |
| Profile Acceleration | 0x6083:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrpm/s |  RW   |  Rx   |

</details>

### 0x6084 – Profile Deceleration

Deceleration used in motion profiles in millirevolutions per minute per second.

<details>

**<summary>Entry table</summary>**

| Name                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data |  Unit  |  SDO  |  PDO  |
| -------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :----: | :---: | :---: |
| Profile Deceleration | 0x6084:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrpm/s |  RW   |  Rx   |

</details>

### 0x6085 – Quick Stop Deceleration

Deceleration applied during a quick stop in millirevolutions per minute per second.

<details>

**<summary>Entry table</summary>**

| Name                    | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data |  Unit  |  SDO  |  PDO  |
| ----------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :----: | :---: | :---: |
| Quick Stop Deceleration | 0x6085:0  | UNSIGNED32 |    32    |    10000     |    —     |    —     | mrpm/s |  RW   |  Rx   |

</details>

### 0x6091 – Gear Ratio

Motor-to-shaft gear ratio configuration.

<details>

**<summary>Entry table</summary>**

| Name                        | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Highest sub-index supported | 0x6091:0  | UNSIGNED8  |    8     |     0x02     |    —     |    —     |   —   |  RO   |   —   |
| Motor Revolutions           | 0x6091:1  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |  Rx   |
| Shaft  Revolutions          | 0x6091:2  | UNSIGNED32 |    32    |      1       |    —     |    —     |   —   |  RW   |  Rx   |

</details>

### 0x60A8 – SI Unit Position

Default position units are encoder increments.

<details>

**<summary>Entry table</summary>**

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| SI Unit Position | 0x60A8:0  | UNSIGNED32 |    32    |  0x00B50000  |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x60A9 – SI Unit Velocity

Default velocity units are millirevolutions per minute.

<details>

**<summary>Entry table</summary>**

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| SI Unit Velocity | 0x60A9:0  | UNSIGNED32 |    32    |  0xFDB44700  |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x60A9 – SI Unit Acceleration

Default acceleration units are millirevolutions per minute per second.

<details>

**<summary>Entry table</summary>**

| Name                 | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| -------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| SI Unit Acceleration | 0x60A9:0  | UNSIGNED32 |    32    |  0xFDC00300  |    —     |    —     |   —   |  RO   |   —   |

</details>

### 0x60C5 – Max Acceleration

Maximum allowed motor acceleration in millirevolutions per minute per second.

<details>

**<summary>Entry table</summary>**

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data |  Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :----: | :---: | :---: |
| Max Acceleration | 0x60C5:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrpm/s |  RW   |  Rx   |

</details>

### 0x60C6 – Max Deceleration

Maximum allowed motor deceleration in millirevolutions per minute per second.

<details>

**<summary>Entry table</summary>**

| Name             | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data |  Unit  |  SDO  |  PDO  |
| ---------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :----: | :---: | :---: |
| Max Deceleration | 0x60C6:0  | UNSIGNED32 |    32    |      0       |    —     |    —     | mrpm/s |  RW   |  Rx   |

</details>

### 0x60C6 – Target Velocity

Desired motor velocity in millirevolutions per minute.

<details>

**<summary>Entry table</summary>**

| Name            | Index:Sub | Type      | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------- | --------- | --------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Target Velocity | 0x60C6:0  | INTEGER32 |    32    |      0       |    —     |    —     | mrpm  |  RW   |  Rx   |

</details>

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

<details>

**<summary>Entry table</summary>**

| Name                  | Index:Sub | Type       | Bit Size | Default Data | Min Data | Max Data | Unit  |  SDO  |  PDO  |
| --------------------- | --------- | ---------- | :------: | :----------: | :------: | :------: | :---: | :---: | :---: |
| Supported Drive Modes | 0x6502:0  | UNSIGNED32 |    32    |  0x00030385  |    —     |    —     |   —   |  RO   |   —   |

</details>

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
|    8    |   1   | Cyclic Synchronous Velocity Mode (CSV)  |
|    7    |   1   | Cyclic Synchronous Position Mode (CSP)  |
|    6    |   0   |     Interpolated Position Mode (IP)     |
|    5    |   0   |            Homing Mode (HM)             |
|    4    |   0   |                Reserved                 |
|    3    |   0   |            Torque Mode (TQ)             |
|    2    |   1   |       Profile Velocity Mode (PV)        |
|    1    |   0   |           Velocity Mode (VL)            |
|    0    |   1   |       Profile Position Mode (PP)        |

</details>