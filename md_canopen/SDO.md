# CANopen SDO Overview

## 1. Introduction

**SDOs (Service Data Objects)** in CANopen provide a **request/response mechanism** to access and configure any object in the **Object Dictionary**.  
Unlike PDOs, SDOs are **slower** but allow reading/writing large or complex data structures.

---

## 2. SDO Communication Concept

- SDO communication is always between a **client** and a **server**.
- The **client** initiates the transfer (read or write), and the **server** responds.
- SDOs can transfer data **up to 4 GB** using segmented communication if needed.

---

## 3. SDO Message Structure

SDO messages are carried using **CAN-ID 0x600 + Node-ID** for **client → server**, and **0x580 + Node-ID** for **server → client**.

| **Field** | **Description** |
|-----------|----------------|
| CAN-ID    | 0x600 + Node-ID for requests, 0x580 + Node-ID for responses |
| Command Specifier (CS) | Defines the type of operation: upload, download, segment, abort |
| Index / Subindex | Identifies the object in the Object Dictionary |
| Data      | Up to 4 bytes (or segmented for longer data) |

---

## 4. SDO Commands (Command Specifiers)

| **Command** | **Hex Value** | **Description** |
|------------|---------------|----------------|
| Initiate Download (Expedited) | 0x2x | Write up to 4 bytes in one message|
| Initiate Upload (Expedited)   | 0x4x | Read up to 4 bytes in one message |
| Initiate Download (Segmented) | 0x2x | Start writing more than 4 bytes |
| Initiate Upload (Segmented)   | 0x60 | Start reading more than 4 bytes |
| Segment Download / Upload     | 0x00 / 0x01 | Transfer next 7 bytes segment |
| Abort Transfer                | 0x80 | Stop current transfer in case of error |

> Note: x => second bytes depend on the length of the data

> Note: Expedited SDO is used for **small data** (≤ 4 bytes), segmented SDO is used for **larger data** (> 4 bytes).

---

## 5. Example of SDO Transfer

**Write 16-bit value 0x1234 to object 0x6040:00 (Controlword) on node 0x05:**

| **CAN-ID** | **CS** | **Index** | **Subindex** | **Data** |
|------------|--------|-----------|--------------|----------|
| 0x605      | 0x23   | 0x6040    | 0x00         | 0x34 0x12 |

**Read the same object:**

| **CAN-ID** | **CS** | **Index** | **Subindex** | **Data** |
|------------|--------|-----------|--------------|----------|
| 0x605      | 0x40   | 0x40 0x60  | 0x00         | –        |
| 0x585      | 0x43   | 0x40 0x60   | 0x00         | 0x34 0x12 |

> Warning: The index and the data must be send in little-endian

---

## 6. Advantages of SDO

- Access **any object** in the Object Dictionary
- Supports **large data transfers** with segmentation
- Ensures **reliable request/response communication**
- Essential for **configuration, diagnostics, and parameterization**

---

## 7. Conclusion

SDOs complement PDOs in CANopen by allowing **flexible and reliable data access**, especially for configuration and larger or less time-critical data.  

✅ Use SDOs for reading/writing configuration parameters  
✅ Use PDOs for real-time process data  
✅ Combine both for a fully functional CANopen system
