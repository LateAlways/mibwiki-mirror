# PQ/ZR units with firmwares 01xx

When patching `01xx` firmware versions you need to consider follwing :

* If the unit has less than `1024MB` of RAM (check in `mibstd2_toolbox→mib_info → Show short system info`), dump/copy operations from MIBSTD2 Toolbox can sometimes lead to crash/reboot of the unit.
* Buggy `SWaPPatcher.exe` and  `SWDLPatcher.exe`  cannot be used for patching firmwares `01xx` correct!
  * Latetest MIBSTD2 Toolbox versions already contain patches for some firmware `01xx` versions.