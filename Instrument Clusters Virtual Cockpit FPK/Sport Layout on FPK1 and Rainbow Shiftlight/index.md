# Sport Layout on FPK1 and Rainbow Shiftlight

:::warning
this procedure is forcing data into the instrument cluster assuming that the instrument cluster firmware supports the feature and uses this memory address for those features.

:::


:::tip
Setting to `RS` will make the rev counter end at 8kRPM. `S` rev counter can end at 6kRPM making it more suitable for diesel cars.

:::

## ODIS procedure


1. Connect with module `0x17` ,
2. Change Session to `Developer mode`,
3. Enter Security Access code `20103`,
4. Go to `Special Function` → `Hex Service` and send one of the commands:

   `3D 14 03 00 3C 09 01 01` - for S style;

   `3D 14 03 00 3C 09 01 03` - for RS style;

   `3D 14 03 00 3C 09 01 00` - for stock setting;
5. If write fails and reply is `7F`,  check if engine is off, hood is open,
6. Send `11 01` to reboot instrument cluster.

## CarScanner procedure

<https://www.drive2.ru/b/637736536393130752/>

CarScanner now supports this function for MQB vehicles.

## VCP Script

Following script was tested and deemed safe, as it also creates a backup of the values changed, tests for requirements and even allows for different modes to be set:

<https://mega.nz/file/etZiWI6a#eaHBINSIwk1K5EYRTMZpaRiGKkRi34gGtBN7uMQ-8eY>

## Raw UDS procedure


:::warning
work in progress

:::


1. Connect with module `0x17`

   UDS command: `???`.
2. Change session to `0x4F  `

   UDS command: `10 4F`.
3. Security access with `20103`

   UDS command: `27 ???`.
4. Read from memory; address `03 00 3C 09`, len: `1` (this is for backup)

   UDS `ReadMemoryByAddr` command: `23 ???`.
5. Write to memory address `03 00 3C 09`, len: `1`, data: `03`

   UDS `WriteMemoryByAddr` command: `3D 14 03 00 3C 09 01 01`
6. Read again to confirm changes.

   UDS `ReadMemoryByAddr` command: `23 ???`.
7. Reboot instrument cluster

   UDS command: `11 01`.

## Reference

* Original post: <https://www.drive2.ru/l/637547970148977368/>
* CarScanner procedure: <https://www.drive2.ru/b/637736536393130752/>
* <https://en.wikipedia.org/wiki/Unified_Diagnostic_Services>


 ![](attachments/dff482b8-7923-49d4-98ab-1f4f37ff70a1.jpg)

[sport_layout.py 1264](attachments/ed190727-3317-4b3f-89c4-3e020f9d4c4a.py)