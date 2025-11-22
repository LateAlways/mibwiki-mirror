# SD card patch for MU0235

:::warning
The script below is just for learning purposes. Use [SD activator by Congo](/MHS2 Delphi/Hardware and recovery via EFU/MHS2 activator by Congo/) instead.

:::

# dlphi.sh

```bash
#!/bin/sh
echo "Remounting SD card in r/w mode"
mount -uw /net/mmx/fs/sda0/

echo "Making backup dir on SD Card"
mkdir /net/mmx/fs/sda0/backup/ 

echo "Persistence backup - ok"
cp -rf /net/rcc/persistence /net/mmx/fs/sda0/backup/

echo "SWaP backup - ok"
cp -f /net/rcc/ffs/extbin/apps/bin/SWaP /net/mmx/fs/sda0/backup/

echo "Backup /ffs/etc/*"
cp -rf /net/rcc/ffs/etc /net/mmx/fs/sda0/backup/

echo "delphibin.ifs backup - ok"
cp -f /net/rcc/ffs/ifs/delphibin.ifs /net/mmx/fs/sda0/backup/

echo "InstallationManager backup - ok"
cp -f /net/rcc/ffs/usr/bin/InstallationManager /net/mmx/fs/sda0/backup/

echo "mmx fs0 backup - ok"
cat /net/mmx/dev/fs0 > /net/mmx/fs/sda0/backup/mmx_fs0

echo "rcc fs0 backup - ok"
cat /net/rcc/dev/fs0 > /net/mmx/fs/sda0/backup/rcc_fs0

echo "APUpdateLight backup - ok"
cp -f /net/rcc/ffs/usr/bin/APUpdateLight /net/mmx/fs/sda0/backup/

echo "start_dlphi_script backup - ok"
cp -f /net/rcc/ffs/sbin/start_dlphi_script /net/mmx/fs/sda0/backup/

echo "SWaP patch - ok"
cp -Vrf /net/mmx/fs/sda0/patch_P2035/SWaP /net/rcc/persistence/SWaP/ && chmod 777 /net/rcc/persistence/SWaP/SWaP

echo "FEC list - ok"
cp -Vrf /net/mmx/fs/sda0/patch_P2035/el_dat_S.datsig /net/rcc/persistence/SWaP/ && chmod 777 /net/rcc/persistence/SWaP/el_dat_S.datsig

echo "envsettings backup - ok"
cp -Vrf /net/rcc/ffs/etc/envsettings /net/rcc/ffs/etc/envsettings.bak

echo "envsettings replace - ok"
cp -Vrf /net/mmx/fs/sda0/patch_P2035/envsettings /net/rcc/ffs/etc/envsettings && chmod 777 /net/rcc/ffs/etc/envsettings

echo "FINISHED - You can now remove SD Card"
rm /net/mmx/fs/sda0/dlphi.sh
shutdown -S reboot
```

# Reference

<https://mibsolution.one/#/1/9/MHS2 - DELPHI MIB-HS/Instruction>


\