# Setting Up a New Motor

This section outlines the recommended procedure for configuring a new motor on MD controllers compliant with the CiA 402 device profile. All configuration steps should be performed while the drive is in the **“Switch On Disabled”** state to ensure safe and consistent initialization.

## Fundamental Motor Parameters Setup

The first stage of motor commissioning involves defining the essential motor characteristics and control parameters. Configure the following registers according to the motor’s specifications and the requirements of your application.

### 1. Motor Parameter Configuration

These registers describe the motor’s electrical and mechanical properties and must be set prior to enabling any control loops:

- **0x6075:0 — Rated Current**
- **0x6076:0 — Rated Torque**
- **0x6072:0 — Maximum Torque**
- **0x6073:0 — Maximum Current**
- **0x6080:0 — Maximum Speed**
- **0x2000:1 — Pole Pairs**
- **0x2000:2 — Torque Constant**
- **0x2000:5 — Torque Bandwidth**
- **0x2000:7 — Motor Shutdown Temperature**
- **0x2000:8 — Gear Ratio**

### 2. Velocity PID Gains

Configure the velocity control loop using:

- **0x2001:1 — Kp**
- **0x2001:2 — Ki**
- **0x2001:3 — Kd**
- **0x2001:4 — Integral Limit**

### 3. Position PID Gains

Set the position control loop parameters:

- **0x2002:1 — Kp**
- **0x2002:2 — Ki**
- **0x2002:3 — Kd**
- **0x2002:4 — Integral Limit**

### 4. Profile Velocity and Position Settings

These registers determine the default motion profiles for velocity and position modes:

- **0x6081 — Profile Velocity**
- **0x6083 — Profile Acceleration**
- **0x6084 — Profile Deceleration**
- **0x6085 — Quick Stop Deceleration**

```{note}
Remember to save all modified parameters. See the **Saving and Calibrating** section for details.
```

## Setting Up an External Encoder

The configuration of an external (output) encoder must be performed **after** all motor parameters have been set and verified. The following registers define the encoder type, calibration behavior, and operational mode:

- **0x2005:1 — Output Encoder Type**  
  Refer to the *Output Encoder* section for supported encoder types and detailed descriptions.

- **0x2005:2 — Calibration Mode**  
  Refer to the *Output Encoder Calibration* section for available calibration procedures.

- **0x2005:3 — Mode**  
  Refer to the *Output Encoder* section for mode definitions and usage guidelines.

```{note}
Remember to save all modified parameters. See the **Saving and Calibrating** section for details.
```

## Saving and Calibrating

Once all motor and (optionally) external encoder parameters have been configured, complete the setup procedure by saving the configuration and performing calibration. These final steps ensure consistent startup behavior and proper sensor alignment.

### 1. Saving Parameters to Non-Volatile Memory

Execute the **Store Parameters** procedure using register **0x1010:1**:

1. Ensure the controller is in the **“Switch On Disabled”** state  
   (write `0x8` to the Controlword **0x6040**).

2. Write the save command value `0x65766173` to **0x1010:1**.

3. Wait for the controller to reboot automatically.

### 2. Performing Calibration

After the parameters have been saved, run the system calibration routine via **0x2003:3**, and, if an external encoder is installed, the output encoder calibration via **0x2003:4**.

1. Ensure the controller is in the **“Operation Enabled”** state:
   - Write sequentially:  
     `0x8 → 0x6 → 0xF` to the Controlword **0x6040**
   - Verify that the Statusword **0x6041** equals `0x39`

2. Set the device to **Service Mode**:
   - Write `-2` to Modes of Operation **0x6060**

3. Start the calibration routine:
   - Write `1` to **0x2003:3**
   - If applicable, write `1` to **0x2003:4** to calibrate the external encoder

4. Wait for the controller to reboot.

---

This concludes the standard motor and encoder configuration process. Once completed, the device is ready for standard operation using the configured parameters.
