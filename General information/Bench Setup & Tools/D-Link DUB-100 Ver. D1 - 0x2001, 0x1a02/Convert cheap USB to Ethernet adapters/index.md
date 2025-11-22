# Convert cheap USB to Ethernet adapters

[https://www.youtube.com/watch?v=NGaXMYTP_YA](https://www.youtube.com/watch?v=NGaXMYTP_YA)


\

:::info
M.I.B is adding support for these cheap adapters to MHI2(Q) units during install!

No need to change vid/pid of adapter in this case.

:::

```bash
# Install required tools
sudo apt-get update && sudo apt-get install ethtool

# Check connected USB devices
lsusb

# Check network interface name
ifconfig

# Check if EEPROM is can be edited
sudo ethtool -i eth1

# Read current EEPROM data
sudo ethtool -e eth1

# Overwrite EEPROM data with VID 0x2001 & PID 0x3c05
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0088 value 0x01
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0089 value 0x20
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x008A value 0x05
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x008B value 0x3c
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0048 value 0x01
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0049 value 0x20
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x004A value 0x05
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x004B value 0x3c

## If you are executing these commands on a newer Linux Distro, you would need to add `length 1` at the end of each `ethtool -E` command to fix `offset & length out of bounds` error
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0088 value 0x01 length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0089 value 0x20 length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x008A value 0x05 length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x008B value 0x3c length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0048 value 0x01 length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x0049 value 0x20 length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x004A value 0x05 length 1
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x004B value 0x3c length 1

# Read current EEPROM data once again to confirm changes
sudo ethtool -e eth1

# Reconnect USB device

# Check if USB device is not visible as D-Link
lsusb
```

```bash
# Alternatively you can use PID 0x1a02
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x008A value 0x02
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x008B value 0x1a
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x004A value 0x02
sudo ethtool -E eth1 magic 0xdeadbeef offset 0x004B value 0x1a
```