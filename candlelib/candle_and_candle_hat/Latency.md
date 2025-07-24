(latency_legacy)=

# Latency

The latency was measured using the [`mdtool test latency 8M`](mdtool_test_latency_legacy) command.
Since the CAN frames are synchronized with master device frames the update rate of the master is the
same as MD. The setup was tested on a PC using only USB bus (PC Ideapad Gaming 3 AMD Ryzen 7 4800H)
and Raspberry PI 3b+ with RT PATCH (4.19.71-rt24-v7+) on USB, SPI, and UART bus.

```{figure} ./images/MD80_latency.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

High task priority was achieved using the following snippet in the mdtool test latency function:

```
    struct sched_param sp;
    memset(&sp, 0, sizeof(sp_legacy));
    sp.sched_priority = 99;
    sched_setscheduler(0, SCHED_FIFO, &sp);
```

To be able to change task priority be sure to call the test with `sudo`.

To change a running task priority use the snippet below. It can be useful when your program cannot
be run directly with sudo - for example, when dealing with ROS nodes.

```
CONTROL_PID=$(sudo pidof -s <NAME_OF_YOUR_EXECUTABLE>)
CONTROL_PRIORITY=99
sudo chrt -f -p ${CONTROL_PRIORITY} ${CONTROL_PID}
```

During testing on Raspberry PI SBCs we have found out that isolating a CPU core (isolcpus_legacy)
specifically for the CANdle process did not result in a performance increase - rather made it less
performant.

```{note}
When dealing with the MD x CANdle ecosystem for the first time we advise using the USB bus that is available on both CANdle and CANdle HAT devices.
```
