# Updating maps

The latest **available** EU maps is **P106_N60S3MIBS2_EU_NT.7z**\nContent of **DBInfo.txt** file on SD:

```
PartNumber1="V03959803RQ"
PartNumber="V03959803RQ"
ApplicationSoftwareVersionNumber="0106"
SystemName="ECE 2023"
```


:::info
To fit P106 maps version onto 8Gb SD card, delete some not needed \*.psf countries

Maps work from original FAT32 formatted 8Gb SD card having special CID and are NOT copied into internal memory of the unit.

It is confirmed that P106_N60S3MIBS2_EU_NT maps work on **MSTD_EU_SE_P5310** from original SD card without installing any FEC! ![](attachments/f158afbe-76a2-46ae-92f2-f465f26c04da.png " =36x45")

:::

## Understanding original SD card and FEC protection

To use the maps you need:


1. Original 8Gb FAT32 SD card with special [CID](https://www.cameramemoryspeed.com/sd-memory-card-faq/reading-sd-card-cid-serial-psn-internal-numbers/) `0941504d49425354102d702df000d700` cards for MST2 Delphi/Technisat can be used too.

   
:::info
   There are following known ways to pass the CID check:\na. Find some old Samsung EVO/EVO+ SD card and change the CID like described [here](http://www.strihanividea.cz/procedure.txt).\nb. Order "Custom CID" SD card from AliExpress. Note: those cards are low quality and die soon.

   c. Patch CID check (**"**MIBST" PNM) in CPU_HMI.EXE. 

   :::
2. To have FECs 00040100 (Navigation) and 022000ee (lifetime EU maps) as **allowed** in "**Activation keys**" of [RED menu](/General information/Audi MMI key combinations/):

    ![](attachments/06871fe1-e28b-44c0-8cdf-6afd1c9c3aef.png)

   
:::info
   You can install [Actvator by Enthusiast](https://mibwiki.one/doc/activator-by-enthusiast-RK36Mez8aJ) to enable all FECs

   :::

   `MSTD_*` firmwares check every \*.psf file in **\\markets\\eu\\map\\MapRegions\\** folder on the maps SD. 

   
:::warning
   Looking at the end of `*.psf`files of P106_N60S3MIBS2_EU_NT maps, you can see that on Audi, Activation key (FEC) `02200030` or higher is required.\n ![](attachments/3b80989e-721c-46e4-a6f9-f77a5d929843.png)

   :::


\