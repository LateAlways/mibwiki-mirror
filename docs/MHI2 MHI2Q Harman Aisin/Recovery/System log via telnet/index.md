# System log via telnet

:::info
UART access to RCC or MMX shows the system log. To see these logs via Telnet (press Ctrl+C to return to shell):

:::

```bash
#show rcc syslog
on -f rcc sloginfo -w
#show mmx syslog
on -f mmx sloginfo -w
```


:::tip
You can start multiple telnet sessions to RCC/MMX at the same time

:::

## Sloginfo syntax

 ![-w will continuously output syslog to shell](attachments/c0966d9d-52cf-4e8d-af76-14bca6102d0f.png)

```bash
#rcc syslog will be written to syslog_rcc.txt on SD1
mount -uw /net/mmx/fs/sda0
on -f rcc sloginfo -w >> /net/mmx/fs/sda0/syslog_rcc.txt
```