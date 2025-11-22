# Hardware MHI2

## Front cover

 ![MHI2 unit with a SIM card slot (LTE module)](attachments/35e62ca3-6d80-424d-858d-e6b60c2383be.png)

## RCC (Radio and Car Control) Mainboard / PCB (Printed Circuit Board)

 ![RCC board bottom view. Chips: RCC, NOR, IOC (Renesas V850) ](attachments/faecbda8-44a6-48c9-aeee-2491aea8de38.png)

\n   ![RCC board top view with MMX board top view on top ](attachments/71c335db-bbf3-40b2-91f8-073ae2cbe10a.png)       ![RCC board top view with MMX board removed](attachments/8a296985-2a7b-46fd-98ba-b4a6b101ee23.png)

## MMX (Multi Media eXtension) Mainboard / PCB (Printed Circuit Board)

 ![MMX board top view. Chips: Tegra30, NAND, 4xSDRAM ](attachments/953c3d7c-8f8f-4f3a-82e7-b0d7d14de818.png)

 ![MMX board bottom view. Chips: NOR ](attachments/fd82e12e-f7c2-469d-996d-9142df7c54bd.png)


 ![MMX board chip details](attachments/0fb20843-25dd-4fee-9bfc-9b5b4e6c0e6c.png)

## MMX - alternative PCB layouts

Over time different MMX PCB layouts can be found in MHI2 units (see also above) ![](attachments/27c82043-d800-40fe-a198-9e366401bf3d.png)MMX Tegra30 Peripherals / Pinouts

[Tegra3_publicTRM_DP05644001_v03.pdf 23726005](attachments/6f30c417-2c55-445a-bc10-68b2c120b8b4.pdf)

UARTD is exposed as the MMX UART console on the quadlock

NOR is at 0x48000000

USB0 is normal connection, USB3 is also configured in QNX

MMC/SD

* sda: 0x78000000 (SDMMC-1) bs=cd=D3:wp=V2:rs=V6
* sdb: 0x78000400 (SDMMC-3) bs=cd=D4:wp=V3:rs=V7

WLAN

* io-sdiorm-mib2 -p33 -c45000000 -h ioport=0x78000200,irq=47,inpclk=45000000

You can find more addresses in **/net/mmx/mnt/system/etc/boot/startup.sh**


:::info
[MMX board on the MHI2Q](/MHI2 MHI2Q Harman Aisin/Hardware MHI2/MHI2Q - Qualcomm/) does not have Tegra30, NOR and NAND chips. They are replaced with Qualcomm and eMMC chips.

:::