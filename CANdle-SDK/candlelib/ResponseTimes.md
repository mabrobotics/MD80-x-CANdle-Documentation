# Response Time

The test was performed on multiple platforms, OS and interfaces. The frequency represents the time it took for the selected frames to reach set amount of drivers plus and for the CANdle device to register confirmation messages from all of successful transfers. The test was performed using an async CANdle-SDK API written and was written in C++.

```{note}
Values listed below may vary for user systems . They depend on the peripheral load as well as the performance of the system itself and other factors.
```

## X86

| MD count | Mean [Hz] | RMSE [Hz] |
| -------: | --------: | --------: |
|        1 |  1992,032 |   115,078 |
|        2 |  1023,541 |    34,572 |
|        3 |   797,448 |     15,89 |
|        4 |   622,665 |    25,201 |
|        5 |   526,316 |    12,742 |
|        6 |   430,849 |    39,979 |
|        7 |   377,786 |     11,56 |
|        8 |   337,952 |     6,853 |
|        9 |   287,109 |     7,913 |
|       10 |    264,34 |     8,874 |
|       11 |   241,138 |     9,885 |
|       12 |   219,829 |    12,758 |

# RPI (USB)

| MD count | Mean [Hz] | RMSE [Hz] |
| -------: | --------: | --------: |
|        1 |  1689,189 |   142,668 |
|        2 |  1037,344 |    89,315 |
|        3 |   752,445 |    40,765 |
|        4 |   564,972 |      31,6 |
|        5 |   490,436 |    16,837 |
|        6 |   365,898 |    14,593 |
|        7 |   327,761 |     8,916 |
|        8 |   301,023 |     9,062 |
|        9 |   279,174 |     9,586 |
|       10 |   249,938 |      4,06 |
|       11 |   217,581 |      5,16 |
|       12 |   207,857 |    12,443 |

# Windows

| MD count | Mean [Hz] | RMSE [Hz] |
| -------: | --------: | --------: |
|        1 |   666,667 |    36,444 |
|        2 |   333,444 |     1,001 |
|        3 |   250,752 |    12,072 |
|        4 |   191,022 |    11,385 |
|        5 |   156,201 |    17,201 |
|        6 |   139,782 |    10,141 |
|        7 |   129,032 |     8,241 |
|        8 |   102,533 |     16,81 |
|        9 |    88,191 |    14,039 |
|       10 |    83,181 |    11,769 |
|       11 |    73,512 |    10,125 |
|       12 |     71,49 |     9,036 |

# RPI (SPI)

| MD count | Mean [Hz] | RMSE [Hz] |
| -------: | --------: | --------: |
|        1 |      1267 |        69 |
|        2 |       885 |        48 |
|        3 |       614 |        79 |
|        4 |       480 |        18 |
|        5 |       456 |        50 |
|        6 |       348 |        68 |
|        7 |       293 |         9 |
|        8 |       286 |        26 |
|        9 |       284 |        28 |
|       10 |       268 |        25 |
|       11 |       225 |        38 |
|       12 |       237 |         9 |


# Summary figure

```{figure} images/ResponseTimes.png
:alt: ResponseTimes
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```