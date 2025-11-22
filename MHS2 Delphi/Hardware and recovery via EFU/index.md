# Hardware and recovery via EFU

![](attachments/e52668c6-b7dd-46eb-95c5-209ae9237d16.png)

Label of chinese Audi MMI with train MHS2_CN_AU_P1615

 ![](attachments/dfcad070-1f11-44cc-9dfe-4b7edc872100.png)


:::info
**GOOD TO KNOW:** Trains MHS2_US_AU_P01\*, MHS2_US_AU_K01\*, MHS2_EU_AU_P01\*, MHS2_EU_AU_K01\*, MHS2_CN_AU_P08\*, MHS2_CN_AU_K08\*, MHS2_CN_AU_P12\*, MHS2_CN_AU_K12\*, MHS2_CN_AU_P16\*, MHS2_CN_AU_K16\* do not support Radio Logo and Gracenote2 DBs

:::

MMX chip located on top of the board. 64Mb NOR is mounted at `/net/mmx/fs/dev/fs0`

and partitioned like:

```
/dev/fs0p1                  1.8M      1.1M      728K      63%  /mnt/system
/dev/fs0p2                  7.8M      1.1M      6.7M      15%  /mnt/persist
```

NAND size is 15Gb

`/dev/mnand0                  15G       15G         0     100%`

partitioned like:

```
/dev/mnand0t177             972M      694M      278M      72%  /mnt/app/
/dev/mnand0t178            1024M      113M      911M      12%  /mnt/boardbook/
/dev/mnand0t179             3.0G      102M      2.9G       4%  /mnt/ota/
/dev/mnand0t178.1           2.4G      2.0G      505M      81%  /mnt/speech/
/dev/mnand0t178.2            64M      2.7M       61M       5%  /mnt/gracenotedb
/dev/mnand0t178.3           256M      4.2M      252M       2%  /mnt/mmebackup/
/dev/mnand0t178.4          1024M       47M      977M       5%  /mnt/icab/
/dev/mnand0t178.5           1.4G       28M      1.4G       2%  /mnt/adb/
/dev/mnand0t178.6          1024M       46M      978M       5%  /mnt/gecache/
/dev/mnand0t178.7          1024M       20M     1004M       2%  /mnt/ols/
/dev/mnand0t178.8           1.6G       58M      1.6G       4%  /mnt/navdb/
/dev/mnand0t178.9            64M      3.2M       61M       6%  /mnt/media/
```

` `      ![Top of the MMX board: nVidia_Tegra2(T30), MMX NOR 64Mb or 128Mb, NAND 15Gb](attachments/bd39cb61-6e0e-49df-87a6-1a2eeadc5974.png)

RCC  (Jacinto 5e) on the bottom. 64Mb (EU units) or 128Mb (US units) NOR is mounted at **/net/rcc/fs/dev/fs0**:

 ![](attachments/3e5c6221-77d9-4c53-b6ea-196d88ea51bd.png)

To start EFU (Emergency Flash Utility), connect to MMX via quadlock, press and hold E on the keyboard and power on the unit via quadlock:

```
 <.STARTUP>
<cpu>: nVidia Quickboot 17.54 (Build Feb 19 2018)
<cpu>: modified by e.Solutions GmbH
<cpu>: Loading stage 2 primary bootloader...
<cpu>: Stage2 loaded
<cpu>: Trying to load kernel 8
<cpu>: Press <E> to run Emergency Flash Utility.
<cpu>: Error reading status register (0x2)
<cpu>: jumping to kernel
VFPv3: fpsid=41033094
coproc_attach(10): attach fe074cd0 (fe076ca4)
coproc_attach(11): attach fe074cd0 (fe076ca4)
Starting i2c interface for PMU
Starting devg-nvpower
Starting /usr/sbin/startup.sh ...
[OOC.Main] INFO: Version 2.2.1-RELEASE
[OOC.Main] INFO: ESO common libs version 4.5.2
[OOC.TimerGroup] INFO: Timer group thread started
[OOC.TimerGroup] INFO: Timer thread started
[ResMgrI2C.I2cIoc] INFO: I2C slave thread started
[OOC.SdisWlan] INFO: fsm:sdis_wlan_start_thread
```

Then EFU starts:

 ![](attachments/6be7ec3e-9cbc-4313-bb79-66a555e89db1.png)

and in the log you may see something like:

 ![](attachments/37f32390-22a0-4270-b4a8-90f964f4dda8.png)

**GOOD TO KNOW:** When primary partition is corrupted then EFU starts directly:

 ![](attachments/6baefbf9-9a4c-4ff0-b242-d2b4a4dc8108.png)

Insert stock MHS2 firmware on **FAT32** formatted SD card into SD1 slot and EFU will automatically start flashing.


:::info
**IMPORTANT!** To prevent automatic shutdown of the unit, press DVD eject button. It will stop watchdog timer.

:::

 ![](attachments/23c3d30e-c20a-498b-9c5e-c771877e8181.png) ![](attachments/fc9941c5-b15a-436a-8d36-d35c951c06bf.png) ![](attachments/5004c676-fa94-4468-8887-ac75f306c6ac.png) ![](attachments/b1b30d3b-0d62-4ad7-b299-8f3b6cac721f.png) ![](attachments/ddce75b2-5ab6-4c04-ba31-268193224b79.png) ![](attachments/e9d53ea0-b437-4148-a2c0-b6de96317e2e.png)