# E2PTool

\
E2PTool is a utility to creat shell commands to edit MHI2 eeprom.

Useful for manual unit conversions

* Region conversions (e.g. US --> EU)
* MIB2.0 --> 2.5


 ![](attachments/82769744-50c7-4169-8122-4cbbe265b387.png)


This tool makes this process easier and safer.

Input field required and press "Generate".


 ![](attachments/657d0b21-cd33-4624-9af5-78eadbe5d05f.png)

E2PTool will generate a list of commands in the syle of

`"on -f rcc /usr/apps/modifyE2P ...."`

These have to be executed within RCC shell either via [UART or Telnet](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/) on the target MHI2 unit


:::info
Depending on what you wnat to change, not all commands are required.

:::


:::warning
In [Emergency Mode](/MHI2 MHI2Q Harman Aisin/Recovery/RCC/How to boot ifs-emergency.ifs (start blue emergency EFU)/) `modifyE2P`  binary is not available

:::

Restart your unit afterwards to apply changes:

`/usr/apps/mib2_ioc_flash reboot`


## Software Requirements:

Oracle JDK 15.0.1 required to run:

* Download link below
* https://www.heise.de/download/product/java-standard-edition-java-se-jdk-34074


## Download

[Link](https://mibsolution.one/wl/?id=OWIa6oE2I0D90iQmMWiHAd4qoRRGsbbv)