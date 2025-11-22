# Replacing files with the patched ones

If MIB STD2 Toolbox does not support live patching of your unit, you can patch files manually yourself and upload them back to unit with the toolbox.

## Procedure


1. Make sure you have installed the latest version of the toolbox from here: [https://github.com/olli991/mib-std2-pq-zr-toolbox](https://github.com/olli991/mib-std2-pq-zr-toolbox/releases).


:::info
Details about [Technisat MIB STD2 Toolbox installation](/doc/technisat-mib-std2-toolbox-installation-GIgwX2camY).

:::


2. Place the external file (for example patched SWDL app) in the proper `custom` directory on the Toolbox SD card.
3. Turn on infotainment, place the SD card in `SD1` port.
4. Enter the Toolbox.
5. Go to `customization` and find option to copy your external file (for example `advanced`, `Copy SWDL to unit`).
6. Toolbox will make a backup copy of the original file from unit and will save it to the SD card. Next it will replace the original file in the unit with the custom one.
7. Reboot the unit. Check [Key combinations and shortcuts](/General information/Useful documents/Key combinations and shortcuts/) to learn how to reboot your unit.

## Example with inserting externally patched SWDL app

|  ![](attachments/9ae70443-e1b3-4f02-b04a-a35929c13d34.jpg) |  ![](attachments/bdf24362-c45d-47e0-9604-ee995f73c2fb.jpg) |  ![](attachments/38222171-4db0-45ef-a237-92a87615afea.jpg) |
|----|----|----|