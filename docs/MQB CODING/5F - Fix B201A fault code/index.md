# 5F - Fix B201A fault code

[https://www.youtube.com/watch?v=0tpPm-ucAwc](https://www.youtube.com/watch?v=0tpPm-ucAwc)



:::info
Fault `B201A` appears after firmware update.

:::

## How to


1. `5F` → adaptation → channel: **Confirmation of installation change** → read
2. Copy current key value.
3. Paste key value into the I'm So XORy tool: http://mib-helper.com/im-so-xory/.
4. Generate new key.
5. `5F` → adaptation → channel: **Confirmation of installation change** → paste new key → save
6. `5F` → faults → clear


:::info
Saving new key can fail (OBDeleven) or old value can be visible (VCDS). That's normal. Attempt of saving new key is enough for MIB to check if the key is valid and change fault status from `permanent/static` to `sporadic`.

:::


:::tip
You can calculate new key manually by XORing old key with `DEC 51666` / `HEX C9D2.`

:::

## Good to know if stuck at firmware update summary

If you have a faulty touch screen and can not exit the firmware update summary, you can try to perform the above procedure and hope that clearing the fault will also reboot the unit into normal operation mode.

[https://youtu.be/ocxY9fMtIkU](https://youtu.be/ocxY9fMtIkU)