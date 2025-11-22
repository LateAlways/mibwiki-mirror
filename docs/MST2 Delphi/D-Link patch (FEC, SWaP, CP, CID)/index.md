# D-Link patch (FEC, SWaP, CP, CID)

:::info
Thanks to -XTR3M3- for creating the base for this how to and Yalmac for translation. This article is based on this work, but not linked in any way directly to the original author.

:::


:::warning
Patch files are different for each FW version. Make sure that you use the correct patch files for your unit.

:::


:::success
Before reading this,  check SD Activator by Congo & Duke. 

:::

| SWaP patch for | CP off patch for |
|----|:---:|
|    | MST2_US_AU_P0504D |
| MST2_EU_AU_P0673D |    |
|    | MST2_EU_AU_P0840D |
|    | MST2_EU_AU_P0962D |
| MST2_EU_VW_P0213D | MST2_EU_VW_P0213D |
| MST2_EU_VW_P0225D |    |
| MST2_EU_VW_P0227D |    |
| MST2_EU_VW_P0231D | MST2_EU_VW_P0231D |
|    | MST2_EU_VW_P0624D |
| MST2_EU_VW_P0628D |    |
| MST2_EU_VW_P0635D | MST2_EU_VW_P0635D |
| MST2_EU_VW_P0640D | MST2_EU_VW_P0640D |
| MST2_EU_VW_P0642D | MST2_EU_VW_P0642D |
|    | MST2_EU_VW_P0757D |
| MST2_EU_VW_P0867D | MST2_EU_VW_P0867D |
| MST2_EU_VW_P0870D |    |
| MST2_EU_VW_P0876D | MST2_EU_VW_P0876D |
| MST2_EU_VW_P0879D | MST2_EU_VW_P0879D |
| MST2_EU_VW_P0891D | MST2_EU_VW_P0891D |
| MST2_EU_VW_P9122D |    |
| MST2_US_VW_P0635D |    |
| MST2_US_VW_P0867D |    |
| MST2_US_VW_P0879D |    |

## **How do I recognize a MST2 Delphi Unit?**

* Delphi Units are always standard devices (`MST2`) and not high (`MHI2`) devices.
* Accordingly, a Delphi unit is always a **MIB2 Discover Media** or **MIB2 Composition Media** and not a Discover Pro type unit.
* __All__ Delphi Units are Discover Media or Composition Media devices. But __not__ all Discover Media and Composition Media devices are Delphi Units! It can also be a Technisat/Preh unit.
* To recognize the unit without removal, it is necessary to hold down the MENU button on the radio for 3 seconds to open hidden service mode. In this menu go to `Software Update/Versions` and check `SW Train`.

  \
   ![Service mode available after holding MENU button for 3 seconds.](attachments/731125ca-a3ae-4b6c-a580-69a90bd843e0.png)                                          ![SW Train example with European Volkswagen firmware.](attachments/73723d74-4ee7-4501-bd99-a6bdc6de93aa.png)
* Delphi SW Train Version scheme example: `MST2_EU_VW_P0891D`.

  \n

 ![](attachments/805a2f34-a588-4dc7-b230-2af158022906.png " =244x38")

 ![](attachments/83405590-6e06-4d6a-9949-9f381002fd5b.png)


 ![Delphi SW Train Scheme](attachments/0c0ef38b-8204-48c2-8355-7b8d9c80da75.png)



:::info
If there is a D at the end of your SW Train version, you have a Delphi Unit.

:::


:::tip
If you see a `PQ` or `ZR` after the vehicle brand or a `T` at the end in your SW Train version, then you have a [Technisat Preh Unit.](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/FW patch overview - newest available FW, Online approval SD Patch possibility/02xx to 04xx firmware update/)

:::

## Requirements - What do you need?

* Delphi MST2 unit,
* Diagnostic tool to enable Developer Mode (`VCDS`, `VCP`, `OBD11`…),
* Quality SD card (how to test SD card),
* Ethernet-USB adapter supported by the unit ([D-Link DUB-E100](/General information/Bench Setup & Tools/D-Link DUB-100 Ver. D1 - 0x2001, 0x1a02/) or alternative),
* Ethernet cable,
* Patch files from mibsolution.one.

