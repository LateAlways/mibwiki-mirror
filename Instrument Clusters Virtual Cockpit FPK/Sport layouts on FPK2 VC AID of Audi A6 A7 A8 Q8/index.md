# Sport layouts on FPK2 VC/AID of Audi A6/A7/A8/Q8

To activate layouts on **Bosch D_AU651** FPK2 (aka gen2) clusters you need:

1\. Flash fw version 0095.


2. Flash fw version 0216.
3. In ODIS-E in block 17 login with 20103.
4. Enable up to any 3 adaptations in block 17:

\[VN\]_designvariant_activation_gen2: \n \[LN\]_variant_1: \[VN\]_active \n \[LN\]_variant_2: \[VN\]_not_active \n \[LN\]_variant_3: \[VN\]_active \n \[LN\]_variant_4: \[VN\]_active \n \[LN\]_variant_5: \[VN\]_not_active \n \[LN\]_variant_6: \[VN\]_not_active \n \[LN\]_variant_7: \[VN\]_not_active


5. To avoid "Basic settings" error in block 17, enable following adaptation :

\[LN\]_lock: \[VN\]_yes


**Mapping of variants to layouts:**

Variant 1 — Klassik (default) \n Variant 2 — S Performance \n Variant 3 — Dynamic \n Variant 4 — Sport \n Variant 5 — RS Performance (this layout not available in fw 0211 but available on 0216) \n Variant 6 — RS Sport (this layout not available in fw 0211 but available on 0216) \n Variant 7 — RS Runway (this layout is not available in fw 0211+)


**Good to know:** if you update from 0095 onto 0211 or 0216, you will automatically enable Klassik, Dynamic and Sport layout without need to change any adaptation.


Reference: [https://www.drive2.com/b/645389137322470068/](https://www.drive2.ru/b/645389137322470068/)

Source: https://mhhauto.com/Thread-Solution-Audi-Virtual-Cockpit-Sport-Layout-Activation-GEN2