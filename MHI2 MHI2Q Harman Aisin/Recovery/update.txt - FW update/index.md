# update.txt - FW update

## What is it used for?


:::info
On the power on and boot the firmware checks `/net/rcc/mnt/efs-persist/update.txt`and if it is not found then `/net/rcc/mnt/efs-persist/update.txt.backup` file. 

If it exists, the normal boot sequence is stopped and SWDL mode is run to complete updates listed in this file.

:::


:::tip
In case you want to stop a failing FW update you can delete it with

`rm /net/rcc/mnt/efs-persist/update.*` 

:::


1. Checking the content of update.txt, helps to identify why a [Audi TT FW update](/MHI2 MHI2Q Harman Aisin/unsorted - testing only/AUDI TT - stuck on blue EFU during FW update/) failed on the mid way from a very old FW to the latest.
2. You can manually generate or modify an `update.txt` to trigger:

   
   1. A **custom FW update** on demand and with specific tasks.
   2. A **FW update on bench**, without a screen connected to system.

## Editing/generation of a custom `update.txt`


:::warning
The basics to edit an `update.txt` will be presented below.

However, this is very likely not complete yet. Feel free to test and add missing knowledge!

:::


As an EXAMPLE, let us use this `update.txt`:

```
CRC = 4ff4205f
MetafileCRC = 9e12c2936b019a6d165cd3586105b85bc85bff2d
initiator = HMI
train = MHI2_ER_AU43x_S1074_1
variant = FM2-H-N-EU-AU-MQT
MUversion = 0884
RCCversion = U8228
AssemblyID = 0
ReleaseName = MHI2_ER_AU43x_P5098
startTime = 2021-10-07 14:09
LogSubDir = /HBpersistence/SWDL/Log/service/2
TransactionImageAddress = 0x540000
TransactionImageSize = 0x15a0530
Source = SD1
Path = /
ReleasePath = 
Phase3Device = IOC
Phase3Device = MuINIC
[AMP16_APN\0\AMP16_APPL\6\default\bootloader]=NO;240;default;240
[AMP16_APN\0\AMP16_APPL\6\default\application]=NO;240;default;240
[FPK\0\gss-qb-recovery\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-qb-recovery\35\default\application]=NO;126;default;126
[FPK\0\gss-stage1-recovery\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-stage1-recovery\35\default\application]=NO;406;default;406
[FPK\0\gss-qb-primary\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-qb-primary\35\default\application]=NO;126;default;126
[FPK\0\gss-stage2\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-stage2\35\default\application]=NO;406;default;406
[FPK\0\gss-stage2-nand\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-stage2-nand\35\default\application]=NO;406;default;406
[FPK\0\gss-stage3\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-stage3\35\default\application]=NO;406;default;406
[FPK\0\gss-applications\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-applications\35\default\application]=NO;406;default;406
[FPK\0\gss-stage1\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-stage1\35\default\application]=NO;406;default;406
[FPK\0\gss-versioninfo\35\default\bootloader]=NO;0;default;0
[FPK\0\gss-versioninfo\35\default\application]=NO;601;default;601
[FPK\0\kss-flashdriver\35\default\bootloader]=NO;0;default;0
[FPK\0\kss-flashdriver\35\default\application]=NO;600;default;600
[FPK\0\kss-application\35\default\bootloader]=NO;0;default;0
[FPK\0\kss-application\35\default\application]=NO;600;default;600
[FPK\0\gss-inic\2\default\bootloader]=NO;0;default;0
[FPK\0\gss-inic\2\default\application]=NO;65536;default;65536
[RCC\0\ifs-emg\32\default\bootloader]=NO;0;default;0
[RCC\0\ifs-emg\32\default\application]=DONE;941;default;953
[RCC\0\ifs-root\32\default\bootloader]=NO;0;default;0
[RCC\0\ifs-root\32\default\application]=TODO;8734;default;9558
[RCC\0\efs-system\32\default\bootloader]=NO;0;default;0
[RCC\0\efs-system\32\default\application]=TODO;7566;default;8388
[RCC\0\dsp\32\default\bootloader]=NO;0;default;0
[RCC\0\dsp\32\default\application]=TODO;571811866;default;672601178
[Tuner\0\E2P\32\default\bootloader]=NO;0;default;0
[Tuner\0\E2P\32\default\application]=DONE;19005440;default;25755648
[IOC\0\Main\32\default\bootloader]=TODO;205;default;211
[IOC\0\Main\32\default\application]=TODO;5304;default;9264
[MuINIC\0\Main\32\default\bootloader]=NO;0;default;0
[MuINIC\0\Main\32\default\application]=NO;16909592;default;16909592
[FC1H33xE\0\FCB\22\default\bootloader]=NO;0;default;0
[FC1H33xE\0\FCB\22\default\application]=DONE;73;default;85
[FC1H33xE\0\FCP\22\default\bootloader]=NO;0;default;0
[FC1H33xE\0\FCP\22\default\application]=DONE;121;default;176
[FC1H33xE\0\FCR\22\default\bootloader]=NO;0;default;0
[FC1H33xE\0\FCR\22\default\application]=DONE;9;default;10
[FC1H33xE\0\HREU\22\default\bootloader]=NO;0;default;0
[FC1H33xE\0\HREU\22\default\application]=NO;12;default;12
[GPS\0\Main\32\default\bootloader]=NO;0;default;0
[GPS\0\Main\32\default\application]=NO;603;default;603
[MMX2\0\qb-recovery\73\default\bootloader]=NO;0;default;0
[MMX2\0\qb-recovery\73\default\application]=DONE;111;default;202
[MMX2\0\qb-primary\73\default\bootloader]=NO;0;default;0
[MMX2\0\qb-primary\73\default\application]=DONE;111;default;202
[MMX2\0\eifs\73\default\bootloader]=NO;0;default;0
[MMX2\0\eifs\73\default\application]=DONE;1380;default;2690
[MMX2\0\mifs-stage2\73\default\bootloader]=NO;0;default;0
[MMX2\0\mifs-stage2\73\default\application]=DONE;1380;default;2690
[MMX2\0\efs-sys\73\default\bootloader]=NO;0;default;0
[MMX2\0\efs-sys\73\default\application]=DONE;1380;default;2690
[MMX2\0\app\73\default\bootloader]=NO;0;default;0
[MMX2\0\app\73\default\application]=DONE;1380;default;2690
[MMX2\0\mifs-stage1\73\default\bootloader]=NO;0;default;0
[MMX2\0\mifs-stage1\73\default\application]=DONE;1380;default;2690
[MMX2\0\efs-pers\73\default\bootloader]=NO;0;default;0
[MMX2\0\efs-pers\73\default\application]=NO;2;default;2
[DVD\0\Main\48\default\bootloader]=NO;0;default;0
[DVD\0\Main\48\default\application]=NO;32;default;32
[SpeechAppRes\0\speech-common-data\0\default\Dir]=TODO;5349;default;5706;MMX
[SpeechAppRes\0\speech-tts-app-data-vg\0\default\Dir]=TODO;5349;default;5706;MMX
[SpeechAppRes\0\speech-sr-data\0\default\Dir]=TODO;5349;default;5706;MMX
[SpeechRes\0\speech-tts-data_EU\0\default\Dir]=TODO;6090;default;7776;MMX
[SpeechRes\0\speech-tts-data_ROW\0\default\Dir]=TODO;6090;default;7776;MMX
[SpeechRes\0\speech-tts-voices\0\default\Dir]=TODO;6090;default;7776;MMX
[MuTnrRef\0\data\0\default\File]=DONE;494;default;190
[MUConsistency\0\Data\0\default\File]=DONE;884;default;1339
{RCC\Post}=TODO;
{RCC\Pre}=DONE;
{Final}=TODO;
```


