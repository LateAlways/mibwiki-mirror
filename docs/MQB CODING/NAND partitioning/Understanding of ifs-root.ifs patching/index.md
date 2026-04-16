# Understanding of ifs-root.ifs patching

On the MHIG units, the RCC NOR flash dump done with:

`cat /net/rcc/dev/fs0 >/net/mmx/fs/sda0/rcc_fs0`

`rcc_fs0` consists of multiple partitions: bootloader (**IPL**), **efs-system.efs**, **ifs-emergency.ifs**, **ifs-root.ifs**

**ifs-root.ifs** itself contains 2 ifs parts, one of which is **ifs-root-stage2** and contains QNX ELF binary **/usr/apps/MIBRoot** that does CP and FECs related checks.


To quickly find the offset of the **ifs-root-stage2.ifs** in **rcc_fs0** or **ifs-root.ifs**, you can search for **EB7EFF00010008** bytes or **#imagefs** string in HxD:                  ![](attachments/6eac729d-c5a0-48d1-bafc-f43a8f60911a.png)

At offset **0x24** you can see the size of the **ifs-root-stage2.ifs** file

## Start addresses of **ifs-root-stage2.ifs** on different train versions:

MHIG_EU_AU_K1549 0xBA0000

MHIG_EU_AU_K1555 0xBA0000

MHIG_EU_VW_K0344 0xBA0000

MHIG_EU_VW_K1550 0xBA0000

MHIG_EU_VW_S1532 0xBC0000

MHIG_JP_VW_S0027 0xBE0000

## Unpacking and packing back **ifs-root-stage2.ifs**

Unpack, modify MIBRoot and pack it back with [IFS_Utility_vLO](https://github.com/lprot/MIB-Tools/raw/master/IFS_Utility_vLO.7z)