# Manual FW update /50/ vs /70/ folders

:::info
While converting a DEV unit (MHI2_CN_AU57x_P0632 → MHI2_ER_SEG11_P4709) with H22 (manufactured in 2013) I noticed, that partitioning on MMX is different from what I have seen so far on G11 units.

Assumption is, that for this configuration `/50/` folders from FW update are needed to run.

:::


Most (if not all) FW updates have two subfolders within the MMX2 update packages

 ![MU1447 - efs-sys](attachments/c4f91842-7128-4423-a187-c3c9c9020c06.png)

Most (at least recent) FW versions seem to need files from `/70/` folders if one is available.

e.g. eifs does not have a `70` folder and therefore `/50/` is used in all cases.

 ![MU1447 - eifs](attachments/22027b44-7218-4657-b42b-f6cac2babaa7.png)

## G11 - H22 MMX NOR partition layout

```
| BCT             | start: 0x00000000 | size: 0x40000   |
| PT              | start: 0x00040000 | size: 0x20000   |
| STAGE1_RECOVERY | start: 0x00060000 | size: 0x40000   |
| STAGE2_RECOVERY | start: 0x000a0000 | size: 0x40000   |
| STAGE1_PRIMARY  | start: 0x000e0000 | size: 0x40000   |
| STAGE2_PRIMARY  | start: 0x00120000 | size: 0x40000   |
| KERNEL_RECOVERY | start: 0x00160000 | size: 0x600000  |
| KERNEL_PRIMARY  | start: 0x00760000 | size: 0x300000  |
| MAIN_STAGE2     | start: 0x00a60000 | size: 0x2e00000 |
| SWDL            | start: 0x03860000 | size: 0x20000   |
| SPLASH          | start: 0x03880000 | size: 0x180000  |
| SYSTEM          | start: 0x03a00000 | size: 0x200000  |
| PERSIST         | start: 0x03c00000 | size: 0x400000  |
```

## G11 - "Normal" MMX NOR partition layout

```
| BCT             | start: 0x00000000 | size: 0x40000   |
| PT              | start: 0x00040000 | size: 0x20000   |
| STAGE1_RECOVERY | start: 0x00060000 | size: 0x40000   |
| STAGE2_RECOVERY | start: 0x000a0000 | size: 0x40000   |
| STAGE1_PRIMARY  | start: 0x000e0000 | size: 0x40000   |
| STAGE2_PRIMARY  | start: 0x00120000 | size: 0x40000   |
| KERNEL_RECOVERY | start: 0x00160000 | size: 0x600000  |
| KERNEL_PRIMARY  | start: 0x00760000 | size: 0x300000  |
| MAIN_STAGE2     | start: 0x00a60000 | size: 0x2a00000 |
| SWDL            | start: 0x03460000 | size: 0x20000   |
| SPLASH          | start: 0x03480000 | size: 0x180000  |
| SYSTEM          | start: 0x03600000 | size: 0x200000  |
| PERSIST         | start: 0x03800000 | size: 0x800000  |
```



:::tip
SWDL, SPLASH, SYSTEM and PERSIST have different offsets between these versions

[ images.zip](attachments/f66cf523-bdcd-40a1-bc3d-d028a9103e16.zip)

:::

## Manual FW restore commands for MHI2_CN_AU57x_P0632 or other `/50/` type units?

