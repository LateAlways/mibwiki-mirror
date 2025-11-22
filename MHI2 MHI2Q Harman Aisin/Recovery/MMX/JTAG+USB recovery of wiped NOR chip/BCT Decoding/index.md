# BCT Decoding

The BCT.bin can be inspected with the bct_dump tool that can be installed on Ubuntu or WSL with:

```none
sudo apt install cbootimage
```

Then decode BCT.bin with:

```none
bct_dump BCT.bin
```

It will produce a long output like

```javascript
Version       = 0x00030001;
BlockSize     = 0x00008000;
PageSize      = 0x00000800;
PartitionSize = 0x08000000;
OdmData       = 0x80399105;
# Bootloader used       = 2;
# Bootloaders max       = 4;
# BCT size              = 6128;
# Hash size             = 16;
# Crypto offset         = 16;
# Crypto length         = 6112;
# Max BCT search blocks = 64;
#
# These values are set by cbootimage using the
# bootloader provided by the Bootloader=...
# configuration option.
#
# Bootloader[0].Version      = 0x0000009b;
# Bootloader[0].Start block  = 28;
# Bootloader[0].Start page   = 0;
# Bootloader[0].Length       = 68656;
# Bootloader[0].Load address = 0x84008000;
# Bootloader[0].Entry point  = 0x84008000;
# Bootloader[0].Attributes   = 0x00000006;
# Bootloader[0].Bl AES Hash  = 3ed5ffb4533055bf5a582a5cd0cfb942;
# Bootloader[0].RsaPssSigBl:
# Bootloader[1].Version      = 0x0000009b;
# Bootloader[1].Start block  = 12;
# Bootloader[1].Start page   = 0;
# Bootloader[1].Length       = 68656;
# Bootloader[1].Load address = 0x84008000;
# Bootloader[1].Entry point  = 0x84008000;
# Bootloader[1].Attributes   = 0x00000004;
# Bootloader[1].Bl AES Hash  = 3ed5ffb4533055bf5a582a5cd0cfb942;
# Bootloader[1].RsaPssSigBl:

SDRAM[0].MemoryType                         = NvBootMemoryType_Ddr3;
SDRAM[0].PllMChargePumpSetupControl         = 0x00000008;
SDRAM[0].PllMLoopFilterSetupControl         = 0x00000000;
SDRAM[0].PllMInputDivider                   = 0x0000000c;
...
SDRAM[2].McEmemArbRsv                       = 0xff00ff00;
SDRAM[2].McClkenOverride                    = 0x00000000;
```

Here we can see two stage 1 bootloaders at block 28 and block 12, with a block size of 0x00008000.

These correspond to the STAGE1_PRIMARY and STAGE1_RECOVERY partitions above.

Importantly, both bootloaders have Load address and Entry point = 0x84008000 that must be supplied as a command line parameter of [nvflash](/MHI2 MHI2Q Harman Aisin/Recovery/MMX/JTAG+USB recovery of wiped NOR chip/).