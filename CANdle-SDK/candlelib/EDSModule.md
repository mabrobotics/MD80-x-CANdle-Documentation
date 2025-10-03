# EDS Module

The **EDS module** stands for *Electronic Data Sheet*.\
This type of file is used in the CANopen protocol and defines all the indexes and sub-indexes
present in the motor driver (cf. CiA 306).\
The goal of this module is to make it easier for the user to work with functionalities related to
EDS files.

You can find the Mab Robotics EDS file at:\
[https://mabrobotics.github.io/MD80-x-CANdle-Documentation/Downloads/Downloads.html#canopen-flashers](https://mabrobotics.github.io/MD80-x-CANdle-Documentation/Downloads/Downloads.html#canopen-flashers)

It can be included in your project via the header file:

```cpp
#include "edsParser.hpp"
```

## Main Features

- **Add new object**: Allows the user to correctly add new objects to the EDS file.
- **Delete object**: Allows the user to correctly remove objects from the EDS file.
- **Generate documentation**: Enables the user to generate HTML or Markdown documentation, which is
  easier to read than the raw EDS file.
- **Find string**: Lets the user search for all occurrences of a string in the EDS file and display
  them in the terminal (similar to `Ctrl+F`).
- **Display**: Shows the entire EDS file in the terminal.
- **Get index**: Displays the object corresponding to a given index in the terminal.

## Code Examples

### [Modify EDS file](https://github.com/mabrobotics/CANdle-SDK/blob/main/examples/cpp/eds_example_update_eds_file.cpp)

This example shows how to use the EDS module.\
It provides examples of how to **add, modify, and delete** an EDS object.\
The example also generates the **object dictionary** from the loaded EDS file, which can then be
directly integrated into the user’s software.