```bash
#Run from Emergency IFS
#Insert FW SD into SD1

#stop system log output
stfu

#RCC flash now
flashunlock
on -f rcc flashit -v -x -d -a 0x00000000 -f /net/mmx/fs/sda0/RCC/ipl/21/default/ipl-mib2.bin #normally not needed, skip
on -f rcc flashit -v -x -d -a 0x00540000 -f /net/mmx/fs/sda0/RCC/ifs-root/21/default/ifs-root.ifs
on -f rcc flashit -v -x -d -a 0x01D40000 -f /net/mmx/fs/sda0/RCC/efs-system/21/default/efs-system.efs
on -f rcc flashit -v -x -d -a 0x03D00000 -f /net/mmx/fs/sda0/RCC/dsp/21/default/AUDI_MIB_DSP.bin.bgz

#MMX flash now
#rename start of image to ANDROID!  41 4E 44 52 4F 49 44 21
on -f rcc flashit -v -x -d -a 0x760000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/mifs-stage1/50/default/mifs-stage1p.img
on -f rcc flashit -v -x -d -a 0xA60000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/mifs-stage2/50/default/mifs-stage2.img
on -f rcc flashit -v -x -d -a 0x3a00000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/efs-sys/50/default/efs-system.img
on -f rcc flashit -v -x -d -a 0x3c00000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/efs-pers/50/default/efs-persist.img

#extracted from MMX dump
on -f rcc flashit -v -x -d -a 0x3860000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/SWDL.img
on -f rcc flashit -v -x -d -a 0x3880000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/SPLASH.img

#partition NAND HW22 -> FW /50/ folders
on -f mmx sh
umount -f /dev/mnand0
fdisk /net/mmx/dev/mnand0 delete -a 
fdisk /net/mmx/dev/mnand0 add -s1 -t177 -c0,357
fdisk /net/mmx/dev/mnand0 add -s2 -t5 -c358,29285
fdisk /net/mmx/dev/mnand0 add -s2 -e1 -t178 -n512
fdisk /net/mmx/dev/mnand0 add -s2 -e2 -t178 -n2048
fdisk /net/mmx/dev/mnand0 add -s2 -e3 -t178 -n2048
fdisk /net/mmx/dev/mnand0 add -s2 -e4 -t178 -n256
fdisk /net/mmx/dev/mnand0 add -s2 -e5 -t178 -n512
fdisk /net/mmx/dev/mnand0 add -s2 -e6 -t178 -n512
fdisk /net/mmx/dev/mnand0 add -s2 -e7 -t178 -n1024
fdisk /net/mmx/dev/mnand0 add -s2 -e8 -t178 -n256
fdisk /net/mmx/dev/mnand0 add -s2 -e9 -t178 -n15872
fdisk /net/mmx/dev/mnand0 add -s2 -e10 -t178 -n5888
fdisk /net/mmx/dev/mnand0 add -s3 -t179 -c29286,30315
mount -e /net/mmx/dev/mnand0 
echo "y" | mkqnx6fs -T runtime -b 1024 -i 22912 /dev/mnand0t177    # /mnt/app 
echo "y" | mkqnx6fs -T media -b 32768 -i 1024 /dev/mnand0t178    # /mnt/boardbook 
echo "y" | mkqnx6fs -T media -b 32768 -i 2048 /dev/mnand0t178.1    # /mnt/speech 
echo "y" | mkqnx6fs -T media -b 32768 -i 256 /dev/mnand0t178.2    # /mnt/gracenotedb 
echo "y" | mkqnx6fs -T media -b 32768 -i 2048 /dev/mnand0t178.3    # /mnt/mmebackup 
echo "y" | mkqnx6fs -T runtime -b 32768 -i 65536 /dev/mnand0t178.4    # /mnt/icab 
echo "y" | mkqnx6fs -T media -b 4096 -i 32768 /dev/mnand0t178.5    # /mnt/adb 
echo "y" | mkqnx6fs -T runtime -b 16384 -i 8192 /dev/mnand0t178.6    # /mnt/gecache 
echo "y" | mkqnx6fs -T media -b 1024 -i 32768 /dev/mnand0t178.7    # /mnt/ols 
echo "y" | mkqnx6fs -T media -b 32768 -i 8192 /dev/mnand0t178.8    # /mnt/navdb 
echo "y" | mkqnx6fs -T media -b 32768 -i 16384 /dev/mnand0t178.9    # /mnt/media 
echo "y" | mkqnx6fs -T runtime -b 32768 -i 16384 /dev/mnand0t179    # /mnt/ota 

#write app to NAND
cat /net/mmx/fs/sda0/MMX2/app/50/default/app.img > /net/mmx/dev/mnand0t177

# reboot unit (disconnect power)
# you might need to clean SDWL from update.txt
```

### [How to prepare mifs-stage1.img and eifs.img for flashing](/MHI2 MHI2Q Harman Aisin/Recovery/MMX/How to prepare mifs-stage1.img and eifs.img for flashing/)


:::warning
follow link above to edit images

Stock FW update image will brick your unit!

:::

### Run normal FW update

To apply updates for IOC, tuner, LTE modem, …

Run a normal (standard) FW update after RCC and MMX are repaired to make sure, that all components have a fitting version for the FW on RCC/MMX.


## update.txt fatched from unit at start of full SWDL update of FW MHI2_ER_SEG11_P4709

MMX uses `/52/` folders which are linked to `/50/` in metainfo2.txt

