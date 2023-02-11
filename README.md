Project pcb-buttonbar
=====================

Overview
--------

This project contains the KiCAD files for a button-bar with
six buttons. Each button uses some additional hardware-components to
debounce the button:

![](schematic-switch.png)

The buttons are pulled up using R1. R2 and C1 serve as a lowpass-filter,
i.e. high frequency bouncing is filtered out. The final inverter, a
74HC14 is a Schmitt-Trigger type inverter. This inverter switches from
high to low at a different level than from low to high (hysteresis),
so this will convert the curve from the RC-filter to sharp edge.


Goodies
-------

The buttonbar supports buttons with four pins spaced 5.08mm x 5.08mm.
Note that normal buttons have spacings of 6.5mm x 4.5mm. 
In addition to the debounce-logic (bottom side of the pcb), there are optional
LEDs on the top.

![](pcb-3d-top.png)
![](pcb-3d-bottom.png)

The footprints for the top-side are 1206, suitable for hand-soldering.
The bottom-side uses 0603, ideal for automatic assembly.


Production Files
----------------

In the directory `production_files` you will find gerber-files, bom and cpl-file
suitable for JCLPCB. Migrating to a format suitable for your favorite
pcb-assembly service should be straightforward.

![](pcb-top.jpg)
![](pcb-bottom.jpg)


Test Program
------------

The directory `src` contains a simple test program. Without the debouncing
in hardware, you would have to pass an additional parameter to the
Button-constructor for debouncing in software.


License
-------

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International
License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]:
https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
