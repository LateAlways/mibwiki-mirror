# Recovering delphibin.ifs via TTL cable

:::info
The procedure below will only work if you installed [MST2 activator by Congo & Duke](https://mibwiki.one/doc/mst2-activator-by-congo-duke-BZSWMHrSq5) before

:::


1. Format SD card in FAT32 and write delphibin.ifs into the root of this SD card
2. Insert SD card to SD slot 1
3. Connect [TTL adapter to MMX of quadlock](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/Connecting TTL adapter to UART on quadlock/)
4. In putty open COM port of TTL adapter with 115200bps speed
5. Copy following string into windows clipboard:

   ```
   mount -t dos /dev/sdc0t12 /tmp/sd1 ; cp -Vf /tmp/sd1/delphibin.ifs /extbin/apps/bin/ ; MountPathSync /extbin/apps ; ls -al /extbin/apps/
   ```
6. Power on the unit via quadlock
7. Quickly, in putty window, press ENTER, press right mouse button to paste string into putty window and again press ENTER. You should see something like:

   ```
   cp: Copying /dev/sd1/delphibin.ifs to /extbin/apps/bin/delphibin.ifs
   100.00% (9316/9316 kbytes, 2498 kb/s)
   Sync of /extbin/apps
   Finished sync of /extbin/apps
   total 162503
   drwxrwxrwx  3 root      root           3584 Feb 01 07:00 .
   drwxrwxrwx 18 root      root           1536 Feb 01 07:25 ..
   -rwxrwxrwx  1 root      root         237947 Feb 01 07:21 ABTUpdate
   -rwxrwxrwx  1 root      root         384143 Dec 12  2019 APUpdate
   -rwxrwxrwx  1 root      root         482967 Feb 01 07:21 AndroidAuto
   -rwxrwxrwx  1 root      root         299599 Feb 01 07:21 AndroidAutoServices
   -rwxrwxrwx  1 root      root         221263 Feb 01 07:21 AppConnect
   -rwxrwxrwx  1 root      root         722167 Feb 01 07:21 ApplicationTestFramework
   -rwxrwxrwx  1 root      root          58612 Feb 01 07:21 BTReset
   -rwxrwxrwx  1 root      root         230967 Feb 01 07:21 BTUpdate
   -rwxrwxrwx  1 root      root           2322 Feb 01 07:21 CTracer.conf
   -rwxrwxrwx  1 root      root         644087 Feb 01 07:21 CarPlay
   -rwxrwxrwx  1 root      root         371199 Feb 01 07:21 CarPlayServices
   -rwxrwxrwx  1 root      root         694751 Feb 01 07:21 ClusterServices
   -rwxrwxrwx  1 root      root          71664 Feb 01 07:21 ConnectMCP
   -rwxrwxrwx  1 root      root         172763 Feb 01 07:21 DSPLogger
   -rwxrwxrwx  1 root      root         334643 Feb 01 07:21 DSPUtility
   -rwxrwxrwx  1 root      root          46515 Feb 01 07:21 DecodeAndSave
   -rwxrwxrwx  1 root      root         110207 Feb 01 07:21 DiagSwVersionMonitor
   -rwxrwxrwx  1 root      root         492087 Feb 01 07:21 DiagnosticsManager
   -rwxrwxrwx  1 root      root         564683 Feb 01 07:21 Exlap
   -rwxrwxrwx  1 root      root           5355 Feb 01 07:21 GPIOTool
   -rwxrwxrwx  1 root      root         337063 Feb 01 07:21 GPSUpdate
   -rwxrwxrwx  1 root      root         226059 Feb 01 07:21 GenericRecorder
   -rwxrwxrwx  1 root      root         158035 Feb 01 07:21 HKPCmd
   -rwxrwxrwx  1 root      root         169955 Feb 01 07:21 HKPLogger
   -rwxrwxrwx  1 root      root         234891 Feb 01 07:21 HKPUpdate
   -rwxrwxrwx  1 root      root         214723 Feb 01 07:21 INICUpdate
   -rwxrwxrwx  1 root      root          67159 Feb 01 07:21 MCPUtility
   -rwxrwxrwx  1 root      root           6919 Feb 01 07:22 MHUtil
   -rwxrwxrwx  1 root      root         765079 Feb 01 07:22 MOSTUpdate
   -rwxrwxrwx  1 root      root          42455 Feb 01 07:22 MTPDriver
   -rwxrwxrwx  1 root      root         471863 Feb 01 07:21 MediaHandler
   -rwxrwxrwx  1 root      root        3323711 Feb 01 07:22 MediaServer
   -rwxrwxrwx  1 root      root         108572 Feb 01 07:22 MemInfo
   -rwxrwxrwx  1 root      root          72564 Feb 01 07:22 MemThroughput
   -rwxrwxrwx  1 root      root         888335 Feb 01 07:22 MirrorLinkApp
   -rwxrwxrwx  1 root      root        1346199 Feb 01 07:22 Most
   -rwxrwxrwx  1 root      root         567999 Feb 01 07:22 MostCanRouter
   -rwxrwxrwx  1 root      root        3982279 Feb 01 07:22 NavServices
   -rwxrwxrwx  1 root      root        4902196 Feb 01 07:22 NavigationServer
   -rwxrwxrwx  1 root      root         742287 Feb 01 07:22 NetFrontNX
   -rwxrwxrwx  1 root      root        2807148 Feb 01 07:22 OnlineServices
   -rwxrwxrwx  1 root      root         431355 Feb 01 07:22 PackageUpdate
   -rwxrwxrwx  1 root      root         179839 Feb 01 07:22 PersShell
   -rwxrwxrwx  1 root      root        3996696 Feb 01 07:22 PhoneServer
   -rwxrwxrwx  1 root      root          20019 Feb 01 07:22 PrioWatchdog
   -rwxrwxrwx  1 root      root          99448 Feb 01 07:22 SDSoftwareTest
   -rwxrwxrwx  1 root      root         362307 Feb 01 07:22 SHController
   -rwxrwxrwx  1 root      root         752444 Dec 12  2019 SWaP
   -rwxrwxrwx  1 root      root         189927 Feb 01 07:22 Security
   -rwxrwxrwx  1 root      root        1136264 Feb 01 07:22 SensorHandler
   -rwxrwxrwx  1 root      root        3419363 Feb 01 07:22 SpeechManager
   -rwxrwxrwx  1 root      root         548367 Feb 01 07:22 SpeechServices
   -rwxrwxrwx  1 root      root         222219 Feb 01 07:22 StressServer
   -rwxrwxrwx  1 root      root         376955 Feb 01 07:22 SysServices
   -rwxrwxrwx  1 root      root          31087 Feb 01 07:22 SystemTimeApp
   -rwxrwxrwx  1 root      root         697235 Feb 01 07:22 TTIHandler
   -rwxrwxrwx  1 root      root         128639 Feb 01 07:22 TargetFileTransfer
   -rwxrwxrwx  1 root      root         293943 Feb 01 07:22 TcsTcpipManager
   -rwxrwxrwx  1 root      root          11875 Feb 01 07:22 ThermalManager
   -rwxrwxrwx  1 root      root          89131 Feb 01 07:22 TransportServer
   -rwxrwxrwx  1 root      root        3668571 Feb 01 07:22 TunerManager
   -rwxrwxrwx  1 root      root        1089447 Feb 01 07:22 UPNPManager
   -rwxrwxrwx  1 root      root         420975 Feb 01 07:22 UPNPServices
   -rwxrwxrwx  1 root      root         158035 Feb 01 07:22 VIPCmd
   -rwxrwxrwx  1 root      root         174235 Feb 01 07:22 VIPLogger
   -rwxrwxrwx  1 root      root         161319 Feb 01 07:22 VIPMisc
   -rwxrwxrwx  1 root      root          92244 Feb 01 07:22 VIPUpdate
   -rwxrwxrwx  1 root      root         150464 Feb 01 07:22 VPController
   -rwxrwxrwx  1 root      root          32408 Feb 01 07:21 airplayutil
   -rwxrwxrwx  1 root      root         643707 Feb 01 07:21 am
   -rwxrwxrwx  1 root      root         162367 Feb 01 07:21 btdiag
   -rwxrwxrwx  1 root      root        9539636 Apr 14  2023 delphibin.ifs
   -rwxrwxrwx  1 root      root         250419 Feb 01 07:21 devb-cd
   -rwxrwxrwx  1 root      root         192919 Feb 01 07:21 dm
   -rwxrwxrwx  1 root      root        2932204 Feb 01 07:21 dsp.bin
   -rwxrwxrwx  1 root      root          26779 Feb 01 07:21 dtcd
   -rwxrwxrwx  1 root      root           5195 Feb 01 07:21 eject
   -rwxrwxrwx  1 root      root          38531 Feb 01 07:21 i2c_drax
   -rwxrwxrwx  1 root      root          70699 Feb 01 07:21 i2c_usb_bridge
   -rwxrwxrwx  1 root      root          75764 Feb 01 07:21 iperf
   -rwxrwxrwx  1 root      root          45527 Feb 01 07:21 iv
   -rwxrwxrwx  1 root      root         157391 Feb 01 07:21 keysim
   -rwxrwxrwx  1 root      root           6877 Feb 01 07:21 mapprefs.xml
   -rwxrwxrwx  1 root      root        1837070 Feb 01 07:21 mcp.bin
   -rwxrwxrwx  1 root      root           5875 Feb 01 07:22 nstool
   drwxrwxrwx  2 root      root            512 Feb 01 07:22 ols_cert
   -rwxrwxrwx  1 root      root           2305 Feb 01 07:22 pvrtraceconfig.json
   -rwxrwxrwx  1 root      root          32659 Feb 01 07:22 sct
   -rwxrwxrwx  1 root      root         289239 Feb 01 07:22 splash
   -rwxrwxrwx  1 root      root         224163 Feb 01 07:22 tmtest
   -rwxrwxrwx  1 root      root         695711 Feb 01 07:22 tuner_utility
   -rwxrwxrwx  1 root      root          11191 Feb 01 07:22 vmem
   -rwxrwxrwx  1 root      root       19406432 Feb 01 07:22 vwjxe.ifs
   
   ```

   
:::info
   Note: if you will not be quick enough - just press Eject button on DVD and unit will reboot and give you one more chance :)

   :::

Good luck!

Reference: [https://www.drive2.com/l/672324698301807382/](https://www.drive2.ru/l/672324698301807382/)



:::tip
if you never installed MST2 activator by Congo & Duke, the console will be disabled and pressing ENTER will not show # prompt.\nIn this case you possibly have following variants:\n1. Connect SPI programmer to QSPI chip, read the image, corrupt STDB partition in this image and write the image back. Then BOOT1 will detect corrupted STDB and will automatically run EMB (emergency OS that will read metainfo2.txt from SD card and start automatic recovery of the unit)


2. Short sysboot5 (by other words L4 pin of DRA74 RCC chip) to GND. This will force IPL to start SD card recovery procedure (loading of custom IPL from SD card). 

:::