# Clean APG Unit (based on Harman-F AiO Firmware (GitHub))

## **Problem description**

Harman DiscoverPro MIB2 (`3G0035021B`) with APG-Patch from 2018 freezes in navigation app after boot-up very often. Reboot needed to get system running again. Probably patch got partially destroyed by frequent map updates. Decision taken to clean device and start from the scratch.


SW Train Version before patch: MHI2_ER_VW==X==11_P3301 (`X` instead of `G` which blocks normal firmware update by user) & no proper green menu:

 ![](attachments/c19ba65d-bd7f-4065-810e-d659636dd669.png)

 ![](attachments/2505d995-d7e7-40ce-b61f-63f13e3c52f5.png)


## **Process of installation**


1. Go to MIB solution Harman section and have a look and download the latest AiO which is matching your car brand and SW Train. In this case: `MHI2_ER_VWG11_K3342_1_AIO_MU1427-20230318`

    ![](attachments/23bf726b-4de7-4a38-8985-f2f843c95337.png)

   \
2. Extract all files to an SD-Card. Please refer to the GitHub from Harman-f for further information:

   <https://github.com/harman-f/MHI2_MIB2_AIO_FW_Update_Template/wiki/AIO-installation>

   \
3. I did not integrate the Gracenote database to the SD-Card at the beginning. This will show up later with an error which can be skipped and ignored during installation.

   \
4. Before installation the `metainfo2.txt` in the root folder of the created SD-Card needs to be modifed as shown here. Changes applied in this case (VW and MIB2 firmware G11):

   `MHI2_ER_VWG11_*` → `MHI2_ER_VWX11_*`           ![](attachments/e93618a1-efc9-475b-b13b-1aeac5301b0c.png)

   If SW Train is not adpated the installation will be refused by the device with a version conflict error:

    ![](attachments/9938384e-9046-450e-a219-4f006666b9b5.png)

   \
5. Insert SD-Card in Harman unit and start installation via normal Firmware update or SWDL-update. This takes a while and a couple of reboots.

    ![](attachments/b4865cc6-8ecd-447f-9db2-f26121aaa735.png)

   \
   Installation finished with expected Gracenote2 error.

    ![](attachments/7bb6bfb4-7f4f-4a73-9c6f-9e4d11e3694f.png)

   \
6. After reboot SW-Train was updated to latest one with `G11`; Green Menu updated as well (with small version of M.I.B. - More Incredible Bash installed)

    ![](attachments/64b3ed4d-5756-4187-8bd9-01a1792ddd32.png)      ![](attachments/b07839ad-b578-4c19-92dd-62efe5f4f177.png)

## **Problem after installation**

No FEC and SWaP Codes available (Navigation, Bluetooth, Voice Control, CarPlay and Android Auto not working)     ![](attachments/e4b317e1-5d8f-48f2-99fc-94790606e3c9.png)


## **Solution**

Symbolic link of FEC folder in the RCC file system (`/mnt/efs-persist/FEC`) needs to be removed and newly created as normal folder. AiO firmware is not able to create patched FEC/SWaP-Codes because symbolic folder FEC is not available. See also here for information: </MHI2 MHI2Q Harman Aisin/Recovery/RCC/Manual Firmware Restore/Clean APG unit/>

 ![](attachments/08a27c48-4f90-4d30-aea0-c474aa8c0310.png)Connect PC via D-Link adapter and login into RCC port `123` with e.g. Putty or Windows Telnet. Execute both Telnet commands.

</MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/Telnet/>

After creating the new FEC folder in `/mnt/efs-persist` (RCC system) run the patch from M.I.B More Incredible Bash again and the FEC and SWaP codes should be created properly.