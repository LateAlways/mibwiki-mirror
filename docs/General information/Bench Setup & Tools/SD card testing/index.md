# SD card testing

How to confirm if SD card is OK before using it for firmware update in vehicle.


:::warning
Fake SD cards can brick main unit. Make sure you are using quality product to avoid problems.

:::

## Testing with H2testw


 1. Download `H2testw` from <https://h2testw.en.lo4d.com/download/mirror-hs1-ssl>.
 2. Unzip it.
 3. Insert SD card.
 4. Format the SD card with `FAT`, `FAT32`, or `exFAT` file system.
 5. Open `h2testw.exe`.
 6. Optionally change language to `English`.
 7. Press `Select target` and point to the SD card root directory.
 8. Make sure that `all available space` is selected.
 9. Press `Write + Verify`.
10. Wait patiently. Test will first write data to the SD card, next it will read it back to verify if full capacity of the card is available and data is not corrupted. This can take some time, depending on the card capacity and read/write speeds.
11. If the SD card is OK, you should see `Test finished without errors` message in the log window.
12. SD card will be full. You need to format it (or delete its content) to use it.