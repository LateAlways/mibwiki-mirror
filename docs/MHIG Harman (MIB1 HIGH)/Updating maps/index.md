# Updating maps

MHIG and MHI2/MHI2Q use the same navigation maps. The latest navi maps version that supports MHIG is P350.


:::info
MHIG firmwares support only Feature Enabling Codes (FEC) for maps:

:::

Audi

```
021000EE lifetime EU maps
021100EE lifetime NAR maps
021200EE lifetime China+Hongkong+Macau maps
021280EE lifetime China only maps
021300EE lifetime Japan maps
021A00EE lifetime South Korea maps
021B00EE lifetime Taiwan maps
021D00EE lifetime RoW maps  
```

Skoda

```
081000EE lifetime EU maps
```

VW

```
091000EE lifetime EU maps
```

To find out which FEC is required to be installed for particular map, take a look into following file on the maps SD:

**P330_N60S5MIBH3_EU.7z\\Mib1\\NavDB\\common_eu\\0\\default\\content.pkg**

 ![](attachments/15dda075-d6ae-4330-8126-a799d6e01129.png "left-50")


\