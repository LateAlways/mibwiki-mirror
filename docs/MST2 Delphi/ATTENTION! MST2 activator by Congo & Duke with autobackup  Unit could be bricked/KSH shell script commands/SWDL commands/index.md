# SWDL commands

In **/extbin/swdl/** is possible to create empty folders as SWDL commands:


**clamp_30_protection** = probably stop watchdog (created during update)

**mmc_update_marker** = probably update process (created during update)

**mmc_wait_sync_marker** = probably update process (created during update)


> drwx------  2 root      root            512 Feb 01 07:04 clamp_30_protection
> drwxrwxrwx  2 root      root            512 Jan 01  1970 mmc_update_marker
> drwxrwxrwx  2 root      root            512 Jan 01  1970 mmc_wait_sync_marker


I had unit stucked on update screen. In **/extbin/** were folders **apps** (full size) and **apps.bak** (just some MB). I guess that after removing **mmc_update_marker** and **mmc_wait_sync_marker** and restart, unit deleted full size **apps** folder and moved **apps.bak** to **apps**. So unit is writing on serial that some libraries are missing and I have black screen with no telnet. Unit is not restarting because I kept **clamp_30_protection** in **extbin** (probably mistake). So I guess there is only way to fix it by reading emmc.


In **metainfo2.txt** is part where is **EXTBIN_APPS.bin** extracted into **/extbin/apps_bak/** so I think it's related. But someone who knows more can fix the information.


 ![](attachments/60636065-1f6d-4614-98dc-5429cf364e47.JPG)


\