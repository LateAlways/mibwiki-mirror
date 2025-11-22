# ExceptionList BUG

:::info
This bug is fixed on current M.I.B versions and ifs-root-stage2 patches available since April 2020

:::


:::tip
Always get [latest M.I.B](https://mib.mibsolution.one) version before patching.

:::

## F&Q

Your unit was patched before April 2020?

* Most likely EL (ExceptionList.txt) based patch was used.
* It turned out, that especially on Audi units this kind of patch could cause the unit to freeze up during boot.
* Unit does not react to any button or screen inputs and it is rebooting every 60s.

## Fix frozen unit

Unit is still accessible via [telnet and uart](/MHI2 MHI2Q Harman Aisin/Shell access via telnet and UART/).

Access unit via Putty and run the following command:

```bash
rm /mnt/efs-persist/FEC/mmx_fec_ids.bin
```


:::tip
After reboot you have about 50s to enter shell and run this command

:::


:::warning
To fix this issue permanently you have to move from EL to FecContainer.fec based patch

:::


## Switch to FecContainer.fec based patch

To permanently fix this issue you have to replace the custom EL with the stock one and edit the FecContainer.fec. Most of the patches available before April 2020 had already a FEC patch included, so applying a new ifs-root-stage2 is not required in most cases.


Use M.I.B and run the following command to replace EL with stock version (BUG free) and edit FecContainer.fec:      ![run "Add new FEcs to FecContainer.fec"](attachments/ba9b9707-79fe-4d44-b454-8f2d34accd5a.png)



:::info
OPTIONAL: If you also want to have the new ifs-root-stage2. Apply stock FW to unit and patch again with latest M.I.B version.

:::