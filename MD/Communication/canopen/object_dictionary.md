(canopen_od)=
# Object Dictionary

Complete reference for object dictionary revision 1.2. The machine readable version is
`md_1.2.eds`, available from [Downloads](device_firmware).

The dictionary is split into three ranges:

- **0x1000 to 0x1FFF, communication area.** CiA 301 objects: identification, heartbeat, SYNC and PDO configuration.
- **0x2000 to 0x5FFF, manufacturer specific area.** MAB objects: motor parameters, encoders, controller gains, status and commands.
- **0x6000 to 0x9FFF, profile specific area.** CiA 402 objects: state machine, modes, setpoints and limits.

Access types are `ro` read only, `wo` write only, `rw` read and write over SDO, and `rww`
read and write over SDO or through a receive PDO. The PDO column says whether the entry can
be mapped into a PDO.

```{note}
Ranges in the notes column are the ones the **firmware** enforces. They are sometimes narrower
than the data type allows and, in a few places, narrower than the EDS declares. A value outside
the enforced range is rejected with SDO abort code 0x06090030.
```

(communication-area)=
## Communication Area

### 0x1000 Device Type

Identifies the device profile. Reads 0x00020192: profile 402 in the low word, servo drive in the high word.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Device Type | UINT32 | ro | 0x00020192 | no |  |

### 0x1001 Error Register

One byte summary of active faults. See [Diagnostics](canopen_diagnostics) for the bit meanings.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Error Register | UINT8 | ro | 0 | yes |  |

### 0x1005 COB-ID SYNC Message

Identifier the drive listens on for SYNC. Fixed at 0x80; the drive never produces SYNC itself.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | COB-ID SYNC Message | UINT32 | ro | 0x00000080 | no |  |

### 0x1008 Manufacturer Device Name

Device name string.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Manufacturer Device Name | STRING | ro | - | no |  |

### 0x1009 Manufacturer Hardware Version

Hardware version string.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Manufacturer Hardware Version | STRING | ro | - | no |  |

### 0x1010 Store Parameters

Saves the configuration to flash, the CiA 301 equivalent of Save Config 0x2023:1. Write-only: reading any sub-index other than 0 aborts with 0x05040001.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x04 | no | always reports 4, although only sub-index 1 is implemented |
| 1 | Save all Parameters | UINT32 | wo | 0x00000000 | no | write the signature 0x65766173, ASCII "save"; any other value aborts with 0x08000020 |

### 0x1011 Restore Default Parameters

Restores factory defaults and saves them, the CiA 301 equivalent of Revert Factory Settings 0x2023:7. Only sub-index 4 is implemented. Write-only: reading any sub-index other than 0 aborts with 0x05040001.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x04 | no | always reports 4, although only sub-index 4 is implemented |
| 4 | Restore manufacturer defined default Parameters | UINT32 | wo | 0x00000000 | no | write the signature 0x64616F6C, ASCII "load"; any other value aborts with 0x08000020 |

### 0x1014 COB-ID EMCY

Identifier the drive transmits emergency messages on.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | COB-ID EMCY | UINT32 | ro | $NODEID+0x80 | no |  |

### 0x1016 Consumer Heartbeat Time

Watchdog on another node. Bits 0-15 are the timeout in milliseconds, bits 16-23 the node ID to watch. A timeout raises a communication error and commands a quick stop. See [Network Management](canopen_nmt).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x01 | no |  |
| 1 | Consumer Heartbeat Time 1 | UINT32 | rw | 0x00000000 | no | ms in bits 0-15, node ID in bits 16-23 |

### 0x1017 Producer Heartbeat Time

Heartbeat period in milliseconds. 0 disables the heartbeat.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Producer Heartbeat Time | UINT16 | rw | 1000 | no | ms |

### 0x1018 Identity Object

Vendor, product, revision and serial identification. The vendor ID is 0 because MAB Robotics has no CiA-assigned vendor ID yet.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x04 | no |  |
| 1 | Vendor-ID | UINT32 | ro | 0x00000000 | no |  |
| 2 | Product Code | UINT32 | ro | 0x00000001 | no |  |
| 3 | Revision Number | UINT32 | ro | 0x00000000 | no |  |
| 4 | Serial Number | UINT32 | ro | 0x00000000 | no |  |

### 0x1400 RPDO communication parameter

Communication parameters for RPDO1. The COB-ID is stored and read back but is not used for filtering; RPDO1 is always received on 0x200 plus the node ID. See [PDO](canopen_pdo).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x05 | no | always reports 5 |
| 1 | COB-ID used by RPDO | UINT32 | rw | 0x200 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |

