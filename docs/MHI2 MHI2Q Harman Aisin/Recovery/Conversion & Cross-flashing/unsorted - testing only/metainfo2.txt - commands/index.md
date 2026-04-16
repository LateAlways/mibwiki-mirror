# metainfo2.txt - commands

## **Add to \[common\] section**


 ![EXAMPLE - MHI2_ER_AU57x_K3663_1 AIO](attachments/22b9e25d-8991-42b7-ba72-884c2e63bfa9.png)

| command | value | details |
|----|----|----|
| checkIfNotEqual | true | will force version compare also for smaller versions (allows FW downgrade) |
| skipMetaCRC | true | will skip CRC check in metainfo |
| checkAllUpdates | true | like full SWDL - all packages will be selected |
| EnableUserDefinedSWDLMode | true | Allows User SWDL without enabling it from SWDL/Green Menu |


\
## Add to any \[package\] section

 ![EXAMPLE - MHI2_ER_SEG11_P4709_1 AIO](attachments/e2ae938f-2f76-497f-9b8b-e2aaad7eda66.png " =442x187")

| command | value | details |
|----|----|----|
| checkUpdate | true | automatically select this packages to \[Y\]es in FW update |