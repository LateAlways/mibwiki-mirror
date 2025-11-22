# Parametrization with CarScanner

:::info
In this example I'm going to describe how to upload dataset for ICC to address `0x7000`.

:::

## Requirements

* iOS/Android phone.
* CarScanner app ([iOS](https://itunes.apple.com/app/car-scanner-elm-obd2/id1259933623?mt=8), [Android](https://play.google.com/store/apps/details?id=com.ovz.carscanner)) with PRO features enabled,
* Quality ELM327 adapter (for example Carista),
* Notepad or any other simple text editor,
* Dataset to upload.

## Preparing dataset


1. Go to mibsolution and find `XML` file that you want to use. For example let's get `/MQB_SOLUTION/Datasets/MQB/5F/#5F_ICC__ONLY.xml`.
2. Download the file, open it and find line with `<PARAMETER_DATA DIAGNOSTIC_ADDRESS="0x005F" START_ADDRESS="0x007000"…>…</PARAMETER_DATA>`.

   You can see here that this data is designed for unit `5F` and for address `0x7000`.

   You can also see the data `0x01,0xA0,0x51,0x41,0x43,0x46,0x01,0x00…`.
3. Copy dataset into new textfile.
4. Remove unnecessary characters like `,` and `0x`. When you are done you should have something like this: `01A0514143460100…`.
5. Save this data as `txt` file that you can access from your phone (via GoogleDocs, Dropbox or whatever…). Name it for example `5F_0x7000_dataset.txt`.

## Preparing CarScanner


1. Open CarScanner app
2. Go to `Settings`, `My cars`, `+`, fill in data.
3. Back in `My cars` make sure the the car is highlighted and press `Select car`.
4. Go to `Settings`, `Adapter`, and configure connection details.

## Uploading dataset


1. Open CarScanner app.
2. Press `Connect` and wait for the connection to be established.
3. Go to `Coding & Service`, `Dataset dump`.
4. Select `Dataset 5F 0x7000` (because in this example we are uploading ICC dataset).
5. Press `Read` and wait.
6. Press `Export` to backup original data. Save the file on the phone. For example as `5F_0x7000_dump.txt`.


:::info
if you see `Current state: UnknownError`, most likely there's no data to read as this address is empty. This is normal if you are trying to parametrize new devices or unsupported features. You will not be able to backup it since there's no dataset over there that you can read.

:::


7. Press `Import` and point to previously prepared `5F_0x7000_dataset.txt` file with dataset.
8. Press `Write` and wait. It will take around 1 minute, during which main unit will reboot.
9. When it's done, you can use `Read` option again to confirm that the data was stored correctly.

## Converting Carscanner dataset output to ODIS format

As discussed above, when reading and writing data using Carscanner, it does not register data in the same format, it ignores `0x,`. To convert it to an ODIS friendly format, the `0x,` must be added back in. The following guide can be used to convert between applications succesfully: [format converter](https://stackoverflow.com/questions/41852893/notepad-insert-characters-every-2-characters-of-a-string).


\