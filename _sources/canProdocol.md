# MD80 FDCAN communication
The easiest way to communicate with an MD80 controller is to use a CANdle device connected to a PC. Even though we are aware some customers want to integrate the MD80 controllers in their product with minimal setup to reduce the costs and the system’s complexity. This manual will guide you through the process of communicating with MD80 actuators from your custom FDCAN-capable master controller.

# Hardware requirements
The main requirement for the host system is to be equipped with an FDCAN peripheral (either a built-in one or an external one) and an FDCAN transceiver capable of speeds up to 8Mbps. Lower maximum speed transceivers can be used as well, however for the cost of limited update rates. Currently, the differential side of the transceiver (the CANH and CANL lines) is supplied with 5V. Depending on your custom setup you should be able to integrate a 120 ohm terminating resistor on both ends of your CAN bus (MD80 controllers from version 2.0 have a built-in resistor that can be controlled by software).

# Communication overview
MD80 controllers are programed to receive a frame that takes the following structure:


<table>
<tr>
<th>Argument</th>
<th>Description</th>
</tr>
<tr>
<td>appDir</td>
<td>The top level directory that contains your app. If this option is used then
it assumed your scripts are in</td>
</tr>
<tr>
<td>baseUrl</td>
<td>By default, all modules are located relative to this path. If baseUrl is not
explicitly set, then all modules are loaded relative to the directory that holds
the build file. If appDir is set, then baseUrl should be specified as relative
to the appDir.</td>
</tr>
<tr>
<td>dir</td>
<td>The directory path to save the output. If not specified, then the path will
default to be a directory called "build" as a sibling to the build file. All
relative paths are relative to the build file.</td>
</tr>
<tr>
<td>modules</td>
<td>List the modules that will be optimized. All their immediate and deep
dependencies will be included in the module's file when the build is done. If
that module or any of its dependencies includes i18n bundles, only the root
bundles will be included unless the locale: section is set above.</td>
</tr>
</table>

```{list-table} 
:header-rows: 1

* - 
  - BYTE 0
  - BYTE 1
  - BYTE 0
  - CANdle ROS
  - CANdle ROS2
  - CANdle device
  - MD80
* - earlier
  - [3.0](https://github.com/mabrobotics/candle/releases/tag/v3.0)
  - [1.1.0](https://github.com/mabrobotics/mdtool/releases/tag/v1.1)
  - [1.2.0](https://pypi.org/project/pyCandleMAB/1.2.0/)
  - [1.1.0](https://github.com/mabrobotics/candle_ros/releases/tag/v1.1)
  - [1.1.0](https://github.com/mabrobotics/candle_ros2/releases/tag/v1.1)
  - 1.4
  - 1.0
* - 12.12.2022 (latest)
  - [3.1](https://github.com/mabrobotics/candle/releases/tag/v3.1_hotfix)
  - [1.2.1](https://github.com/mabrobotics/mdtool/releases/tag/v1.2.1)
  - [1.3.1](https://pypi.org/project/pyCandleMAB/)
  - [1.2.0](https://github.com/mabrobotics/candle_ros/releases/tag/v1.2)
  - [1.2.0](https://github.com/mabrobotics/candle_ros2/releases/tag/v1.2)
  - [2.0](https://drive.google.com/drive/folders/10wIX2uEaf42pkwGgW9fVAcGT7zrbptN9?usp=share_link)
  - [2.0](https://drive.google.com/drive/folders/10wIX2uEaf42pkwGgW9fVAcGT7zrbptN9?usp=share_link)
```
