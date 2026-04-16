# error - Stuck or Freeze in (old) Bootscreen after update

:::tip
Just set first byte `17` and `18` to `00 00`  (vcds, obd11, odis) reboot, if boots into menu proceed with fw update. then make sure IOC is set to Y  both app and bolo. when fan is updating ioc, after first ioc process will you get again working swdl process and see last part updating ioc, after reboot secuence is starting finalscript and update is done…( make allways sure having dlink, ugreen or ax88772 based lan usb) you get faster help if you know right people))

:::


OLD))))My case: `5F0035020V`, `HW41`, `SW0123` (`MHI_ER_SEG11_S0257`).


Byte `18`: HEX `05`: Bit 0,2 (Experience Skin - important for error!) → Update to 1447_AIO

After 6 modules in update process, Speech TTS voices were last after around 20 min, the unit reboot and stuck in bootscreen (old = Seat Sound, e.g. Experience Logo). I wait for another 15 min and nothing happen.


To resolve the issue have to change Byte `18` to HEX `01`: Bit `0` (FR) or HEX `02`: Bit `1` (Cupra) and restart unit (hold power button).



---

(Additionally mandatory for `5F0035043A`, `HW42`, `SW0319` (`MHI2_ER_SEG11_S2105`)) → Update to 1447

Byte `17` = HEX `02`: Bit 1,1 (old FR skinning skin - important for error!) after updating to 1447

To resolve the issue change Byte `17` = HEX `04`: Bit 2,1


---


You can change that not only with vcds, obd11 or odis. D-Link DUB-E100 works also and the commands are

`on -f rcc /usr/apps/modifyE2P w 102 04 01`

`on -f rcc /usr/apps/mib2_ioc_flash reboot`

`04` is byte 17

`01` is byte 18

and `01` sets to fr in longcoding……..

`02` Cupra

`0A` New Cupra Logo Bronze



:::warning
DON'T DO IT TO EARLY IN UPDATE PROCESS, THE UNIT WILL STAY 2-3 TIMES IN BOOTSCREEN FOR SOME MINUTES!!!!!!

:::


In my mind the failure occure because the old bootscreen isn't compatible with the newer software (without adaption maybe).