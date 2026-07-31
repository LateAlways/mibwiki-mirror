# Updated MHS2 maps after end of life

MHS2 units have reached end-of-life and are no longer receiving navigation map updates from Audi. However, MHI2 (Harman) units continue to receive new map data, and their map format is largely compatible with MHS2 after some structural changes.

The MHI2-to-MHS2 Map Converter automates this process. It takes an MHI2 map archive and restructures it into the MHS2 directory layout, handling region data, speech resources, truffles, eggnog databases, and path remapping. Instructions for using the converter can be found below.



!!! warning

    **DISCLAIMER:** This software and any accompanying documentation are provided "as is" and "with all faults." The author makes no representations or warranties of any kind concerning the safety, suitability, lack of viruses, inaccuracies, typographical errors, or other harmful components of this software. There are inherent dangers in the use of any software, and you are solely responsible for determining whether this tool is compatible with your equipment and other software installed on your system. You are also solely responsible for the protection of your equipment and backup of your data, and the author will not be liable for any damages you may suffer in connection with using this software or the files it produces. You are also solely responsible for any modifications made to the software of your MIB system. The author will not be liable for any claims from the vendor of your vehicle or head unit concerning the use of third-party software, modified map data, or patched libraries on the MIB system.


!!! info

    **Notice**: This converter cannot generate valid content.sig files. The navigation binaries check for these files when verifying the navigation database. Fortunately, I have already taken care of this by patching the `/mnt/app/navigation/libPresentationController.so` library, but you need to upload it to your unit. I will provide a simple zip file with the payload below.

# Instructions:

## 1. Obtain an MHI2 map file

This can be done either on [here](/General information/Maps download links/), [mibsolution.one](https://mibsolution.one/#/1/19/MHIG%20-%20MHI2(Q)) or [mib-helper.com](https://mib-helper.com/show.php?all=maps#details) (make sure to scroll to the MHI2/MHI2Q section)

## 2. Download the MHI2 to MHS2 converter

You can get it on Github [here](https://github.com/LateAlways/MHI2-to-MHS2). Unzip the archive and place it somewhere. (e.g. on your desktop)

## 3. Put your maps inside the `Input` (case-sensitive) folder (if it doesn't exist, create one)

The folder hierarchy should look like this:

* Top level
  * Input (folder) **==(create it)==**
    * Mib1 (folder)
    * Mib2 (folder)
    * metainfo2.txt (file)
  * Output (folder) **==(create it)==**
  * LICENSE
  * main.py
  * README.md

## 4. Run the script

Open a terminal in the top level of the folder and run `python main.py`

## 5. Copy the `Output` folder contents

Copy all the files inside of your `Output` folder to the SD card.

## 6. Patch `libPresentationController.so` **==(THIS IS THE MOST IMPORTANT STEP)==**

Download the corresponding payload for your unit based on [your version](/General information/Useful documents/Key combinations and shortcuts/) (Check Red/Engineering menu) below:


!!! warning

    Make sure to download the right one, if not **this could make your navigation app stop loading entirely** until resolved!


!!! tip

    If your version is not supported, update your unit to one of the supported versions. (Recommended: MHS2_xx_AU_P1242) You can get the firmware files on [mibsolution.one](https://mibsolution.one).

### P2035/P2037

[P2035-P2037.zip 3874503](attachments/68b7881e-1cac-41f6-8784-80cee1e31ef0.zip)

### P1242

[P1242.zip 3817929](attachments/3b697581-cbc0-4b66-abcd-e5c93745f9aa.zip)

a. Unzip the payload file downloaded onto the sd card

b. Insert the SD Card into slot 1 (left side)

c. Wait for the unit to reboot

d. Once rebooted, connect the SD card to a computer and check whether a SUCCESS file or ERROR.txt file is present.


If you have an ERROR.txt file, the reason for the failure should be inside of the file, open it in notepad. Your unit was not affected by the patch. Make sure to resolve the errors mentionned

If you have a SUCCESS file, everything worked perfectly, you may remove the SUCCESS file and the backup folder from the SD card.

(You may need to reinsert the SD card after the reboot for the maps to load)

# Common errors:

The list is very limited as these are errors that I believe could happen, because they happened to me during development.

## "My navigation app no longer loads!"

You have very probably downloaded the wrong patch payload file for your unit. 


\