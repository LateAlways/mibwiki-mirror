# MH2p Wireless CarPlay

1. Update firmware to `P2470` or higher, min 2711
2. Unpair the phone from the car (both from Bluetooth and wired CarPlay connections),
3. Change `5F` adaptations and long coding:

   `Vehicle Configuration - MirrorLink` → `On`

   `Vehicle Configuration - WiFi_Client_HMI` → `On`

   `Vehicle Configuration - Apple_DIO_Wireless` → `On`

   `Vehicle Configuration - wlan_5ghz_switch` → `Activated.`

   `Vehicle Configuration - Apple_DIO` → `On`

   `Long Coding - WLAN` → `On`
4. Reboot the unit

   
:::info
   How to reboot Audi MMI

   :::
5. Go to MMI settings and turn on Wi-Fi hotspot,
6. Pair the iPhone with MMI via Bluetooth - it will ask you if you want to use CarPlay.


:::tip
If you can't use CarPlay, make sure Siri is turned on. Also check out CarPlay common issues.

:::


:::tip
If, for some reason, you can't make Wireless CarPlay to work, you can use one of the [wired-to-wireless adapters](/General information/Enhancements/JAVA HMI PatchesV2/Wireless CarPlay adapters/).

:::

Source: https://forum.obdeleven.com/thread/6663/2019-wireless-carplay-activation-cars