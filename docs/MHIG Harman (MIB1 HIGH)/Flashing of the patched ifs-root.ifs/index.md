# Flashing of the patched ifs-root.ifs

:::tip
The description below is for learning purposes only. The easiest way to apply

the patch is **[More Incredible Bash](https://github.com/Mr-MIBonk/M.I.B._More-Incredible-Bash/archive/refs/heads/main.zip)** via GEM>**m.i.b.>patch_unit_aio**

:::

## You will need:

* `ifs-root.ifs` from https://mibsolution.one/#/1/9/_pre MIB2/MHIG - HARMANor patched by you
* Good SD card
* D-Link DUB-E100 or UART (TTL) adapter and [PuTTY](https://www.chiark.greenend.org.uk/\~sgtatham/putty/latest.html)

  **GOOD TO  KNOW!** You can do it without any adapter with [M.I.B.](https://github.com/Mr-MIBonk/M.I.B._More-Incredible-Bash/archive/refs/heads/main.zip)

  \

## Connection to MIB


1. Use D-Link Dub-E 100 over USB or UART adapter over Quadlock pins to connect with RCC.
2. Login into the RCC console.

   Login: `root`

   Password: depends on MU version


:::info
While typing in the password you will not see characters. that's normal.

:::


3. Send `stfu` command to stop debug messages from being send via console.

## Create backup


1. Insert SD card is into `SD1` slot.
2. Mount the SD card: `mount -uw /net/mmx/fs/sda0/`
3. Backup EEPROM: `on -f rcc /usr/apps/modifyE2P r 0 10000 > /net/mmx/fs/sda0/eeprom.txt`
4. Backup FECs: `cp -rf /net/rcc/mnt/efs-persist/FEC /net/mmx/fs/sda0/`
5. Backup Variant: `cp -f /net/rcc/mnt/efs-persist/SWDL/Variant.txt /net/mmx/fs/sda0/`
6. Backup RCC flash: `cat /net/rcc/dev/fs0 > /net/mmx/fs/sda0/rcc_fs0`
7. Backup MMX flash: `cat /net/mmx/dev/fs0 > /net/mmx/fs/sda0/mmx_fs0`

## Flashing


:::warning
If you are working on bench without ignition on signal, main unit will turn off automatically after 30 minutes. That's you time gap to perform flashing if you want to risk it without ignition on signal.

:::


:::warning
Steps below assume that the new ifs-root.ifs file starts at address `540000`.

:::


1. Make sure that the SD card is in `SD1` port and new `ifs-root.ifs` image is in the root directory of the SD card.
2. Unlock flash: `flashunlock`
3. Flash new image: `flashit -a 540000 -d -v -f /net/mmx/fs/sda0/ifs-root.ifs`
4. Lock flash: `flashlock`
5. Wait 3-5 minutes for erasing, programming, and verifying the freshly flashed image.

## Reboot

Use [button combination](/General information/Useful documents/Key combinations and shortcuts/) to reboot your unit.