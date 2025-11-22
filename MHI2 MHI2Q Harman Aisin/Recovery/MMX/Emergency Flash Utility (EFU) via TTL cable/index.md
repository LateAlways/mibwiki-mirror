# Emergency Flash Utility (EFU) via TTL cable

:::info
Connect via TTL cable to [MMX UART on the quadlock](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/Connecting TTL adapter to UART on quadlock/). Press and hold shift+e while powering on the unit. This will run RED EFU (Emergency Flash Utility). Unit must receive the key presses before you see "Press <E> to run Emergency Flash Utility."

:::


1. Power on the unit via quadlock and keep pressing shift+e until you see something like:

 ![](attachments/475b945a-28ca-45e5-9106-24291b221be5.png)



2. As a confirmation that shift+e worked, you should see:

```javascript
[efu.Main] INFO: Emergency mode forced by user.
[efu.Main] INFO: Starting emergency flash utility
[efu.EmergencyFlashUtility] INFO: Starting EFU Version 2.5.0
[efu.EmergencyFlashUtility] INFO: Searching for internal update info.
[efu.EmergencyFlashUtility] INFO: Use external update info.
[efu.EmergencyFlashUtility] INFO: Please insert update media with update info or reboot.  
```

If IOC watchdog is active you will see a hint telling you how to stop MMX from the rebooting:

```
PDK: QC_CRM_BUILD_/local/mnt/workspace/CRMBuilds/QXA.QA.1.1-00010_7 (Built 2018/01/30-21:45:04-PST)ERROR DisplayControl_SanitizeInput[434] strncmp(hdr=!, SPLASH_METADATA_HEADER=SPLASH!) FAILED, HDR_MAX_BYTES=8
ERROR DisplayControl_StartSplash[767] DisplayControl_SanitizeInput() FAILED
ERROR DisplayControl_SplashInit[898] DisplayControl_StartSplash() FAILED
DisplayControl_SplashInit() FAILED
PDK: QC_CRM_BUILD_/local/mnt/workspace/CRMBuilds/QXA.QA.1.1-00010_7 (Built 2018/01/30-21:45:04-PST)
activating ringbuffer @ 0x96400000 size 16352
Qualcomm: fpsid=51406f10
coproc_attach(10): attach fe099cd0 (fe09bca4)
coproc_attach(11): attach fe099cd0 (fe09bca4)
rstp: rstp: Version 1.7.5
rstp: rm count: 1
rstp: [00] /dev/rstp/pwrmanlegacy_datanc, type DATANC, channels: 0xfe,
rstp:  using /dev/ser2 with 115200 baud
Creating a 100 MB ramdisk ramdisk mounted at /ramdisk
Path=0 -
 target=0 lun=0     Direct-Access(0) - ram  Rev:
31
31
Loading EHCI driver for USB1
start_qcore_eifs.sh: Proper BCT detected
Loading EHCI driver for USB3
qc8064_eifs.build::start_sdcard.sh: waitfor  /dev/nvsku/project 60000...
    0.01s real     0.00s user     0.00s system
qc8064_eifs.build::start_sdcard.sh: REVISION is 402
C sample or newer - change SDCard slots
qc8064_eifs.build::start_sdcard.sh done.
start CDROM driver...
/proc/boot/start_qcore_eifs.sh[347]: /sbin/devb-eide-mmx: cannot execute - No such file or directory
start_qcore_eifs.sh: start autorunner...
start_qcore_eifs.sh: autorunner started
Unable to start "echo" (2)
Unable to start "echo" (2)
Unable to start "echo" (2)
Unable to start "echo" (2)
Unable to start "echo" (2)
[efu.Main] INFO: Emergency Flash Utility (Production Build)
[efu.Main] INFO: Production Build
[efu.Main] INFO: Copyright (c) 2011 - 2015 e.solutions GmbH. All rights reserved.


[efu.Main] INFO: Starting graphical user interface
[efu.Main] INFO: Establishing IOC communication
rstp: register queue [0] 0xFE

[efu.Main] INFO: Starting monitor
[efu.Main] INFO: Read project identifier: 45323.
[efu.Main] INFO: Detected board revision 402.
screen create context OK
screen_post_thread is created tid:004
screen_draw_thread is created tid:005
[efu.Main] INFO: [EFU] screen size [1024 x 480]
[efu.IOC] INFO: toggleMmxIocGpio: toggle executed
login: [efu.Main] INFO: Powerstate: 0xe
[efu.Main] INFO: Warning: System is not in SWDL state.


############
System will reset automatically
enter 'donotreset' to prevent reset
############


[efu.Main] INFO: Emergency mode forced by user.
[efu.Main] INFO: Starting emergency flash utility
[efu.EmergencyFlashUtility] INFO: Starting EFU Version 2.5.0


login: root
Password:
```


3. Login, enter donotreset and restore damaged partitions [manually](/MHI2 MHI2Q Harman Aisin/Recovery/RCC/Manual Firmware Restore/)