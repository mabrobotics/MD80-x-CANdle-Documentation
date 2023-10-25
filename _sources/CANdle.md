# CANdle and CANdle HAT

CANdle is a translator device used to communicate between MD80 controllers and the host device. Currently, there are two CANdle versions - CANdle and CANdle HAT.

```{figure} images/CANdle_joined.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

The first one is a simple version that uses only the USB bus to communicate with the host, whereas the latter can communicate using USB, SPI, and UART bus, and is easy to integrate with SBCs such as Raspberry PI. The communication with MD80 controllers is performed using FDCAN bus. 


```{figure} images/hardware_setup2.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```


To achieve the fastest communication speeds you should aim for the SPI bus. For more details on the latency topic please check out the [latency section](latency).

```{important}
Currently CANdle supports only Linux operating systems.
```
