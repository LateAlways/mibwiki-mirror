# Mounting VMDK in QNX VM

## Add your Dump (IMG as VMDK)


1. Install VMWare Workstation
2. [Convert img to vmdk](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Installation via eMMC dump (VM QNX  .vmdk)/Converting IMG to VMDK with QEMU/)
3. Download QNX VM from [https://mibsolution.one/index.php/f/17124](https://mibsolution.one/index.php/f/183112) and add to VMWare Workstation
4. Open QNX VM properties and add the Dump.vmdk as Storage.
5. Boot QNX VM, login as root, open Terminal and check that VMDK is mounted in /fs/xxx


:::info
You can an USB stick and mount it into the VM (this is the easiest way to exchange data between VM and PC).

:::

## Ready to modify

Now you can start to modify whatever you want.

For example:

Install MIB2 Toolbox (TechniSat/Preh)

Copy and/or replace SWaP file, CP file or whatever you want.

Shutdown the VM when you have finnished the modifications.


## Useful file locations (also see [here](/MST2 TechniSat Preh/MIB STD2 PQ ZR Toolbox/Understanding of the patching process/Useful File locations/))

| Object | Path | File |
|----|----|----|
| FEC | `/tsd/bin/swap/` | `tsd.mibstd2.system.swap` |
| CP | `/tsd/hmi/` | `tsd.mibstd2.hmi.ifs` |
| EL | `/tsd/etc/slist/` | `signed_exception_list.txt` |
| Network Config | `/tsd/etc/networking/` | `pf.config` |
| Boot logo | `/tsd/etc/startanim/` | `startup_x.boot` |
| Startup | `/tsd/bin/system/` | `startup` |


:::tip
If you don't know how to patch the FEC or CP file take a look at this topic:

<https://mibwiki.one/share/5260f4df-06c1-4e34-9cd8-2514b4b794f2>

:::


\