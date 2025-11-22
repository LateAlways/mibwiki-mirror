# Manual Firmware Restore

:::warning
Proceed only if you know what you are doing and always flash only from Emergency IFS (on RCC) or EFU (on MMX)!!!

:::

If some partitions of the RCC NOR, MMX NOR or MMX NAND are damaged, mixed FW partitions are installed or unit is infected by APG it might be useful to restore it manually.

Makes it sense to reflash completely or only in parts - depends on what was done to your MIB.


:::tip
Take files from stock FW update or extract out of RCC_fs0 and MMX_fs0 backup

:::


:::warning
Stock **mifs-stage1.img** and **eifs.img** **MUST** be [edited with hex editor](/MHI2 MHI2Q Harman Aisin/Recovery/MMX/How to prepare mifs-stage1.img and eifs.img for flashing/) (first bytes of these files should start from ANDROID! string).

If you ignore this and flash files starting from AÿDÿOÿDÿ you will brick the unit. Read how to change AÿDÿOÿDÿ→ANDROID! here.


Before running commands below, check the folder structure of your target FW as it might be different from the example below.

Make sure, that all files are available and commands fit your FW.

:::

Example:

```bash
#Run from RCC Emergency IFS
#Insert FW SD into SD1 slot

#RCC NOR flash
flashunlock
#normally not needed, skip | on -f rcc flashit -v -x -d -a 0x00000000 -f /net/mmx/fs/sda0/RCC/ipl/21/default/ipl-mib2.bin #normally not needed, skip
#on Firmware MHI2_ER_AU37x_P5089_MU1326 the directory is not 21 but 31
on -f rcc flashit -v -x -d -a 0x00540000 -f /net/mmx/fs/sda0/RCC/ifs-root/21/default/ifs-root.ifs
on -f rcc flashit -v -x -d -a 0x01D40000 -f /net/mmx/fs/sda0/RCC/efs-system/21/default/efs-system.efs
on -f rcc flashit -v -x -d -a 0x03D00000 -f /net/mmx/fs/sda0/RCC/dsp/21/default/AUDI_MIB_DSP.bin.bgz

#MMX NOR flash
#don't forget to change first bytes of mifs-stage1.img ANDROID!  41 4E 44 52 4F 49 44 21
on -f rcc flashit -v -x -d -a 0x760000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/mifs-stage1/70/default/mifs-stage1.img
on -f rcc flashit -v -x -d -a 0xA60000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/mifs-stage2/70/default/mifs-stage2.img
on -f rcc flashit -v -x -d -a 0x3600000 -p /net/mmx/dev/fs0 -f /net/mmx/fs/sda0/MMX2/efs-sys/70/default/efs-system.img

#write app to MMX NAND partition 
cat /net/mmx/fs/sda0/MMX2/app/70/default/app.img >/net/mmx/dev/mnand0t177

#clean SDWL queue
rm /net/rcc/mnt/efs-persist/SWDL/update*

# reboot unit (repower unit)
```

## Run normal FW update

To apply updates for IOC, tuner, LTE modem, …

Run a normal (standard) FW update after RCC and MMX are repaired to make sure, that all components have a fitting version for the FW on RCC/MMX.