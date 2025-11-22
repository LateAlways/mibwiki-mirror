# Installation via USB2HSD cable (aka solderless or OTG method)

[Video_Instruction.mp4 18089642](attachments/561d1d5c-5408-43a6-84e5-962cb5f576e9.mp4)


:::info
The video above serves only for illustrating purposes. This "solution" was stolen by evaldas who wanted to sell it but failed. Original author is **Malec**.

:::


**LIMITATIONS:** This method is compatible with one and two SD slot `cpu` and `cpuplus` units but not with `mainstd` units **without** `iMX6` chipset. 

Units without `iMX6` have part numbers like `xxx 035 81*` and `xxx 035 82*`. 

E.g `5Q0 035 819*`, `5Q0 035 824*`.

This will **not work** on **some** `cpuplus` units too, as the drivers included into `custom_plus.ifs` are not compatible with all types of the units.

Detailed description of how it works as well as **FREE **`imx_usb tool` (aka patcher) can be found here