:::tip
update.txt will be accepted by the SWDL only if `CRC =` and `MetafileCRC =` contain correct values. Otherwise update.txt will be renamed to `update.txt.Cancelled`

:::

### CRC = is the CRC32 of all update.txt lines WITHOUT the CRC line (including \\n) - in this example: `CRC = 4ff4205f`

 ![CRC line removed](attachments/13d4a9fd-8ec6-4ed1-abcd-9d2f20070792.png)

If you calculate CRC32 of the`update.txt`with the CRC line, SWDL will consider the file as damaged:            ![CRC32 of update.txt does not fit](attachments/6abb8622-b8b8-47b5-933e-8698bf5e18a7.png)

### MetafileCRC = contains SHA1 value of `MetafileChecksum` from `metainfo2.txt`.

### SWDL will check if this value matches `MetafileChecksum` value in `metainfo2.txt`.

Example from FW MHI2_ER_AU43x_P5098

 ![SHA1 hash matches](attachments/513f50a5-7389-46fa-880c-382f6c80380f.png)


:::info
`MetafileChecksum =` inside of the metainfo2.txt is SHA1 hash of the `metainfo2.txt`without removed `MetafileChecksum =` line.

:::

### MetafileCRC = skip


:::tip
If you removed `MetafileChecksum` from metainfo.txt and used `skipMetaCRC = "true"` instead, then you must set `MetafileCRC = skip` in update.txt 

