# Telnet Activation

:::info
All described below can be simply done in [MIB STD2 PQ/ZR Toolbox](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/) via `Network→Activate permanent telnet and console access`

:::

## Modify the "startup" and "networking" file

Open the startup file `/tsd/bin/system/startup`

Search for '`# Start cpu root in a subshell, so that cpu root can run in foreground and after exit we can call the shutdown stuff`

Add in a new line before and save:

```javascript
# Start inetd
/usr/sbin/inetd &
```


Open the pf.conf file `/tsd/etc/networking/pf.conf`

Search for:

```javascript
#HMI Logging
pass in quick on ax proto tcp from any to any port 15001 keep state
```


Add in line after that and save:

```javascript
# Enable Telnet
pass in quick on ax proto tcp from any to any port 23 keep state
```


## Also possible for SD Patch

For that use the 2 files from FW Update files:

startup: `/cpu/config_EU_sec_xxx/xx/default/cpu_configEU_xxx.tar.gz/config_EU_sec_xxx/xx/cpu_configEU_xxx.tar/tsd/bin/system/startup`


pf.conf:

`/cpu/networkmgr_sec/xx/default/cpu_networkmgr_sec_xxx.tar.gz/cpu_networkmgr_sec_xxx.tar/tsd/etc/networking/pf.conf`


After modifying the 2 files as written above you have to use the DIY SD Patch files from:

<https://mibwiki.one/share/5260f4df-06c1-4e34-9cd8-2514b4b794f2>


Copy the startup file  to `/tsd/bin/system/`

Copy the pf.conf file to `/tsd/etc/networking/`

Generate hashes.txt and copy this Telnet Activation Patch to the SD Card.