# OPSX
An open sourced Polaroid SX-70 core board

This is an open sourced Polaroid SX-70 instant camera core board with the Raspberry Pi RP2040 as the MCU. The aim of this project is to provide a fully resource accessible and hobbyist friendly replacement core board. It offers more extensibility and hacking ideas while implementing all the features of the original camera.

The structure of the repository:

1. The [bom](https://github.com/sunyitong/OPSX/tree/master/bom) folder contains an html-based interactive bill of material. You can use it to find the component types and locations

2. The [code](https://github.com/sunyitong/OPSX/tree/master/code) folder holds the program files necessary to run the core board. The programs are implemented in two separate programming languages:

   - [Micropython](https://docs.micropython.org/en/latest/rp2/quickref.html): Similar syntax to python, easy to modify and testing.
   - [Rust](https://docs.rs/rp2040/latest/rp2040/) (TODO): Ultimate performance with zero runtime loss.

3. The [gerber](https://github.com/sunyitong/OPSX/tree/master/gerber) folder stores the PCB files necessary for factory production.

4. The [schematic](https://github.com/sunyitong/OPSX/tree/master/schematic) folder holds a PDF file which illustrating the circuit principles.


## Table of Contents

- [OPSX](#opsx)
  - [Table of Contents](#table-of-contents)
  - [Hardware](#hardware)
    - [Fabrication](#fabrication)
  - [Software](#software)
    - [Uploading](#uploading)
  - [Contributor](#contributor)
  - [License](#license)


## Hardware
TODO
> Remander: Special tools are required to replace the original core board, please read the [Disassembly Guide](https://instantphotography.files.wordpress.com/2010/12/polaroid-sx-70-camera-repair-book.pdf) first.
### Fabrication
Please select a **dual copper layer PCB** with a thickness of **0.8 mm** or less for fabrication.
## Software
TODO
### Uploading
TODO
## Contributor
[@Yitong Sun](https://github.com/sunyitong) - a PhD candidate in the Computer Science Research Centre at the Royal College of Art.

[RCA website](https://www.rca.ac.uk/research-innovation/research-degrees/research-students/yitong-sun/) - [E-mail](yitong.sun@network.rca.ac.uk)
## License
Any distribution or modification based on this project should be clearly attributed to the source.
[GPL 3.0](LICENSE) © Yitong Sun