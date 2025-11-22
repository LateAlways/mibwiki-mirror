# Converting IMG to VMDK with QEMU

## Installation:


1. Install QEMU  <https://qemu.weilnetz.de/w64/.>
2. Choose **Start** > **Computer** and right-click **Properties**.
3. Click **Advanced system settings**.
4. In the **System Properties** dialog box, click **Advanced** > **Environment Variables**.
5. In the **Environment Variables** dialog box, search for **Path** in the **System Variable** area and click **Edit**. Add the installation path from QEMU (example: **C:\\Program Files\\qemu** to **Variable Value)**. Use semicolons (;) to separate variable values.


## Commands:

Save img into the QEMU folder (commands are easier) and open the QEMU folder in CMD → as Admin!


### IMG to VMDK

```javascript
c:\Program Files\qemu\>qemu-img convert -p -f raw -O vmdk xx.img xx.vmdk
```


### VMDK to IMG

```javascript
c:\Program Files\qemu\>qemu-img convert -p -f vmdk -O raw xx.vmdk xx.img
```


 ![](attachments/7cba637a-e2b2-4ed7-8648-c1bcd9f5af0c.png)