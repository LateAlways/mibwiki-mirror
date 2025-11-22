# Conversion of US > EU

:::info
Unit can be converted via Manual SWDL by skipping the update of some partitions

:::


Below is just a bricking example that many got while trying to convert MSTD_US_VW_P4430 or MSTD_US_VW_P3470 etc without knowing what to skip: ![](attachments/0d30d39d-7ebc-4d23-85e0-501e2c1e65d2.png)

to MSTD_EU_VW_P4470 by adding a variant to the very end of metainfo2.txt after the \[signature\] lines like:

```
[common]
Variant="17147"
Region="USA"

[common_Release_2]
Name="MSTD_EU_VW_P4470"
path=".\VW_PLUS_SSB\"
Variant="17147"
Region="USA"
```

and correspondingly into metainfo2.txt in VW_PLUS_SSB folder:

```
[common]
Variant="17147"
Region="USA"
```

This allows to install EU firmware update:  ![](attachments/b0ed82a0-bc9a-479d-b802-c1b8c29f983e.png)

But when the update finishes, you get endless bootloop: ![](attachments/23649a02-8596-4872-97e5-ea96ca246f55.png)

The reason of the bootloop is crash of **CPU_HMI.EXE** (the log is collected via quadlock via TTL adapter on 115200bps speed)

[US2EU_BRICK_115200bps_log.txt 69395](attachments/bafcdfac-4a3c-45fe-8f02-a17b5bd627b3.txt)