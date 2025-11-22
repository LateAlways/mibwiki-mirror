# Parametrization with OBDeleven

:::info
This works only for Android version. iOS version does not support direct EEPROM access.

:::


:::info
In this example I'm going to show how to enable VIM under `0x240` address.

:::

## Requirements


1. OBDeleven app ([Android](https://play.google.com/store/apps/details?id=com.voltasit.obdeleven)),
2. OBDeleven PRO or ULTIMATE license,
3. OBDeleven dongle.

## Parameter read/write


1. Connect with the vehicle.
2. Go to list of modules.
3. Select module `5F - Multimedia`.
4. Select `EEPROM` option at the bottom of the list.
5. Enter `Address(hex) = 240` and `Length(dec) = 30`. This will read `30` hexdec bytes, starting from the `0x240` address.
6. Press `R` at the bottom of the screen to read data.
7. You will get something like this:

   `00 00 06 02 06 02 00 00 00 14 06 02 FF 00 FE 00 FF 00 06 02 06 02 FF 00 00 07 45 34 BD C7`.
8. Change it to something like this:

   `ff 00 06 02 06 00 00 00 00 00 ff 00 ff 00 ff 00 ff 02 ff 02 05 00 ff 00 00 00 30 34 97 5b`.

   You can see that couple `00` and `06` are changed to `ff`.  Basically this means that speed limits for certain features were changed from `0km/h` and `6km/h` to `255km/h`.


:::info
Last `4` bytes (`30 34 97 5b`) are version ID (`ASCII`) and checksum (`CRC-16 CCITT-FALSE`).

:::

## How to read different parameters

Unlike other applications. In order to read the dataset, not only must you specify which dataset you would like to read within OBDeleven, but you must also tell it the length of the dataset. Stating the wrong byte length results in an error. There are some missing lengths, if found. It is greatly appreciated if these can be filled out.

| Dataset / Address (hex) | Length / Bytes (dec) |
|----|----|
| `0x000240` | 30 |
| `0x000280` | 22 |
| `0x002D00` | 389 |
| `0x000440` | 18 |
| `0x003000` | 1330 |
| `0x000460` |    |
| `0x003600` | 633 |
| `0x000DA0` | 60 |
| `0x003F00` | 404 |
| `0x000700` | 254 |
| `0x002F00` | 102 |
| `0x003B00` | 55 |
| `0x004500` |    |
| `0x007000` |    |


## Limitations

* OBDeleven does not allow to upload parameter into empty space. It can only write modification to address that can it can read. So in a case of an empty address, currently OBDeleven is not able to write data over there.
* OBDeleven does not allow to copy/paste data in parameterization. Which makes sending long datasets a real pain, because you need to type it in manually, byte by byte…

## Example in Audi Q3 with RMC system

[https://youtu.be/jsi80Yr3aoY](https://youtu.be/jsi80Yr3aoY)

## Background reading

<https://forum.obdeleven.com/thread/7316/eeprom-facility>