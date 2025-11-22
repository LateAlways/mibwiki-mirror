# Telnet connection

**==IMPORTANT!==** ==Do not install this on devices without navigation, otherwise you will get a cyclic reboot in update mode.==


Unpack MSTD_Audi_NAV_Telnet to FAT32 formatted SD and install like a firmware update.

Tested on **MSTD_EU_AU_P3151** navi unit.


:::info
If you want to install it with MSTD_SE/SK/VW navi units, just add variants at the end of the metainfo2.txt

ax88178 USB2Ethernet adapter with VID_2001/PID_3C05 (Dlink DUB-E100 rev.B) can be used. 

:::

[MSTD_Audi_NAV_Telnet.zip 1948](attachments/f1bf96ca-e467-4d45-967d-3da19f86af3b.zip)

Reference: <https://www.digital-eliteboard.com/threads/audi-a3-mib-s-supportthread-mib1-mstd.432868/post-4160763>


## Unlock Expert Boot Mode


:::info
Expert Boot Mode enables special boot menu in UART console on quadlock, where you can enable/disable loading of different drivers (keyboard/usb ethernet).

:::

To enable Expert Boot Mode enter in telnet:

```
\MMC\TOOLS\SetBootMenu -w E
```

Now you can connect via TTL adapter to quadlock and in UART console can do following:

```
U + Enter enable/disable keyboard support
D + Enter enable/disable UBS ethernet adapter support
0 + Enter enable/disable Expert Boot Mode
1 + Enter enable/disable booting from snapshot image
```