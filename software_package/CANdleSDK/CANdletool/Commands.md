(candletool_commands)=
# Commands

CANdleTool CLI tree is build around each of devices provided by MAB. There it is split into actions that can be performed. Most of the commands are described below.

```{note}
Some commands are not listed in this document. You can explore all of the commands in the branch by issuing `-h` flag. 
```
## Global parameters

`**-h, --help**` - Display help.

`**-d, --datarate**` - Sets a datarate of CAN network when using CANdle device.

`**-v, --verbosity**` - Sets printing verbosity of the CANdleTool. Supported values are 0,1,2,3. 

`**-s, --silent**` - Turns off output of CANdletool logger.

`**--version**` - Prints a version of CANdleSDK used.


## **candle**

(candletool_update)=
### Update

Updates firmware on the CANdle device using provided [MAB firmware file](mab_files).

## **md**

Branch of CLI dedicated for [MD](md) devices. Most of the commands use `--id` parameter to specify which MD drive to operate on. 

### blink
Blink built-in LEDs on MD drive. 
### can                         
Configure CAN network parameters id, datarate and timeout with corresponding flags. `--save` flag can be used to save the configuration to flash memory.
### calibration                 
Calibrate the MD drive. If no options are provided the command will perform all of the necessary calibrations. Type of calibration can be specified using `-e` flag (main or aux). `-t` flag can be used to perform tests after calibration. The results of the test are printed in the `info` command output.
### clear                       
Clear MD drive errors and warnings. 
### config                      
Configure MD drive using (MAB configuration file)[md_config_file]. Config can also be downloaded from the MD drive using `md config download <file>` command. 
### discover                    
Discover MD drives on the network. This command does not require any parameters. It will print a list of all MD drives connected to the CANdle device on the selected CAN datarate.
```{important}
This command will not work if the MD drives are not powered on, nor when they are configured to use different CAN datarate than the one set in the `candletool` command.
```
### save                        
Save MD drive configuration to flash memory. 
### info                        
Get debug information about the MD drive. 
### register                    
Register operations for MD drive. They can be written or read using `write` or `read` subcommands. Specifying register can be done using either address or name. For example:
```
candletool md register read 0x010 --id 100
```
or
```
candletool md register read motorName --id 100
```

All of the available registers can be found in the [MD registers](registers) section of this document.
### test                        
Test the MD drive movement. The movement can be done in positional relative (impedance) or positional absolute mode (position profile). 

### update                      
Update firmware on MD drive using [MAB firmware file](mab_files). 

## **pds**

Branch of CLI dedicated for [PDS](pds) device.

### Main module 

When issuing `candletool pds` command, the user can operate on the PDS device. All of the commands here are tied to the main PDS module.

Main commands for the PDS control module are:
- `info` - Get information about the PDS device.
- `update` - Update firmware on the PDS device using [MAB firmware file](mab_files).
- `can` - Configure CAN network parameters id, datarate and timeout with corresponding flags.
- `save` - Save PDS configuration to flash memory.
- `disable` - Shutdown the PDS device with timeout specified in the configuration file.
- `setup_cfg` - Setup PDS configuration file. This command will create a configuration file in the current directory. 


To access submodules, the user can use `candletool pds <module_name> <module_socket_number>` command.

Module names are:
- `ps` - Power supply module.
- `br` - Brake resistor module.
- `ic` - Isolated power converter module.

Main submodule commands are:
- `info` - Get information about the PDS module.
- `enable` - Enable the PDS module.
- `disable` - Disable the PDS module.

## **MDCO**

Branch of CLI dedicated for [MDCO](mdco) device.

### blink

Blink built-in LEDs on MD drive. 

### clear

Clear Errors and Warnings.

### config

Configure CAN network parameters id, datarate and timeout with corresponding subcommands. Don't forget to save your modification before shunting down your driver.

### EDS

EDS file analizer and generator.

### encoder

Display MD motor position.

### heartbeat

Test heartbeat detection of a device.

### nmt

Send NMT commands. Usefull for changing NMT state of the MD state machine

### pdo

Try to send pdo can frame instead of sdo.

### ping

Discover MD drives on CAN bus.

This command will not work if the MD drives are not powered on, nor when they are configured to use different CAN datarate than the one set in the `candletool` command.

### register

Access MD drive via register read/write. Specifying register can be done using either address + subaddress or name. For example:
```
candletool mdco register read --id 10 --index 0x2000 --subindex 0x06
```
or
```
candletool mdco register read --id 10 --value motorName 
```

### reset

Reset MD drive. 

### setup

Setup MD using (MAB configuration file), and calibrate.

### sync

Send a sync CANopen message. This type of message is used for avoiding future CAN message collision.

### segmented

Send a message using SDO segmented transfer. Segmented are usefull for register with more than 4 bytes of data (e.g. Motor Name).

### test

Basic MD drive testing routines like moving the motor. 

### time

Send a time stamp message to the MD using the computer's clock.