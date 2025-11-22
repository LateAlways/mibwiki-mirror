# TSR for A4 B9

Module 17 - Dashboard - Security access 25327
Long Coding 2

* Byte 05 - Activate Bit 2 "Traffic Sign Recognition"
  Long Coding 1 (tick if below did NOT get ticked while doing Long Coding 2)
  \-traffic_sign_display_BAP (YES)
  \-traffic_sign_detection (YES)

Module 5F - Multimedia - Security access 20103
Long Coding 2

* Byte 24  Enable Bit 6 to make traffic signs appear
* Byte 24  Enable Bit 7 for Predictive Route Data (Mandatory otherwise you'll get the error!)

Long Coding 1 (tick if below did NOT get ticked while doing Long Coding 2)

* Byte_3_Country_Navigation (choose your region)
* Byte_24_Navigation_System (activated)
* Byte_24_VZA (activated)

Adaptation

* Car_Function_Adaptations_Gen2
* menu_display_road_sign_identification - Change value to "Activated"
* menu_display_road_sign_identification_over_threshold - Change value to "Activated"
* Car_Function_List_BAP_Gen2
* traffic_sign_recognition_0x21 - Change value to "Activated"
* traffic_sign_recognition_0x21_msg_bus - Change value to "Comfort data bus"

Module A5 - Driver Assistance - Security access 20103
Long coding 2

* Byte 01 - Activate Bit 0 - Up to MY16
  or
* Byte 16 - Activate Bit 4 - From MY17

Adaptation

* find in the menu ''function_module_road_sign_recognition'' change to 'activated'
* find in the menu 'VZF_country_code' change to '0'
* find in the menu 'VZE_show_administrative_speed_limits' change to 'show_always'
* find in the menu 'VZE_show_valid_additional_signs' change to 'activated'
* find in the menu 'VZE_prioritize_moisture' change to 'not activated'
* find in the menu 'VZE_sorting_valid_signs' change to '174'
* find in the menu 'CCP_interface' change to  'not activated'
* find in the menu 'VZE_sorting_alternative_signs' change to '425' Set all 6 functions related to 'Dev_messages……' to 'not activated'
* find in the menu 'mask_error_reactions_for_development' change to 'not activated'
  Set all 4 'masked_fault_classes' to '255'
* find in the menu "road sign detection fusion mode" change the value to "road sign fusion"
* find in the menu "display end of speed limit symbol" change the value to "active"
* find in the menu "display no passing allowed" change the value to "active"
* find in the menu 'predictive route data run time' change the value to "0 ms"
* find in the menu "display valid additional signs" change the value to "100111"

If an error is stored in the Module 13, the following must be coded:
Module 13 - Adaptive Cruise Control - Security access 20103
Long coding 2

* Byte 01 - Activate Bit 0  "Traffic sign detection"