### 0x1401 RPDO communication parameter

Communication parameters for RPDO2, received on 0x300 plus the node ID.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x05 | no | always reports 5 |
| 1 | COB-ID used by RPDO | UINT32 | rw | 0x300 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |

### 0x1402 RPDO communication parameter

Communication parameters for RPDO3, received on 0x400 plus the node ID.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x05 | no | always reports 5 |
| 1 | COB-ID used by RPDO | UINT32 | rw | 0x400 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |

### 0x1403 RPDO communication parameter

Communication parameters for RPDO4, received on 0x500 plus the node ID.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x05 | no | always reports 5 |
| 1 | COB-ID used by RPDO | UINT32 | rw | 0x500 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |

### 0x1600 RPDO mapping parameter

Mapping for RPDO1. Default: Target Position and Target Torque.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 2 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x607A0020 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x60710010 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1601 RPDO mapping parameter

Mapping for RPDO2. Default: Target Velocity and Target Torque.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 2 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60FF0020 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x60710010 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1602 RPDO mapping parameter

Mapping for RPDO3. Default: Controlword, Target Position and Target Torque.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 3 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60400010 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x607A0020 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x60710010 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1603 RPDO mapping parameter

Mapping for RPDO4. Default: Controlword, Target Velocity and Target Torque.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 3 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60400010 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x60FF0020 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x60710010 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1800 TPDO communication parameter

Communication parameters for TPDO1. The COB-ID is used exactly as stored, with no node ID offset. See [PDO](canopen_pdo).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no | always reports 5 |
| 1 | COB-ID used by TPDO | UINT32 | rw | 0x180 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 3 | Inhibit time | UINT16 | rw | 0 | no | accepted but not enforced |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |
| 6 | SYNC start value | UINT8 | rw | 0 | no | declared in the EDS but not implemented |

### 0x1801 TPDO communication parameter

Communication parameters for TPDO2.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no | always reports 5 |
| 1 | COB-ID used by TPDO | UINT32 | rw | 0x280 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 3 | Inhibit time | UINT16 | rw | 0 | no | accepted but not enforced |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |
| 6 | SYNC start value | UINT8 | rw | 0 | no | declared in the EDS but not implemented |

### 0x1802 TPDO communication parameter

Communication parameters for TPDO3.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no | always reports 5 |
| 1 | COB-ID used by TPDO | UINT32 | rw | 0x380 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 3 | Inhibit time | UINT16 | rw | 0 | no | accepted but not enforced |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |
| 6 | SYNC start value | UINT8 | rw | 0 | no | declared in the EDS but not implemented |

### 0x1803 TPDO communication parameter

Communication parameters for TPDO4.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no | always reports 5 |
| 1 | COB-ID used by TPDO | UINT32 | rw | 0x480 | no | COB-ID |
| 2 | Transmission type | UINT8 | rw | 255 | no | 0 every SYNC, 1-240 every n-th SYNC, 254 and 255 event driven |
| 3 | Inhibit time | UINT16 | rw | 0 | no | accepted but not enforced |
| 5 | Event timer | UINT16 | rw | 0 | no | ms, transmit PDOs only |
| 6 | SYNC start value | UINT8 | rw | 0 | no | declared in the EDS but not implemented |

### 0x1A00 TPDO mapping parameter

Mapping for TPDO1. Default: Statusword and Quick Status.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 2 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60410010 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x20220110 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1A01 TPDO mapping parameter

Mapping for TPDO2. Default: Position Actual Value and Velocity Actual Value.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 2 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60640020 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x606C0020 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1A02 TPDO mapping parameter

Mapping for TPDO3. Default: Torque Actual Value, Power Stage Temperature and Motor Temperature.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 3 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60770010 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x20040108 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x20040208 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

### 0x1A03 TPDO mapping parameter

Mapping for TPDO4. Default: DC Link Circuit Voltage.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Number of mapped application objects in PDO | UINT8 | rw | 1 | no | number of mapped objects, 0 to 8, write 0 before changing entries |
| 1 | Application object 1 | UINT32 | rw | 0x60790020 | no | index, sub-index, length in bits |
| 2 | Application object 2 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 3 | Application object 3 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 4 | Application object 4 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 5 | Application object 5 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 6 | Application object 6 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 7 | Application object 7 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |
| 8 | Application object 8 | UINT32 | rw | 0x00000000 | no | index, sub-index, length in bits |

