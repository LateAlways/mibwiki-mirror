# 5F - Rear View Camera (RVC-LOW) installation

:::warning
Units `xxx 035 819` and `xxx 035 820` does not support RVC (no video input support).

:::


:::tip
Most likely any NTSC camera can be used as RVC-LOW with MIB units.

For example: [Viofo dashcam with A/V out](https://youtu.be/6qY7-JNMQ8c).

:::


:::info
RVC-LOW have static green guidance lines.

:::


:::info
RVC-LOW doesn't have any calibration/parametrization capabilities.

:::


:::info
RVC-LOW is not connected to CAN-BUS network. It's triggered by reverse light signal.

:::


:::info
As an alternative you can [install RVC-HIGH camera](/MQB CODING/5F - Rear View Camera (RVC-HIGH) installation/) with more features.

:::

## Coding

`5F` → Long Coding → Byte: `19` → Bit: `4` → `enable`

`10` → Long Coding → Byte: `02` → Bit: `4` → `enable`


:::info
Some cars will have module `0x76` available instead of `0x10`.

:::


:::tip
Since the camera is triggered by reverse light signal, one should also adjust the setting of the reverse light circuit. By default reverse light bulbs are powered with PWM signal with \~90% duty cycle, which can create interference on the video signal. Changing the dimmwert to `100` or `127` should fix this issue.

:::


> Source: <http://ilovecarmods.com/vw/discover-media-mib2>

## MIB pinout

MIB → Quadlock  → connector B (blue) → pin `6` → video signal

MIB → Quadlock  → connector B (blue) → pin `12` → shield


:::tip
[VW Golf MK7 5G - Current Flow Diagram - low rvc.pdf](attachments/17f758e1-9198-4f8b-be41-6f62de0b09e6.pdf)

:::


:::tip
[Quadlock - pin layout](/General information/Bench Setup & Tools/Quadlock - pin layout/)

:::