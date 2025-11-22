# Backup MMX NOR

:::warning
Is important to have a backup if you start playing with MMX

:::

Connect to UART with TTL cable and connect USB pen drive to USB port as described [here](/Instrument Clusters Virtual Cockpit FPK/TTL and USB connection/)

Login via TTL [as root](/Instrument Clusters Virtual Cockpit FPK/MMX root passwords/) and enter following command (will take about 1-5 minutes):


:::tip
cat /dev/fs0 > /fs/usb0/mmx_fs0

:::