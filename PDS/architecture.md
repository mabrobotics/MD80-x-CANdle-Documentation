# FDCAN Architecture

In order to connect using recommended architecture please solder correct bridges underneath the Micro-Fit molex connector.
These bridges connect CAN-L and CAN-H to another CAN-L/H of neighbor connector so the connection is transmitted without any adapters.

```{figure} images/power_stage/pds_ps_bridges.jpg
:alt: pds_power_stage_bridges
:align: center

FDCAN bridge placement

```


Also control board has its own built-in CAN termination. 
If possible CAN termination should be placed on each ends of CAN circuit as shown below in recommended architecture examples.

## **Example 1**

In this example there are: CANdle, Control board, two Power Stage modules, six MD actuators (two per Micro-Fit molex connector) and CAN termination. In this example, termination on the CANdle is disabled.

```{figure} images/control_board/PDS_CAN.png
:alt: PDS_CAN_architecture_example_1
:align: center

FDCAN architecture with 2 Power Stage modules

```

## **Example 2**

In this example there are: CANdle, Control board, one Power Stage module and six MD actuators (two per Micro-Fit molex connector).This is the type of example that shows how to use all ports of single Power Stage without additional CAN termination. In this example, termination on CANdle is set to ON.


```{figure} images/control_board/PDS_CAN_3port.png
:alt: PDS_CAN_architecture_example_2
:align: center

FDCAN architecture with 1 Power Stage module

```