# Fabrication Guide

OPSX is designed for the physical constraints of the Polaroid SX-70 body.

## Recommended PCB Settings

- 2 copper layers
- 0.8 mm thickness or less
- Standard solder mask
- Review edge cuts before ordering
- Review the SMT position CSV if using assembly service

## Production Files

Use the files under `gerber/`:

- copper: `OPSX-F_Cu.gbr`, `OPSX-B_Cu.gbr`
- solder mask: `OPSX-F_Mask.gbr`, `OPSX-B_Mask.gbr`
- paste: `OPSX-F_Paste.gbr`, `OPSX-B_Paste.gbr`
- silkscreen: `OPSX-F_Silkscreen.gbr`, `OPSX-B_Silkscreen.gbr`
- drills: `OPSX-PTH.drl`, `OPSX-NPTH.drl`
- board outline: `OPSX-Edge_Cuts.gbr`
- SMT placement: `OPSX-pos.csv`

## Pre-Order Checklist

- Confirm board thickness with the manufacturer.
- Open the Gerbers in an independent viewer.
- Check connector orientation and board outline.
- Review the interactive BOM in `bom/OPSX_bom.html`.
- Confirm that every component is available or has a tested substitute.
