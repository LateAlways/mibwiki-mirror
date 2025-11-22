# MHI2_ER_AU57x_K3663_1 MU1425 AIO

:::info
Custom all-in-one FW update based on [metainfo2 exploit](/MHI2 MHI2Q Harman Aisin/unsorted - testing only/metainfo2.txt exploit/).

:::


:::warning
Read all before updating.

:::


:::tip
Last update March 30 2022

:::

## Requirements

* Audi with MMI MIB2 system (any `MHI2_ER_AUG11` or `MHI2_ER_AU57x`),
* quality SD card, `16GB` capacity or more ([how to check SD card](/General information/Bench Setup & Tools/SD card testing/)),
* Update package (download: <https://mibsolution.one/au_3663_aio>).

## How to install


1. Format SD card with `FAT32` file system.
2. Extract the content of All-In-One package to the root directory of SD card.
3. Turn the ignition on, wait for the Audi MMI system to boot up.


:::warning
Make sure that the car key will not leave the vehicle during the firmware update procedure (learn more about [Kessy and updates](/General information/Kessy & Updates/)).

:::


4. Restore factory settings by going to `MENU` → `Setup MMI` → `Factory Settings` → `Select all entries` → `Restore factory settings`.
5. Wait for about 20 seconds for the factory settings to be done.
6. Place SD card in `SD 1` port.
7. Press and hold `BACK` + `TOP-LEFT` to enter REM (hidden Red Engineering Menu).


:::info
Check how to do it in your car with [Audi MIB2 key combinations](/General information/Audi MMI key combinations/).

:::


6. Go to `Update` → `SD 1` → `Standard`.
7. Scroll down to the end of the list and select `Start update` → `Start`.
8. Wait for the update to be installed. It will take some time, the system will reboot couple times during firmware update procedure. Screen can stay off or stuck on Audi logo for several seconds. Be patient and wait. In my case it took 34 minutes to go from old `S0037` to new `K3663`.

## Video tutorial

[https://youtu.be/VS21Lyess7o](https://youtu.be/VS21Lyess7o)

## Features


1. All in one update from any `MHI2_ER_AUG11` or `MHI2_ER_AU57x` firmware directly to `MHI2_ER_AU57x_K3663_1`. No need to manually edit EEPROM. No need to disable or loop MOST.
2. Developer Mode with GEM (hidden Green Engineering Menu) will be enabled during the installation. No need for `OBDeleven`, `VCDS`, `VCP`.
3. Patched IFS-Root (FEC & CP patch) will be used during the installation.
4. FecContainer will be adjusted with missing FECs (`00040100`, `00050000`, `00070200`, `00030000`, `023000EE`, `00060800`, `00060900`) during the installation.
5. CarPlay and AndroidAuto will be enabled during the installation.
6. GraceNote2 `v21` will be installed.
7. Fix for rear control head error after update from `P0040` or older.

## Bose Sound System & B&O update

**Standard is not including BOSE and B&O update.**

By default this procedure will not update Bose amplifier. `metainfo2.txt` was prepared to skip this component, because updated amplifier will required parametrization which must be done with VCP or ODIS.


:::warning
Without the parametrization you will have no sound.

:::

If you wish to update Bose you can use different `metainfo2.txt` to do it.


1. Remove `metainfo2.txt` from both `/1/` and `/2/` directories.
2. Rename `metainfo2-Bose-BO.txt` to `metainfo2.txt` in both `/1/` and `/2/` directories.
3. Run the update from red engineering menu.
4. Perform parametrization afterwards.

 ![rename metainfo2-Bose.txt to metainfo2.txt if you want to enable BOSE update](attachments/031e5730-483b-4df5-bafa-530538ed88e6.png)

## SVM

If you have access to official SVM (ODIS/Geko) you can use that with SVM code MHI2ER3663.

On older models with stock - before you updated to 3663 - 00xx and 2xxx versions firmwares you can use the "Downgrade" update in the `K3663-to-K2589-Downgrade-SVM(MHI2ER2589).7z` archive.

This will downgrade all needed modules - BUT will leave 3663 on unit -  to be able to pass SVM with code MHI2ER2589, all activations and features remain.

After SVM you will have to enable Carplay and AA again in adaptions! Use e.g. M.I.B to reactivate them.

Unit will get new Calibration from SVM, FECs should remain.