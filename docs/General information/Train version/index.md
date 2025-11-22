# Train version

:::info
Before asking any question it is a MUST to know and refer to Train (firmware version) of your MIB (Multimedia Infotainment Box). To see the Train version you need to press special button combination. 

Also check most recent firmware version for your unit.

:::

## Mapping of train version to unit generation, tier, manufacturer and brand

| Train version | Generation | Tier and manufacturer | Audi | VW | Skoda | Seat | Bentley | Lamborghini | Porsche |
|----|----|----|----|----|----|----|----|----|----|
| `MENT_xx_xx_xxxx` | `MIB1` | `Entry`  | MMI | Composition Touch | Swing |    |    |    |    |
| `MSTD_xx_xx_xxxxx` | `MIB1` | `Standard` Panasonic | MMI | Composition/\nDiscover Media | Bolero/\nAmundsen | Navi System |    |    |    |
| `MHIG_xx_xx_xxxxx` | `MIB1` | `High` \nHarman | MMI Navigation | Discover Pro | Columbus | Navi System |    |    |    |
| `MEN2_xx_xxxxx_xxxxxx` | `MIB2` | `Entry` \nLG | - | Composition Touch/Colour | Swing2/Swing3 |    |    |    |    |
| `MST2_xx_xx_xxxxD CNS2_xx_xx_xxxxD` | `MIB2` | `Standard` Delphi | MMI Radio plus / MMI Low | Composition Media (CM) \n Discover Media (DM) | - | - |    |    |    |
| `MST2_xx_xx_xxxxT` | `MIB2` | `Standard` Technisat/Preh | - | Composition Media (CM) \n Discover Media (DM) | Bolero/Amundsen | Navi System 6P0 |    |    |    |
| `MHI2_xx_xxxxx_xxxxx` | `MIB2` | `High` [Harman](/MHI2 MHI2Q Harman Aisin/Hardware MHI2/), Aisin | MMI Navigation plus / MMI High | Discovery Pro | Columbus | Navi System Plus |    |    |    |
| `MHI2Q_xx_xxxxx_xxxxx` | `MIB2` | `High` Harman, Aisin [(Qualcomm chipset)](/MHI2 MHI2Q Harman Aisin/Hardware MHI2/MHI2Q - Qualcomm/) | MMI Navigation plus / MMI High | - | - | - |    |    |    |
| `MS2p_xx_xxxxx_xxxxxD` | `MIB2` | `Standard Plus` \nAptiv (Delphi) | MMI radio plus | - | - | - |    |    |    |
| `MH2p_xx_xxxxx_xxxxx` | `MIB2` | `High Plus` Alpine | MMI navigation plus / MMI Plus | Discover Premium | - | - |    |    |    |
| `MHS2_xx_xx_xxxxx` | `MIB2` | `High Scale` Delphi | MMI Radio Plus with Connectivity Package / MMI Navigation with Audi Connect | - | - | - |    |    |    |
| `MEN3_xx_xxxxx_xxxxxx` | `MIB3` | `Entry` Panasonic | - |    | Bolero (aka Swing4) |    |    |    |    |
| `MOI3_xx_xx_xxxxxx` | `MIB3` | `Standard`\n LG | - | Discover Pro |    |    |    |    |    |
| `MOI3_xx_xxxxx_xxxxxx CNS3_xx_xxxxx_xxxxxx` | `MIB3` | `Standard`  Preh/Joynext | - |    | Amundsen/Columbus |    |    |    |    |
| `MHI3_xx_xx_xxxxx MHI3_xx_xxxxx_xxxxx MHI3_xx_xxxxxx_xxxxx` | `MIB3` | `High` \nAptiv | MMI navigation |    |    |    |    |    |    |
| `MPR3_xx_xx_xxxxx MPR3_xx_xxxxx_xxxxx MPR3_xx_xxxxxx_xxxxx` | `MIB3` | `Premium` Aptiv | MMI navigation plus |    |    |    |    |    |    |
| `MBA3_xx_xxxxxx_xxxxx` | `MIB3` | `Basic`\nAptiv | MMI radio plus |    |    |    |    |    |    |

xx - have meaning as listed below:

## Region

* `AS` = Asia
* `CN` = China
* `EU` = Europe
* `ER` = Europe + RoW
* `JP` = Japan
* `KR` = South Korea
* `NAR` = North America Region
* `RoW` = Rest of the World
* `RoA` = Rest of Asia
* `TW` = Taiwan
* `US` = United States
* `XB` = South Korea

## Brand and Variation

* `AU` = Audi 10.1" screen
* `AUG` = Audi
* `AUASUV` = Audi e-tron MHI3
* `AUG33` = Audi 9.2" screen MH2p
* `AUG35` = Audi 10,1" screen MH2p
* `AUG45S` = Audi 15" screen MHI3
* `BYG24` = Bentley
* `BYG46S` = Bentley MHI3
* `BYSUV` = Bentley
* `LB` = Lamborghini
* `LB636` = Lamborghini MH2p
* `LB46S` = Lamborghini MPR3
* `POG` = Porsche
* `PO416` = Porsche 10.9" MH2p
* `POG11` = Porsche
* `POG24` = Porsche
* `POG35` = Porsche 12.3" MH2p
* `POG46` = Porsche MPR3
* `SE` = Seat
* `SEG11` = Seat with 8" screen
* `SEGPx` = Seat MEN3 with 6,5" screen
* `SEMQB` = Seat MOI3
* `SK` = Skoda
* `SKG11` = Skoda with 8" screen
* `SKG13` = Skoda with 9.2" screen (a.k.a. MIB2.5)
* `SKGPx` = Skoda MEN3 with 6,5" screen
* `SKMQB` = Skoda MOI3
* `VW` = Volkswagen
* `VW37W` = Volkswagen MHI3
* `VWG11` = Volkswagen with 8" screen
* `VWG13` = Volkswagen with 9.2" screen (a.k.a. MIB2.5)
* `VWG33` = Volkswagen 9.2" screen MH2p
* `VWG36` = Volkswagen 15" screen MH2p
* `VWGPx` = Volkswagen MEN3 with 6,5" screen
* `VWMQB` = Volkswagen MOI3

## Platform

* `PQ` = all-in-one unit where display and main unit are in the same enclosure for PQ25/35 platforms
* `ZR` = Zentral Rechner (Central Calculating Module or Main Unit). Units with separate display and separate main unit. Used on PQ26/PQ27/MQB and VW Commercial Vehicles. 

## Version

* `E` = Engineering / Developer / Beta
* `K` = Customer Update
* `P` = Production
* `R` = Release/Production
* `S` = Security Fix