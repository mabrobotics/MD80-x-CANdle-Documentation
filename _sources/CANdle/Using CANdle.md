# Using CANdle and CANdle HAT

## PC (USB bus)

The library does not require any additional software to be functional, It can work as-is. However, to make full use of it we recommend using setserial package (for increasing maximal access frequency to the serial port used for communication with CANdle). To install it please call:

```
sudo apt install setserial
```
To enable access to CANdle from userspace, the user should be added to dialout group by calling:
```
sudo usermod -a -G dialout <user>   # where <user> is current username
```
If this is not possible, devices access level can be granted by:
```
sudo chmod 777 /dev/ttyACMx   # where x is CANdle port number, usually 0
```
If this is also not possible, programs that use CANdle (including examples), can be launched with sudo.


## SBC (USB/SPI/UART)

Running CANdle or CANdle HAT using a USB bus on SBC is identical to running it on a Linux PC (section above). However, when using SPI or UART a few other requirements have to be met. We will guide you through the setup process on Raspberry PI 4.

```{note}
When using SBCs other than Raspberry the process may vary and should be performed according to the board manual or with the help of the manufacturer.
```

## SPI
To enable the SPI bus you should call:
```
sudo nano /boot/config.txt
```
uncomment the following line, save the file
```
dtparam=spi=on
```
and reboot:
```
sudo reboot
```
to make sure SPI is enabled call:
```
ls /dev | grep spi
```
you should see an output similar to this:
```
spidev0.0
spidev0.1
```

## UART

To enable the UART bus you should call:
```
sudo nano /boot/config.txt
```

and add the following lines on the end of the file 
```
enable_uart=1
dtoverlay=disable-bt
```
after that open the cmdline.txt
```
sudo nano /boot/cmdline.txt
```
and remove the part:
```
console=serial0,115200
```
and reboot:
```
sudo reboot
```