# Update firmware 01xx to higher version

# 1xx update to higher


:::info
**RAM differences**

1xx PLUS units have 2x **D9PTJ** modules

1xx NAV units have 4x **D9PTJ** modules

2xx and higher PLUS units have 2x **D9PZV** modules

2xx and higher NAV units have 4x **D9PZV** modules

:::


:::info
**D9PTJ** - on internet are identified as MT41K**128M**16JT 125 AIT cpu (nav) unit has 2x more RAM then `1xx` cpuplus unit

**D9PZV** -on internet are identified as MT41K**256M**16HA-125 AIT

:::

 ![1xx PLUS unit](attachments/e24aaeff-4172-45ec-8ddf-c348a849d164.JPG)


:::info
I don't have 1xx NAV unit but it will be 2-times more then 1xx PLUSI don't understand why in **showmem -S** are such high amount of RAM, because:

1xx PLUS should have2x128MB = **256MB** and showmem see is as **512MB**

2xx PLUS should have 2x256MB = **512MB** and showmem see is as **1024MB**

4xx NAV should have 4x256MB = **1024MB** and showmem see is as **2048MB**

Someone who knows why are there these differences could add more info.

:::


:::tip
If your NAV or PLUS unit has just D9PTJ modules then appconnect after update won't work.If your NAV or PLUS unit has just D9PTJ modules then appconnect after update won't work.

2xx FW will work on small RAM unit, just appconnect not, during connecting phone to Android Auto / Carplay unit freeze and after few seconds will reboot itself.

3xx and 4xx have more requirements on RAM, so on small RAM unit will 3x self reboot during startup, and on 4th boot will boot without working audio. FW will work on small RAM unit, just appconnect not, during connecting phone to Android Auto / Carplay unit freeze and after few seconds will reboot itself.

:::


:::info
**So steps for update from 1xx to 2xx and higher is:**

* update to latest official FW (VW ZR 0140)
* patch swdownload (==patched files are in 7zip at bottom of these instructions==)
* link your HW number to metainfo from 254 update, metainfo generator can do it
* swdl update
* check all
* uncheck emergency in CPU and MAIN (it's better to keep 0140 recovery)
* uncheck HMI (big file)
* uncheck stationdb (big file)
* uncheck all voice files (vocon, nuanceres, tts, wavefiles) - big files

  ==it's necessary to uncheck all these big files, because partition is smaller and you need to update boot files, all of these files will be restored in next step==
* start update
* be careful at last parts, you have to unplug power when unit shows screen that update will continue after restart
* connect to BDM and restore 254 backup to EMMC
* unplug BDM and start unit
* now you can update to any FW (Skoda, SEAT, VW, 2xx, 3xx, 4xx) but WIFI won't work on newer FW then 2xx

:::

[ VW_ZR_140_swdownload_patched.7z](attachments/5aaff186-f9c4-4ec3-9b9d-9cdd72a6c349.7z)

 ![](attachments/8c8b00e8-f129-4699-bea3-948c58b8d03f.jpg)

 ![](attachments/68d2b513-fcde-4a77-a6a0-11eff9bddfb0.jpg)

 ![](attachments/b7f3f8d6-cf44-43d3-a82d-ad906f706be8.jpg)

 ![](attachments/eb0d6b86-607b-473c-933d-0f2ce9cf0f28.jpg)

 ![](attachments/0ae8bb44-cc82-4572-ab50-fea014755400.jpg)

 ![](attachments/eec91015-3814-404b-9467-03984beb657b.jpg)

 ![](attachments/d5da376c-2100-4fed-aace-cd7136302a6d.jpg)

 ![](attachments/3b43a28d-0fbd-4e0d-aaf4-e0113a0d49f4.jpg)

 ![](attachments/95c98818-6f77-40ec-997c-6d3f5828447b.jpg)

 ![](attachments/ed01126e-4b0f-4090-9bb3-10ed93a88262.jpg)

 ![](attachments/3f85358d-af9d-42af-b2ca-418455b44e88.jpg)

 ![](attachments/5bca2137-e176-4292-8968-7895652eb3fa.jpg)

 ![](attachments/98350f0d-d3d8-4ece-9e59-587a91f1c554.jpg)

 ![](attachments/4cceacb2-31df-4f8e-af17-1c9e72e9a1d4.jpg)

 ![](attachments/3777be8f-e466-4f5c-8b2f-0939689defa5.jpg)

 ![](attachments/e67f2e7c-2456-4ee5-ab4e-41410b74543b.jpg)

 ![](attachments/98bd63a4-cb76-4c3a-8e8e-5534783169ed.jpg)