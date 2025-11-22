# MMX Tegra Boot Process Details

For anyone interested in the MMX recovery process, I have got a fair bit figured out - but still no full USB only solution.


In a normal Tegra system, the hw/fuse straps on the CPU tell its startup system to load the BCT sector from NOR chip, as the BCT contains the address of the RAM where the stage1 bootloader should be loaded and executed. See <https://http.download.nvidia.com/tegra-public-appnotes/tegra-boot-flow.html>


The BCT is a hardware specific chunk that has details about the exact model of SDRAM used on the board and where to load the bootloader - importantly the BCT is in a M.I.B. mmx backup, but it's not in a firmware upgrade pack because it's unit (or at least hardware model) specific.


When in USB recovery mode, nvflash can be used to load the BCT from MMX backup and any chunk of data/code into a specified ram location, then run that code.

So I can snip the stage 1 bootloader (qboot) out of backup (or grab it from any fw pack) and use nvflash to load it into the right bit of ram, then run it. On it's own though it quickly crashes because it jumps to an empty location in ram.


Qboot previously checks in this location in ram for the stage 2 bootloader, if it's not there it tries to loads the stage 2 bootloader from nor, if that fails with loads the stage 2 recovery instead from nor.

I found that if I merge the binary data for qboot and stage 2 with the right offset so that stage2 is in the right location when the merged copy is loaded with nvflash it successfully jumps directly to stage 2.

Stage 2 then initialises some more hardware, checks some jumpers and watches for E on UART to decide whether to load the primary kernel or the recovery one.  The kernel is the image with ANDROID! at the start, though this header is slightly obfuscated in the firmware packs. Other than that it's in standard Android boot image format.

Similar to qboot, stage2 looks for the kernel in a specified location which can be preloaded in a merged binary.
This isn't the kernel directly from nor/fw pack though. In fw/pack and in nor this has a 0x800 byte header before the kernel which is zlib compressed. I had to merge the header plus a manually decompressed kernel at the right location for it to run any code from the kernel - but it only gets a few kernel lines of log on UART before failing with errors accessing files like the serial port and /etc/boot.sh (which look like they should exist in the kernel image).


What I did figure out is:

| partition | addr | end |
|----|----|----|
| STAGE1_RECOVERY | 0x84008000 | 0x84018c30 |
| STAGE2_RECOVERY | 0x84063000 | 0x8406b310 |
| KERNEL_RECOVERY | 0x8406b30f | 0x84c60b8f |

Stage1 (qboot) takes up about 67K, then there's a 296K gap before the location that stage2 needs to be loaded at.

Stage2 is \~ 32K long of real data - the last byte of which is a 0.

If you look close, Kernel overlaps this by 1 bytes - stage2 looks at this last byte in is range, if it's a null string it tries to find a kernel and loads it here, replacing the 0. Once that's loaded, the ANDROID! string is present at this memory location.


All this gets the kernel booting - if I use KERNEL_PRIMARY instead of KERNEL_RECOVERY I get a slightly different startup log, but still ends/fails at the same point.
I've completely failed to figure out why the kernel doesn't boot properly - this error message doesn't give me much to go on.

Fair chance my manual decompressing isn't quite right, maybe some bits are supposed to be moved or something.

PS. Loading these merged binaries in ghidra works surprisingly well to disassemble / decompile the code. It turns out stage 2 runs plenty of functions from stage 1 (qboot) - they've got a fair bit of shared code.


There are a lot of places in the ghidra decompilation of the the bootloader / memory loading code that look for data in the gap between stage1 and stage2, but I don't know what's supposed to be there. Most importantly, when stage2 tries to load and decompress a kernel from the name KERNEL_PRIMARY or KERNEL_RECOVERY it looks for a whole heap of things here first.


Since this initial investigation I've used JTAG to investigate a running system. It seems that once stage 2 is running, it starts to use / overwrite some places in stage 1 bootloader.


The gap in between certainly does get data loaded into it too, but that data doesn't directly match anything in the NOR backup. At the start of the gap a number of snippets of data are loaded, mostly pointers / address lookups to strings in other areas. In the latter half of the gap a section of data does match the Partition Table format, but the content doesn't match the NOR chip. I'm not sure where it comes from.


When a Kernel is running on a working system it seems to be loaded / running from addresses in the 0xFC000000 or 0xFE000000 range, not in 0x84060000. Memory read from these ranges again doesn't seem to match anything in the compressed or decompressed images directly, so again there appears to be more complex memory organising taking place than the static table I started with above.


[ create_image.py](attachments/7146202c-106d-4623-a022-8837a472504c.py)


[ Tegra3_publicTRM_DP05644001_v03.pdf](attachments/3e39d466-d7f6-4f8d-91da-fb043e9fd9c8.pdf)


This project describes patches to fastboot to enable uart logs <https://github.com/tofurky/tegra30_debrick>

The MMX uses UARTD rather than UARTA used on most off-the-shelf tegra boards. [uart_payload_ouya.bin](https://github.com/tofurky/tegra30_debrick/blob/master/payload/uart_payload_ouya.bin) in that project appears to be configured for UARTD so might work if patched into a fastboot (or other bootloader) that works in other ways.


[ u-boot-dtb-tegra.bin](attachments/8b10d51b-3e32-4233-859f-d45fafb431e4.bin)

```javascript
nvflash --bct BCT.img --bl u-boot-dtb-tegra.bin --go
```