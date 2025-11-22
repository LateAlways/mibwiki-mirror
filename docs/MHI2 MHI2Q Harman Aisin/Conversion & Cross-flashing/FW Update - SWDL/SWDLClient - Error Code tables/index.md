# SWDLClient - Error Code tables

:::tip
Especially section [2. Filecopy specific errors](/MHI2 MHI2Q Harman Aisin/Conversion & Cross-flashing/FW Update - SWDL/SWDLClient - Error Code tables//edit#h-21-filecopy-errors) error are normally related to bad FW SD, meaning:

* bad partition on SD → format again FAT32
* missing files → bad FW archive or skipped files during copying to SD
* **damaged SD card! → this one is __very__ often the case**

:::


:::info
Always get a 2nd SD just in case something is wrong!

And yes, also brand new SD cards can be bad!

:::

# 1. Device specific errors

## 1.1.  Cinterion Errors

| **Error Code** | **Error Description** |
|----|----|
| 128 | SHA1 checksum error! Please verify data on your download medium.\[SWDL_ERROR_SHA1\] |
| 150 | Inialization failed\[SWDL_ERROR_CINTERION_INIT\] |
| 151 | Transfer error while flashing device\[SWDL_ERROR_CINTERION_TRANSFER\] |
| 152 | Path could not be found\[SWDL_ERROR_CINTERION_SET_PATH\] |
| 153 | Firmware stat/fstat error\[SWDL_ERROR_CINTERION_STAT_FILE\] |
| 154 | ASI connection is broken\[SWDL_ERROR_CINTERION_CONNECTION\] |
| 155 | Module infos could not been correctly retrieved\[SWDL_ERROR_CINTERION_MODULE_INFO\] |

## 1.2.  DVD Errors

| **Error Code** | **Error Description** |
|----|----|
| 128 | SHA1 checksum error! Please verify data on your download medium.\[SWDL_ERROR_SHA1\] |
| 150 | Flash process failed\[SWDL_ERROR_FLASHFAILED\] |

## 1.3.  MMX2 Errors

| **Error Code** | **Error Description** |
|----|----|
| 128 | SHA1 checksum error! Please verify data on your download medium.\[SWDL_ERROR_SHA1\] |
| 150 | Could not save update info from emergency\[SWDL_ERROR_SAVEUPDATEINFO\] |
| 151 | Could not remove update info from emergency\[SWDL_ERROR_REMOVEUPDATEINFO\] |
| 152 | MMX emergency image is not correct flashed. Select module MMX2/eifs again\[SWDL_ERROR_NO_MMX_EMERGENCY_IMG\] |
| 153 | RCC emergency image is not flashed or is corrupted.\[SWDL_ERROR_NO_RCC_EMERGENCY_IMG\] |
| 154 | Quickboot recovery is not operable. Select MMX2/qb_recovery to flash next time.\[SWDL_ERROR_QB1_INVALID\] |
| 155 | Quickboot primary is not operable. Select MMX2/qb_primary to flash next time.\[SWDL_ERROR_QB2_INVALID\] |
| 156 | nvTools function error\[SWDL_ERROR_NVTOOLS\] |

## 1.4.  Generic Errors

| **Error Code** | **Error Description** |
|----|----|
| 220 | Not enough memory to allocate\[SWDL_ERROR_MALLOC\] |
| 221 | Memory comparison failed\[SWDL_ERROR_MEMCMP\] |
| 222 | Driver has returned an error\[SWDL_ERROR_DRIVER\] |
| 223 | Partition group sanity check failed! Android header for Primary Group (mifsstage1/mifs-stage2/app/efs-system) or Recovery Group (eifs/qb) is not correct\[SWDL_ERROR_GROUP\] |
| 224 | Cannot find partition or determine partition properties (stat)\[SWDL_ERROR_PARTITION\] |
| 225 | Unable to start thread\[SWDL_ERROR_THREAD\] |
| 226 | Most unlock detected. Waiting for most lock\[SWDL_ERROR_MOST\] |
| 227 | Error in container state corrupt data or MOST unlock\[SWDL_ERROR_CONTAINER_GENERIC\] |
| 228 | Error in container version information: Upgrade to another version first!\[SWDL_ERROR_CONTAINER_VERSION\] |
| 229 | Timeout for getting next block waiting for data\[SWDL_ERROR_IMG_GET\] |
| 230 | Error writing image block\[SWDL_ERROR_IMG_WRITE\] |
| 231 | Could not find image file\[SWDL_ERROR_FILENOTFOUND\] |
| 232 | Could not open file through MOST\[SWDL_ERROR_OPENFILE\] |
| 233 | image file greater than target partition\[SWDL_ERROR_FILESIZE\] |
| 234 | Error while writing image to device. Please press retry.\[SWDL_ERROR_WRITE\] |
| 235 | Error seeking on device\[SWDL_ERROR_SEEK\] |
| 236 | Failed to mount partition\[SWDL_ERROR_MOUNT\] |
| 237 | Failed to unmount partition. Maybe device is busy.\[SWDL_ERROR_UMOUNT\] |
| 238 | Could not open local device\[SWDL_ERROR_OPENDEV\] |
| 239 | Could not prepare device for flashing\[SWDL_ERROR_PREPARE\] |
| 240 | Erasing device failed\[SWDL_ERROR_ERASE\] |
| 241 | Flash memory could not be unlocked\[SWDL_ERROR_UNLOCK\] |
| 242 | Temporary directory creation failed\[SWDL_ERROR_MKDIR\] |
| 243 | failed to change directory to temporary dir\[SWDL_ERROR_CHDIR\] |
| 244 | Could not remove temporary image\[SWDL_ERROR_REMOVE\] |
| 245 | Image file could not be renamed\[SWDL_ERROR_RENAME\] |
| 246 | Error while reading img file\[SWDL_ERROR_READ\] |
| 247 | Pre or post script could not be started\[SWDL_ERROR_SCRIPTSTART\] |
| 248 | Pre or post script returns an error\[SWDL_ERROR_SCRIPTRETURN\] |
| 249 | Script checksum error\[SWDL_ERROR_SCRIPTCHECKSUM\] |
| 255 | unknown error occured\[SWDL_ERROR_UNKN\] |

# 2. Filecopy specific errors

Filecopy will be executed for the following packages:

•       NavDB

•       Speech

•       Gracenote

•       Truffles

•       Eggnog,  Boardbook

## 2.1.  FileCopy Errors

| **Error Code** | **Error Description** |
|----|----|
| 128 | reserved\[FC_ERRORS_BACKUP_BEFOR_COPY_OTHER_ERROR\] |
| 129 | file/folder could not be removed\[FC_ERRORS_DELETE_DEST_BEFORE_COPY_RMDIR_ERROR\] |
| 130 | file version info write failed\[FC_ERRORS_WRITE_FILE_INFO_OPEN\] |
| 131 | could not create a folder\[FC_ERRORS_CREATE_PATH\] |
| 132 | rename TMP file/folder to destination file/folder has failed\[FC_ERRORS_RENAME_TMP\] |
| 133 | partition mount error\[FC_ERRORS_MOUNT_FAILED\] |
| 134 | file information could not be determined\[FC_ERRORS_STAT\] |
| 135 | checksumsize is zero\[FC_ERRORS_CHECKSUMSIZE\] |
| 136 | memory allocation error\[FC_ERRORS_MALLOC\] |
| 137 | source file is missing\[FC_ERRORS_OPEN_SRC\] |
| 138 | read error on source file\[FC_ERRORS_READ_BLOCK\] |
| 139 | sha1 checksum\[FC_ERRORS_SHA1_CHECK1\] |
| 140 | destination file write error\[FC_ERRORS_WRITE_BLOCK\] |
| 141 | reserved\[FC_ERRORS_SHA1_CHECK2\] |
| 142 | rename NEW file/folder to destination file/folder has failed\[FC_ERRORS_RENAME\] |
| 143 | hashes.txt could not be parsed\[FC_ERRORS_HASH_PARSE\] |
| 144 | thread not started\[FC_ERRORS_THREAD_START\] |
| 145 | checkpoint tag in metainfo has wrong size\[FC_ERRORS_CHECKPOINT\] |
| 146 | unexpected error\[FC_ERRORS_OTHER\] |