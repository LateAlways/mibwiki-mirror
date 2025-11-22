# Conversion & Cross-flashing

:::info
So you want to upgrade your car to a MIB Harman unit, but the cheap ones online come from wrong country / brand? No worries, you can flash between (some of) them!

:::


For all of these, it's expected you've already got console access to your unit eg. via telnet/user/password or MIBToolbox/ssh


Also you really want a backup or your units current state before proceeding. Especially EEPROM is a good idea:

```bash
mount -uw /net/mmx/fs/sda0/
on -f rcc /usr/apps/modifyE2P r 00 8000 > /net/mmx/fs/sda0/eeprom.txt
```



:::tip
ALWAYS run a full backup (Backup + app.img) with [M.I.B](/MHI2 MHI2Q Harman Aisin/M.I.B. - More Incredible Bash/) before starting.

:::


There are different kind of cross flashing possible: