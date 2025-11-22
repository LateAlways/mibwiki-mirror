# JAVA HMI Patches. Remove PDC ParkPilot Popup

**How to remove "The ParkPilot is currently not available." Popup:**

Update:

**There are 2 possible easier Ways to remove the  RVC popup without Java patching. See last section.**

Introduction:

Installed a cheap china RVC camera and enabled RVClow by coding. Cam voltage is taken from reversing bulbs. When putting gear to R, cam gets powered and reversing cam is now shown in MIB2. By putting gear lever back to some forward gear, reverse light goes off, cam does not send video. But MIB2 & official RVC cam has some timer before switching back to normal MIB2 HMI fronted/switch off camera, most likely in order to avoid bad looking switching/syncing screens often during parking maneuver back and forth. Especially if you have a motorised hidden cam behind the logo on the boot lid that must moved. But as the cheap camera does not send any video during while the reverse light if off, video loss is detected. An annoying popup will be shown once per lifecycle "The ParkPilot is currently not available." You have to tap "OK" to close the popup, it does not disappear by itself....

Three options:

\-get mad by the popup on every drive...

\-buy an additional RVC Timer circuit that will power the cam some minutes longer than the reversing light is on ( and eventually drain your battery later...). lame.

\-get rid of this popup by patching, for free and for science.

Doing is similar to CP off patch:

Disclaimer: You may brick you MIB2. Do backup copy of all files, anytime. Have MIB2 console activated automatically on every start-up, Without need of using the Green Menu/Toolbox in case your patch fails and HMI does not start up any more and you are screwed. With console you can still restore your backuped IFS Files.

This patch was tested with MIB2 PQ cpuplus Skoda HMI SW Version 253 and SW Version 478 only. Other Versions might need a different Event ID and therefore different Patch!

**Lets go:**
\-Copy tsd.mibstd2.hmi.ifs e.g. from MIB2 /tsd/hmi to your working folder on PC
\-Use IFSTool.exe to "Unpack" the IFS File
\-Open the new tsd.mibstd2.hmi-unpacked.ifs in some HEX Editor
\-Search for hex string 11 18 27 b6 , it should exist exactly 2 times.
If you have less or more than 2 hits, abort here!
\-replace both hits by e.g. 11 FF FF B6
\-save file with different name
\-use IFSTool to "Pack" patched IFS file
\-copy to SD
\-backup your IFS in /tsd/hmi
\-mount disk as read/write
\-copy file from SD to your MIB2 /tsd/hmi folder
\-replace the old IFS file with your patched IFS
\-make sure attributes for file are like before (executable etc)
\-reboot and enjoy

