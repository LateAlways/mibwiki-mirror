# NAND partitioning

Manual partitioning of the MMX NAND

```bash
on -f mmx sh
fdisk /net/mmx/dev/mnand0 delete -a
fdisk /net/mmx/dev/mnand0 add -s1 -t177 -c0,357
fdisk /net/mmx/dev/mnand0 add -s2 -t5 -c358,29285
fdisk /net/mmx/dev/mnand0 add -s2 -e1 -t178 -n512
fdisk /net/mmx/dev/mnand0 add -s2 -e2 -t178 -n2048
fdisk /net/mmx/dev/mnand0 add -s2 -e3 -t178 -n2048
fdisk /net/mmx/dev/mnand0 add -s2 -e4 -t178 -n256
fdisk /net/mmx/dev/mnand0 add -s2 -e5 -t178 -n512
fdisk /net/mmx/dev/mnand0 add -s2 -e6 -t178 -n512
fdisk /net/mmx/dev/mnand0 add -s2 -e7 -t178 -n1024
fdisk /net/mmx/dev/mnand0 add -s2 -e8 -t178 -n256
fdisk /net/mmx/dev/mnand0 add -s2 -e9 -t178 -n15872
fdisk /net/mmx/dev/mnand0 add -s2 -e10 -t178 -n5888
fdisk /net/mmx/dev/mnand0 add -s3 -t179 -c29286,30315
mount -e /net/mmx/dev/mnand0
echo "y" | mkqnx6fs -T media -b 32768 -i 256 /dev/mnand0t178    # /mnt/boardbook
echo "y" | mkqnx6fs -T media -b 32768 -i 2048 /dev/mnand0t178.1    # /mnt/speech
echo "y" | mkqnx6fs -T media -b 32768 -i 256 /dev/mnand0t178.2    # /mnt/gracenotedb
echo "y" | mkqnx6fs -T media -b 32768 -i 2048 /dev/mnand0t178.3    # /mnt/mmebackup
echo "y" | mkqnx6fs -T runtime -b 32768 -i 65536 /dev/mnand0t178.4    # /mnt/icab
echo "y" | mkqnx6fs -T media -b 4096 -i 32768 /dev/mnand0t178.5    # /mnt/adb
echo "y" | mkqnx6fs -T runtime -b 16384 -i 8192 /dev/mnand0t178.6    # /mnt/gecache
echo "y" | mkqnx6fs -T media -b 1024 -i 32768 /dev/mnand0t178.7    # /mnt/ols
echo "y" | mkqnx6fs -T media -b 32768 -i 8192 /dev/mnand0t178.8    # /mnt/navdb
echo "y" | mkqnx6fs -T media -b 32768 -i 16384 /dev/mnand0t178.9    # /mnt/media
echo "y" | mkqnx6fs -T runtime -b 32768 -i 4096 /dev/mnand0t179    # /mnt/ota
```

Flash images and app.img similar to MHI2/MHI2Q