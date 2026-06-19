# Calibration Notes

OPSX interacts with electromechanical parts whose behavior can vary across camera bodies. Treat the default values as a starting point, not as guaranteed production settings.

## Solenoid Threshold

`SOLENOID_THRESHOLD` is used to hold the shutter solenoid after the initial actuation pulse.

Recommended process:

1. Start with conservative values.
2. Test actuation outside the camera body if possible.
3. Check heat, current draw, and mechanical response.
4. Increase only when the shutter does not hold reliably.
5. Record the working value for the specific board and camera.

## Sensor Checks

- Confirm I2C communication before triggering mechanical actions.
- Confirm distance readings from the VL53L1X sensor.
- Confirm OLED output before final assembly.

## Exposure Modes

The MicroPython firmware contains exposure constants such as `ev7`, `ev8`, and `ev16`. If changing exposure behavior, document the mapping and test with real film only after bench verification.
