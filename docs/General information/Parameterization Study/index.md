# Parameterization Study

## About

This page will be used to collect different webpages that study parameterization - focusing on the `0x5F` unit (+ related like audio amplifier). Aiming to post findings and potential retrofits, modifications in the future.

## Some MIB2 0x5F dataset addresses

* `0x000200` - `ASAM_ODX_MUX_dataset` - unit identifier string
* `0x000240` - `hmi_control_speed_dataset`  - responsible for disabling functions when speed thresholds are exceeded
* `0x000280` - `language_dataset` - Stores the default language information for interface, voice control and navigation.
* `0x002D00` **-** `visible_MMI_language_dataset` - Shows available languages in MIB
* `0x003000` - `audio_parameter_sound_dataset EQ_Details`
* `0x003600` **-** `audio_parameter_sound_announcement_dataset`
* `0x003900` **-** `audio_paramater_Sound 2nd dataset EQ Details for open roof (cabrio/convertible)`
* `0x003B00` - `audio_parameter_sound_configuration_dataset`
* `0x007000` **-** `in_car_communication`

Listed above are some of the datasets you can find within the 5F module. They are used to control the function of the headunit. Allows it to understand everything from speaker configuration (the number of speakers and their locations), and also whether there is an external amplifer connected. Along with other varibles such as what speed it should no longer playback video `0x000240` and features such as electronic voice amplifer `0x007000`. More information regarding datasets can be found in the links below.

### 0x000240 - HMI control speed dataset

* `byte 00` - Video Speed limit (km/h)
* `byte 01` - Video Speed Hysterese (km/h)
* `byte 02` - Car Menu Speed limit (km/h)
* `byte 03` - Car Menu Speed Hysterese (km/h)
* `byte 04` - DAB Slideshow Speed limit (km/h)
* `byte 05` - DAB Slideshow Speed Hysterese (km/h
* `byte 06` - DAB Slideshow Update rate #1 (s)
* `byte 07` - DAB Slideshow Update rate #2 (s)
* `byte 08` - User Manual Speed limit (km/h)
* `byte 09` - User Manual Speed Hysterese (km/h)
* `byte 10` - Road Guide Speed limit (km/h)
* `byte 11` - Road Guide Speed Hysterese (km/h)
* `byte 12` - Web Browser Speed limit (km/h)
* `byte 13` - Web Browser Speed Hysterese (km/h)
* `byte 14` - Destination input Speed limit (km/h)
* `byte 15` - Destination input Speed Hysterese (km/h)
* `byte 16` - Bluetooth/MirrorLink Speed limit (km/h)
* `byte 17` - Bluetooth binding Hysterese (km/h)
* `byte 18` - SMS Editor Speed limit (km/h)
* `byte 19` - SMS Editor Hysterese (km/h)
* `byte 20` - Radiotext Speed limit (km/h)
* `byte 21` - Radiotext Speed Hysterese (km/h)
* `byte 22` - Radiotext refresh rate (s)
* `byte 23` - Reserved
* `byte 24` - Reserved
* `byte 25` - Reserved
* `byte 26-27` - ASCII representation of dataset version
* `byte 28-29` - checksum

### Additional information

When reading Dataset via ODIS E, you can find the dataset version of each dataset

* if Equil to `**` the dataset is not supported by the headunit
* if Equil to `--` the dataset is supported and contains the content written at the factory.

## Tools to use for data read/write/modify parameters

* ODIS
* VCP
* [OBDeleven](/General information/RadioStationLogo (RSDB)/Parametrization with OBDeleven/) for Android
* CarScanner for iOS and Android

## Reference

* Video in motion: <https://www.drive2.ru/l/574649307970404656/>
* MIB2 Sound parameter study: <https://www.drive2.ru/l/611261670785849626/>
* MIB3 Sound parameter study: <https://www.drive2.ru/l/611148421088161236/>
* MIB2 MQB Sound settings study: <https://github.com/NumberOneBot/mqb-mib2-sound-datasets>
* MIB2 Toolbox VIM menu: <https://github.com/jilleb/mib2-toolbox/blob/master/Toolbox/GEM/mqb-vim_advanced.esd>


\

\