# MIB FEC/SWaP Code Generator

## Link

<https://mst2fecgen.mibsolution.one/>


 ![MST2 FEC/SWaP Code Generator screenshot](attachments/32ec32d4-0db0-4a98-b001-eca2556fd902.png)

## Usage


1. Go to the generator.
2. Fill replace `VIN` and `VCRN` with desired values.
3. Toggle checkboxes next to desired codes.
4. Codes will be generated on the right side. Use [OBDeleven](/MQB CODING/5F - Inserting FECs with OBDeleven/)  or VCP or ODIS to upload codes to MIB.


:::info
Codes will not be properly signed and will be recognized as `invalid` if MIB is not patched.

:::


:::tip
Service codes `FFFFFFF9 - FFFFFFFE` will also be rejected if the unit is not patched (tested on `MST2_VW_EU_P0254T`).

:::

## Demo

[https://youtu.be/fvZPQg2oMpU](https://youtu.be/fvZPQg2oMpU)