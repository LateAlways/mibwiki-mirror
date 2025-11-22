# Telnet access

[1 mh2p tutorial.pdf 461443](attachments/a4b4261b-13f0-4b5b-9d91-71d30a6e8635.pdf)


# Telnet activation


1. Insert SD card with [Toolbox](https://disk.yandex.com/d/7WKZix6ocBNLCw) and hold two fingers in top right corner to enter **Engineering** (**RED**) menu

 ![](attachments/288275af-f6a5-46c9-b7fc-d530985ce578.png)


2. Press **Update**

 ![](attachments/fb5d7aaf-9181-418c-857e-6f2848b324bf.png)


3. **Start update**.

 ![](attachments/c71d6edb-8887-4374-88b4-2efe220c0b2e.png)


4. Press **Resume**

 ![](attachments/d012c96e-f2b8-4f27-8d72-252bedc17ba4.png)



 5. Connect usb of D-Link DUB-E100 compatible cable into usb of MH2p.
 6. Connect ethernet port of the D-Link DUB-E100 into ethernet port of the laptop.
 7. In the network properties of the laptop's ethernet adapter set IP address **172.16.250.123** netmask **255.255.255.0**
 8. Connect with putty in telnet mode to IP **172.16.250.248:22111** and select hexadecimal text string you see (it will be copied into copy&paste buffer automatically). Do **NOT** close the putty window
 9. Paste copied challenge string into **mmx_challenge.txt**, save the file and run **response.exe** to generate **mmx_response.txt**
10. Copy and paste content of **mmx_response.txt** into putty window and press ENTER. The window should close automatically.
11. Now you can connect with putty in telnet mode to **172.16.250.248:23**
12. Enter root and you should be in shell #

**GOOD TO KNOW!** Depending on firmware/brand, you may need to do this in regular mode or in Engineering (RED) menu.

Good luck!


Read more [https://www.drive2.com/b/644918546345774500](https://www.drive2.ru/b/644918546345774500)