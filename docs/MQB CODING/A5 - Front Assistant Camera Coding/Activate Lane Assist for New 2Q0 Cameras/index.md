# Activate Lane Assist for New 2Q0 Cameras

![](attachments/2daf173f-c35e-4507-844c-45032e9d0f96.png)


## Modul "A5 Front Sensor" → Long coding

* "**ACC**" →  **__Coded__** (if equipped)
* "**Point_of_Intervention**" →  "**__early_setting_over_menu__**"
* "**Configuration_for_lane_departure_warning_kl15**" →  "**__Last_setting__**"
* "**Lane_Assist_system_mode**" →  "**__Selection_over_menu__**"
* "**HC**" →  **__Coded__**
* "**HC_messages**" →  **__Coded__**
* "**HC_Warning_intensity**" →  "**__Seting_over_Menu__**"
* " **HC_Variante**"  →  "**__Variante_1__"**


## Modul "5F Information Electr." → Adaptation :

* "**Car_Function_List_BAP_Gen2**"  → "**LDW_HCA_0x19**"  →   "**__activated__**"
* "**Car_Function_List_BAP_Gen2**"  → "**LDW_HCA_0x19_msg_bus**"  →   "**__Databus Extended__**"
* "**Car_Function_Adaptations_Gen2**"  → "**menu_display_Lane_Departure_Warning**"  →  "**__activated__**"
* "**Car_Function_Adaptations_Gen2**" → "**menu_display_Lane_Departure_Warning_over_threshold_high**"  →   "**__activated__**"
* "**Car_Function_Adaptations_Gen2**"  →  "**menu_display_Lane_assistant**"  →  "**__activated__**"
* "**Car_Function_Adaptations_Gen2**"  →  "**menu_display_Lane_assistant_over_threshold_high**"  →  "**__activated__**"


## Modul "17 Instruments" → Long Coding → HEX:

* **Byte 04**  →  **Bit 6** **__activated__**("Spurhalteassistent / Lane Assist verbaut")
* **Byte 11**  →  Bit 1 **__activated__** ("Spurhalteassistent / Lane Assist Information (BAP) verbaut/aktiv")


## Control unit 44 → Long Coding → HEX:

* **Byte 03**  →  **Bit 0** **__activated__** ("Spurhalteassistent verbaut")


\