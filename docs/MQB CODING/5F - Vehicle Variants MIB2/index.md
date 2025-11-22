# 5F - Vehicle Variants MIB2

This information is stored in module `5F`, long coding, bytes `00`, `01`, `02`.

## Long Coding List

[https://docs.google.com/spreadsheets/d/1FmosUVzzY4LPDC1Ro28tzKRUZnh5ww%5FApsRmBqW1tMo/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1FmosUVzzY4LPDC1Ro28tzKRUZnh5ww%5FApsRmBqW1tMo/edit?usp=sharing)

## Decoding

### Brand

* `x1 xx xx` - Audi
* `x2 xx xx` - Volkswagen
* `x3 xx xx` - Skoda
* `x4 xx xx` - Seat
* `x5 xx xx` - Bentley
* `x6 xx xx` - VW Commercial
* `x7 xx xx` - Porsche
* `x8 xx xx` - MAN
* `x9 xx xx` - Lamborghini

### Body type

* `xx xx x0` - Hatchback
* `xx xx x1` - Sedan
* `xx xx x2` - Variant / Kombi / Van
* `xx xx x3` - Sportback
* `xx xx x4` - Coupe
* `xx xx x5` - Cabriolet
* `xx xx x6` - SUV
* `xx xx x8` - Minivan

## Audi

* `01 24 06` - Audi Q5 (80A)
* `01 37 06` - Audi Q7
* `01 73 00` - Audi A3 (8V1) (3DR)
* `01 73 05` - Audi A3 Cabriolet
* `01 73 01` - Audi A3 Limousine / Sedan / Saloon
* `01 73 03` - Audi A3 Sportback
* `01 73 51` - Audi S3 Limousine / Sedan / Saloon
* `01 73 53` - Audi S3 Sportback
* `01 73 61` - Audi RS3 Limousine / Sedan / Saloon
* `01 73 63` - Audi RS3 Sportback
* `01 94 52` - Audi S4 Avant
* `01 94 62` - Audi RS4 Avant
* `01 75 03` - Audi A7
* `01 75 42` - Audi A6 Allroad facelift
* `01 75 63` - Audi RS7
* `01 94 03` - Audi A5
* `01 94 54` - Audi S5 Coupe
* `01 72 06` - Audi Q2
* `01 33 04` - Audi TT Coupe
* `01 33 05` - Audi TT Roadster
* `01 33 54` - Audi TTS Coupe
* `01 33 55` - Audi TTS Roadster
* `01 33 64` - Audi TTRS Coupe
* `01 33 65` - Audi TTRS Roadster
* `01 27 04` - Audi R8 Coupe
* `01 27 05` - Audi R8 Spyder

  ## Volkswagen
* `02 13 06` - Volkswagen Tiguan (5N)
* `02 62 00` - Volkswagen Polo MK6
* `02 63 01` - Volkswagen Jetta
* `02 72 00` - Volkswagen Polo MK7
* `02 72 06` - Volkswagen T-Roc
* `02 73 00` - Volkswagen Golf MK7 Hatchback
* `02 73 01` - Volkswagen Jetta
* `02 73 02` - Volkswagen Golf MK7 Variant & Alltrack
* `02 73 06` - Volkswagen Tiguan MK2
* `02 73 08` - Volkswagen Touran
* `02 73 09` - Volkswagen Sportsvan
* `02 73 10` - Volkswagen Golf MK7.5 Hatchback
* `02 73 12` - Volkswagen Golf MK7.5 Variant/Estate
* `02 73 70` - Volkswagen eGolf MK7
* `02 74 04` - Volkswagen Passat CC
* `02 84 01` - Volkswagen Passat (B8) Sedan
* `02 84 02` - Volkswagen Passat (B8) Variant/Estate
* `02 84 03` - Volkswagen Arteon

## Skoda

* `03 62 00` - Skoda Fabia
* `03 62 02` - Skoda Fabia Kombi
* `03 73 01` - Skoda Octavia
* `03 73 02` - Skoda Octavia Kombi
* `03 73 42` - Skoda Octavia Kombi Scout
* `03 73 51` - Skoda Octavia vRS
* `03 73 52` - Skoda Octavia Kombi vRS
* `03 73 11` - Skoda Octavia lifting
* `03 73 12` - Skoda Octavia lifting Kombi
* `03 53 31` - Skoda Rapid
* `03 53 30` - Skoda Rapid Spaceback
* `03 53 71` - Skoda Rapid lifting
* `03 53 70` - Skoda Rapid lifting Spaceback
* `03 84 01` - Skoda Superb
* `03 84 02` - Skoda Superb Kombi
* `03 23 06` - Skoda Karoq
* `03 23 46` - Skoda Karoq Scout
* `03 23 16` - Skoda Kodiaq
* `03 23 66` - Skoda Kodiaq Scout

## Seat

* `04 24 08` - Seat Alhambra
* `04 23 06` - Seat Ateca
* `04 23 86` - Seat Ateca Xcellence
* `04 72 00` - Seat Ibiza
* `04 52 00` - Seat Ibiza
* `04 52 04` - Seat Ibiza FR
* `04 52 10` - Seat Ibiza Cupra
* `04 73 00` - Seat Leon MK3 (5F) Stylance
* `04 73 02` - Seat Leon MK3 (5F) Kombi Cupra
* `04 73 03` - Seat Leon MK3 (5F) Kombi
* `04 73 60` - Seat Leon MK3 (5F) FR
* `04 73 80` - Seat Leon MK3 (5F) facelift Hatchback
* `04 73 82` - Seat Leon MK3 (5F) facelift Kombi
* `04 23 16` - Seat Tarraco Xcellence
* `04 52 01` - Seat Toledo
* `04 53 01` - Seat Toledo
* `04 12 06` - Seat Arona

## Bentley

* `05 37 96` - Bentley Bentayga

## VW Commercial

* `06 18 07` - VW Amarok (S6B)
* `06 33 07` - VW Caddy (SAJ)
* `06 45 00` - VW Crafter (SYB)
* `06 57 00` - VW Transporter/Multivan (SGA/SGF/SGJ/SGM)

## Porsche


:::info
Porsche does not fit into the body type template.

:::

* `07 14 06` - Porsche Macan
* `07 25 06` - Porsche Cayenne S e-Hybrid
* `07 26 33` - Porsche Panamera
* `07 26 03` - Porsche Panamera 971
* `07 44 04` - Porsche Cayman
* `07 44 05` - Porsche Boxter
* `07 44 06` - Porsche Macan
* `07 44 54` - Porsche Cayman GT4
* `07 76 04` - Porsche 911 Carrera Coupe
* `07 76 14` - Porsche 911 Carrera 4 Coupe
* `07 76 34` - Porsche 911 Turbo Coupe

## MAN

* `08 45 00` - 0805040000?
* `08 45 70` - 0805040007?
* `08 45 03` - 0805040300?
* `08 45 04` - 0805040400?

## Lamborghini

* `09 36 06` - Lamborghini Urus

## Example coding with OBDeleven

[https://youtu.be/joCBD6Rez58](https://youtu.be/joCBD6Rez58)