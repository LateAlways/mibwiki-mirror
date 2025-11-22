# Installation via eMMC dump (VM QNX *.vmdk)

1. Mount the memory dump (`.vmdk`) in your Virtual Machine.


:::info
You should see it in the file manager under `/fs/xxx`

:::


2. Copy data from the Toolbox to an USB stick and mount the USB stick to your Virtual Machine.


:::info
You should see the USB stick as `/fs/usb0`

:::


3. Open the Terminal and execute `ksh /fs/usb0/install.sh`. It should recognise the Dump automatically and install the Toolbox.


:::tip
If you encounter problems (like freezing VM or errors like `Input/Output error` while the script runs, try to create a .iso (via [AnyToIso Lite](https://crystalidea.com/anytoiso)) from the contents of the toolbox and mount the iso via CD drive. You can then run `ksh /fs/cd0/install.sh`!

:::


4. Shutdown the Virtual Machine after it has finished.
5. Convert current Dump `.vmdk` image back to Dump `.img` image and write it back to your Unit.

## Convert

<https://mibwiki.one/share/b790e4dd-d831-4c5c-bc12-989540b8f067>