# PDO Overview

## 1. Introduction

**PDOs (Process Data Objects)** are CANopen messages used for **real-time data exchange** between
nodes. Unlike SDO (Service Data Objects), PDOs transmit data without a request/response mechanism.

______________________________________________________________________

## 2. Types of PDOs

CANopen defines four types of PDOs per node:

| **PDO Type** | **Direction** | **CAN-ID Range** | **Purpose**                                |
| ------------ | ------------- | ---------------- | ------------------------------------------ |
| TPDO1–4      | Transmit PDOs | 0x180–0x1FF      | Data sent by the node to the network       |
| RPDO1–4      | Receive PDOs  | 0x200–0x27F      | Data received by the node from the network |

______________________________________________________________________

## 3. PDO Message Structure

A PDO message can carry up to **8 data bytes**.\
Its CAN-ID and mapping are fully configurable via **communication** and **mapping** parameters.

| **Field**  | **Description**                                                     |
| ---------- | ------------------------------------------------------------------- |
| **CAN-ID** | Identifies which PDO it is (default values can be remapped)         |
| **DLC**    | Number of data bytes (0–8)                                          |
| **Data**   | Mapped application objects (e.g., sensor values, actuator commands) |

______________________________________________________________________

## 4. PDO Communication Parameters

Each PDO has a **Communication Parameter Record** (object 0x1400 for RPDO1, 0x1800 for TPDO1, etc.)
that defines how it is sent/received. cf: [Object Dictionary](receive_pdo1_mapping)

| **Parameter**     | **Description**                                                                    |
| ----------------- | ---------------------------------------------------------------------------------- |
| COB-ID            | The CAN-ID used for the PDO                                                        |
| Transmission Type | Defines how the PDO is triggered (synchronous, asynchronous, event-driven, cyclic) |
| Inhibit Time      | Minimum time between two PDO transmissions                                         |
| Event Timer       | Periodic transmission time (in ms)                                                 |

______________________________________________________________________

## 5. PDO Mapping Parameters

PDO mapping parameters (object 0x1600 for RPDO1, 0x1A00 for TPDO1, etc.) define **which application
objects** are packed into the PDO data bytes.

| **Entry**                | **Description**                                                   |
| ------------------------ | ----------------------------------------------------------------- |
| Number of Mapped Objects | Number of data objects included in this PDO                       |
| Mapped Object 1..n       | Each entry specifies the object index, subindex, and size in bits |

Example of a mapped TPDO1:

| **Byte Offset** | **Mapped Object**  | **Description**           |
| --------------- | ------------------ | ------------------------- |
| 0–1             | 0x6041:00 (16-bit) | Statusword                |
| 2               | 0x6061:00 (8-bit)  | Mode of Operation Display |

______________________________________________________________________

## 6. Conclusion

PDOs are the **fast data carriers** of CANopen.\
They allow efficient, low-overhead communication for process data, with flexible mapping and
triggering options.

✅ Use TPDOs to broadcast sensor data\
✅ Use RPDOs to control actuators\
✅ Configure transmission types carefully for deterministic real-time performance
