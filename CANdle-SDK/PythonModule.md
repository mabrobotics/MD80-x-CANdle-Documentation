(python_module)=

# Python Module

## Overview

CANdle-SDK is equipped with python module that is bonded via pyBind11 to candlelib. It can be used for simple applications that does not require real-time efficiency of C++.

```{important}
Python API of CANdle-SDK is slower than C++ API so it should never be used for time-sensitive applications.
```

```{note}
CANdleSDK python API requires python versions newer than:
- 3.13 for Windows
- 3.12 for Linux
```

## Installation

The recommended way of installing python module of CANdle-SDK is to use [pypi CANdle-SDK repository](https://pypi.org/project/candlesdk/) along with [virtual environment for python](https://docs.python.org/3/library/venv.html).

The commands may look like this:

```
python3 -m venv venv
source ./venv/bin/activate
python3 -m pip install candlesdk
```

## Usage

For usage examples please refer to the [python examples](https://github.com/mabrobotics/CANdle-SDK/tree/main/examples/py).

```{important}
If you have installed the CANdle-SDK using virtual environment remember to call `source` command on `activate` script inside virtual envrionment directory whenever you are trying to execute code with CANdleSDK.
```

```{seealso}
See [getting started](getting_started) section for the exact step-by-step guide to running python examples.
```
