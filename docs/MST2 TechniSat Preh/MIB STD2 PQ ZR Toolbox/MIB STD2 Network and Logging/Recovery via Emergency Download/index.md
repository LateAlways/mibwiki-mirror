# Recovery via Emergency Download

:::info
This tutorial was made base on my personal experience with recovering Technisat MIB2 in vehicle, without bench setup.

I'm not sure if the procedure is the same for PQ units, for MIB2 Standard by Delphi, for MIB2High by Harman, and other MIB units.

:::

## Required

* Quality SD card, `4GB` or larger ([how to check SD card](/General information/Bench Setup & Tools/SD card testing/)),
* The firmware that is shown on the label of the cover of the unit (you should respect the region EU/US etc. and use any corresponding version. For example if firmware is `0456`, you can use any `04xx`. If `0356` then any `03xx` and so on),
* USB-UART signal converter,
* PC/laptop with PuTTY,
* Main unit removal keys,
* Torx driver,
* Tweezers.

## Procedure

### Prepare SD card


1. Format with `FAT32`, set smallest available cluster size.
2. Extract original firmware to the root of the SD card.

### Prepare main unit


1. Use removal key to unlock the unit and slide it out.
2. Disconnect QuadLock connector.
3. Remove top lid from the unit (4 visible screws, 1 hidden under the sticker).
4. Lift up the CD drive for main board access.

### Prepare and test serial communication


:::info
Check [Quadlock - pin layout](/General information/Bench Setup & Tools/Quadlock - pin layout/) for details

 ![](attachments/efd98ffd-fbbb-4116-b0e6-2377e4340943.png)

:::


 1. Set signal converter to `3.3V` logic level.
 2. Remove purple lock from QuadLock.
 3. Insert two terminals for `Tx` and `Rx` connection on the "J5" TTL terminals.
 4. Insert purple lock back to lock new pins.
 5. Connect `Tx` from MIB to `Rx` in converter.
 6. Connect `Rx` from MIB to `Tx` in converter.
 7. Connect `Gnd` from MIB to `Gnd` in converter.
 8. Connect converter to PC, open Device Manager, check what's the COM port number.
 9. Start PuTTY, set connection type to Serial, input port name, set baudrate to `115200bps`, start connection.
10. Connect QuadLock to confirm that the serial communication is working and you can see logs from MIB on your PC while the main unit is in boot loop.


:::tip
You can use crocodile clip for Gnd connection on the MIB housing. It's easier and faster than to use GND from the QuadLock.

:::

|  ![MIB end of the cable.](attachments/18f9e449-0131-4ec9-839d-74c56e1c6e35.jpg " =250x250") |  ![PC end of the cable and USB serial converter.](attachments/c2a5b6e1-d526-42c4-b376-4964070db601.jpg " =83x83") |  ![MIB connected to PC over serial.](attachments/b0abdbdf-0f1b-4e8b-8adf-a10f13e0bb30.jpg "right-50 =277x277") |  ![Live logs from normal boot procedure.](attachments/325df63d-4497-4fec-acbb-c25c52df3d37.jpg) |
|----|----|----|----|

2

### Enter recovery Menu


:::info
TODO: photo of the main board jumper

:::


:::warning
Use external power supply of 3A minimum or turn on the engine to prevent voltage drops and power issues while the procedure is in progress.

:::


1. Turn the ignition on. If you have Kessy (keyless ignition) make sure that the key stays in the vehicle at all times (here's why: [Kessy & Updates](/General information/Kessy & Updates/)).
2. Disconnect QuadLock.
3. Insert prepared SD card to `SD1` port.
4. Make sure that the serial connection on your PC is still active.
5. Use tweezers to short two point on the main board.
6. Connect QuadLock while the tweezers are still shorting the main board.
7. In Putty you should see a recovery menu with 7 options.

### Restore system


1. While in recovery menu press `2` then  in Putty to select `Emergency Download`.
2. MIB should start in `Emergency Download` mode and should immediately start system recovery. This will take around 30 minutes. It will perform download of around 100 firmware parts.
3. MIB will reboot before installing last 2 parts.
4. After the reboot you should see normal update screen and last 2 parts will be installed (`cpu::emergency` and `main::emergency`) and MIB will reboot.
5. Now you should boot into working system.
6. After the reboot you will see update raport, which you can can exit with the arrow in upper-right corner, next press `Cancel`. Unit will reboot.
7. Now start a normal update as some modules may still need updates.

   \

|  ![Bridging ZR main board to enter recovery menu.](attachments/b8f352a3-7eb5-4a2e-a1dc-f94894c9151a.jpg) |  ![PQ board connections](attachments/24b282b5-dc29-4ca8-a9e1-06b399256744.jpeg) |  ![Recovery menu available on PC.](attachments/4da0f2a5-60dc-4648-b63f-946ef659e386.jpg) |  ![Emergency download in progress.](attachments/1e6a4ead-cb55-4996-b18c-6f418c2a837f.jpg) |
|----|----|----|----|

## After the recovery

Emergency download will overwrite custom changes in your system, like CP patch, SWDL patch, SWaP patch, CID-lock patch, Toolbox, skins and sounds. You will have to apply patches again.

## Video tutorial

[https://youtu.be/Pdel-Kb-hZ0](https://youtu.be/Pdel-Kb-hZ0)