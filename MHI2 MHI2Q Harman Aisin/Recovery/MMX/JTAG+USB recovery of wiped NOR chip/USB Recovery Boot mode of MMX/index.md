# USB Recovery Boot mode of MMX

To use the USB recovery mode, a [USB Type-A Male to USB Type-A Male cable](https://www.amazon.com/UGREEN-Transfer-Enclosures-Printers-Cameras/dp/B00P0E3954) will be needed to plug the standard MMX USB port into a PC/Laptop USB port. Having this MMX cpu should appear in Windows Device Manager as USB device named as APX.


To be safe you should probably disconnect the 5V line in the USB cable somewhere to avoid any conflicts in the 5V rail between your PC and the MMX, eg:


\
 ![](attachments/c6c45ea1-6ca0-427c-81b3-ab0ecced4352.jpg)


When you plug in the USB and power up the MIB unit, you should get a new device popup in Windows. If this doesn't happen, either your cable isn't correct, or more likely the Tegra isn't booting in CPU mode.

The USB recovery (RMC) mode can be forced with a jumper on the main PCB in the MIB2 unit, but this does require unscrewing the bottom cover. You'll need a T8 torx for this.


The top cover is the smaller cover, this is the one with the big HARMAN label on the. This one will need to come off to get the MMX jtag port.


The bottom cover includes the sides of the unit - this is the one that needs to come off to get to the USB jumper.


You should be able to take out all the screws on the bottom then pull just that bottom/sides off in one go, levering it against the ports and the front cover. It can take a bit to get off as there's heatsink putty that kind of sticks the bottom cover to some of the chips. If you wiggle it back and forth enough it should come free.


Once you get it off though, the main PCB will be exposed:

 ![](attachments/9f46df82-d060-4cb8-9107-cb3b4c95f3af.png)

Jumping these two pads together while powering on the MIB will force the MMX to boot in USB recovery mode.


 ![](attachments/3d59fb91-3f3e-4151-bb77-78d848564764.jpg)

If you expect to use USB recovery mode often then you can solder a switch there:

 ![](attachments/3028a58c-1f43-48df-a9fa-c1bc3e723805.jpg)

Now, with the jumper/switch turned on (shorted out) while turning on the MIB, with USB cable plugged in, you should get a new device "APX" show up on windows.


Install tegram_rcm_usbpcdriver_32_64.zip and the device should then show up in the device manager as "NVIDIA USB Boot-recovery driver for Mobile devices"

[ tegram_rcm_usbpcdriver_32_64.zip](attachments/874199d3-1a31-4ec9-a07c-a8b008268529.zip)

Once driver is installed you can run nvflash_3.1.zip

[ nvflash_3.1.zip](attachments/9ec7bf62-a191-425d-84da-d5c816c1bd30.zip)