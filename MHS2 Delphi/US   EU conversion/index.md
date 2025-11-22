# US > EU conversion

:::warning
**NEVER** use **MHS2_US2EU_P2037.sh** script and **metainfo2-US-EU.txt** floating around. Do NOT patch InstallationManager. All these "solutions" are wrong and will lead to different kind of problems. To do a correct US>EU conversion, strictly follow all the steps below which are valid for all **MHS2_US_AU_P01xx/K01xx/P04xx/K04xx/P1xxx/K1xxx/K2xxx/P2xxx firmwares**

:::


1. Download **MHS2_US_AU_P2037** and unpack onto FAT32 formatted [quality SD card](/General information/Bench Setup & Tools/SD card testing/).
2. Insert SD card into SD1 slot and update from RED menu standard way (without any modification of metainfo2.txt)
3. Refer to: https://www.drive2.com/b/650960912496213150/

Reference: [https://www.drive2.com/b/650960912496213150/](https://www.drive2.ru/b/650960912496213150/)

[metainfo2.txt 229951](attachments/83acd675-ce11-44e3-aa3a-82c8f8ef5121.txt)


## Changing variant on old trains


:::info
**GOOD TO KNOW:** On trains lower than 1xxx (01xx and 0x4xx) it may be possible to change the variant with following shell command:

:::

```
on -f rcc /ffs/extbin/apps/bin/VIPCmd ee vw VARIANT_STRING FM2-HS-N-EU-AU-MLE-DE
#to check variant
on -f rcc /ffs/usr/bin/APUpdateLight -i
```


:::info
To run the commands above you can telnet on port 23 (to MMX) via dlink and login via root

Alternatively you can put these commands into dlphi.sh in SD card root and reboot the unit to run it.

:::

## Meaning of symbols in the third position of the variant string (features):

```
D=DAB
L=LTE
N=Navigation
S=SiriusXM
```

## Syntax of the VIPCmd command:

```
on -f rcc /ffs/extbin/apps/bin/VIPCmd
****** VIPCmd Tool for Sending Shell Messages to VIP ********

usage: VIPCmd [cmd] [arg0] [arg1].
example: VIPCmd help
example: VIPCmd trace 255 5
```