## Network settings

 ![](attachments/9c872184-f400-4c76-a01b-6cb3a76495fe.png)

 ![](attachments/20bed7c2-72a1-4e96-aa5a-dbdebb2ffccc.png)

 ![](attachments/44d85952-bf29-4c23-abb9-6db6b44a3117.png " =296x337")

## Software-Version


:::info
The patch files are different for each SW-Train and software version! \n Therefore, make sure that you use the right patch files for your unit!

:::


:::warning
If you use the wrong patch files, you will brick your unit in the worst case!

:::


:::info
In addition to the SW-Train mentioned in the first section, there is also the software version, which can be read at the end of the same menu item.

:::

 ![](attachments/0c4facc7-8828-4032-83bf-f487b436a2aa.png)

## Activate Developer mode and GEM

Activate the Green Engineering Menu (GEM) with `VCDS`, `OBDEleven`, `VCP`, or any other diagnostic interface.

Check: [5F - Enabling Developer Mode and Hidden Menu](/MQB CODING/5F - Enabling Developer Mode and Hidden Menu/) for more details.

# Update FW


:::info
Train\*\*~~In the~~ `~~08xx~~` ~~series, the firmware updates have not always been released ascending order.~~

~~The~~ `~~0891~~` ~~is not the latest firmware, but~~ `~~0879~~` ~~is!~~

:::

~~P9122D (MU0842) ➔ P0867D (MU0867) \* ➔ P0890D (MU0890) ➔ P0891D (MU0891) ➔ P0876D (MU0876) \* ➔ P0879D (MU0879) \*\*~~

\* = Telnet is not activated on this FW

\*\*= there is a modified firmware (**MST2_EU_VW_P0879D-wTelnet**) on the mibsolution.one server **with** telnet activated. Read in the folder oft this FW: patch\\howto.txt !!!


:::tip
Downgrade/upgrade to a version supporting **telnet** and or having an **available patch**

:::

## Run FW update


1. Format SD card to FAT32.
2. Copy firmware update files to the SD card.
3. Insert the SD card into the SD card slot 1.
4. Remove all other SD cards and USB devices!
5. Press the MENU button on the radio longer until another (service) menu opens. Select the test mode there.

    ![](attachments/775f4134-1c54-461d-a606-38d85db6f4b1.png)
6. Switch to the "SWDL" category.

    ![](attachments/327f9c3a-bb45-47bd-bf1d-9408ce878891.png)
7. Activate Software Download Manual Download and tap "Start Download".

    ![](attachments/6441ca2d-f584-49d3-ae33-4523214aeff9.png)
8. Select source (SD card), select everything and start firmware update.

    ![](attachments/6bec0955-597d-4bce-9452-4333a2eb8174.png)


:::warning
What should be considered when updating the firmware?

•	Leave the ignition on

•	Turn off unnecessary consumers (lights, ventilation, ...)

•	Connect charger(at least  15A charging power, better 20A and more)

•	Depending on the unit (RAM/CPU), the update takes 20 to 60 minutes

:::

## Fix Software Version Management (SVM) error

Use VCDS / OBDEleven / VCP to clear the erroro from unit.

# TELNET Connection


:::tip
Ethernet must be activated in GEM to enable telnet access.

:::

## Enable ethernet

Hold down the MENU button on the radio until the Service menu appears.

Navigate to `Testmode`


 ![](attachments/82eccf29-8c19-4bf5-aeaa-6425077e9118.png)

Select `Green Engineering Menu`

(optionally you can also get there directly by pressing the MENU button for a very long time)

 ![](attachments/beeab519-370e-452b-a7da-ee08451035ad.png)

Change to the category "debugging mlp"

 ![](attachments/2aee805a-8803-4d80-8ea4-daa339f88b27.png)

Check `Ethernet` box and restart the unit (hold down the power button for at least 10 seconds)

 ![](attachments/051a4c9d-210d-425e-9062-cb724b4bcc03.png)

After the unit has been restarted enter same menu again and also check `Switch to MLP` must be checked. (Note: If only removing CP, it does not seem MLP needs to be selected 8/7/2023)

 ![](attachments/9c514631-8649-43c4-babe-bd13518cfe14.png)

