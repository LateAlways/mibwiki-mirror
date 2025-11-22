# GEM.jar - AppDevelopment.jar

:::info
Responsible for displaying GEM and building up menu structure from \*.esd files

:::


Both located in `/net/mmx/mnt/app/eso/hmi/lsd/jars`

| MU version | train | file name | version | SH1 |
|----|----|----|----|----|
| 0335 | MHI2_ER_AUG11_P0040 | AppDevelopment.jar | Component-Version: 3.4 | 3725aad3ed38cd72a132e76908db43b9f49dd19c |
| 1119 | MHI2_ER_POG11_K4185 | AppDevelopment.jar | Component-Version: 4.12 | 43024c7ba4c452fc0bda70c9cd91adb28027d494 |
| 1329 | MHI2Q_ER_AUG22_P5092 | AppDevelopment.jar | Component-Version: 4.14 | 4826f6b657faa144eacc5ddaecb4dd5430eb8f46 |
| 1421 | MHI2_ER_AUG22_K2161 | AppDevelopment.jar | Component-Version: 3.6 | 0ebe8b0226b27fd9f5124cc406559c5fe84d6e34 |
| 1425 | MHI2_ER_AU57x_K3663 | AppDevelopment.jar | Component-Version: 4.11 | 2e2a11083b6998db760bcbfbb04c552786b4d56d |
| 1429 | MHI2_ER_AU57x_K2589 | AppDevelopment.jar | Component-Version: 4.0 | ae2645648d0a8dec1500af9df21fc556d91f25d2 |
| 1438 | MHI2_ER_AUG22_K3346 | AppDevelopment.jar | Component-Version: 4.5 | ffc63dca034d61fa8d7aa2cf000a5a08f78e4725 |
| 1440 | MHI2_ER_SKG13_P4526 | GEM.jar | Component-Version: 4.12 | 43024c7ba4c452fc0bda70c9cd91adb28027d494 |


So far, all checked GEM.jar or AppDevelopment.jar have the same internal structure.

* MU1438 4.5st is running fine on MU1440 unit
* MU0335 3.4 is not starting on MU1440 unit
* MU1421 3.6 is not starting on MU1440 unit
* MU1429 4.0 is starting on MU1440 unit, but is lagging full touch screen support

→ Downgrades below v 4.0 are not working


Upgrades from 3.X to 4.X seem to work so far:

* MU1421 3.6 to 4.12
* MU0335 3.4 to 4.12


Older GEM versions do not support all elements used in latest \*.esd files

Open \*.jar in e.g. 7zip - `\de\audi\gem\elements\`

 ![left MU0335 - middle MU1429 - right MU1440](attachments/bb79c7ea-25ad-4764-b610-41c58add97a1.png)



:::info
"Bit-Elements" were only introduced with later GEM versions (starting 4.0). Only 4.11+ support Bitvalue (used a lot by M.I.B).

GEM will fail loading \*.esd, as soon as an unknown element is parsed.

:::


### M.I.B 3.0.0 BETA on GEM 3.6

\*.esd files parser stops at 1st encounter of bit-element

Still, backup_restore and patch_ifs_root_aio are usable.

 ![](attachments/957befaa-31bf-4b68-af16-3516516d2916.png)