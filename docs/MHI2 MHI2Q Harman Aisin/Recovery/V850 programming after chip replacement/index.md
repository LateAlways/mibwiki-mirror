# V850 programming after chip replacement

:::info
Tested on MHIG and MHI2 Harman and should work everywhere where V850 is used.

:::

**You will need**:

FT232 TTL adapter and Renesas Flash Programmer V2.05.03

Alternatively: Orange5 with it's own software


**Make the connection**:

* On the unit side you can make the connection directly to the chip or find test pads on the board with a multimeter:

 ![](attachments/cb6dcde3-f370-417d-9d17-ba2489537b04.jpg)

 ![](attachments/55923905-86e1-4440-b3ed-efb31c72e0c4.jpg)


:::info
Some MHI2 (like JP AUG22) do not have V850 RST on the 24 pin connector. Use multimeter to find the test pads on the motherboard and directly solder there 

:::

* On the FT232 TTL adapter side:

 ![](attachments/8c2cf1bb-00b3-44e2-92a4-3c86a0fb6a22.jpg)

On the photo above, ft232 adapter has following pinout(from top to the bottom): \npin1=GND, pin2=CTS, pin3=VCC/3,3V, pin4=TX, pin5=RX.

pin2 (CTS) supplies 3,3V to FLMD0 that forces V850 to go into flash programming mode when you power on the unit via quadlock. By other words unit will stay powered off as long as FLMD0 is in high state.


:::info
Switch/button must be pressed after each action you do in the flashing software, like READ, WRITE, BLANK, SECURITY

**WARNING!** Do NOT use pin3 of ft232 as RESET and FLMD0 at the same time as the press of the switch will reset the ft232 adapter as well!

:::

**Power on the unit via quadlock, run Renesas Flash Programmer V2.05.03 and use following settings:**

* Full mode:

   ![](attachments/cdf1fbbe-60d2-4e23-accc-221e97d7cb5e.jpg)
* Select chip:

   ![](attachments/286ebd50-7d8e-4fe1-a8f9-09f85814c6ea.jpg)
* Select COM port (check in Windows Device Manager):

   ![](attachments/bac12089-59a5-451e-93fd-20c0dc33115a.jpg)
* Interface Speed 115,200bps, Frequency (4.00Mhz):

   ![](attachments/a3e20039-b082-42db-83af-66f0f8431af4.jpg)

**Select V850bolo_MQB.bin:**


 ![](attachments/aedde788-ba13-4a01-bba8-e29843cc65d1.jpg)

After you flashed the bolo, power on the unit, and update IOC App [manually](/MHI2 MHI2Q Harman Aisin/Recovery/Manual IOC Update via telnet or TTL cable/) or run a full firmware update from SD card