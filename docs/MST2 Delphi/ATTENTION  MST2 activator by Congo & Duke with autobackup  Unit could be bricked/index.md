---
title: "ATTENTION! MST2 activator by Congo & Duke with autobackup: Unit could be bricked"
---

# ATTENTION! MST2 activator by Congo & Duke with autobackup: Unit could be bricked

# SD Activator by Congo & Duke


:::warning
BEFORE YOU READ FURTHER:


1.  On VW, press and hold `MENU` button on the display of your MIB2 for 3 seconds and then go to `Software Update/Versions` and take a look at `SW Train` string.

   On Audi use corresponding [button combo](/General information/Useful documents/Key combinations and shortcuts/) to open RED menu and then look into `Versions info`
2. 2 On VW, go to `MST2` and take a look at `D` string (on Audi take a look into `MST2_EU_VW_P0891D`).
:::

 ![](attachments/42c24972-0fd0-4cba-ba7c-c9d231c1ebd2.png)


:::tip
If your SW Train ends with `T` (for example `MST2_EU_VW_ZR_P0254T`) your unit is Technisat/Preh for which you need [MIB STD2 PQ/ZR Toolbox](/MST2 TechniSat Preh/SWaP patch/)).
:::

:::info
If you want to see more details about your SW Train, use http://mib-helper.com
:::

## Supported firmwares (trains)

All Audi and VW firmwares of any region with train matching pattern`MST2_xx_xx_xxxxxD`

Tested and confirmed FW versions: `P0120D`, `P0123D`, `E0220D`, `P0225D`, `P0227D`, `E0231D`, `P0314D`, `P0628D`, `P0631D`, `P0635D`, `P0642D`, `P9122D`, `P0867D`, `P0870D`, `P0876D`, `P0890D`, `P0891D`, `P0879D`, `P0883D`

## Installation


1. Format quality 4Gb+ SD card in `FAT32` with the smallest`cluster size` possible ( usually`4096 bytes`)
2. Unpack [activator with autobackup](https://disk.yandex.com/d/LjKOqapLPomY3A) onto the SD card and make sure metainfo2.txt is in the root.

### Removing DTC error 1555 (B201A fault)

After installation you will see DTC `1555` also known as`B201A` fault code in block `5F`. To remove/clear it, read