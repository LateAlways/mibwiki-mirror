# Region conversion

\

## Requirements


1. Quality SD card, `4GB` or more ([how to check SD card](/General information/Bench Setup & Tools/SD card testing/)),
2. `SWDL` patch,
3. New firmware

## Enabling Developer Mode

Developer mode access is required to perform region conversion.

Check out [5F - Enabling Developer Mode and Hidden Menu](/MQB CODING/5F - Enabling Developer Mode and Hidden Menu/) for more information about enabling developer mode in MIB units with OBDeleven, VCDS, VCP, CarScanner.

## Patching SWDL

SWDL app (`tsd.mibstd2.system.swdownload`)needs to be patched in order to accept custom `metainfo2.txt` file. Check out [SWDL Patch - install unsupported firmware](/doc/swdl-patch-install-unsupported-firmware-0ItY5zf31T) for information about different methods of patching SWDL app in Technisat units.

## Preparing new firmware

### ZR unit

Make sure to add your device variant to the variant list in the `metainfo2.txt` file.

Make sure to change CPU ID to the one from your device in the `metainfo2.txt` file.

> This can be done with the `metainfo_link_generator.py` file from [https://github.com/lprot/MIB-Tools](/doc/httpsgithubcomlprotmib-tools-cQkzBgdnPC). Place it beside the original `metainfo2.txt` file, run the generator and enter the CPU ID from your device.

### PQ unit

Make sure to add your device variant to the variant list in the `metainfo2.txt` file.

Make sure to change CPU ID to the one from your device in the `metainfo2.txt` file.

> This can be done with the `metainfo_link_generator.py` file from [https://github.com/lprot/MIB-Tools](/doc/httpsgithubcomlprotmib-tools-cQkzBgdnPC). Place it beside the original `metainfo2.txt` file, run the generator and enter the CPU ID from your device.

[Link to (nearly all) PQ Variants  ](https://mibwiki.one/share/8f584c31-3479-4e5e-a296-33f6e70bc109)

## New firmware installation


1. Insert SD card with prepared firmware in `SD1` port.
2. Turn on the ignition. If you have Kessy (keyless ignition) make sure that the key stays in the vehicle during the procedure (here's why: [Kessy & Updates](/General information/Kessy & Updates/)).
3. Turn on the unit.
4. Press and hold `MENU` button for 10 seconds to enter  `Testmode` menu
5. Go to `SWDL`, enable `Software Download Manual Download`.
6. Select `Start Download`.
7. Make sure all modules are selected.
8. Press `Start` and wait.

## Regional coding


:::info
Review module `5F` coding and adaptation values for navigation region, radio band region, SDS region, mirror link region. More details needed.

:::

## Other things that you might need to do

### Patching CP

### Patching SWaP

[TechniSat SWaP Patch with Toolbox](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Installation via eMMC dump (VM QNX  .vmdk)/SWaP patch/)

### Removing old map FEC/SWaP codes


:::info
If unit still has FEC/SWaP code for old navigation region it might not let you use navigation.

:::

### Uploading FEC/SWaP codes

[5F - Inserting FECs with OBDeleven](/MQB CODING/5F - Inserting FECs with OBDeleven/)

### Patching CID


:::info
If you don't have the original VW/Seat/Skoda SD card, you can patch CID and use any SD card for navigation database.

:::

[TechniSat CID Patch with Toolbox](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/CID patch to allow maps from any SD/)

### Clearing fault codes

[5F - Fix B201A fault code](/MQB CODING/5F - Fix B201A fault code/)