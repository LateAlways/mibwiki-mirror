# Hardware and software parts

## Hardware and software


:::info
There are 3 types of MSTD units: **Nav**, **Plus** and **Std**.

:::

RCC is booted from 2Mb NOR and runs under QNX

MMX is 200MHz [SH-4](https://en.wikipedia.org/wiki/SuperH) CPU with 256Mb RAM. **EBoot** bootloader loads "Standard OS" binary **nk.bin** (Windows CE 5.0) and if it is corrupted uses "Emergency OS" **nk.bin**.

4Gb MMC has 8 partitions (on Std units only 6 partitions are used because weak CPU doesn't support Nav and SDS so MMC4 and MMC5 are not needed). Content of some partitions can be found in the firmware update package and extracted from partition.bin files with 7zip:

**MMC1:** System partition, contains **START.BAT** that runs **/MAIN/CPU_HMI.EXE** ![](attachments/9eec0d81-9b51-4750-9c03-5c45400a66f9.png)

**MMC2:** Resources (esd menu, fonts, images.mif, skin1, ringtones) ![](attachments/bb16ca5e-0063-4d50-8ba4-38a36edce2e1.png)

**MMC3:** Storage for persistence, errors, screenshots etc ![](attachments/addfe058-81ef-4cb5-8e71-2f0ccf4031cb.png)

**MMC4:** Navigation binary and resources ![](attachments/d4b8bfe7-fd16-4c3b-bb07-de10856f8a68.png)

**MMC5:** Speech (svox_res) resources\n ![](attachments/60ea47a7-0980-4776-8b6e-b656856e54c2.png)

**MMC6:** Contains copy of **NVM_DB**

**MMC7:** Contains public keys for checking signatures of data, SWaP/FECs, metainfo2.txt and FECs in **FEC_DB** file: ![](attachments/84fa0909-5352-4415-a60d-8953c41a633e.png)


:::info
**FEC_DB is [SQLite database](https://sqlitebrowser.org/dl/). Columns fsid-fsid12, contain FECs in decimal format. To enable newer maps it is enough to change 35651xxx to 35651822 (lifetime maps 22000EE) and delete** rpkpsh4.bin in MMC8.

:::


:::success
You can also create here a special **slist.txt** file with additional FECs

:::

**MMC8:** Contains rpkpsh4.bin, encrypted VCRN that participates in the check of FEC signature. If you delete rpkpsh4.bin then modified FEC_DB will be accepted. The disadvantage of this method is that you cannot install updates via metainfo2.txt anymore. As VCRN becomes all zero, you also will not be able to get parametrisation with ODIS-S from online. But who cares? :)