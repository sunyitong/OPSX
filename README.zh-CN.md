# OPSX-SX70

中文 | [English](README.md)

[![License: GPL-3.0](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Hardware](https://img.shields.io/badge/Open%20Hardware-RP2040%20Core%20Board-0F766E)](gerber/)
[![Firmware](https://img.shields.io/badge/Firmware-MicroPython-2B5B84)](code/micropython/)
[![PCB](https://img.shields.io/badge/PCB-Gerber%20Ready-7A3E9D)](gerber/)

OPSX-SX70 是一个面向 **Polaroid SX-70** 即时相机的开源替代核心板，基于 Raspberry Pi RP2040。它的目标是在保留原相机核心控制行为的同时，提供一个更容易维修、调试和扩展的硬件平台。

## 亮点

- 基于 RP2040 的相机控制板；
- 可直接用于生产的 Gerber 文件；
- 交互式 HTML BOM，便于查找元件和位置；
- 原理图 PDF，便于电路检查；
- MicroPython 固件，方便快速迭代；
- 预留 Rust 固件目录，用于未来高性能控制实现。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| [`bom/`](bom/) | 交互式 HTML BOM。 |
| [`code/micropython/`](code/micropython/) | 当前 RP2040 固件实现。 |
| [`code/rust/`](code/rust/) | 未来 Rust 固件预留目录。 |
| [`gerber/`](gerber/) | PCB 生产文件与 SMT position CSV。 |
| [`schematic/`](schematic/) | 一页式原理图 PDF。 |
| [`docs/`](docs/) | 打板、固件、校准与安全说明。 |

## 硬件

OPSX 面向 SX-70 机身内部的空间限制，因此 PCB 厚度和装配尺寸很关键。

推荐打板设置：

- **层数：** 双层铜；
- **厚度：** 0.8 mm 或更薄；
- **装配：** 下单或手工焊接前先检查交互式 BOM；
- **文件：** 使用 [`gerber/`](gerber/) 中的生产文件。

制造前请阅读 [`docs/fabrication.md`](docs/fabrication.md)。

## 固件

当前固件使用 MicroPython，位于 [`code/micropython/`](code/micropython/)。

核心文件：

- `main.py`：相机控制循环、快门/电机逻辑、曝光模式、距离显示和传感器集成；
- `ssd1306.py`：OLED 显示驱动；
- `vl53l1x.py`：飞行时间距离传感器驱动。

烧录前请阅读 [`docs/firmware.md`](docs/firmware.md)。

## 校准与安全

OPSX 会控制快门电磁铁和电机等机电部件。错误校准可能损坏相机或电路板。

首次使用前：

1. 阅读 [`docs/safety.md`](docs/safety.md)；
2. 检查焊接和短路；
3. 校准 `main.py` 中的 `SOLENOID_THRESHOLD`；
4. 尽可能在机身外测试电机与传感器行为；
5. 控制稳定后再装回相机。

## 常用链接

- 交互式 BOM：[`bom/OPSX_bom.html`](bom/OPSX_bom.html)
- 原理图：[`schematic/OPSX_schematic.pdf`](schematic/OPSX_schematic.pdf)
- Gerber：[`gerber/`](gerber/)
- KiCad 源文件请求：[issue #2](https://github.com/sunyitong/OPSX-SX70/issues/2)
- SX-70 维修参考：<https://instantphotography.files.wordpress.com/2010/12/polaroid-sx-70-camera-repair-book.pdf>

## Roadmap

- 补充完整装配照片；
- 将 Gerber/BOM/原理图打包为 GitHub Releases；
- 增加固件上传脚本；
- 实现 Rust 固件版本；
- 补充不同 SX-70 机身的校准记录。

## 作者

Created by [Yitong Sun](https://github.com/sunyitong)，研究与开发方向包括 computational design、sensing systems、XR 与 open hardware。

- Website: <https://www.yitongsun.com>
- Email: <hi@yitongsun.com>

## 许可证

本项目采用 [GNU General Public License v3.0](LICENSE)。任何基于本项目的分发或修改都应清晰标注来源。