(manufacturer-specific-area)=
## Manufacturer Specific Area

### 0x2000 Actuator Config

Motor and actuator identity. These values describe the physical motor and are needed before calibration can run. Sub-index 0 reports 10.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x0A | no |  |
| 1 | CAN ID | UINT8 | rw | 100 | no | 10 to 127 |
| 2 | Pole Pairs | UINT8 | rw | 0 | no | 2 to 42 |
| 3 | Phase Inductance | REAL32 | rw | 0.0 | no | H, 5e-9 to 0.1 |
| 4 | Phase Resistance | REAL32 | rw | 0.0 | no | ohm, 0.005 to 20 |
| 5 | Torque Bandwidth | UINT16 | rw | 0 | no | Hz, 10 to 2500 |
| 6 | Motor Name | STRING | rw | MD | no | up to 24 characters, segmented transfer only |
| 7 | Motor Shutdown Temperature | UINT8 | rw | 80 | no | degrees C, 10 to 120 |
| 8 | Motor Calibration Mode | UINT8 | rw | 0 | no | stored, not currently acted on by the firmware |
| 9 | Motor Torque Constant | REAL32 | rw | 1.0 | no | Nm/A, must be greater than 0 |
| 10 | Motor KV Rating | REAL32 | rw | 0.0 | no | RPM/V, must be greater than 0; writing it recomputes 0x2000:9 and is stored as a whole number |

### 0x2001 Main Encoder

Onboard commutation encoder.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Type | UINT8 | rw | 0 | no | encoder type identifier, see [Setting Up a New Motor](canopen_setup) |
| 2 | Direction | REAL32 | rw | -1.0 | no | -1.0 or 1.0 only |

### 0x2002 Auxiliary Encoder

Optional encoder on the output shaft. See [Encoders](aux_encoders).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no |  |
| 1 | Type | UINT8 | rw | 0 | no | encoder type identifier, see [Setting Up a New Motor](canopen_setup) |
| 2 | Direction | REAL32 | rw | 1.0 | no | -1.0 or 1.0 only |
| 3 | Mode | UINT8 | rw | 0 | no | 0 none, 1 startup, 2 motion, 3 report; takes effect after reboot |
| 4 | Calibration Mode | UINT8 | rw | 0 | no | 0 full, 1 direction only |
| 5 | Position | INT32 | ro | 0 | yes | micro-revolutions |
| 6 | Velocity | INT32 | ro | 0 | yes | micro-revolutions per second |

### 0x2003 Torque Sensor

Optional external torque sensor. See [External Torque Sensor](md_torque_sensor).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Type | UINT8 | rw | 0 | no | 0 none, 1 XJC sensor |
| 2 | Value | REAL32 | ro | 0.0 | yes | Nm |

### 0x2004 Temperature

Measured temperatures.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Power Stage Temperature | UINT8 | ro | 0 | yes | degrees C |
| 2 | Motor Temperature | UINT8 | ro | 0 | yes | degrees C |

### 0x2010 Position PID Controller

Position loop gains, used in Cyclic Synchronous Position. See [Position PID](position-pid).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x04 | no |  |
| 1 | Kp | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 2 | Ki | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 3 | Kd | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 4 | Integral Limit | REAL32 | rw | 0.0 | no | must be 0 or positive |

### 0x2011 Velocity PID Controller

Velocity loop gains, used in Cyclic Synchronous Velocity and by both profile modes. See [Velocity PID](velocity-pid).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x04 | no |  |
| 1 | Kp | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 2 | Ki | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 3 | Kd | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 4 | Integral Limit | REAL32 | rw | 0.0 | no | must be 0 or positive |

### 0x2012 Impedance PD Controller

Impedance mode stiffness and damping. See [Impedance PD](impedance-pd).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Kp | REAL32 | rw | 0.0 | no | must be 0 or positive |
| 2 | Kd | REAL32 | rw | 0.0 | no | must be 0 or positive |

### 0x2020 Hardware Info

Read-only board identification, programmed during production.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no |  |
| 1 | Device Type | UINT8 | ro | 0 | no |  |
| 2 | Device Revision | UINT8 | ro | 0 | no |  |
| 3 | Legacy Version | UINT8 | ro | 0 | no |  |
| 4 | Core ID | OCTET_STRING | ro | - | no |  |
| 5 | Batch Code | OCTET_STRING | ro | - | no |  |
| 6 | Production Date | STRING | ro | - | no |  |

### 0x2021 Firmware Info

