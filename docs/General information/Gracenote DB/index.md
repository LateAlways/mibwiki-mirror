# Gracenote DB

:::info
Gracenote2 is an algorithm that uses ID of the played CD/DVD or file to read the artist metadata, cover art, music genre, mood information, descriptions, episode information etc. from Gracenote2 database and makes the media player to display it.

:::

The latest Gracenote2 DB version for MHI2/MHI2Q/MHS2/MH2p/MHI3/MPR3 units can be found on mibsolution.one


**MHI2/MHI2Q/MHS2** use 170x170 pixel logos, so use "**MQB_Solution/MHI2 — HARMAN/Gracenote"** folder. There are two versions:

* **Gracenote2 EU V23-0010-1.1.1.2934-20230223.7z (2022 database for EU region only)**
* [GN2_gdb-EU-v24-0010-1.1.1.3119-20231019.zip](https://mega.nz/file/I85jiTaA#_O9j1BLcGZMqdeMefJ_P2JsvR9vdwPPx11-xZWTWaTw) **(2023 database for EU region only)**
* **Gracenote2_AIO_payload.7z (older version but for both EU & RW region)**

These packages contain metainfo2.txt and can be installed on MHI2/MHI2Q like regular software updates. For MHS2 you need to use MHS2 Toolbox.


**MH2p/MHI3/MPR3** use 300x300 pixel logos, so use "**MQB_Solution>MH2P - ALPINE>Gracenote" folder.**  There is **mh2p_mhi3_mpr3_gdb-EU-0010-1.1.1.2679-20220316.7z** which you need to install with a toolbox or manually in putty.



:::success
**GOOD TO KNOW!** BMW **MGU** navi units use the same Gracenote2 DB format but get updates more frequently than MHI2/MHI2Q/MHS2/MH2p/MHI3/MPR3 units. To use BMW MGU Gracenote2 DB on MHI2/MHI2Q/MHS2 you need to convert 300x300 images in DB to 170x170 images.

:::

Comparison of BMW and VAG gdb_info in [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

| BMW MGU type | **MHI2/MHI2Q/MHS2** |
|----|----|
|  ![Gracenote-DB for MGU 03-2022 Europe_ENTD_000055EB_003_022_003](attachments/c7734de4-7cb6-4654-b50d-8cc0e2032e35.png) |  ![V21](attachments/7cf2db39-41b1-42ef-8ab4-eeb70e0fb4b6.png) |

# BMW MGU type download sources:

## EU:

<https://f30.bimmerpost.com/forums/showthread.php?t=795170&page=35> <https://cartechnology.co.uk/showthread.php?tid=64015&highlight=gracenote>

## US/ROW and others:

<https://f30.bimmerpost.com/forums/showpost.php?p=29189530&postcount=1189>

Release name: *Gracenote*-*DB 22-1 for MGU* 03/2022 *Rest of the World*

\--Release 03.2022-- \n ENTD_000055ED_006_022_007 = Gracenote-DB 22-1 for MGU21 07/2022 Japan \n ENTD_000055EC_005_022_003 = Gracenote-DB 22-1 for MGU 03/2022 China/Korea \n ENTD_000055EB_003_022_003 = Gracenote-DB 22-1 for MGU 03/2022 Europe \n ENTD_000055ED_006_022_003 = Gracenote-DB 22-1 for MGU18 03/2022 Japan \n ENTD_000055EE_004_022_003 = Gracenote-DB 22-1 for MGU 03/2022 North America \n ENTD_000055EA_002_022_003 = Gracenote-DB 22-1 for MGU 03/2022 Rest of the World

\--Release 07.2023-- 

ENTD_000055ED_006_023_004 = Gracenote-DB 23-1 for MGU21 03/2023 Japan\nENTD_000055EC_005_023_003 = Gracenote-DB 23-1 for MGU18 03/2023 China/Korea\nENTD_000055EB_003_023_003 = Gracenote-DB 23-1 for MGU18 03/2023 Europe\nENTD_000055ED_006_023_003 = Gracenote-DB 23-1 for MGU18 03/2023 Japan\nENTD_000055EE_004_023_003 = Gracenote-DB 23-1 for MGU18 03/2023 North America\nENTD_000055EA_002_023_003 = Gracenote-DB 23-1 for MGU18 03/2023 Rest of the World


# Gracenote1 DB format used on MHIG ([MIB1 High](https://mibwiki.one/collection/mhig-harman-mib1-high-yWXdNjSDcm)) and BMW EVO units

 ![](attachments/8b8dbefc-caa4-4085-be68-9948595e5007.png)

The same format is also used on [Accura](https://acuranavi.navigation.com/cms/page.GracenoteAlpine3.2/en_US/AcuraNA/USD), [Fiat](https://21stcenturyfiat124spider.wordpress.com/2022/12/05/gracenote-music-database-version-12-update/), [Mazda2](https://infotainment.mazdahandsfree.com/gracenote), [Toyota](https://toyota-en-us.visteoninfotainment.com/how-to-update-gracenote) Visteon (RAV4/Prius/Yaris),  and [Honda](http://dls.download.navigation.com/filedownload/DownloadFile?rid=r1593554258) MIBs. Password for **\*.up** file **5X/9vAVhovyU2ygK**

Content of **Gracenote_EU_January2022.up/gracenotedb/files.ini.gz/files.ini**

```javascript
[Settings]

[Instructions]
Count = 24
1 = Execute,"echo ========== Start updating /gracenotedb =========="
2 = Execute,"[ -f /resources/gracenotedb/gn_version.ini ] && cp -f /resources/gracenotedb/gn_version.ini /data_persist/reflash/gn_version.ini || echo Gracenote DB not found!"
3 = Execute,"sync"
4 = Execute,"mount -o remount,rw,sync /tmp/mnt/resources"
5 = Remove,"/resources/gracenotedb/"
6 = Remove,"/resources/gracenotedb_temp/"
7 = Create,"/resources/gracenotedb_temp/",0775
8 = Copy,"gracenotedb/f0000000001.dat","/resources/gracenotedb_temp/pstplgen.bml",0775,0x47AD2B5D
9 = Copy,"gracenotedb/f0000000002.dat","/resources/gracenotedb_temp/gn_version.ini",0644,0x715DAE33
10 = Copy,"gracenotedb/f0000000003.dat","/resources/gracenotedb_temp/genres.tbl",0775,0x4230544D
11 = Copy,"gracenotedb/f0000000004.dat","/resources/gracenotedb_temp/elists.inv",0775,0x57DB8663
12 = Copy,"gracenotedb/f0000000005.dat","/resources/gracenotedb_temp/emms.pmx",0775,0x2C179071
13 = Copy,"gracenotedb/f0000000006.dat","/resources/gracenotedb_temp/emms.cax",0775,0x82B06B09
14 = Copy,"gracenotedb/f0000000007.dat","/resources/gracenotedb_temp/cddbplm.gcf",0775,0x80604DA3
15 = Copy,"gracenotedb/f0000000008.dat","/resources/gracenotedb_temp/contrib.tbl",0775,0x3F2D3E5A
16 = Copy,"gracenotedb/f0000000009.dat","/resources/gracenotedb_temp/emms.cgx",0775,0xEDD1A013
17 = Copy,"gracenotedb/f0000000010.dat","/resources/gracenotedb_temp/album.tbl",0775,0x58D2C966
18 = Copy,"gracenotedb/f0000000011.dat","/resources/gracenotedb_temp/emms_current.cfg",0775,0x6303B41C
19 = Copy,"gracenotedb/f0000000012.dat","/resources/gracenotedb_temp/gnlists.db",0775,0x24BED2BC
20 = Copy,"gracenotedb/f0000000013.dat","/resources/gracenotedb_temp/emms.cgm",0775,0x31E72D52
21 = Copy,"gracenotedb/f0000000014.dat","/resources/gracenotedb_temp/emms.cam",0775,0x284B086F
22 = Rename,"/resources/gracenotedb_temp/","/resources/gracenotedb"
23 = Execute,"rm -rf /data_persist/reflash/gn_version.ini"
24 = Execute,"sync"
```

# Gracenote2 DBs protected with unknown passwords 

## Polestar

<https://www.polestar.com/de/manual/polestar-1/2021/downloads/gracenote/>

 ![](attachments/4b56f866-94a9-4a9f-bfcd-ab6aff0a22ed.png)

 ![](attachments/c411192c-6a57-44e4-be39-42aec2e159c7.png)

## Mazda

<https://connect.mazda.com/en/support/gracenote_update/>

 ![](attachments/0837fd0f-7241-4388-9255-e32bb4eab82d.png)