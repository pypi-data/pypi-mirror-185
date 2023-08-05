# Have a piece of SugarPie

SugarPie is a Python library to drive the PiSugar UPS / Battery (https://github.com/PiSugar).

The main motivations to create this library are:
- The official driver takes the form of a web server, which is not always practical.
- The official driver does not support all the features of the product (eg: the watchdog).

This library is based upon the official documentation for the PiSugar 3 Series: https://github.com/PiSugar/PiSugar/wiki/PiSugar-3-Series

Support for other versions of the product may be added later.

## Usage
Suggested installation is through `pip`: `pip install sugarpie`

Make sure I2C is activated on the Raspberry Pi (it is the communication
channel used to control the PiSugar). One option to execute the following
command on the device:
`raspi-config nonint do_i2c 0`.

You can find some examples in the contrib directory with some `systemd` services and corresponding
Python scripts that use the library.

`from sugarpie import pisugar`

`pisugar.switch_system_watchdog('on')`  
`pisugar.reset_system_watchdog()`  
`pisugar.switch_system_watchdog('off')`  
`pisugar.get_temperature()`

(Be careful when playing with the system watchdog. When turned on, you need to either stop
it or reset it regularly, or the PiSugar will restart the power! You can find a complete
example in the contrib/systemd folder.)

## Supported Features
The goal is to support all the features advertised officially in the PiSugar documentation. Here
is a list of the currently supported features.  
You can find more details within the `src/pisugar.py` module where each feature should have its
corresponding method with a well described docstring.

- Sytem Watchdog: turn on, turn off and reset the watchdog: `pisugar.switch_system_watchdog('on|off')` + `pisugar.reset_system_watchdog()` every < 30 seconds by default.
- Boot Watchdog: turn on, turn off and reset the watchdog: `pisuagr.switch_boot_watchdog('on|off')` + `pisugar.reset_boot_watchdog()` (currently not working on the PiSugar 3 Plus, see [this issue](https://github.com/PiSugar/pisugar-power-manager-rs/issues/81))
- Power Output Switch: turn off the power delivered to the Raspberry Pi with an optional delay: `pisugar.switch_power_output(delay in seconds)` (Useful for completely cutting power after a shutdown.) (The delay is currently not working on the PiSugar 3 Plus, please see [this issue](https://github.com/PiSugar/pisugar-power-manager-rs/issues/82)
- Get the PiSugar temperature: `pisugar.get_temperature()`
- Get the PiSugar firmware version: `pisugar.get_firmware_version()`

## How it works
Everything happens over the i2c bus by setting bits at specific addresses. It depends on the SMBus
library.

In case you are interested, here is a (incomplete) map of the registers and their corresponding functions:
![Registers Addresses](PiSugar_Registers_Addresses.png)

## Contributing
Contributions are welcome. The project is organized such as it should be simple to just add
new support, withtout having to modify the current structure (*trying* to respect the SOLID principles).  
When contributing, please format your code with [Black](https://github.com/psf/black), or the CI
will break.

## License
MIT License.
