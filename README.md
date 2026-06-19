# OPSX-SX70

[中文](README.zh-CN.md) | English

[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Hardware](https://img.shields.io/badge/Open%20Hardware-RP2040%20Core%20Board-0F766E)](gerber/)
[![Firmware](https://img.shields.io/badge/Firmware-MicroPython-2B5B84)](code/micropython/)
[![PCB](https://img.shields.io/badge/PCB-Gerber%20Ready-7A3E9D)](gerber/)

OPSX-SX70 is an open-source replacement core board for the **Polaroid SX-70** instant camera, built around the Raspberry Pi RP2040. It provides a hackable, repair-friendly electronics platform while preserving the essential camera-control behavior of the original board.

## Highlights

- RP2040-based camera control board.
- Factory-ready Gerber files.
- Interactive HTML bill of materials.
- Schematic PDF for circuit inspection.
- MicroPython firmware for rapid iteration.
- Rust firmware workspace reserved for future high-performance control code.

## Repository Layout

| Path | Contents |
| --- | --- |
| [`bom/`](bom/) | Interactive HTML bill of materials for component lookup and placement. |
| [`code/micropython/`](code/micropython/) | Current firmware implementation for the RP2040 board. |
| [`code/rust/`](code/rust/) | Placeholder for future Rust firmware. |
| [`gerber/`](gerber/) | PCB production files and SMT position CSV. |
| [`schematic/`](schematic/) | One-page schematic PDF. |
| [`docs/`](docs/) | Fabrication, firmware, calibration, and safety notes. |

## Hardware

OPSX targets a thin two-layer PCB suitable for the physical constraints of the SX-70 body.

Recommended fabrication settings:

- **Layers:** 2 copper layers
- **PCB thickness:** 0.8 mm or less
- **Assembly:** review the interactive BOM before ordering or hand assembly
- **Files:** use the Gerber package under [`gerber/`](gerber/)

Read [`docs/fabrication.md`](docs/fabrication.md) before manufacturing.

## Firmware

The current firmware is written in MicroPython and lives in [`code/micropython/`](code/micropython/).

Core modules:

- `main.py`: camera-control loop, shutter/motor logic, exposure modes, distance display, and sensor integration.
- `ssd1306.py`: OLED display driver.
- `vl53l1x.py`: time-of-flight distance sensor driver.

Read [`docs/firmware.md`](docs/firmware.md) before flashing the board.

## Calibration and Safety

OPSX controls camera electromechanical parts including a shutter solenoid and motor. Incorrect calibration can damage the camera or board.

Before first use:

1. Read [`docs/safety.md`](docs/safety.md).
2. Inspect soldering and continuity.
3. Calibrate `SOLENOID_THRESHOLD` in `main.py`.
4. Test motor and sensor behavior outside the camera body where possible.
5. Reassemble only after confirming stable control behavior.

## Useful References

- Interactive BOM: [`bom/OPSX_bom.html`](bom/OPSX_bom.html)
- Schematic: [`schematic/OPSX_schematic.pdf`](schematic/OPSX_schematic.pdf)
- Gerbers: [`gerber/`](gerber/)
- KiCad source request: [issue #2](https://github.com/sunyitong/OPSX-SX70/issues/2)
- SX-70 repair reference: <https://instantphotography.files.wordpress.com/2010/12/polaroid-sx-70-camera-repair-book.pdf>

## Roadmap

- Document complete assembly photographs.
- Package Gerber/BOM/schematic as GitHub Releases.
- Add firmware upload scripts.
- Add Rust firmware implementation.
- Add calibration logs for different SX-70 bodies.

## Author

Created by [Yitong Sun](https://github.com/sunyitong), a researcher and developer working across computational design, sensing systems, XR, and open hardware.

- Website: <https://www.yitongsun.com>
- Email: <hi@yitongsun.com>

## License

This project is released under the [GNU General Public License v3.0](LICENSE). Any distribution or modification based on this project should clearly attribute the source.
