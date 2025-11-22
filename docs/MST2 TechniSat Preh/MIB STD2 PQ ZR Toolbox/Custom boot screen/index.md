# Custom boot screen

:::warning
This tutorial was made 2021, December 9th. Tools used here were still experimental and under development.

:::


:::tip
Keep your working directory well organized. It will help you work faster and make a proper modification.

:::

## Tools

* `MIB STD2 Toolbox` [from here](https://github.com/olli991/mib-std2-pq-zr-toolbox/releases).
* Alternative `compress-startup_x.boot.py` compression script from [this post](https://github.com/olli991/mib-std2-pq-zr-toolbox/issues/2#issuecomment-968259023).
* `Gimp` [from here](https://www.gimp.org/downloads/).
* `mib2image` Gimp plugin from [this post](https://github.com/olli991/mib-std2-pq-zr-toolbox/issues/2#issuecomment-988947378).
* `python3` [from here](https://www.python.org/downloads/).

## Set up the environment


1. Download and install `Gimp`.
2. Download `mib2image` plugin and place it in the plugins directory of your `Gimp` installation.
3. Install `python3`.
4. Download `MIB STD2 Toolbox`.
5. Download alternative `compress-startup_x.boot.py` script.
6. Replace original `` `/tools/compress-startup_x.boot.py `` with the alternative one.

## Get original boot screen

You can get the original boot screen file from:

* firmware update package
* by dumping it from the unit with the toolbox
* copy it manually via FTP access to your main unit.

In this example I'm going to use `startup_4.boot` file from `VW ZR EU P0245T` and I'm going to place it in `startanim/1-original/` directory.

## Extract files


1. Open `Command Line Interface` or `Terminal`.
2. Extract the file with command `python3 /Volumes/HDD/mib-std2-pq-zr-toolbox/tools/extract-startup_x.boot.py /Volumes/HDD/startanim/1-original/startup_4.boot /Volumes/HDD/startanim/2-original_extracted/`.
3. Open the `2-original_extracted/` directory and check if you see `.png` files inside. Those `.png` images will be black&white but you will be able to see which file is which.
4. Duplicate the `2-original_extracted/` and name the duplicate `3-original_with_mods/`.
5. Open the `3-original_with_mods/`. This is your working directory, so it's a good idea to keep it organized. I'm going to create `fender`, `dynaudio`, `bluemotion`, and `vw` directories inside to place the .png files inside them.
6. Change extensions from `.png` to `.mib` of all files from the `3-original_with_mods/` directory and subdirectories.
7. Right-click on a `.mib` file and open it with `Gimp`. If the file opens correctly, you can associate `.mib` extension with `Gimp` for future convenience.

## Modify


1. Open `.mib` files that you wish to modify.
2. Use your graphic design skills to modify original files.
3. Export each modified file with `File` > `Export As…`, open the `Select File Type (By Extension)` section, highlight `MIB2STD BOOT image`, press `Export`, and `Replace`. Set the `Extract label to separate file` to `No`, and press `OK`.
4. Change extensions of  `.mib` files back to `.png`.
5. Once again duplicate the `2-original_extracted/` and name the duplicate `4-mod_unpacked/`.
6. Use your custom `.png` files to overwrite stock ones in the `4-mod_unpacked/` directory.

## Compress


1. Open `Command Line Interface` or `Terminal`.
2. Compress files with command `python3 /Volumes/HDD/mib-std2-pq-zr-toolbox/tools/compress-startup_x.boot.py /Volumes/HDD/startanim/1-original/startup_4.boot /Volumes/HDD/startanim/5-mod/startup_4.boot /Volumes/HDD/startanim/4-mod_unpacked/`.

## Check


1. Check if `startanim/5-mod/startup_4.boot` files was created correctly.
2. Unpack it again, just to be sure that everything is fine. Use command `python3 /Volumes/HDD/mib-std2-pq-zr-toolbox/tools/extract-startup_x.boot.py /Volumes/HDD/startanim/5-mod/startup_4.boot /Volumes/HDD/startanim/6-mod_test/`.
3. If everything goes OK, you should be able to extract the modified file.

## Upload to MIB


1. Use FTP access or MIB STD2 Toolbox to upload your modified file.
2. Review module `5F` long coding to make sure that the module is coded to use boot screen that you were working on.
3. Reboot the unit with [button combination](/General information/Useful documents/Key combinations and shortcuts/).


:::info
Special thanks to everyone that was involved in making this possible: Olli991, jille, jtomtos, yox2019.

:::