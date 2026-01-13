(python_module)=
# Python Module

## Overview

CANdle-SDK is equipped with python module that is bonded via pyBind11 to candlelib. It can be used for simple applications that does not require real-time efficiency of C++. 

```{important}
Python API of CANdle-SDK is much slower than C++ API so it should never be used for time-sensitive applications.
```

```{note}
CANdleSDK python API requires python versions never than:
- 3.13 for Windows
- 3.12 for Linux
```

## Installation

Most strait forward way of getting the CANdleSDK python module is via pypi repository using pip. The link to the repository can be found [here](https://pypi.org/project/candlesdk/).