:::

 ![](attachments/bedf6dab-16bf-4afc-899c-1da9c901640d.png)


:::info
To calculate CRC32 hash for CRC and SHA1 hash for MetafileCRChashes, use [HashMyFiles](https://www.nirsoft.net/utils/hash_my_files.html) or something similar

:::

### Update packages

To quickly see how much packages are remaining to be installed, check with:


:::tip
`cat /net/rcc/mnt/efs-persist/update.txt | grep TODO `

:::

Lines may look like:

`[RCC\0\ifs-root\32\default\application]=TODO;8734;default;9558`

Let's break down the line contend:

\[RCC\\0\\ifs-root\\32\\default\\application - similar to the line in metainfo2.txt with adding a device number\]===Status (see below)==;`version of the module in unit`;default(unknown)`target version on SD/USB card update`

 ![section from metainfo2.txt for MHI2_ER_AU43x_P5098](attachments/203f10de-87d2-4165-abc0-3d48f84a13ac.png)

### Status: NO/TODO/DONE

| Status | Meaning |
|----|----|
| NO | nothing to be done to this package |
| TODO | still open and has to be finished by FW update process |
| DONE | finished by FW update process |


Based on the example above, these other lines also play a role in update.txt

Not all are required for a custom build update.txt

Not all are used by the different types of FW updates, like map updates, POI, …

| Line | Description | mandatory |
|----|----|----|
| initiator = HMI | which module created the file  | ? |
| train = MHI2_ER_AU43x_S1074_1 | train of FW at start of update | ? |
| variant = FM2-H-N-EU-AU-MQT |    | ? |
| MUversion = 0884 | MU version of original FW at start of update | ? |
| RCCversion = U8228 |    | ? |
| AssemblyID = 0 |    | ? |
| ReleaseName = MHI2_ER_AU43x_P5098 | Pulled from metainfo2.txt \n   ![](attachments/13b05c2c-a0b0-49fb-b85e-aac0152e39c6.png) | ? |
| startTime = 2021-10-07 14:09 |    | ? |
| LogSubDir = /HBpersistence/SWDL/Log/service/2 | storage location on unit on RCC for Log of this update | ? |
| TransactionImageAddress = 0x540000 | RCC hex start address of ifs-root image | ? |
| TransactionImageSize = 0x15a0530 |    | ? |
| Source = SD1 |    | ? |
| Path = / |    | ? |
| ReleasePath = |    | ? |
| Phase3Device = IOC |    | ? |
| Phase3Device = MuINIC |    | ? |
| {RCC\\Post}=TODO; |    | ? |
| {RCC\\Pre}=DONE; |    | ? |
| {Final}=TODO; | Status of FinalScript in metainfo2.txt \n   ![](attachments/10203f16-7dc7-4f5f-9e7e-1e2c763d88f1.png) | ? |
| Feel free to add more here! |    |    |