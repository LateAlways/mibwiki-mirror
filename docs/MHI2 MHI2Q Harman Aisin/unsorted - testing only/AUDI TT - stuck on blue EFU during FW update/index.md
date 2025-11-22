# AUDI TT - stuck on blue EFU during FW update

## This happens when you update MHI2_ER_AU43x_S1074_1 to MHI2_ER_AU43x_P5098

Updating from very old FW version leaves the MIB unit stuck in the blue EAU screen. The update.txt is present but the automatic recovery via blue EAU ist not working.

It scans metainfo and does nothing. Inserting stock MHI2_ER_AU43x_P5098 SD does not help too.

 ![](attachments/f2fa30b7-6d2a-4617-9694-365a368d0c52.png)

 ![](attachments/d60f3ec8-1a9b-4aeb-81d6-1b4e0d6713a4.png)

## Manually flash to fix

To fix the unit you must enter into [Emergency IFS](/MHI2 MHI2Q Harman Aisin/Recovery/RCC/How to boot ifs-emergency.ifs (start blue emergency EFU)/) using [UART](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/Connecting TTL adapter to UART on quadlock/) connection and manually flash ifs-root and DSP binary. You can see them in the [update.txt](/MHI2 MHI2Q Harman Aisin/unsorted - testing only/AUDI TT - stuck on blue EFU during FW update//edit#h-updatetxt-from-unit-with-failed-fw-update-from-train-mhi2erau43xs10741) below with the TODO status that means that they are not updated yet: 

 ![manually flash ifs-root and DSP](attachments/736d482f-cf92-4dc5-b9ae-2c7376633254.png)

## update.txt from the unit with MHI2_ER_AU43x_S1074_1 train where FW update to MHI2_ER_AU43x_P5098 failed

```
CRC = c94cbed6
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