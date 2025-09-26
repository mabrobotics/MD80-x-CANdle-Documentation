# CANopen NMT Overview

## 1. Introduction

**Network Management (NMT)** in CANopen is a service that manages the
state of nodes (slaves) on the network and ensures smooth operation.
The NMT acts like a **conductor**, coordinating the transitions of nodes
between different operating states. During the boot-up, if the motor have correct parameter, the motor should enter automatically into the Operational mode.

------------------------------------------------------------------------

## 2. NMT States

A CANopen node can be in one of the following states:

-   **Initialization** -- The node starts up and initializes itself.
-   **Pre-Operational** -- The node can communicate via SDO and receive
    NMT commands, but PDOs are not active.
-   **Operational** -- Full communication is enabled (PDO, SDO, SYNC,
    etc.).
-   **Stopped** -- The node stops PDO/SDO communication but stays
    present on the network and can still receive NMT commands.

    ```{figure} images/NMT_state_machine.jpg
    :align: center
    :width: 1000px
    ```

### 2.1. Allowed Communication per State

| **State**         | **PDO Communication** | **SDO Communication** | **NMT Commands Accepted** |
|-------------------|---------------------|---------------------|--------------------------|
| Initialization    | ❌                 | ❌                 | None                    |
| Pre-Operational   | ❌                 | ✅                 | Start, Stop, Reset      |
| Operational       | ✅                 | ✅                 | Stop, Reset            |
| Stopped           | ❌                 | ❌                 | Start, Reset           |

---

## 3. NMT Message Structure

An NMT message always uses **CAN-ID 0x000** and has a fixed length of **2 bytes**:

| **Byte** | **Content** |
|---------|-------------|
| 0       | **NMT Command** (Start, Stop, Reset, etc.) |
| 1       | **Node-ID** (0x00 = broadcast to all nodes) |

### 3.1. NMT Commands

| **Command**              | **Hex Value** | **Effect** |
|-------------------------|--------------|-----------|
| Start Remote Node       | 0x01         | Switches node to **Operational** |
| Stop Remote Node        | 0x02         | Switches node to **Stopped** |
| Enter Pre-Operational   | 0x80         | Switches node to **Pre-Operational** |
| Reset Node              | 0x81         | Reboots the node and reinitializes application variables |
| Reset Communication     | 0x82         | Reboots only the communication stack |


## 4. Heartbeat

The **Heartbeat** is a monitoring mechanism that ensures nodes are alive
and functioning.\
Each node periodically sends a message containing its current NMT state.

### 4.1. Heartbeat Message Structure

  Field    Content
  -------- -----------------------------------------------
  CAN-ID   0x700 + Node-ID
  Data     1 byte representing the NMT state of the node

**Example:**\
If node **0x05** is in **Operational** state, it will send:\
**CAN-ID = 0x705, Data = 0x05**

### 4.2. Purpose of Heartbeat

-   Detect nodes that are offline or unresponsive
-   Allow the master to monitor network health
-   Trigger safety actions when communication is lost

------------------------------------------------------------------------

## 5. Conclusion

NMT services are crucial for:\
✅ Setting nodes to the desired state\
✅ Monitoring their presence with Heartbeat\
✅ Reacting quickly to network failures

Together, **NMT** and **Heartbeat** provide **reliability and safety**
in CANopen-based communication systems.
