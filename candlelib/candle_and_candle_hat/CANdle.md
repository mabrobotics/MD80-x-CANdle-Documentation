(candle_and_hat_legacy)=
# CANdle and CANdle HAT

CANdle is a converter used to communicate between MD controllers and the host device. Currently, there are two CANdle versions - CANdle and CANdle HAT.

```{figure} images/CANdle_joined.webp
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

The first one is a simple version that uses only the USB bus to communicate with the host, whereas the latter can communicate using USB, SPI, and UART bus, and is easy to integrate with SBCs such as Raspberry PI. The communication with MD controllers is performed using FDCAN bus. 


```{figure} images/hardware_setup2.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

To achieve the fastest communication speeds you should aim for the USB bus. For more details on the latency topic please check out the [latency section](latency_legacy).

```{important}
Currently CANdle supports only Linux operating systems.
```
