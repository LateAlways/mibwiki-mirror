# Toolbox

1. Download and unzip https://disk.yandex.com/d/7WKZix6ocBNLCw (the latest version is always here) onto FAT32 formatted SD card
 2. Insert SD card into any SD slot of MIB .
 3. Long press `MENU` button or press with two fingers in the right top corner of the touch screen. The unit will reboot into Engineering (aka RED or SWUP) mode.
 4. Update
 5. Connect USB port of D-Link DUB-E100 to the vehicle USB port.

    
    1. **GOOD TO KNOW:** A compatible adapter has the following hardware ID: `VID_2011 & PID_1A02` (Windows Device Manager → Device Properties → Details Tab → Hardware Ids)
    2. An adapter based on chip `Asix AX88772`, such as `UGREEN USB 2.0 100Mbps`, may possibly be converted to work. The following youtube video describes a process for doing this:

       [https://www.youtube.com/watch?v=NGaXMYTP%5FYA](https://www.youtube.com/watch?v=NGaXMYTP%5FYA)

 6. On the laptop in ethernet adapter settings set Set IP address `172.16.250.123` netmask `255.255.255.0`.
 7. `ping 172.16.250.248 -t`
 8. If ping is ok, connect with putty in telnet mode to `172.16.250.248:22111` and you will see:

     ![](attachments/31990ac8-f6e7-4f45-bd46-c845f435b2b9.png)
 9. Select hexadecimal string and putty will copy it into clipboard. Do **NOT CLOSE** putty window.
10. Open `mmx_challenge.txt` in **notepad++** and press `Ctrl` **+** `V` to paste copied string. Save.
11. Run `response.exe` and it will generate `mmx_response.txt`
12. Copy string from `mmx_response.txt` into putty window and press `ENTER`. Putty window should close automatically.
13. Open putty and connect in telnet mode to `172.16.250.248:23`
14. Run Toolbox with one of the following commands depending on where your SD inserted:

    `ksh /fs/sdb0/toolbox.sh` \n `ksh /fs/sda0/toolbox.sh` \n `ksh /fs/usb0_0/toolbox.sh`

Reference: [https://www.drive2.com/b/644918546345774500/](https://www.drive2.ru/b/644918546345774500/)