# Maps download links

## MSTD (MIB1 Std)

<https://mibsolution.one/#/1/15/MSTD>

## MHS2 (MIB2 High Scale) 2024

https://mibsolution.one/#/1/15/MHS2

## MH2P (MIB2 Premium)

### Europe

2025: <https://navigation-maps.volkswagen.com/vw-maps/P720_MIB2P_EU.7z>

2024/2025: [https://navigation-maps.volkswagen.com/vw-maps/P690_MIB2P_EU.7z](https://navigation-maps.volkswagen.com/vw-maps/P690_MIB2P_CN.7z)

2025/2026: <https://navigation-maps.volkswagen.com/vw-maps/Update_25_25/P0780_MIB2P_EU.7z>

### ROW

2025: <https://navigation-maps.volkswagen.com/vw-maps/P723_MIB2P_RW.7z>

2024/2025: <https://navigation-maps.volkswagen.com/vw-maps/P693_MIB2P_RW.7z>

## MOI3

### Europe

2025/2026: https://updateportalmaps.blob.core.windows.net/maps/OI_P154_EU_202534_Offline_Update.zip

## MHI3/MPR3 (MIB3 High/Premium)

### Europe

2025/2026 https://navigation-maps.volkswagen.com/vw-maps/Update_25_25/P1420_MIB3_EU.7z

2025 https://download04.audi.com/soko2-mapcare/packages/70001124234?token=ba2a3b69-6a80-47b4-a14d-ce5e8d3215b7

2024 <https://disk.yandex.com/d/QHC3oDwJ_OIO_A>

### NA

2025 <https://vwgoa.app.box.com/s/zexspm3t3veqm5y4q893eid9gsvvv1kv>

## MHIG/MHI2/MHI2Q (MIB1 and MIB2 High units)


:::info
These units are known as VW Discover Pro, Seat Navi System Plus, Skoda Columbus, Audi MMI Navigation Plus

:::


:::tip
MIB1 and MIB2 HIGH are using internal [NAND](https://en.wikipedia.org/wiki/Flash_memory#NAND_memories) to store navigation database.

For installation you will need any 64Gb SD card or USB drive formatted in `FAT32`, `exFAT` or `NTFS` .

Run update from **MENU>Settings>Software Versions (on non Audi cars)** or **System maintenance (on Audi)**.

Installation may take up to 2 hours but it is absolutely not requred to do it in one go. If have no time, just switch off the ignition, do not remove SD card and leave the car. When next time you will come back to the car and turn on ignition the installation will automatically continue from the file where it was interrupted.

On the bench it makes sense to run the installation from Service (long MENU press) or Engineering (RED) menu as it does not require ignition signal.

:::


:::warning
Do NOT delete `/MIB1/` folder from the map update as it is required for MIB2 units too!

:::


:::info
In case maps refuse to install/update, run the installation from Service (long MENU press) or Engineering (RED) menu as in that mode you will get more detailed description of the error.

To understand which installed FEC is required for particular map version, take a look into (for example) following file P330_N60S5MIBH3_EU.7z\\Mib2\\NavDB\\common_eu\\0\\default\\content.pkg.

This line shows which installed FECs is required: "FSC": "02300032,09300002,08300002,07300032,06300032,03300032.

For MIB1 High see [here](/MHIG Harman (MIB1 HIGH)/Updating maps/).

:::

### ECE (Europe)

2025/2026 **MHI2(Q) only**: <https://navigation-maps.volkswagen.com/vw-maps/Update_25_25/P410_N60S5MIBH3_EU.7z>

2025 **MHI2(Q) only:** https://navigation-maps.volkswagen.com/vw-maps/P390_N60S5MIBH3_EU.7z

2024/2025 MHI2(Q) only: <https://navigation-maps.volkswagen.com/vw-maps/P370_N60S5MIBH3_EU.7z>

2024 very last for MHIG: https://navigation-maps.volkswagen.com/vw-maps/P350_N60S5MIBH3_EU.7z

2024/2023: <https://navigation-maps.volkswagen.com/vw-maps/P330_N60S5MIBH3_EU.7z>\n2023: <https://navigation-maps.volkswagen.com/vw-maps/P310_N60S5MIBH3_EU.7z>

### ROW (Rest of the World)

2025 MHI2(Q) only: <https://navigation-maps.volkswagen.com/vw-maps/P393_N60S5MIBH3_ROW.7z>

2024/2025 MHI2(Q) only: <https://navigation-maps.volkswagen.com/vw-maps/P373_N60S5MIBH3_ROW.7z>

2024 very last for MHIG: <https://navigation-maps.volkswagen.com/vw-maps/P353_N60S5MIBH3_ROW.7z>

2023/2024: <https://navigation-maps.volkswagen.com/vw-maps/P333_N60S5MIBH3_ROW.7z>\n2023: <https://navigation-maps.volkswagen.com/vw-maps/P313_N60S5MIBH3_ROW.7z>

### Japan

2024: <https://navigation-maps.volkswagen.com/vw-maps/MapDB_JPN_9010.7z>\n2023: <https://navigation-maps.volkswagen.com/vw-maps/MapDB_JPN_8810.7z>\n2022: <https://navigation-maps.volkswagen.com/vw-maps/MapDB_JPN_8610.7z>

### **Taiwan**

2024: <https://navigation-maps.volkswagen.com/vw-maps/MapDB_TWN_9010.7z>\n2023: <https://navigation-maps.volkswagen.com/vw-maps/MapDB_TWN_8810.7z>\n2022: <https://navigation-maps.volkswagen.com/vw-maps/MapDB_TWN_8620.7z>


:::tip
Other regions are not available for direct download from VAG try to find them on [mibsolution.one](https://mibsolution.one/#/1/15/MHI2(Q))

GOOD TO KNOW: Maps can be dumped via putty and can be installed onto another units via putty and command line.

:::


## MST2 (MIB STD2 PQ/ZR Technisat/Preh on VW/Seat/Skoda, MIB2 STD Delphi on VW


:::info
These types of MIB2 are known as VW Discover Media, Seat Navi System (6P0), Skoda Amundsen.

On this units navigation database (maps) are working directly from original VW/Seat/Skoda SD card that has has a special [CID](https://www.cameramemoryspeed.com/sd-memory-card-faq/reading-sd-card-cid-serial-psn-internal-numbers/) `0941504D494253540210565936010201`

To make navigation database work from regular SD card you need:

* for MIB2 STD (Delphi) units install [Congo Activator with Autobackup](https://disk.yandex.com/d/qR3HkgjS-yFL0g)
* for MIB STD2 PQ/ZR (Technisat/Preh) units buy custom CID SD card from aliexpress (they are usually wear out in some months because of low quality) or install MIB2 PQ/ZR Toolbox and run there **mibstd2_toolbox→customization→navi→Patch navigation config**

:::


:::tip
To make ECE AS maps package size fit 16Gb SD card you can remove unused languages from `/maps/00/sds/`

:::

## ECE 2026

| Name | Size | Regions | Download Link |
|----|----|----|----|
| **ECE A1** \nAS | 17 GB (32 GB SD Card) | Full | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU_AS_202525.zip> |
| **ECE 1**\nEU1 | 8 GB (16 GB SD Card) | West | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU1_202525.zip> |
| **ECE 2**\nEU2 | 7 GB (16 GB SD Card) | East | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU2_202525.zip> |
| **ECE 3**\nEU3 | 6 GB (16 GB SD Card) | Central | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU3_202525.zip> |
| **ECE 4**\nEU-DL1 | 10 GB (16 GB SD Card) | West, Central | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU_DL1_202525.zip> |
| **ECE 5**\nEU-DL2 | 10 GB (16 GB SD Card) | West, Central, GB | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU_DL2_202525.zip> |
| **ECE 6**\nEU-DL3 | 9 GB (16 GB SD Card) | West, Scandinavia | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU_DL3_202525.zip> |
| **ECE 7**\nEU-DL4 | 8 GB (16 GB SD Card) | Central, East | <https://infotainment-cdn.skoda-auto.com/base/maps/STD2_2510_EU_DL4_202525.zip> |

 ![](attachments/a80fc015-eef3-4113-b4da-c58054674a5f.bin)


## ECE 2025/2026

EU Full Pack (32GB SD needed): <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-AS_2410_V21.7z>

EU1: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU1_2410_V21.7z>

EU2: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU2_2410_V21.7z>

EU3: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU3_2410_V21.7z>

EU4: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_2410_V21.7z>

EU5: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL2_2410_V21.7z>

EU6: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL3_2410_V21.7z>

EU7: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL4_2410_V21.7z>

## ECE 2025

EU Full Pack (32GB SD needed): [https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-AS_2310_V20.7z]()

EU1: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU1_2310_V20.7z>

EU2: https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU2_2310_V20.7z

EU3: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU3_2310_V20.7z>

EU4: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_2310_V20.7z>

EU5: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL2_2310_V20.7z>

EU6: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL3_2310_V20.7z>

EU7: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL4_2310_V20.7z>

## ECE 2024/2025

EU Full Pack (32GB SD needed): <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-AS_2210_V19.7z>\nEU1: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU1_2210_V19.7z>\nEU2: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU2_2210_V19.7z>\nEU3: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU3_2210_V19.7z>\nEU4: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_2210_V19.7z>\nEU5: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL2_2210_V19.7z>\nEU6: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL3_2210_V19.7z>\nEU7: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL4_2210_V19.7z>

## ECE 2024 (old)

EU Full Pack (32GB SD needed): <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-AS_2110_V18.7z>\nEU1: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU1_2110_V18.7z>\nEU2: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU2_2110_V18.7z>\nEU3: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU3_2110_V18.7z>\nEU4: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_2110_V18.7z>\nEU5: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL2_2110_V18.7z>\nEU6: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL3_2110_V18.7z>\nEU7: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL4_2110_V18.7z>

## ECE 2023: 5NA 919 866 DF, V03959820CC, 5L0051236DB, 7CE919866CK / 2010 (released 2022.11)

EU ECE AS: [https://vw-maps-cdn.lighthouselabs.eu/vw-maps/DiscoverMedia2_EU-AS_2010_V17.7z](https://vw-maps-cdn.lighthouselabs.eu/vw-maps/DiscoverMedia2_EU-AS_1910_V16.7z)\nEU ECE 2: https://vw-maps-cdn.lighthouselabs.eu/vw-maps/DiscoverMedia2_EU2_2010_V17.7z\nEU DL 1: [https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_2010_V16.7z](https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_1910_V16.7z)

## ECE 2022: 5NA 919 866 CK / 1910

EU AS: <https://vw-maps-cdn.lighthouselabs.eu/vw-maps/DiscoverMedia2_EU-AS_1910_V16.7z>\nEU2: <https://vw-maps-cdn.lighthouselabs.eu/vw-maps/DiscoverMedia2_EU2_1910_V16.7z>\nEU DL1: <https://navigation-maps.volkswagen.com/vw-maps/DiscoverMedia2_EU-DL1_1910_V16.7z>

## ECE 2021: 5NA 919 866 CA / 1810 (released 2021.10)

ECE AS: <https://seatmapdownloads.akamaized.net/EUAS/EU_AS_STD_1810.zip>\nECE 1: <https://seatmapdownloads.akamaized.net/EU1/EU1_STD_1810.zip>\nECE 2: <https://seatmapdownloads.akamaized.net/EU2/EU2_STD_1810.zip>\nECE 4: <https://seatmapdownloads.akamaized.net/EUDL1/EU_DL1_STD_1810.zip>\nECE 5: <https://seatmapdownloads.akamaized.net/EUDL2/EU_DL2_STD_1810.zip>\nECE 6: <https://seatmapdownloads.akamaized.net/EUDL3/EU_DL3_STD_1810.zip>\nECE 7: <https://seatmapdownloads.akamaized.net/EUDL4/EU_DL4_STD_1810.zip>\nROW 1: <https://seatmapdownloads.akamaized.net/MRM1/MRM1_STD_1810.zip>\nROW 2: <https://seatmapdownloads.akamaized.net/MRM2/MRM2_STD_1810.zip>\nROW 3: <https://seatmapdownloads.akamaized.net/MRM3/MRM3_STD_1810.zip>

## Coverage

### ECE AS

Albania \*, Andorra, Austria, Belarus \*, Belgium, Bosnia and Herzegovina \*, Bulgaria \*, Croatia, Cyprus \*, Czech Republic, Denmark, Estonia \*, Finland, France, Germany, Gibraltar, Great Britain, Greece, Hungary, Iceland, Ireland, Italy, Kosovo \*, Latvia \*, Liechtenstein, Lithuania \*, Luxembourg, Malta, Moldova \*, Monaco, Montenegro \*, Netherlands, Northern Macedonia \*, Norway, Poland, Portugal, Romania \*, Russia \*, San Marino, Serbia \*, Slovakia, Slovenia \*, Spain, Sweden, Switzerland, Turkey \*, Ukraine \*, Vatican City \n \* partially

### ROW

Argentina \*, Australia, Bahrain, Botswana \*, Brazil \*, Brunei \*, Chile \*, Indonesia \*, Israel, Jordan, Kuwait, Lesotho \*, Malaysia, Mexico \*, Mozambique \*, Namibia \*, New Zealand, Oman, Philippines \*, Qatar, Reunion \*, Saudi Arabia, Singapore, South Africa, Swaziland \*, Thailand \*, Turkey \*, United Arab Emirates

\* partially

## Installation

### Audi with MHI2 system MMI (A7 4G)

[https://youtu.be/ryMud5Q9h9U](https://youtu.be/ryMud5Q9h9U)

### Audi With MHI2Q system MMI (Q7 4M)

[https://youtu.be/3K6wevz2wrk](https://youtu.be/3K6wevz2wrk)

### Volkswagen with MST2 system Discover Media (Golf MK7)

[https://youtu.be/vEbEAhXKvho](https://youtu.be/vEbEAhXKvho)

### Skoda with MHIG system Columbus (Octavia MK3 5E)

[https://www.youtube.com/watch?v=K99RMdsWcWM](https://www.youtube.com/watch?v=K99RMdsWcWM)

### Porsche with PCM4.0 (MHI2)

[https://youtu.be/0ZAJWgnmGW4](https://youtu.be/0ZAJWgnmGW4)

## More direct links

<http://mib-helper.com/show.php?all=maps#details>