**How was it done?
How to make own HMI Java patches?**
Needed Tools:
\-IFSTool.exe
\-https://github.com/spacemeowx2/jxe2jar (Python2.x !)
\-https://www.benf.org/other/cfr/
\-(http://java-decompiler.github.io/)
\-Some Hex Editor

\-use IFS tool to EXTRACT IFS file

\-find .\\tsd\\hmi\\ifs\\MIBHMI.jxe File in output --> Main HMI Functionality is implemented here

\-could not find much debug tooling for Intel JXE but there is for JAR. Attention they use different Endianess!

\-convert JXE to JAR with JXE2JAR.py e.g. py -2 JXE2JAR.py .\\tsd\\hmi\\ifs\\MIBHMI.jxe .\\tsd\\hmi\\ifs\\MIBHMI.jxe.jar

If you get CRC-32 exception here: PXE and JAR are ZIP Files but usually without using compression. But ZIP Files also contain CRC32 checksum of each file to check if extraction/uncompress went right. By applying binary patches like above or CP OFF , this CRC32 is not matching any longer. But MIB2 does not care about this.

Now here you have two options to get JXE2JAR to do stuff:

\-try a virgin  unpached, official IFS File instead or

\-patch the python library to ignore CRC32:

COPY zipfile.py from your Python 2.x library folder to the folder with JXE2JAR.py replace 'raise BadZipfile("Bad CRC-32 ....' with 'print("Bad CRC-32 for file...' in zipfile.py python will now use the local copy of the zip library and only print this error to the console instead of skipping the "bad"/already patched file.

\-now you can use tools like JD-GUI or CFR Java decompiler to get more human readable code back from CLASS Files within the created JAR ZIP file

e.g. Decompile with CFR (the whole JAR file, takes some time…):

java -jar cfr-0.152.jar --lomem true --outputdir somedir  .\\tsd\\hmi\\ifs\\MIBHMI.jxe.jar

Or open JAR as ZIP and copy the interesting CLASS files and decompile one by one

**Understand the RVC Popup Patch:**
Have a look for example at
MIBHMI.jxe.jar.zip\\de\\vw\\mib\\asl\\internal\\car\\parkassistence\\opsvps\\OpsVpsHsmTarget.class or better decompiled OpsVpsHsmTarget.java and find this function
sendPDCFailureEvent(....
....
if (this.pdcFailureActive && !this.pdcFailureNotificationDone) {
...
this.pdcFailureNotificationDone = true;
this.sendHMIEvent(10008);
....
Note: the sendHMIEvent(10008) is used some lines later again, so we must find it TWICE in the binary.

pdcFailureNotificationDone likely is for preventing the popup from coming a second time in one lifecycle. What could be done: initialise variable with true on startup, remove the "not" from the boolean expression, remove the sendHMIEvent.. But what is the easiest patch without adding/removing code? Manipulate the event ID 10008 and prevent from getting sent and trigger some action. 10008 decimal is 0x2718 (in JAR/Class) but in IFS/JXE the endianess is different so search for 0x1827 and replace with HOPEFULLY :-) not existing Event e.g 0xFFFF .

To be secure: Apply binary patch to OpsVpsHsmTarget.class and do decompile again with CFR to check you were patching the correct spot.

\-->now: this.sendHMIEvent(-1);  →ok

Well lets hope Event -1 is not used. At least it worked for me so far.

As the whole decompiling and JXE<->JAR process seemed to me not to be not very secure/reversible, you better patch the IFS directly, to be sure you only change the few identified bytes in the end. As you will find a lot of hits for 18 27 in IFS, take the opcode bytes before and after the value 1008 as found in the CLASS file: 0x11 0x27 0x18 0xB6 (Class/JAR) /0x11 0x18 0x27 0xB6 (IFS) to identify the very spots to patch in the much larger IFS or JXE Files.

Patch was tested with Skoda MIB2 PQ cpuplus HMI SW Version 253 and SW Version 478 only.
Other HMI Versions /Brands might perhaps need a different Event ID than 10008!
Tip: Version 478 was much more fun to decompile as  the decompiled JAVA files were more detailed with speaking variable names.

Have Fun and share your Patches with the Community

Edit: the Delphi STD 0231D firmware is using the same 10008 Event ID.

Edit2: if the author (jojothemojo) sees this message then I ask him to contact me on Telegram because I have some ideas about improving this HMI patch. My username is @Devian LLC .

Sorry i have not Telegram, contact me on Discord


# Update: Easier ways to get rid of RVC Failed popup without Java manipulation:

In /tsd/hmi/HMI/res you will find .res files.

## Method1: (tool in progress…)

In binary file popupinfo.res there is a possibility to set a Maximum Display Time for every popup. Setting it to 2000msec timeout will make it even dissapear before you even can see it during the RVC Screen time. Do not set it to too low values. The only annoying thing is to find out the correct entry Id, which might differ from SW to SW. You will need to get the "PopupInfoId" fo the popup "Picpf". Enable logging to your SD and open then RVC with the Popup. In the Traces you should now find when the RVC Failed Popup came up with this  "picpf" entry:

```javascript
INFO [0x40000, 0x4, 0xbbad0b83] consumeEvent (DynamicState): DynamicStateEvent - dynamicStateId: 228, command: 0, popupInfoId: 329
INFO [0x40000, 0x4, 0xbbad0b83] consumeEvent (PopupViewEvent): PopupViewEvent - dynamicStateId: 228, popupViewId: Picpf, command: 0, popupInfoId: 329
```

You  need the PopuiInfoId 329 to know that you will have to change the Entry 329 in the popupinfo Array in popupinfos.res with a hex editor.

More on that will follow soon, a tool to decode the popupinfo.res might be released in near future.

## Method2:(to be verified, be the first…)

**Untested but should also work. Give feedback if you tried this one and it did the trick, or not. Make sure you have a root console access to restore a backup of the file in case it did break more/the HMI startup.**

In asldatapool.res you should find only one occurrence of 10008 as Hex "18 27 00 00" (reverse hex Byte order of 10008 decimal) . This is the exitpoint of a java hash Map Data. If entry value ( incoming event 10008) and the exit value do no longer match, the event should be discarded as well before the Statemachine. so you could edit it to any value you like like "18 27 DE AD"


\