## Connect with Putty - Telnet

Now the USB-LAN adapter can be connected to the USB port in the vehicle and connected to the laptop via LAN cable. If the LEDs othe adapter light up, if the cabling and network configuration on your PC/notebook are correct.


Putty can now be started.


\
The IP address is taken from the GEM menu `debugging mlp`.

IP `192.168.1.4`  and port `23` are default on all units.

 ![Click open to connect to unit](attachments/77c2892a-2f95-43ed-8102-e8c788774938.png)

If everything has been configured correctly, you can tell from the QNX Neutrino login message that it worked.

Only the word `root` (NO password) is required as a login to Delphi units.

 ![](attachments/d8d8a43d-a8f5-413f-8c2f-ecd1d061d3b6.png)

As soon as `Welcome` is shown, commands can be entered.

 ![](attachments/619b37b2-9a1d-4308-96b3-73ea1d2ed588.png)

# Patch unit

## Common shell commands:

* `cp`  = copy
* `rm`  = delete
* `chmod`  = change rights (e.B. chmod  777  = full read/write permissions)
* `mkdir`  = create directory (folder)
* `mount` = mount path
* `umount` = unmount path
* `&&`  = execute another command


Attributes:

* `-f`  =  force  (overwrite / force)
* `-R` = recursive (e.B. copy/delete folder including contents and subfolders)
* `-t`  = mount request / special type (e.B followed by  qnx6)
* `-u` = update (remount)
* `-V` = progress indicator
* `-w` = read/write permissions (when mounting)


## Create backup - **recommended**


:::warning
It is important to create a backup before starting to patch!

:::

Insert empty the SD card into `SD 1` port and execute the following commands via putty.

Enter the commands exactly!

Unintentionally set spaces can lead to bricking of the unit!

This note is especially relevant for users who use a translator because they partially insert unwanted spaces.

### Manual input


 1. Mount SD card

    `cd / && mount -uw /sdc1/`
 2. Create backup folders on the SD card

    `mkdir /sdc1/backup/`
 3. Securing FEC Containers

    `cp -VRf /persistence/SWaP/* /sdc1/backup/`
 4. Save ifs

    `cp -Vf /extbin/apps/bin/delphibin.ifs /sdc1/backup/delphibin.ifs`
 5. Back up the installation manager

    `cp -Vf /ffs/sbin/InstallationManager /sdc1/backup/InstallationManager`
 6. Save profiles

    `cp -Vf /ffs/etc/profile /sdc1/backup/profile`
 7. Save Config

    `cp -Vf /extbin/apps/cfg/MHConfig.cfg /sdc1/backup/MHConfig.cfg`
 8. Back up fs0

    `cat /dev/fs0 > /sdc1/backup/fs0`
 9. Save Unit Info

    `APUpdateLight -i >> /sdc1/backup/unit_info.txt`
10. Save eMMC serial number

    `sdtool emmc info >> /sdc1/backup/emmc_serial_number.txt`


### Script version

This script has to be copied to SD card and executed by typing \n `cd / && /sdc1/MST2_backup.sh`


```bash
#!/bin/sh

echo "ROOT access - OK"
cd / && mount -uw /sdc1/; sleep 1

echo "Making backup dir on SD Card - OK"
mkdir /sdc1/backup/; sleep 1

echo "SWaP *.fec files backup - OK"
cp -Rf /persistence/SWaP/* /sdc1/backup/; sleep 1

echo "backup /ffs/etc/* - OK"
cp -Rf /ffs/etc/* /sdc1/backup/; sleep 1

echo "delphibin.ifs backup - OK"
cp -f /extbin/apps/bin/delphibin.ifs /sdc1/backup/delphibin.ifs; sleep 1

echo "InstallationManager backup - OK"
cp -f /ffs/sbin/InstallationManager /sdc1/backup/InstallationManager; sleep 1

echo "SWaP engine backup - OK"
umount -f /persistence && mkdir /home/mmc0t180_tmp && mount -t qnx6 /dev/mmc0t180 /home/mmc0t180_tmp && cp -Rf /home/mmc0t180_tmp/SWaP/* /sdc1/* && umount -f /home/mmc0t180_tmp && rm -R /home/mmc0t180_tmp; sleep 1

echo "profile backup - OK"
cp -f /ffs/etc/profile /sdc1/backup/profile; sleep 1

echo "MHConfig.cfg backup - OK"
cp -f /extbin/apps/cfg/MHConfig.cfg /sdc1/backup/MHConfig.cfg; sleep 1

echo "fs0 backup - OK"
cat /dev/fs0 > /sdc1/backup/fs0; sleep 1

echo "Saving unit info to file - OK"
APUpdateLight -i >> /sdc1/backup/unit_info.txt; sleep 1

echo "emmc serial numbler - SAVED"
sdtool emmc info >> /sdc1/backup/emmc_serial_number.txt; sleep 1

echo "FINISHED - You can now remove SD Card"
```


