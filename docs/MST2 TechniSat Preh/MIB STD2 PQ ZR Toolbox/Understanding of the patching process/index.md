# Understanding of the patching process

:::tip
The simplest way to patch is to install MIB STD2 PQ/ZR Toolbox

Legacy methods can be found here

All information below serves only for the learning purposes.

:::

Getting a "Patch" done always consist of two main steps:


1. Getting the patched files ready
2. Getting these files on the unit


For 1. there are different types of "**manual**" ways to build your patch:

* all started with manually patching system files in programs like IDA
* Nowadays, there are ready to use [tools](https://mibsolution.one/#/1/9/MST2%20-%20TechniSat%20Preh/Tools) like JXETools, IFSTool and some python scripts


Same applies to 2., where all started with changing these files via physical access to EMMC → dumping raw image, file system extraction, file system manipulations and writing back to EMMC.

We are now in the convenient situation, that most systems can be "opened up" via SD card to enable direct patching, file copying and telnet access.


All this made possible by:

* Update-Approval_SOP4_signed - SD card solution
* and a lot of brain power!



:::info
One of the ways to apply these tools is described in **[DIY - How to create a SD Patch](https://mibwiki.one/share/5260f4df-06c1-4e34-9cd8-2514b4b794f2)**

:::

# Now

By utilizing a combination of knowledge based on patch tools, online approval and [MIB STD2 Toolbox](/doc/technisat-mib-std2-toolbox-installation-GIgwX2camY) we have it even better today!


* Pre/self-created patches can easily be uploaded to the unit by utilizing [MIB STD2 Toolbox](/doc/technisat-mib-std2-toolbox-installation-GIgwX2camY) functions
* MIB STD2 Toolbox is even able to directly patch CP, SWAP , SWDL (some restrictions apply, see the github repository) and do other cool stuff.

  \

Check the nested documents below for more details about these solutions.