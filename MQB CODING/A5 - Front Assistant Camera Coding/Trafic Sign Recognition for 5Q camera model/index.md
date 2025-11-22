# Trafic Sign Recognition for 5Q camera model

**Unit A5   (Security Access Code is 20103. Ignition ON, engine OFF, bonnet OPEN while coding this module**) \n  \n**Long __Coding 2__** \nByte 01 - Enable Bit 0

Byte 04 - Enable Bit 0

Byte 06 - Enable Bits 0 and 1

Byte 07 - Enable Bits according to your MIB type (Standard/High) \*Note if you have 'High' but have issues with traffic signs you'll want to tick Bits 0 and 2\*


**Long Coding 1** (tick if below did NOT get ticked while doing Long Coding 2)

\-coding_VZE (enabled)

\-VZE_Cam type (MQB_MFK) \n  \n**__Adaptions__** \nfind in the menu ''function_module_road_sign_recognition'' change to 'activated'

find in the menu 'VZF_country_code' change to '0'

find in the menu 'VZE_show_administrative_speed_limits' change to 'show_always'

find in the menu 'VZE_show_valid_additional_signs' change to 'activated'

find in the menu 'VZE_prioritize_moisture' change to 'not activated'

find in the menu 'VZE_sorting_valid_signs' change to '174'

find in the menu 'CCP_interface' change to  'not activated'

find in the menu 'VZE_sorting_alternative_signs' change to '425'

Set all 6 functions related to 'Dev_messages……' to 'not activated'

find in the menu 'mask_error_reactions_for_development' change to 'not activated'

Set all 4 'masked_fault_classes' to '255'

find in the menu "road sign detection fusion mode" change the value to "road sign fusion"

find in the menu "display end of speed limit symbol" change the value to "active" \nfind in the menu "display no passing allowed" change the value to "active"

find in the menu 'predictive route data run time' change the value to "0 ms"

find in the menu "display valid additional signs" change the value to "100111"


\+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n

**Unit 5F** 

\n**Long __Coding 2__** \nByte 24 - Enable Bit 6 to make traffic signs appear \nByte 24 - Enable Bit 7 for Predictive Route Data (Mandatory otherwise you'll get the error!) \n

**Long Coding 1** (tick if below did NOT get ticked while doing Long Coding 2)

Byte_3_Country_Navigation (choose your region)

Byte_24_Navigation_System (activated)

Byte_24_VZA (activated)

\n **__Adaptions__** \n Find 'Vehicle configuration' and inside look for:

\-'VZAPro' and set to 'ON'


Find 'Car_Function_Adaptations_Gen2' and inside look for:

\-'menu_display_road_sign_identification' and set to 'Active' \n-'menu_display_road_sign_identification_over_threshold_high' and set to 'Active'

\n Find 'Car_Function_List_BAP_Gen2' and inside look for:

\-'traffic_sign_recognition_0x21' and set to 'Activated' 

\-'traffic_sign_recognition_0x21_msg_bus' and set to 'Databus Extended' \n  \n

\+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

\n  \n Unit 17

\n**Long __Coding 2__** \nByte 05 - Enable Bit 2

Byte 14 - Enable Bit 6


**Long Coding 1** (tick if below did NOT get ticked while doing Long Coding 2)

\-traffic_sign_display_BAP (YES)

\-traffic_sign_detection (YES)