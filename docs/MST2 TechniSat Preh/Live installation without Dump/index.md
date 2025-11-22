# Live installation without Dump

* After you connected EMMC to SD adapter, add the Drive to the opened QNX Virtual Machine.


* Put the content of the Toolbox folder on  a USB drive and add the drive to Virtual Machine too.


* Open a command prompt,  write the command `ksh /fs/usb0/install.sh` and wait till the Toolbox will be installed.  \n**==IMPORTANT:==** ==you have to change the number of usb"0" to the one where the Toolbox is stored.==\n==Use the QNX File Explorer and check which USB is the correct one. If Toolbox is inside usb1 then you have to write== `ksh /fs/usb1/install.sh`\n
* Don't forget to change the cpu folder in Toolbox according to the installed firmware of your unit\n**https://github.com/olli991/mib-std2-pq-zr-toolbox/blob/master/README.md**

[https://youtu.be/rkEOTRyYsvI](https://youtu.be/rkEOTRyYsvI)