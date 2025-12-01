(candletool_commands)=

# Commands

CANdleTool CLI tree is build around each of devices provided by MAB. There it is split into actions
that can be performed. Most of the commands are described below.

```{tip}
Some commands are not listed in this document. You can explore all of the commands in the branch by issuing `-h` flag.
```

## Global parameters

`-h, --help` - Display help.

`-d, --datarate` - Sets a datarate of CAN network when using CANdle device.

`-v, --verbosity` - Sets printing verbosity of the CANdleTool. Supported values are 0,1,2,3.

`-s, --silent` - Turns off output of CANdletool logger.

`--version` - Prints a version of CANdleSDK used.

## **candletool candle ...**

(candletool_update)=

### update

Updates firmware on the CANdle device using provided .mab file.

(md_commands)=

## **candletool md ...**

Branch of CLI dedicated for [MD](/MD/intro) devices. Most of the commands use `--id` parameter to
specify which MD drive to operate on.

### blink

Blink built-in LEDs on MD drive.

### can

Configure CAN network parameters id, datarate and timeout with corresponding flags. `--save` flag
can be used to save the configuration to flash memory.

### calibration

Calibrate the MD drive. If no options are provided the command will perform all of the necessary
calibrations. Type of calibration can be specified using `-e` flag (main or aux). `-t` flag can be
used to perform tests after calibration. The results of the test are printed in the `info` command
output.

### clear

Clear MD drive errors and warnings.

### config

Configure MD drive using (MAB configuration file)[md_config_file]. Config can also be downloaded
from the MD drive using `md config download <file>` command.

### discover

Discover MD drives on the network. This command does not require any parameters. It will print a
list of all MD drives connected to the CANdle device on the selected CAN datarate.

```{important}
This command will not work if the MD drives are not powered on, nor when they are configured to use different CAN datarate than the one set in the `candletool` command.
```

### save

Save MD drive configuration to flash memory.

### info

Get debug information about the MD drive.

### register

Register operations for MD drive. They can be written or read using `write` or `read` subcommands.
Specifying register can be done using either address or name. For example:

```
candletool md register read 0x010 --id 100
```

or

```
candletool md register read motorName --id 100
```

All of the available registers can be found in the [MD registers](registers) section of this
document.

### test

Test the MD drive movement. The movement can be done in positional relative (impedance) or
positional absolute mode (position profile).

### update

Update firmware on MD drive using MABs firmware file (.mab).

(pds_commands)=

## **candletool pds ...**

Branch of CLI dedicated for [PDS](pds) device.

When issuing `candletool pds` command, the user can operate on the PDS device. All of the commands
here are tied to the main PDS command module (CTRL).

Commands for the PDS control module are:

- `info` - Get information about the PDS device.
- `update` - Update firmware on the PDS device using .mab files.
- `can` - Configure CAN network parameters id, datarate and timeout with corresponding flags.
- `save` - Save PDS configuration to flash memory.
- `disable` - Shutdown the PDS device with timeout specified in the configuration file.
- `setup_cfg` - Setup PDS configuration file. This command will create a configuration file in the
  current directory.

To access submodules, the user can use `candletool pds <module_name> <module_socket_number>`
command.

Module names are:

- `ps` - Power supply module.
- `br` - Brake resistor module.
- `ic` - Isolated power converter module.

Main submodule commands are:

- `info` - Get information about the PDS module.
- `enable` - Enable the PDS module.
- `disable` - Disable the PDS module.
