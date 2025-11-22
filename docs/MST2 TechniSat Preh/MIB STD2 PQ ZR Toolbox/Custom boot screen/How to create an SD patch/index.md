# How to create an SD patch

:::warning
REMEMBER! Every intervention to MIB firmware can result a boot loop. If this happens you will have to flash the original FW via emergency mode. Everything you do is at your own risk!

:::

# Basic information


:::info
With this tutorial you will be able to create your own SD Card patch depending on your system and needs.

:::


:::warning
Read all steps before start working with this!

:::

## Tools required


1. `MST2_DIY_SD_patch_bundle.7z` tool package stored on MIBSolution.one in MQB_Solution/MST2 - TechniSat Preheating /Instruction.
2. FW on your unit or better and easier the FW file you want to update to.

# Steps


:::info
If you want to build a new Patch, always use a fresh download of `DIY SD Patch.7z`.

:::


:::info
Never use the template again if you have already built a patch with it!

Always start with a clean copy.

:::

* The `xx` in some file names and folders below are placeholders, as these parts differ depending on the FW you are working with.
* Every `JXETool` will create a modified file in the same place as the original file is stored.
* There is also a German `Liemich.txt` coming with the archive ;-)

## **CP OFF, or FEC ALL or CID OFF**


:::tip
Decide which patches you need: [CP_OFF](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Custom boot screen/How to create an SD patch/#h-cpoff-modify-tsdmibstd2hmiifs), or FEC_ALL, or [CID_OFF](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Custom boot screen/How to create an SD patch/#h-cidoff)

:::

### FEC_ALL (modify `tsd.mibstd2.system.swap`)


:::info
This will enable all FECs supported by unit

:::


1. Get `cpu_swap_xx_default.tar.gz` in folder`cpu/swap/xx/default/` from FW file
2. Get `tsd.mibstd2.system.swap` stored in `tsd/bin/swap/`
3. Unpack this file into `/JXETools/` folder and run`SWaPPatcher.exe` then press Enter if the filename is still `tsd.mibstd2.system.swap` and the file `tsd.mibstd2.system.swap.patch` will be created.
4. Move the file `tsd.mibstd2.system.swap.patch` to `_patch_template\cpu\onlineservices\1\default\tsd\bin\swap` folder and rename it to `tsd.mibstd2.system.swap`
5. FECs will be added by **Exception list** `signed_exception_list.txt` which is already stored in `_patch_template\cpu\onlineservices\1\default\tsd\etc\slist`. Just leave the file as it is.


:::tip
No additional upload of SWAPs is required with this method!

:::

* If you also need `CP_OFF`, continue with the CP_OFF part.
* If you need only needed `FEC_ALL` patch you have to use [HashesGenerator.exe](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Custom boot screen/How to create an SD patch/#h-signing-with-hashesgeneratorexe) now!

### CP_OFF (modify `tsd.mibstd2.hmi.ifs`)


:::info
CP will be patched out - error in `5F` will stay

:::


1. Get `cpu_hmixx_xx_default.tar.gz` in folder`cpu/hmixxx/xx/default/` from FW file
2. Get the whole `hmi` folder stored in `tsd/tmp/`
3. Unpack the `hmi` folder to `_patch_template\cpu\onlineservices\1\default\tsd\tmp\hmi`. Get file `tsd.mibstd2.hmi.ifs` from `_patch_template\cpu\onlineservices\1\default\tsd\tmp\hmi`and **move** it into IFSTool folder. Run `IFSTool.exe` and load `tsd.mibstd2.hmi.ifs`
4. Click "Unpack" and `tsd.mibstd2.hmi-unpacked.ifs` will be created in a folder. Copy this file to the same folder as `CPPatcher.exe` (`JXETools`folder) and run it. The file `tsd.mibstd2-hmi-unpacked.ifs.patched` will be generated.
5. Load  `tsd.mibstd2-hmi-unpacked.ifs.patched` into `IFSTool` and click "Pack".
6. Now there will be a file `tsd.mibstd2-hmi-unpacked.ifs-repacked.patched`. Copy it into `_patch_template\cpu\onlineservices\1\default\tsd\tmp\hmi` folder and **rename** to `tsd.mibstd2.hmi.ifs`
7. Copy the whole (modified) `hmi` folder to `cpu/onlineservices/1/default/tsd/tmp/`.

* If you also need `CID_OFF`, continue with the [CID_OFF](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Custom boot screen/How to create an SD patch/#h-cidoff) part.
* If you need only needed `CP_OFF` patch you have to use [HashesGenerator.exe](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Custom boot screen/How to create an SD patch/#h-signing-with-hashesgeneratorexe) now!

### CID_OFF


:::warning
This will add support for all SD cards for maps

:::


:::info
Select folder below based on your FW train version `02xx`, `03xx`, `04xx`.

:::

Copy `/nav/` folder from `/CID xXX/nav/` to `_patch_template/cpu/onlineservices/1/default/tsd/etc/`.

`mibstd2_nav_target.ini` is already changed to support all SD cards.


:::info
Run HashesGenerator.exe now!

:::

## Signing with HashesGenerator.exe


:::warning
Do this only once at the end, when all patches you need are prepared.

:::

After you have built your custom patches files have to be "signed" with the "HashesGenerator.exe" which is stored in `_patch_template/cpu/onlineservices/1/default`. It will generate the correct `hashes.txt` so that all files are accepted by FW update process.

# Installing the patch from SD via FW update


1. Insert SD card into SD slot of the unit
2. Press and hold `MENU` button for 3 seconds to enter `Service menu` video.
3. Go to `Software update/versions` →  `Update` → continue with the installation