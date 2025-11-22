# Converting US > EU

# Converting US > EU


:::info
Firmwares with **MEN3**, **MBA3, MHI3**, **MPR3** trains already contain EU languages.

:::

You can enable them in "**Engineering Testmode>Software System>HMI Look and Feel>System Languages>Availability of languages"** and/or write new 720B and 720C datasets into block 5F with ODIS-E or CarScanner like described in https://www.drive2.com/b/651557397554272550/

## Good to know

On MBA3/MHI3/MPR3 units that contain no EU languages, it is possible to desolder eMMC/UFS153 chip, [activate sshd](https://mibwiki.one/doc/mhi3mpr3-enable-sshd-7jJdphliiw) and flash with the patched EU firmware.

Reference: https://www.drive2.com/b/676131757312982724/