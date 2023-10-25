# CANdle Python library

CANdle Python library is a translated version of the C++ library using pybind11. The package can be found on PyPi: https://pypi.org/project/pyCandleMAB/ and installed using pip:
```
python3 -m pip install pyCandleMAB
```
It can be used to quickly start playing with the actuators, without the need to build the C++ software pack. Example usage of Python examples is shown in the [getting started guide](https://www.youtube.com/watch?v=bIZuhFpFtus&t=1s). To achieve the best performance in low latency systems we advise using the C++ libraries directly.

```{note}
We distribute the binaries as well as sources - in case your platform is not recognized with the available binaries pip will try to build and install the library from the source.
```