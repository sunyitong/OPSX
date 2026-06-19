# Firmware Guide

The current OPSX firmware is implemented in MicroPython for RP2040.

## Files

- `code/micropython/main.py`: control logic and camera behavior
- `code/micropython/ssd1306.py`: OLED display driver
- `code/micropython/vl53l1x.py`: time-of-flight sensor driver

## Flashing Workflow

1. Install a MicroPython RP2040 firmware image on the board.
2. Copy the files in `code/micropython/` to the board filesystem.
3. Power-cycle the board.
4. Observe OLED output and sensor readings.
5. Calibrate `SOLENOID_THRESHOLD` before actuating the shutter inside a camera body.

## Important Constant

`SOLENOID_THRESHOLD` in `main.py` controls the hold duty cycle for the shutter solenoid. It should be tuned through self-test and should not be treated as universal across boards or camera bodies.

## Future Work

The `code/rust/` directory is reserved for a future Rust firmware implementation.
