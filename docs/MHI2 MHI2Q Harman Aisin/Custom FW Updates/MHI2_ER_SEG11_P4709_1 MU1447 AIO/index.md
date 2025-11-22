# MHI2_ER_SEG11_P4709_1 MU1447 AIO

# MHI2_ER_SEG11_P4709_1 MU1447 AIO


:::info
Custom all-in-one FW update based on [metainfo2 exploit](/MHI2 MHI2Q Harman Aisin/unsorted - testing only/metainfo2.txt exploit/).

:::

## Requirements

* Seat with MIB2 High system
* quality SD card, `16GB` capacity or more ([how to check SD card](/General information/Bench Setup & Tools/SD card testing/)),
* Update package (download: [https://mibsolution.one/?module=fileman&section=do&page=download&paths\[\]=%2FROOT%2F1%2F9%2FMHI2%20-%20HARMAN%2FFirmware%2FSeat%2FMHI2_ER_SEG11_P4709_1_AIO_MU1447_20230320.7z](https://mibsolution.one/?module=fileman&section=do&page=download&paths%5B%5D=%2FROOT%2F1%2F9%2FMHI2%20-%20HARMAN%2FFirmware%2FSeat%2FMHI2_ER_SEG11_P4709_1_AIO_MU1447_20230320.7z)).
* [https://mibsolution.one/#/1/9/MHI2 - HARMAN/Firmware/Seat](https://mibsolution.one/#/1/9/MHI2%20-%20HARMAN/Firmware/Seat)
* Check for more info: <https://github.com/harman-f/MHI2_MIB2_AIO_FW_Update_Template/wiki/AIO-installation>

## How to install

### Fully automated FW update


:::info
With this new method you ony have to place the created SD card in unit and reboot unit via key combination.

Installation will automatically start after reboot of unit.

Check more [key combinations and shortcuts](/General information/Useful documents/Key combinations and shortcuts/).

:::

`Swdlautorun.txt` in root will trigger an automatic installation of M.I.B without further user interaction.

This function is deactivated by default. To enable automatic install rename `_Swdlautorun.txt` to `Swdlautorun.txt`

### Manual FW update


1. Format SD card with `FAT32` file system.
2. Extract the content of All-In-One package to the root directory of SD card.
3. Turn the ignition on, wait for the infotainment system to boot up.


:::warning
Make sure that the car key will not leave the vehicle during the firmware update procedure (learn more about [Kessy and updates](/General information/Kessy & Updates/)).

:::


4. Restore factory settings in system settings.
5. Place SD card in `SD 1` port.
6. Press and hold `MENU` button to enter Service Menu.


:::info
Check more [key combinations and shortcuts](/General information/Useful documents/Key combinations and shortcuts/).

:::


6. Go to `Software update/Versions` → `Update` → `SD 1`.
7. Wait for the update to be installed. It will take some time, the system will reboot couple times during firmware update procedure.


:::warning
If you are stuck in bootscreen for a long time, check [this information](/MHI2 MHI2Q Harman Aisin/Conversion & Cross-flashing/FW Update - SWDL/error - Stuck or Freeze in (old) Bootscreen after update/).

:::

## Features


1. Patched IFS-Root (FEC & CP patch) will be used during the installation.
2. FecContainer will be adjusted with missing FECs during the installation including code for latest maps (`073000EE`).


:::tip
`addFecs.txt` in `/common/tools/` can be adjusted as needed. Change add FECS with e.g. notepad.

:::


 3. Skin 4 (Carbon) will be configured during install to avoid boot up issues
 4. Screening 1 will be configured during install to avoid boot up issues.
 5. CarPlay and AndroidAuto will be enabled during the installation.
 6. Developer Mode with GEM (hidden Green Engineering Menu) will be enabled during the installation. No need for `OBDeleven`, `VCDS`, `VCP`.
 7. RadioStationDB `01.20.20 2020608`
 8. GraceNote `EU V21 - RW V13`
 9. M.I.B. - More Incredible Bash will be installed.
10. Fully automated FW install after reboot

**Version:** `20220627`

### Screen - manual install

 ![](attachments/7d275af9-e206-4233-8033-68d07cb44180.png)

 ![](attachments/0e294f6a-4982-40ee-b9dc-dcd70bcbfcd8.png)

 ![](attachments/cc66e94e-80a6-4d31-a7b4-7c795e3b8478.png)

 ![](attachments/03df9fa7-ed7f-41aa-8942-22fe1fa2835f.png)

 ![](attachments/e8fcea44-e047-423c-888e-e919bf01a923.png)