# shadow - how to retrieve hash of root password from the unit

Despite the fact that [m.i.b](/MHI2 MHI2Q Harman Aisin/M.I.B. - More Incredible Bash/) includes a comprehensive password list, it still lacks passwords for RCC, MMX, and/or RCC Emergency IFS for some trains/MUs.


# Dump RCC and/or MMX NOR to find root password hashes

The most easy way is to check the RCC-fs0.bin and MMX-fs0.bin in the m.i.b. backup. 

But if the backup is absent and you have no password for RCC/MMX and/or RCC Emergency IFS, then you can upload an emergency.ifs from a FW with a known root password via [ZMODEM](/MHI2 MHI2Q Harman Aisin/Recovery/RCC/How to boot ifs-emergency.ifs via zmodem in CLI/) :)

After emergency.ifs is running and you logged in, and dump RCC & MMX NORs to SD card like:

```
mount -uw /net/mmx/fs/sda0/
cat /net/rcc/dev/fs0 >/net/mmx/fs/sda0/RCC_fs0.bin
cat /net/mmx/dev/fs0 >/net/mmx/fs/sda0/MMX_fs0.bin
```

# MMX/RCC hash of root password

## Extracting from FW update or MMX-fs0.bin

Open`\MMX2\efs-sys\XX\default\efs-system.img`or MMX-fs0.bin in any hex editor like HxD and search for`root:`

 ![](attachments/80bc4e78-d958-479e-9bdf-b948b8af80cd.png)

Hash is brWtVCU7RcmTw in this case.


# RCC Emergency IFS root password hash

## Extracting from FW update files

Use IFSTool to split and unpack`\RCC\ifs-root\XX\default\ifs-root.ifs`to find the hash in /etc/shadow_rcc file.

## Extracting from RCC-fs0.bin

Hash is stored in shadow_rcc file that is compressed in ifs-root-stage1 partition that holds Emergency IFS.

To get ifs-root-stage1 you need to exctract IFS-root.ifs from the RCC-fs0.bin first:

* start offset 0x0540000
* end offset somewhere with PORSCHE, which is the end of ifs-root-stage2 image

   ![](attachments/64237170-698e-4719-be5e-37c88b43d30c.png)

Save selection from start offset till end offset as a new file and split it into stage1 and stage2 with IFSTool, then unpack ifs-root-stage2.ifs and get `/etc/shadow_rcc` file:

 ![](attachments/486676f7-944c-4132-84aa-ce69c758d8da.png)Alternatively you can find the hash in the unpacked image file using `root:` in HxD search 


# Brute force the hash to find password

QNX6.5 on MHI2 uses DES hashes with salt stored in the first two characters of the hash.

E.g. in hash: WmRI0ymbfbbUw the salt is: Wm  


:::info
Usually brute forcing can be done in 2 days.

Sometimes, with limiting the possible characters and their combinations used in other known password even in a couple of hours.

:::