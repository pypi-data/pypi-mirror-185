1.4.0:
- Add feature: get the current battery power level.
1.3.0:
- Add the feature to get the current firmware version.
1.2.1:
- Fix the library import: `from sugarpie import pisugar` now works as expected.
1.2.0:
- Add the temperature feature.
1.1.0:
- Add the power output switch off feature, with its optional delay.
(it has an [open issue](https://github.com/PiSugar/pisugar-power-manager-rs/issues/82))
1.0.3:
- Update the systemd examples to better practices.
1.0.2:
- Add the documentation to activate I2C on the Raspberry Pi.
1.0.1:
- Add a table documenting the I2C registers.
1.0.0:
- Add the boot watchdog feature (it has an [open issue](https://github.com/PiSugar/pisugar-power-manager-rs/issues/81))
- breaking change in the API that triggers a major version number bump:
	- the call to turn_on / off_system_watchdog() is now replaced
	  with switch_system_watchdog('on' / 'off')
