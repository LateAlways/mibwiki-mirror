# SWaP patch

1. Make sure you have installed the latest version of the toolbox from here: https://github.com/olli991/mib-std2-pq-zr-toolbox.


:::info
Details about Technisat MIB STD2 Toolbox installation.

:::


2. Make sure that Toolbox SD card is inserted into SD1 port. It's required for origian files backup before patching.
3. Press and hold MENU button for 10 seconds to enter `Testmode menue`.
4. Go to `Green Engineering Menu` →  `mibstd2_toolbox` →  `Tools` →  `Patch tsd.mibstd2.system.swap and generate EL`.
5. Wait about 15 seconds for the script to perform modifications.
6. Press and hold volume control knob for 10 seconds to reboot the unit.
7. Check if FEC/SWaP protected features are working.

[https://youtu.be/a9uwYmBPc1Q](https://youtu.be/a9uwYmBPc1Q)


:::info
MIB STD2 Toolbox SWaP Patching supports most common firmwares. If your firmware is not supported, report it in the repository or update firmware to the most recent/supported version.

:::


:::info
Performance Monitor will not be enabled by this method. You will need to upload self-generated FEC/SWaP code. More details:

MIB FEC/SWaP Code Generator

[5F - Inserting FECs with OBDeleven](/MQB CODING/5F - Inserting FECs with OBDeleven/)

:::