# CANdle ROS/ROS2 nodes

```{hint}
TL;DR: [MD x CANdle - ROS/ROS2 startup guide](https://www.youtube.com/watch?v=6sLQNaJKuJY&t=3s)
```

While C++ API is the most flexible way of interfacing with CANdle/MDxx, ROS/ROS2 APIs are also
available. These have been designed as standalone C++ nodes that use the CANdle library on the
backend. The nodes are designed to be used with already configured drives, thus functions such as
setting FDCAN parameters are unavailable via ROS/2 API. We recommend configuring all drives first
using MDtool or C++/Python API.

Nodes use ROS/2 services to perform initialization and enable/disable the drives. The initialization
services available are:

```
/add_md80s
/zero_md80s
/set_mode_md80s
```

There are also two additional services for enabling/disabling the drives:

```
/enable_md80s
/disable_md80s
```

Once the drives are enabled via `enable_md80s` service, the nodes will ignore all calls to services
other than `disable_md80s`. When enabled, communication switches from service-based to topic-based.
The nodes will publish to the topic:

```
/md80/joint_states
```

And will subscribe to topics:

```
/md80/motion_command
/md80/impedance_command
/md80/velocity_pid_command
/md80/position_pid_command
```
