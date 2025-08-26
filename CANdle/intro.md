(candle_and_hat)=

# CANdle and CANdle HAT

CANdle is a converter used to communicate between MD controllers, PDS and the host device.
Currently, there are two CANdle versions - CANdle and CANdle HAT.

```{figure} images/CANdle_joined.webp
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

The first one is a simple version that uses USB bus to communicate with the host, whereas the latter
can communicate using USB or SPI and is easy to integrate with SBCs such as Raspberry PI. The
communication with MDs and PDS is performed using CAN bus, using either MABs propriatary protocol,
or CANOpen (only MD).

```{figure} images/hardware_setup2.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

CANdle can be accessed via [**CANdle-SDK**](/CANdle-SDK/intro), which is comperhensive set of tools,
that can be used to develop applications with MAB products.

## Purpose & Limitations

While CANdle and CANdleHAT are very capable devices, their main purpose is to allow the users to
quickly get onboard with MD and PDS family of produces. While developing CANdle and CANdle-SDK, we
aim for flexibility, ease-of-use and reliability over performance. **The main purpose of CANdle and
HAT, is to be a great starting point in product development process**, but not neccessarly a final
motion-control solution.

```{figure} images/ecosystem.jpg
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

This means that it is usually not possible to fully unravel the potential of some of our products,
when accessing them exclusively throught CANdle. We are constatnly working on improving the
performance of the Ecosystem, but due to many factors that are out of our control (operating system
latency, user space limitations, kernel behaviour, unknown host hardware etc.), we are not able to
deliver out of the box solution for high-performance, production-ready systems.

Where CANdle will work great as is:

- AGVs,
- ROVs,
- drones,
- simple robotic arms and cobots,
- testing benches and setups,
- MVP of mechatronics products,

Where CANdle will likely be too slow:

- high DoF humanoid robots,
- agile, dynamic quadrupedal robots,
- high-freq control loops (500Hz+).
