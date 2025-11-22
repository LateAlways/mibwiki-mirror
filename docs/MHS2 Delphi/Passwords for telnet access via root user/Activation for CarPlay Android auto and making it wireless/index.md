# Activation for CarPlay Android auto and making it wireless

Commands that need to be entered while in red engineering menu through putty while connected to system.


\

\[\[ ! -d /mnt/app \]\] && mount -t qnx6 /dev/mnanda0t177.1 /mnt/app # Mount app if in Engineering

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:7.4 1 # PAG/AU only , /gem/anpassungen/0x22ad fahrzeug-konfiguration- Attribute: Online Medien auf „ein"

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:7.6 0 #for ER Region ,Enable Baidu CarLife

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:7.7 1 # Google GAL on

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:8.0 1 # Apple DIO on

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:8.2 1 # Wifi_Client_HMI on

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:23.3 1 # Apple DIO Wireless on

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:17.5 1 # Wifi 5GHz switch activated

/mnt/app/armle/usr/bin/pc b:0x5F22:0x22AD:20.2 1 # must enable if enable baidu carlife

/mnt/app/armle/usr/bin/pc b:0x5F22:0x600:19.6 1 # USB iPod

/mnt/app/armle/usr/bin/pc b:0x5F22:0x600:19.7 1 # USB iPod

/mnt/app/armle/usr/bin/pc b:0x5F22:0x600:24.3 1 # WLAN on


\
echo gem-reset > /dev/ooc/system # Reboot system