```
CRC = 23220dbc
MetafileCRC = 1e48215eb13a83742bdea3dc5e785fc216ed19d8
initiator = HMI
train = MHI2_ER_SEG11_P4709
variant = FM2-H-ND-EU-SE-MQB
MUversion = 1447
RCCversion = U8987
AssemblyID = 0
ReleaseName = MHI2_ER_SEG11_P4709
startTime = 1970-01-01 01:09
LogSubDir = /HBpersistence/SWDL/Log/service/1
TransactionImageAddress = 0x540000
TransactionImageSize = 0x159208c
Source = SD1
Path = /
ReleasePath =
Phase3Device = IOC
Phase3Device = MuINIC
[Tuner\0\E2P\22\default\bootloader]=NO;0;default;0
[Tuner\0\E2P\22\default\application]=TODO;25755648;default;25755648
[DAB\0\Main\22\default\bootloader]=NO;0;default;0
[DAB\0\Main\22\default\application]=TODO;197632;default;197632
[RCC\0\ifs-emg\22\default\bootloader]=NO;0;default;0
[RCC\0\ifs-emg\22\default\application]=TODO;951;default;951
[RCC\0\ifs-root\22\default\bootloader]=NO;0;default;0
[RCC\0\ifs-root\22\default\application]=TODO;9495;default;9495
[RCC\0\efs-system\22\default\bootloader]=NO;0;default;0
[RCC\0\efs-system\22\default\application]=TODO;8325;default;8325
[RCC\0\dsp\22\default\bootloader]=NO;0;default;0
[RCC\0\dsp\22\default\application]=TODO;655755610;default;655755610
[IOC\0\Main\22\default\bootloader]=TODO;210;default;210
[IOC\0\Main\22\default\application]=TODO;8863;default;8863
[DUK107\0\ABT\42\default\bootloader]=NO;0;default;0
[DUK107\0\ABT\42\default\application]=NO;31;default;31
[GPS\0\Main\22\default\bootloader]=NO;0;default;0
[GPS\0\Main\22\default\application]=TODO;603;default;603
[MuINIC\0\Main\22\default\bootloader]=NO;0;default;0
[MuINIC\0\Main\22\default\application]=TODO;16909592;default;16909592
[MMX2\0\qb-recovery\52\default\bootloader]=NO;0;default;0
[MMX2\0\qb-recovery\52\default\application]=TODO;155;default;184
[MMX2\0\qb-primary\52\default\bootloader]=NO;0;default;0
[MMX2\0\qb-primary\52\default\application]=TODO;155;default;184
[MMX2\0\eifs\52\default\bootloader]=NO;0;default;0
[MMX2\0\eifs\52\default\application]=TODO;1657;default;1657
[MMX2\0\mifs-stage2\52\default\bootloader]=NO;0;default;0
[MMX2\0\mifs-stage2\52\default\application]=TODO;1657;default;1657
[MMX2\0\efs-sys\52\default\bootloader]=NO;0;default;0
[MMX2\0\efs-sys\52\default\application]=TODO;1657;default;1657
[MMX2\0\app\52\default\bootloader]=NO;0;default;0
[MMX2\0\app\52\default\application]=TODO;1657;default;1657
[MMX2\0\mifs-stage1\52\default\bootloader]=NO;0;default;0
[MMX2\0\mifs-stage1\52\default\application]=TODO;1657;default;1657
[MMX2\0\efs-pers\52\default\bootloader]=NO;0;default;0
[MMX2\0\efs-pers\52\default\application]=TODO;1;default;1
[DVD\0\Main\68\default\bootloader]=NO;0;default;0
[DVD\0\Main\68\default\application]=TODO;32;default;32
[MuTnrRef\0\data\0\default\File]=TODO;244;default;244
[RadioStationDB\0\data\0\default\File]=TODO;0;default;11010;MMX
[RadioStationDB\0\InfoFile\0\default\File]=TODO;0;default;11010;MMX
[SpeechAppRes\0\speech-common-data\0\default\Dir]=TODO;0;default;5645;MMX
[SpeechAppRes\0\speech-tts-app-data-vg\0\default\Dir]=TODO;0;default;5645;MMX
[SpeechAppRes\0\speech-sr-data\0\default\Dir]=TODO;0;default;5645;MMX
[SpeechRes\0\speech-tts-data_EU\0\default\Dir]=TODO;0;default;8638;MMX
[SpeechRes\0\speech-tts-data_ROW\0\default\Dir]=TODO;0;default;8638;MMX
[SpeechRes\0\speech-tts-voices\0\default\Dir]=TODO;0;default;8638;MMX
[MUConsistency\0\Data\0\default\File]=TODO;1447;default;1447
[ExceptionList\0\data\0\default\File]=NO;1;default;1
{Final}=TODO;
{RCC\Post}=TODO;
{RCC\Pre}=DONE;
```


# Open Question?!

If this observation and assumption made are correct.

* How can one see which folders are needed by a particular unit without looking at MMX partitions?
* Is this linked to the Hardware version written on the unit?
  * Looks like Porsche is using HW ID to differentiat between MHI2 and MHI2Q units. At least it looks like that if you look closer to the images. Maybe someone can support or destroy this "theory". At least for 5xxx MU i would see it like that.