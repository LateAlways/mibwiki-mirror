# MIB STD2 Network and Logging

The USB Port offers to connect a compatiple USB Network interface 

D-Link or  ASIX AX8772B compatibles like Edimax EU-4208


Open TCP Ports found with nmap:

54321 MLP Logging most of it as MLP Textmessage

55555 Unknown

50000 Unknown

15001 MLP Logging Mainly Binary encoded

15361 Unknown

8911 Unkown

1234 Unkown

23 Telnet  (imX console)

22 FTP


\
# **MLP Logging**

Ports 54321 and 15001 provide a Logging Output port and will costantly stream out Logging events

A MLP Message consists of 4Bytes Packet Length +Tag "€MLP"+ Outer MLP Frame header (containing a MSG type)+ Inner Frame Header (depending on the MSG type, and containing a codec version number)

Knowing the Message Type and Codec Version, the MLP Mesage can be decoded.

As the binary encoding might change from Version to Version or Train to Train, it makes no sense to reimplement a too detailed interpreter for everything, as it would not work for all Versions


Luckily the needed libraries to decode are shipped with the HMI in the HMI in /tsd/hmi/HMI/jar/MIBTestDebug-HXX.YYY.ZZ-STD2xxxx_EU.jar/MIB-CodecsClient

Not beeing a JAVA Head , i only have a quick POC. If someone is interested in making progress on that and give back to the community, you might try to contact me


Messages of Type 260 and >500 are usually Text encoded and quite readable. Only Values like Integers, floats , Bits are unfortunately not directly printed as Text but as binary encoded objects within the string. this can be decoded easily. A Python POC is available 


\

\

\

\

\