## SWaP (FEC) patch


:::info
**This patch is required to disable the verification of the signature of the FEC containers.** \n [Open MIB2 Delphi FEC Generator ](https://www.digital-eliteboard.com/threads/mib2-delphi-fec-generator-by-xtr3m3.495976/) by  XTR3M3 and select the appropriate featureenablecodes as desiredand thencreate/save the FEC container (right button). The VCNR and VIN can either be entered manually or imported from an existing (backup) FEC container.

:::


 ![](attachments/ebc8aa25-ee68-4042-9af1-f07ad31d29fe.png)

However, an already patched FEC container can also be easily changed with your VCNR and FIN.

This `*.fec`  file and patched  `SWaP`  will be copied to SD card and insert it into slot 1 of the unit.


First, the patched  SWaP file is copied to unit.


:::warning
Enter the commands exactly! Unintentionally set spaces can lead to bricking  of the unit! This note is  especially  relevant for users who use a translator because they partially insert unwanted spaces.

:::

### MST2_patch.sh - manual input


1. SD card mount

   `cd / && mount -uw /sdc1/`
2. Temporarily mount path and copy SWaP  file

   ```bash
   umount -f /extbin && mkdir /home/mmc0t177_tmp && mount -t qnx6 /dev/mmc0t177 /home/mmc0t177_tmp && cp -VRf /sdc1/SWaP /home/mmc0t177_tmp/apps/bin/ && chmod 777 /home/mmc0t177_tmp/apps/bin/SWaP
   ```
3. Temporary path unmount

   `umount -f /home/mmc0t177_tmp`
4. Delete temporary path

   `rm -R /home/mmc0t177_tmp`


### MST2_patch.sh - script version

This script has to be copied to SD card and executed by typing \n `cd / && /sdc1/MST2_patch.sh`


```bash
#!/bin/sh

echo "ROOT access - OK"
cd / && mount -uw /sdc1/;  sleep 1

echo "SWaP patch - OK"
umount -f /extbin && mkdir /home/mmc0t177_tmp && mount -t qnx6 /dev/mmc0t177 /home/mmc0t177_tmp && cp -VRf /sdc1/SWaP /home/mmc0t177_tmp/apps/bin/ && chmod 777 /home/mmc0t177_tmp/apps/bin/SWaP;  sleep 1

echo "Unmounting TEMP directory - OK"
umount -f /home/mmc0t177_tmp;  sleep 1

echo "Deleting TEMP directory - OK"
rm -R /home/mmc0t177_tmp;  sleep 1

echo "FINISHED - You can now remove SD Card"
```



:::info
Restart unit by long pressing the power button. \n A reboot can be seen by the boot logo and short-term loud fan noises

:::


---


:::info
Now the patched FEC container is copied to unit.

:::


:::warning
Enter the commands exactly! Unintentionally set spaces can lead to bricking  of the unit! This note is especially relevant for users who use a translator because they partially insert unwanted spaces.

:::

### MST2_fec.sh - manual input


1. SD card mount

   `cd / && mount -uw  /sdc1/`
2. Temporary path mount

   `umount -f /persistence && mkdir /home/mmc0t180_tmp && mount -t qnx6 /dev/mmc0t180 /home/mmc0t180_tmp`
3. Delete original FEC Container

   `rm -Vf /home/mmc0t180_tmp/SWaP/pg/*.fec`
4. Copy patched FEC Container

   `cp -Vrf /sdc1/*.fec /home/mmc0t180_tmp/SWaP/pg/`
5. Temporary path unmount

   `umount -f /home/mmc0t180_tmp`
6. Delete temporary path

   `rm -R /home/mmc0t180_tmp`


### MST2_fec.sh - script version

This script has to be copied to SD card and executed by typing

`cd / && /sdc1/MST2_fec.sh`

```bash
#!/bin/sh

echo "ROOT access - OK"
cd / && mount -uw /sdc1/;  sleep 1

echo "Mounting"
umount -f /persistence && mkdir /home/mmc0t180_tmp && mount -t qnx6 /dev/mmc0t180 /home/mmc0t180_tmp;  sleep 1

echo "Moving old *. FEC to ILLEGAL - OK"
cp -Vrf /home/mmc0t180_tmp/SWaP/pg/*.fec /home/mmc0t180_tmp/SWaP/illegal/;  sleep 1

echo "Removing old *. FEC - OK"
rm -f /home/mmc0t180_tmp/SWaP/pg/*;  sleep 1

echo "Installing new *. FEC - OK"
cp -Vrf /sdc1/*.fec /home/mmc0t180_tmp/SWaP/new;  sleep 1

echo "Unmounting TEMP directory - OK"
umount -f /home/mmc0t180_tmp;  sleep 1

echo "Deleting TEMP directory - OK"
rm -R /home/mmc0t180_tmp;  sleep 1

echo "FINISHED - You can now remove SD Card"
```

## Config (CID) patch


:::info
**This patch disables SD card check for navigation (aftermarket SD cards).**

:::


:::warning
Enter the commands exactly! Unintentionally set spaces can lead to bricking  of the unit! This note is  especially relevant for users who use a translator because it can insert unwanted spaces into the translated text..

:::

This script can be copied to SD card or just executed by typing

```bash
grep -v "MIBST" /extbin/apps/cfg/MHConfig.cfg > /tmp/MHConfig.cfg && cp /tmp/MHConfig.cfg /extbin/apps/cfg/MHConfig.cfg && sync
```

## delphibin.ifs (CP) patch


:::info
**This patch disables component protection check**

:::


:::warning
Enter the commands exactly! Unintentionally set spaces can lead to bricking  of the unit! This note is  especially relevant for users who use a translator because it can insert unwanted spaces into the translated text.

:::


1. Copy patched `delphibin.ifs` that corresponds to Train and unit type onto the root of SD card
2. Insert SD card into `SD 1` slot of the unit.
3. Create backup of the original `delphibin.ifs`: \n `cp -Vfr /extbin/apps/bin/delphibin.ifs /sdc1/backup_delphibin.ifs`
4. Copy patched `delphibin.ifs`to the head unit: \n cp -Vfr /sdc1/delphibin.ifs /extbin/apps/bin/delphibin.ifs
5. Sync file system:

   `MountPathSync /extbin/apps`
6. Restart the unit

   `shutdown -S reboot`

# [FEC Generator](https://www.digital-eliteboard.com/threads/mib2-delphi-fec-generator-by-xtr3m3.495976/)

 ![](attachments/523b3a29-5274-4af4-9aa2-3b7d80ceb25f.png)

# References

[DEB - \[HOW TO\] MIB2/MST2 Delphi Unit (MST2_VW_xxxxxD) patchen \[FEC/SWAP/CID/CP\]](https://www.digital-eliteboard.com/threads/how-to-mib2-mst2-delphi-unit-mst2_vw_xxxxxd-patchen-fec-swap-cid-cp.495796/)

**DEB-en**  <https://www-digital--eliteboard-com.translate.goog/threads/how-to-mib2-mst2-delphi-unit-mst2_eu_vw_xxxxxd-patchen-fec-swap-cid-cp.495796/?_x_tr_sl=de&_x_tr_tl=en&_x_tr_hl=de&_x_tr_pto=wapp>

[DEB - MIB2/MST2 Delphi Patches (CP Off + SWaP)](https://www.digital-eliteboard.com/threads/mib2-mst2-delphi-patches-cp-off-swap.501808/)

[DEB - MIB2 Delphi FEC Generator by XTR3M3](https://www.digital-eliteboard.com/threads/mib2-delphi-fec-generator-by-xtr3m3.495976/)