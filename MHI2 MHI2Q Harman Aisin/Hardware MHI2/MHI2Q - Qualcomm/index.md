# MHI2Q - Qualcomm

:::tip
MHI2Q units are manufactured by Harman and Aisin for some Audi A4, A5, Q5, Q7 and have trains

**MHI2Q_XX_AUG22_XXXXX**

:::

RCC board is the same as on MHI2:

* no visible changes from shell access visible
* MIBROOT patch still the same like on regular MHI2 units


MMX board has different design:

* Qualcomm chip instead of [Tegra30](/MHI2 MHI2Q Harman Aisin/Hardware MHI2/#h-mmx-pcb)
* eMMC instead of NAND
* NOR is removed, its partitions stored in the eMMC and mapped internally, so the file system layout similar to MHI2 is achieved. There is no /mmx/dev/fs0 and that's why m.i.b. does not create MMX_fs0.bin backup


:::info
As no MHI2Q unit is directly available for m.i.b development, support is just based on a random remote access to some of these units:grinning: 

:::