# Allow navigation maps from SD with any CID (aka CID patch)

Navigation on Technisat/Preh MIB STD2 PQ/ZR, Delphi MIB2 STD and Panasonic MSTD checks [CID](https://www.cameramemoryspeed.com/sd-memory-card-faq/reading-sd-card-cid-serial-psn-internal-numbers/) of SD card. For example following CID will be accepted `0941504D494253540210565936010201`

CID check is done on purpose so firmware distinguishes between regular SD with media data and SD with navigation data.

Adding of two strings with [the Toolbox for example](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/CID patch to allow maps from any SD/):

`[NavigateFromAllMedia]` \n `NavigateFromAllMedia = 42`

to `\tsd\etc\nav\mibstd2_nav_target.ini` , turns the CID check off.

But doing this makes media and navi data scanners to interfere with each other and in block 5F you will see OBD2 error: `2562 B126CF0 Navigation Database Error`

To avoid this, you can order  `32GB` Custom CID SD card from aliexpress.


:::info
Custom CID SD cards from aliexpress are low quality and usually randomly die in winter or very hot summer.

:::


:::tip
If you want to fit latest ECE AS maps onto 16GB SD card, you can remove unused languages from `/maps/00/sds/`

:::