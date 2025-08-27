(candletool)=

# CANdleTool

CANdleTool is a program with a set of utilities intended to help the user in configuration and
testing of MD products.

## Main Features

CANdleTool main features

- Updating software in all of MAB devices.
- Downloading debug information and configurations from the target device.
- Uploading configuration to the device.
- Testing device functionalities.

## Distribution

We distribute whole CANdle-SDK package as free and open source software via
[github](https://github.com/mabrobotics/CANdle-SDK) under MIT license.

We also provide binaries for the CANdleTool package via releases on github and in the
[downloads](downloads) section of this document.

We distribute packages for apt package manager for architectures x86_64, arm64 and armhf (not
recommended), as well as an installer for Windows x86_64. All of them can be found on
[release pages](https://github.com/mabrobotics/CANdle-SDK/releases).

## Usage

CANdleTool is a CLI program. You can issue commands using CLI interface, for example:

```
candletool md blink --id 100
```

will blink built-in LEDs on MD controller.

```
candletool md test relative 10.0 --id 100
```

This command will make a MD driver connected to the CANdle device move 10.0 radians
counter-clockwise using Impedance Mode motion controller.

To explore different commands the user can always use `-h` option.

```
$ candletool -h

   ___     _     _  _      _   _         _____               _
  / __|   /_\   | \| |  __| | | |  ___  |_   _|  ___   ___  | |
 | (__   / _ \  | .` | / _` | | | / -_)   | |   / _ \ / _ \ | |
  \___| /_/ \_\ |_|\_| \__,_| |_| \___|   |_|   \___/ \___/ |_|

For more information please refer to the manual: https://mabrobotics.pl/servos/manual



candletool [OPTIONS] [SUBCOMMAND]


OPTIONS:
  -h,     --help              Print this help message and exit
  -d,     --datarate TEXT:{1M,2M,5M,8M} [1M]
                              Select FD CAN Datarate CANdleTOOL will use for communication.
          --bus TEXT:{USB,SPI} [USB]
                              Select bus to use (only for CandleHAT).
          --device TEXT       For SPI: {path to kernel device endpoint} | For USB: {device
                              serial number}
  -v{1},  --verbosity{1} [0]  Verbose modes (1,2,3)
          --version           Show software version
  -s,     --silent            Silent mode
          --log               Redirect output to file

SUBCOMMANDS:
  candle                      CANdle device commands.
  md                          MD commands.
  pds                         Tweak the PDS device
```

For more details visit [Commands](candletool_commands) section.
