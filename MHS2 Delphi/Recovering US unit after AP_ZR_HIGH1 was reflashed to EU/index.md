# Recovering US unit after AP_ZR_HIGH1 was reflashed to EU

# Understanding the problem

US and EU units have different RCC NOR sizes 128Mb vs 64Mb and correspondingly the partitioning:

```
Firmware P2037
Board variant: FM2-HS-S-US-AU-MLE-DE
Board region: NAR
   OTP: prod                                                            NOR offset Size
   IPL: vers     57 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x00000000 0x00020000 0001
 BOOT1: vers     52 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x00020000 0x00020000 0001
 BOOT2: vers     52 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x00040000 0x00020000 0001
  VIP1: vers   1191 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x00060000 0x00280000 0020
  VIP2: vers   1191 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x002e0000 0x00180000 0012
  DIAG: vers    500 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x00460000 0x00080000 0004
   EMB: vers   1078 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x004e0000 0x00800000 0064
  STDB: vers   1078 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x00ce0000 0x00800000 0064
  STDF: vers   1078 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x014e0000 0x05640000 0690
  HOME: vers    113 , MHS2_NAR_AU HS_AP_180427_P 2018/04/27 14:58:18  : 0x06b20000 0x00080000 0004
Persistence partition (20Mb):                                           0x06ba0000 0x01400000

Firmwares K01xx/P01xx/K04xx/P04xx
Board variant: FM2-HS-N-EU-AU-MLE-DE
Board region: Europe
   OTP: prod
   IPL: vers     53 , MHS2_EU_AU HS_AP_150806_SOP1_P 2015/08/06 08:01:19  : 0x00000000 0x00020000 0001
 BOOT1: vers     50 , MHS2_EU_AU HS_AP_150806_SOP1_P 2015/08/06 08:01:19  : 0x00020000 0x00020000 0001
 BOOT2: vers     50 , MHS2_EU_AU HS_AP_150806_SOP1_P 2015/08/06 08:01:19  : 0x00040000 0x00020000 0001
  VIP1: vers    863 , MHS2_EU_AU HS_AP_160711_SOP1_K 2016/07/11 13:51:42  : 0x00060000 0x00200000 0016
  VIP2: vers    863 , MHS2_EU_AU HS_AP_160711_SOP1_K 2016/07/11 13:51:42  : 0x00260000 0x00200000 0016
  DIAG: vers    500 , MHS2_EU_AU HS_AP_150806_SOP1_P 2015/08/06 08:01:19  : 0x00460000 0x00080000 0004
   EMB: vers    906 , MHS2_EU_AU HS_AP_160711_SOP1_K 2016/07/11 13:51:42  : 0x004e0000 0x00800000 0064
  STDB: vers    906 , MHS2_EU_AU HS_AP_160711_SOP1_K 2016/07/11 13:51:42  : 0x00ce0000 0x00800000 0064
  STDF: vers    906 , MHS2_EU_AU HS_AP_160711_SOP1_K 2016/07/11 13:51:42  : 0x014e0000 0x02040000 0258
  HOME: vers    113 , MHS2_EU_AU HS_AP_150806_SOP1_P 2015/08/06 08:01:19  : 0x03520000 0x00080000 0004
Persistence partition (10Mb):                                               0x035a0000 0x00A00000

Firmwares K1xxx+/P1xxx/K2xxx/P2xxx
Board variant: FM2-HS-NDL-EU-AU-MLE-DE
Board region: Europe
   OTP: prod
   IPL: vers     57 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x00000000 0x00020000 0001
 BOOT1: vers     52 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x00020000 0x00020000 0001
 BOOT2: vers     52 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x00040000 0x00020000 0001
  VIP1: vers   1188 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x00060000 0x00280000 0020
  VIP2: vers   1188 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x002e0000 0x00180000 0012
  DIAG: vers    500 , MHS2_EU_AU HS_AP_161116_SOP2_P 2016/11/17 08:49:36  : 0x00460000 0x00080000 0004
   EMB: vers   1073 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x004e0000 0x00800000 0064
  STDB: vers   1073 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x00ce0000 0x00800000 0064
  STDF: vers   1073 , MHS2_ER_AU HS_AP_180305_P 2018/03/05 23:12:39       : 0x014e0000 0x02040000 0258
  HOME: vers    113 , MHS2_EU_AU HS_AP_161116_SOP2_P 2016/11/17 08:49:36  : 0x03520000 0x00080000 0004
Persistence partition (10Mb):                                               0x035a0000 0x00A00000
```

As you can see, when you update AP part of the RCC NOR of the US unit with the EU one, a repartitioning will happen and new persistence partition will be created by **format_flash.sh** (take a look at AP_ZR_HIGH1 folder on MHI2_ER_AU2035 update) and files from existing persistence partition (5F coding, datasets, SWaP/FECs etc) will be copied into new persistence partition.

All seems good but sound will not work as hardware and AP code is different between US and EU units.

And when you realise that and decide to do a back reflash of AP_ZR_HIGH1 from EU to US the InstallationManager will just update IPL, BOOT1, BOOT2 and VIP1 partitions and stuck on VIP2 as existing partition will be partially overwritten because of the offset shift.

When you reboot, IPL will detect that AP flashing went bad and will trigger EAU (Emergency Assist Utility):

 ![](attachments/912d557f-7940-407e-ba97-bbccde4088e4.png)

If you are lucky (smart enough) to have SD card with stock US fw inserted into SD1 slot, EAU will repartition the NOR correctly and you can finish the fw update from RED menu (you will have about 5 minutes to start that).

In case you have bad luck you will get a non booting soft brick. To fix it, connect TTL cable to MMX UART via quadlock, hold E in putty and Emergency Flash Utility will start. EFU will flash US fw from SD card:

 ![](attachments/4a6f750a-084e-408d-9cd3-aa211cda0c3b.png)