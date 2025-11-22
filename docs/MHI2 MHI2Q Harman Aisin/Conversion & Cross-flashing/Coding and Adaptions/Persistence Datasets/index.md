# Persistence Datasets

:::tip
Run before using any of the commands below - otherwise they will not work!

:::

```bash
export PATH=:/proc/boot:/sbin:/bin:/usr/bin:/usr/sbin:/net/mmx/bin:/net/mmx/usr/bin:/net/mmx/usr/sbin:/net/mmx/sbin:/net/mmx/mnt/app/armle/bin:/net/mmx/mnt/app/armle/sbin:/net/mmx/mnt/app/armle/usr/bin:/net/mmx/mnt/app/armle/usr/sbin
export LD_LIBRARY_PATH=/net/mmx/mnt/app/root/lib-target:/net/mmx/mnt/eso/lib:/net/mmx/eso/lib:/net/mmx/mnt/app/usr/lib:/net/mmx/mnt/app/armle/lib:/net/mmx/mnt/app/armle/lib/dll:/net/mmx/mnt/app/armle/usr/lib
export IPL_CONFIG_DIR=/etc/eso/production
```



:::tip
If you just hard reset your unit changes will not be stored

Changes will only have effect to unit after reboot

:::

```bash
#store changes to persistence
on -f mmx /eso/bin/apps/pc b:0:1 0
#reboot to save settings to unit!
on -f rcc /usr/apps/mib2_ioc_flash reboot
```


## Analysis


:::warning
Expert Level - only use this if you really know what you are doing.

Meaning you have at least a basic idea, what this is :wink:

:::


[https://docs.google.com/spreadsheets/d/11jJueBEbyBhkcEXmLNO3LIE5JX-ozgO3zKnJfRz5heM/edit?usp=sharing](https://docs.google.com/spreadsheets/d/11jJueBEbyBhkcEXmLNO3LIE5JX-ozgO3zKnJfRz5heM/edit?usp=sharing)


There is even more hiding in persistence of MHI2(Q) units, but the above parts are at least half cooked and ready to use for some of you:

* 5F datasets
* Vehicle_Configuration
* Long_Coding
* Car_Function_Adaptations_Gen2
* Car_function_list_bap_gen2_ext
* Car_Function_List_BAP_Gen2
* Car_Function_List_CAN_Gen2
* Dashboard_Display_Configuration


Feel free to add your observations and knowledge.


\