# Coding and Adaptions

Coding and adpations can be written to MHI2(Q) units via console commands

```
# always needed before execution of persistence commands to link libaries and binaries
export PATH=:/proc/boot:/sbin:/bin:/usr/bin:/usr/sbin:/net/mmx/bin:/net/mmx/usr/bin:/net/mmx/usr/sbin:/net/mmx/sbin:/net/mmx/mnt/app/armle/bin:/net/mmx/mnt/app/armle/sbin:/net/mmx/mnt/app/armle/usr/bin:/net/mmx/mnt/app/armle/usr/sbin
export LD_LIBRARY_PATH=/net/mmx/mnt/app/root/lib-target:/net/mmx/mnt/eso/lib:/net/mmx/eso/lib:/net/mmx/mnt/app/usr/lib:/net/mmx/mnt/app/armle/lib:/net/mmx/mnt/app/armle/lib/dll:/net/mmx/mnt/app/armle/usr/lib
export IPL_CONFIG_DIR=/etc/eso/production

#write/read to persistence
on -f mmx /eso/bin/apps/pc

#store changes to persistence
on -f mmx /eso/bin/apps/pc b:0:1 0		

#reboot to save settings to unit!
on -f rcc /usr/apps/mib2_ioc_flash reboot
```


PC command syntax:

```
pc <type>:<namespace>:<key>[:<byte offset>[.<bit offset>]] 
      [<value> [<mask> [<offset in byte>]]]
 
Type: i=int, b=blob, s=string

The <byte offset>.<bit offset> notation is only available for blobs.

Examples for blob handling:
   read complete blob:
    pc b:0:0xC0020054

   read a single byte from blob:
    pc b:0:0xC0020054:3

   read a single bit from blob:
    pc b:0:0xC0020054:3.7
   
   set complete blob; can also change size (spaces in data string are ignored):
    pc b:0:0xC0020054 "04 5684 32 d4 56c4 bb"   
    
   set a byte in blob:
    pc b:0:0xC0020054:6 0x0A
   or the same:
    pc b:0:0xC0020054:6 16   

   set a bit in blob:
    pc b:0:0xC0020054:6.7 1
    
   set some bytes at offset 5 with a mask in blob,
   value and mask must have the same size:
    pc b:0:0xC0020054 "56D42B" "FF0F3A" 5
```