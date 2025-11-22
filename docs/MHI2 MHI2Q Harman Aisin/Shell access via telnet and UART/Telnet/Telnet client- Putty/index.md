# Telnet client- Putty

## Telnet client

Any Telnet client can be used. The most popular (easy to use) is <https://www.putty.org/>


The MHIG/MHI2/MHI2 supports two ports to login by telnet.

Each of its main components - MMX and RCC - have their own access.

·         IP for both: 172.16.250.248

·         RCC port: 123 (**recommended**)

·         MMX port: 23


:::info
Recommendation: Always use RCC, in case of wrongly used flash commands the risk to damage MMX is smaller.

:::

## Putty settings


:::info
[D-LINK](/General information/Bench Setup & Tools/D-Link DUB-100 Ver. D1 - 0x2001, 0x1a02/) or compatible USB to ethernet adapter required

Set IP in PC to IP: 172.16.250.123 MASK: 255.255.255.0

:::

 ![MMX settings](attachments/b1ab754e-f8bf-4d4d-b5de-85c0bc7a0617.png)


 ![RCC settings](attachments/0af731dd-f58c-4803-ba7b-b1a92d9485b0.png)


\