# PR-9VD 9.1 sound system retrofit

:::warning
This is experimental. `9VD` retrofits had been done before, but not exactly like this one.

:::

## Intro

Some vehicles like Audi A3 (8V) and Seat Leon MK3 (5F) had option of `PR-9VD` sound system (Audi Sound System, Seat Sound System). It's 9.1 configuration with 10 speakers connected to MIB main unit internal 6-channel amplifier, without MOST and external amplifier (like Bose, B&O, Dynaudio, Fender…).

One of the most popular audio configs is `PR-8RM`, 8 speakers connected to 4 audio channels of the MIB internal amplifier. Since some MIBs internal amp has 6 channels, this leaves 2 channels unused. 5th for subwoofer under the trunk floor, 6th for front center under the dashboard.

In addition there should be a more precise equalizer available (5 slider instead of 3) + separate subwoofer control adjustment.

## Requirements


1. MIB main unit with 6-channel internal amplifier,
2. Diagnostic interface to change coding (VCDS, OBDeleven…),
3. Diagnostic interfaca to upload parametrization (VCP, CarScanner…),
4. Additional speakers (front center + subwoofer), cables, terminals, connectors.


:::info
Some door speakers are different for 8.0 setup and 9.1 setup (4Ω 20W vs 2Ω 40W).

:::

## Connection diagram


:::info
Pending

:::

## Wiring


1. Quadlock, pin `9` (positive) and pin `13` (negative) for subwoofer `R211`.
2. Quadlock, pin `10` (positive) and pin `14` (negative) for front center `R208`.

## Parametrization


1. Module `0x5F`, Parametrization, address `0x000200` - this adjusts the unit identifier string.
2. Module `0x5F`, Parametrization, address `0x003B00` - this controls GUI (equalizer + subwoofer sliders).
3. Module `0x5F`, Parametrization, address `0x003000` - this controls sound curves for all audio channels.


:::info
This file should be picked according to your car options (model, body style, steering wheel side).

:::

## Coding


1. Module `0x5F`, Long Coding, bytes `4-7`, new value `FF 0A 00 00` - this sets speakers configuration.
2. Module `0x5F`, Long Coding, byte `11`, new value `01` - this makes sure that the unit is set to internal amplifier.

## VW with 9VD?


:::info
What I'm trying to accomplish is to enable 9.1 config in VW Golf MK7, which never had the `PR-9VD` option available from the factory. This can be done in `MHI2` units, but not `MST2` units.

:::

Connected speakers to quadlock, send dataset from Seat Leon Kombi Left-Hand-Drive with 9VD to `0x003000`, coded `0x5F` bytes `4-7` with `FF0A0000`.

Effect? No sound from additional speakers, no new equalizer controls, `0x5F` fault code about incorrectly coded module. It looks like VW audio processing not the same as in Seat and Skoda. VW app controls 4 channels, Seat can control 6 channels, Skoda has an individual option with virtual subwoofer.

Later on I opened my main unit only to find out that it's missing some hardware. Looks like VW version of `MST2` main unit not equipped with required hardware for additional audio channels. Below you will find picture of Seat MST2 unit with 6-channel internal amp, and VW MST2 units with 4-channel internal amp, to compare the hardware differences.

 ![Seat Leon (5F) main unit with 6-channel internal audio amplifier](attachments/57af3684-11f2-4b68-bec6-47ae4d38d743.jpg)

 ![VW Golf (5G) main unit with 4-channel internal audio amplifier](attachments/1d45b11b-8692-44a9-96a3-2a4e3c7373b3.jpg)

## Sources and reference

* <https://www.drive2.ru/l/503688201903276921/>
* <https://www.drive2.ru/l/472901326569734572/>
* <https://www.drive2.ru/l/551818223897546321/>