Read-only firmware and bootloader identification.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x06 | no |  |
| 1 | Firmware Build Date | UINT32 | ro | 0 | no |  |
| 2 | Firmware Version | UINT32 | ro | 0 | no |  |
| 3 | Firmware Commit Hash | STRING | ro | - | no |  |
| 4 | Bootloader Build Date | UINT32 | ro | 0 | no |  |
| 5 | Bootloader Version | UINT32 | ro | 0 | no |  |
| 6 | Bootloader Commit Hash | STRING | ro | - | no |  |

### 0x2022 Status

Manufacturer status registers. Bit meanings are documented in [Status](status) and summarised in [Diagnostics](canopen_diagnostics).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x0A | no |  |
| 1 | Quick Status | UINT16 | ro | 0 | yes |  |
| 2 | Main Encoder Status | UINT32 | ro | 0 | yes |  |
| 3 | Auxiliary Encoder Status | UINT32 | ro | 0 | yes |  |
| 4 | Calibration Status | UINT32 | ro | 0 | yes |  |
| 5 | Bridge Status | UINT32 | ro | 0 | yes |  |
| 6 | Hardware Status | UINT32 | ro | 0 | yes |  |
| 7 | Communication Status | UINT32 | ro | 0 | yes |  |
| 8 | Motion Status | UINT32 | ro | 0 | yes |  |
| 9 | Misc Status | UINT32 | ro | 0 | yes |  |
| 10 | Config Status | UINT32 | ro | 0 | yes |  |

### 0x2023 Commands

Manufacturer commands. Trigger one by writing 1; any other value aborts with 0x06090030. Several of these reboot the drive.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x0E | no |  |
| 1 | Save Config | UINT8 | rw | 0 | no |  |
| 2 | Test Main Encoder | UINT8 | rw | 0 | no |  |
| 3 | Test Auxiliary Encoder | UINT8 | rw | 0 | no |  |
| 4 | Run Calibration | UINT8 | rw | 0 | no |  |
| 5 | Run Auxiliary Encoder Calibration | UINT8 | rw | 0 | no |  |
| 6 | Calibrate Current PI Gains | UINT8 | rw | 0 | no |  |
| 7 | Revert Factory Settings | UINT8 | rw | 0 | no |  |
| 8 | Reset Controller | UINT8 | rw | 0 | no |  |
| 9 | Clear Warnings | UINT8 | rw | 0 | no |  |
| 10 | Clear Errors | UINT8 | rw | 0 | no |  |
| 11 | Blink LEDs | UINT8 | rw | 0 | no |  |
| 12 | Set Zero | UINT8 | rw | 0 | no |  |
| 13 | Reinitialise CAN | UINT8 | rw | 0 | no |  |
| 14 | Zero Torque Sensor | UINT8 | rw | 0 | no |  |

### 0x2024 User GPIO

The two user GPIO pins. See [GPIO](GPIO) for the electrical limits.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | GPIO Mode | UINT8 | rw | 0 | no | 0 input, 1 brake |
| 2 | GPIO State | UINT8 | ro | 0 | yes |  |

(profile-specific-area)=
## Profile Specific Area

### 0x603F Error Code

CiA 402 code for the most recent fault. Latches until the drive is reset.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Error Code | UINT16 | ro | 0 | yes |  |

### 0x6040 Controlword

Commands the CiA 402 state machine. See [State Machine](canopen_state_machine).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Controlword | UINT16 | rww | 0 | yes |  |

### 0x6041 Statusword

Reports the CiA 402 state. Carries the state bits only.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Statusword | UINT16 | ro | 0 | yes |  |

### 0x6060 Modes of Operation

Selects the active controller. See [Modes of Operation](canopen_modes).

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Modes of Operation | INT8 | rww | 0 | yes |  |

### 0x6061 Modes of Operation Display

Reports the active mode. Gives the same answer as reading 0x6060.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Modes of Operation Display | INT8 | ro | 0 | yes |  |

### 0x6064 Position Actual Value

Measured output shaft position.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Position Actual Value | INT32 | ro | 0 | yes | micro-revolutions |

### 0x6067 Position Window

Tolerance used to decide that a position move has arrived. Reported through bit 15 of Quick Status.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Position Window | UINT32 | rw | 15915 | no | micro-revolutions |

### 0x606C Velocity Actual Value

Measured output shaft velocity.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Velocity Actual Value | INT32 | ro | 0 | yes | micro-revolutions per second |

### 0x606D Velocity Window

