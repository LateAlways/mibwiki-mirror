# Aisin MHI2/MHI2Q units with AW7 hardware

:::info
Aisin MHI2 and MHI2Q units are manufactured by AISIN AW CO., LTD. for Audi, Porsche, and VW in the Asian market. These units are based on the same MHI2/MHI2Q hardware, but have some software differences.

They feature CN/JP/KR/TW train versions.

In these units, the FAZIT in the EEPROM does not start with "JTB" (as in EU units), "JTH" (as in US units), or other typical Harman identifiers, but instead starts with the characters "AW7", which can also be found on the label:

:::

 ![FAZIT AW7 = AISIN](attachments/0703b5cd-6ddf-421d-bfea-68bbab2cfe8e.png)

## MMX Board information

MMX PCB on AW7 is identified like: 

```
BOM: 699
Project: 61852
SKU: 0001
Version: 900
```

# Conversion to EU

* Following m.i.b. backups were studied:
  * MU0618-MHI2_CN_AUG22_P0618-AW7-MON28.04.1600012345
  * MU0816-MHI2_TW_AU37x_P0901-AW7-MON10.11.1700012345
  * MU1005-MHI2_CN_AU57x_K1006-AW7-MON05.07.1700012345
  * MU0035-MHI2_KR_AU57x_S0035-AW7-MON13.08.1500012345
  * MU0817-MHI2_KR_POG24_P0817-AW7-MON08.09.1700012345
  * MU1214-MHI2_CN_AU276_P1214-AW7-MON13.03.1800012345
  * MU0623-MHI2_CN_AU57x_P0623-AW7-MON01.07.1600012345
  * MU0836-MHI2_TW_VW48x_P0952-AW7-MON23.02.1800012345
  * MU0627-MHI2_CN_VW48x_P0627-AW7-MON29.05.1700012345
  * MU0627-MHI2_CN_VW48x_P0627-AW7-MON19.01.1600012345
  * MU1101-MHI2_JP_VW48x_P1101-AW7-MON20.06.1900012345
  * MU0843-MHI2_JP_VW48x_P0953-AW7-MON18.11.1700012345
  * MU0734-MHI2_JP_VW48x_K0735-AW7-MON30.01.1700012345
  * MU0637-MHI2_JP_VW48x_P0651-AW7-MON18.01.1700012345
  * MU1201-MHI2_JP_VW48x_P1201-AW7-MON22.07.1900012345


:::success
The first Aisin unit coverted to EU had train MHI2_TW_VW48x_P0952 MU0836 and was converted to MHI2_ER_VWG13_P4521 MU1367

:::

 ![MHI2_TW_VW48x_P0952 MU0836 - PN: 5NA035032](attachments/d103a28d-a4cd-49e6-8ea9-670b58b2e865.png)


:::info
Conversion was **successful** but take into consideration that [MMX NAND](/MHI2 MHI2Q Harman Aisin/Hardware MHI2/#h-mmx-pcb) on AW7 is partitioned differently compared to Harman G11/G13 units.

:::

# NAND partitions

Partition mapping of the [Harman units](/doc/mib25-g13-mib2-g11-conversion-tRLwExVcWG) differs from [Aisin G11 and G13 units](/General information/Train version/):

 ![on the left Harman G13, on the right Aisin G13](attachments/f633720f-975a-4cdd-afdf-15b12ef123d1.png)

```
 _____OS_____     Start      End     ______Number______   Size    Boot  
     name    type    Cylinder  Cylinder  Cylinders   Blocks                 

1.   QNX6     177          0        685       686     2809792   1371 MB
2.   Extd'd     5        686      28005     27320   111902720  54640 MB
2.1  QNX6     178        686        997       312     1277888    623 MB
2.2  QNX6     178        998       2277      1280     5242816   2559 MB
2.3  QNX6     178       2278       4325      2048     8388544   4095 MB
2.4  QNX6     178       4326       4453       128      524224    255 MB
2.5  QNX6     178       4454       4965       512     2097088   1023 MB
2.6  QNX6     178       4966       5477       512     2097088   1023 MB
2.7  QNX6     178       5478       6501      1024     4194240   2047 MB
2.8  QNX6     178       6502       6757       256     1048512    511 MB
2.9  QNX6     178       6758      22731     15974    65429440  31947 MB
2.10 QNX6     178      22732      27851      5120    20971456  10239 MB
2.11 QNX6     178      27852      28005       154      630720    307 MB
3.   QNX6     179      28006      30315      2310     9461760   4620 MB
4.   ------   ---   --------   --------   -------  --------  -----      
```

Partition 2.8 is smaller and partition 2.11 is added: 

`/dev/mnand0t178.10        630528     10752    619776       2%  /mnt/aw-persiste`

## Examples

MU0623-Partition.txt

[ MU0623-Partition.txt](attachments/e25e639b-fe04-4916-a7c1-7164a4d51ce0.txt)

MU0836-Partition.txt

MEN2 

# Changes in the MMX NAND file system

```
/mnt/navdb/db/SPOT/      1557896   1557896         0     100%  /mnt/navdb/spot/
/mnt/navdb/db/DBICO         9324      9324         0     100%  /mnt/navdb/dbico
/dev/mnand0t178.10        630528     10752    619776       2%  /mnt/aw-persiste
/ramdisk/pps_dummy_            0         0         0     100%  /ramdisk/pps
```


:::tip
There might be more, but time and access to this unit was limited.

:::

# Conclusions

For a cleaner conversion to EU it would be better to repartition the NAND too.

A conversion from EU to CN/JP/KR/TW will most likely only work if the NAND is partitioned like shown [above](/MHI2 MHI2Q Harman Aisin/Hardware MHI2/Aisin MHI2 MHI2Q units with AW7 hardware//#h-nand-partitions) to have FW running correctly.

This special partitioning seems to be just FW related and bound to Asian market and not a hardware limitation.