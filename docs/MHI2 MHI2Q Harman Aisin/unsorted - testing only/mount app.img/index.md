# mount app.img

:::tip
For some reason this is not working all the time …

 ![](attachments/2d8b2437-9e38-43d2-8fb0-f314f0330d3c.png)After a few restarts, mounting suddenly started to work again…

:::


```bash
#create new folder "mounted"
#this will aid as mounting target 
mount -uw /mnt/app/
mkdir /mnt/app/mounted

#mount app.img from e.g. SD card to the previously generated folder
mount -rt qnx6 /fs/sda0/app.img /mnt/app/mounted

#in some cases you have to add -o loop
mount -t qnx6 -o loop /fs/sda0/app.img /mnt/app/mounted
```


 ![read/write access to mounted app.img (here via SSH connection)](attachments/06368b23-a354-487a-91d6-6628733b4a22.png)