Tolerance used to decide that a velocity command has been reached.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Velocity Window | UINT16 | rw | 14041 | no | micro-revolutions per second |

### 0x6071 Target Torque

Torque setpoint, and the feed-forward torque in Impedance mode.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Target Torque | INT16 | rww | 0 | yes | 1/1000 of 0x6076 |

### 0x6072 Max Torque

Torque limit applied to every mode.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Max Torque | UINT16 | rw | 0 | no | 1/1000 of 0x6076 |

### 0x6073 Max Current

Phase current limit.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Max Current | UINT16 | rw | 0 | no | 1/1000 of 0x6075 |

### 0x6075 Motor Rated Current

Nameplate current of the motor. Must be non-zero before 0x6073 can be used.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Motor Rated Current | UINT32 | rw | 0 | no | mA |

### 0x6076 Motor Rated Torque

Nameplate torque of the motor. Must be non-zero before 0x6071, 0x6072 or 0x6077 can be used.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Motor Rated Torque | UINT32 | rw | 0 | no | mNm |

### 0x6077 Torque Actual Value

Measured torque at the output shaft.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Torque Actual Value | INT16 | ro | 0 | yes | 1/1000 of 0x6076 |

### 0x6079 DC Link Circuit Voltage

Measured DC link voltage.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | DC Link Circuit Voltage | UINT32 | ro | 0 | yes | mV |

### 0x607A Target Position

Position setpoint. In Profile Position it is the destination; in Cyclic Synchronous Position it is applied directly; in Impedance it is the equilibrium point.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Target Position | INT32 | rww | 0 | yes | micro-revolutions |

### 0x607B Position Range Limit

Hard bounds of the position representation. Read only, and fixed to the full INT32 range.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Min Position Range Limit | INT32 | ro | -2147483648 | no | micro-revolutions |
| 2 | Max Position Range Limit | INT32 | ro | 2147483647 | no | micro-revolutions |

### 0x607D Software Position Limit

Software position limits. Setting both sub-indices to the same value disables limiting.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Min Position Limit | INT32 | rw | 0 | no | micro-revolutions |
| 2 | Max Position Limit | INT32 | rw | 0 | no | micro-revolutions |

### 0x6080 Max Motor Speed

Speed limit applied to every mode, and the clamp on the position loop output.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Max Motor Speed | UINT32 | rw | 0 | no | micro-revolutions per second |

### 0x6083 Profile Acceleration

Acceleration used by the trajectory generator in both profile modes.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Profile Acceleration | UINT32 | rw | 0 | no | micro-revolutions per second squared |

### 0x6084 Profile Deceleration

Deceleration used by the trajectory generator in both profile modes.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Profile Deceleration | UINT32 | rw | 15915494 | no | micro-revolutions per second squared |

### 0x6085 Quick Stop Deceleration

Deceleration used for quick stop, including the automatic quick stop on a heartbeat timeout.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Quick Stop Deceleration | UINT32 | rw | 15915494 | no | micro-revolutions per second squared |

### 0x6091 Gear Ratio

Gearbox ratio. All shaft quantities are computed with it applied.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| 0 | Highest sub-index supported | UINT8 | ro | 0x02 | no |  |
| 1 | Motor Revolutions | UINT32 | rw | 1 | no |  |
| 2 | Shaft Revolutions | UINT32 | rw | 1 | no |  |

### 0x60A8 SI Unit Position

Declares the position unit, micro-revolutions. Read only.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | SI Unit Position | UINT32 | ro | 0xFAB40000 | no |  |

### 0x60A9 SI Unit Velocity

Declares the velocity unit, micro-revolutions per second. Read only.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | SI Unit Velocity | UINT32 | ro | 0xFAB40300 | no |  |

### 0x60AA SI Unit Acceleration

Declares the acceleration unit, micro-revolutions per second squared. Read only.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | SI Unit Acceleration | UINT32 | ro | 0xFAB45700 | no |  |

### 0x60FF Target Velocity

Velocity setpoint. In Profile Velocity it is the target; in Profile Position it is the cruise velocity; in Cyclic Synchronous Velocity it is applied directly; in Impedance it is the equilibrium velocity.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Target Velocity | INT32 | rww | 0 | yes | micro-revolutions per second |

### 0x6502 Supported Drive Modes

Bit field of supported CiA 402 modes. Reads 0x00000185.

| Sub | Name | Type | Access | Default | PDO | Notes |
| --- | ---- | ---- | ------ | ------- | --- | ----- |
| - | Supported Drive Modes | UINT32 | ro | 0x00000185 | no |  |

