# How to boot ifs-emergency.ifs (start blue emergency EFU)

## [Stop IPL by sending break on power on](/MHI2 MHI2Q Harman Aisin/Recovery/RCC/How to stop IPL, enter CLI, boot ifs-emergency.ifs and restore ifs.root-stage2/)

In CLI prompt, enter "boot -t emerg" to start Emergency IFS which loads from **ifs-emergency.ifs** of **RCC NOR partition**

Emergency IFS runs in two modes:

* 1st boot
* 2nd boot


:::tip
Stopping IOC watchdog in Emergency IFS on the 1st boot is not possible! After 60 seconds it will force the reboot of the Emergency IFS and log you off.

So the best you can do on the 1st boot is to login as root with RCC emergency password and enter:

```
echo dummy >/HBpersistence/DeveloperMode 
```

:::

Example of the Emergency IFS 1st boot:

 ![1st boot sequence - IOC watchdog will reboot Emergency IFS after 60 seconds](attachments/e77e8232-41c7-4907-b5da-aaffb44ab86e.png)


After 60 seconds on the 2nd boot, Emergency IFS detects that it was rebooted, switches off IOC watchdog, shows a special banner and starts it's own countdown timer:


 ![2nd boot sequence - Emergency EFS shows a countdown timer before reboot](attachments/385959d6-956a-4958-9ee4-1cc4f172909c.png)If DeveloperMode is off (by default), to stop Emergency IFS't timer from rebooting, you have to login via root with RCC emergency password and enter:

"slay -9 MIBEmergency"

After this you have unlimited time to fix stuff ;)


### Enabling DeveloperMode in Emergency IFS

```
***********************************************************
**  You can enable DeveloperMode like this:              **
**  echo dummy > /HBpersistence/DeveloperMode            **
**       or temporarily                                  **
**  echo dummy > /tmp/HBpersistence_DeveloperMode        **
***********************************************************
```

This commands can be entered in Emergency IFS on 1st boot, 2nd boot and even in normal boot mode too:

```
mount -uw /net/rcc/mnt/efs-persist
echo dummy > /HBpersistence/DeveloperMode 
```


:::tip
DeveloperMode prevents 2nd boot Emergency IFS from running a countdown timer, so you do not need to enter "slay -9 MIBEmergency" anymore.

When DeveloperMode is enabled, Emergency IFS will not show a special banner anymore.

:::


 ![2nd boot sequence - with enabled DeveloperMode](attachments/55af4b04-4a14-4ebc-8a2e-b44df6b935e4.png)