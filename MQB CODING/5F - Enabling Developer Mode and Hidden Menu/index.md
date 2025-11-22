# 5F - Enabling Developer Mode and Hidden Menu

:::warning
Hidden menus, bootloaders, etc… Don't use functions that you are not 100% sure about or will break your unit.

:::

## MIB


:::info
Requires `Development mode` session instead of standard `Diagnostic mode` session. Not all diagnostic tools can switch session modes.

:::

### with OBDeleven


1. `5F` → `Change Service` → `Development mode`
2. `5F` → Adaptation → `Developer mode` → `activated`
3. Reboot the unit with [key combination](/General information/Useful documents/Key combinations and shortcuts/) for your device.

### with VCDS


1. `5F` → Security Access → `S12345`
2. `5F` → Adaptation → `Developer mode` → `activated`
3. Reboot the unit with [key combination](/General information/Useful documents/Key combinations and shortcuts/) for your device.


:::info
Old versions of VCDS will not support `S12345` code. This "dirty hack" to change diagnostic mode, which was introduced in one of the latest VCDS versions.

:::

### with VCP


1. Connect with module `5F`.
2. Change diagnostic mode to `Engineer mode`.
3. Go to `Security Access` and enter code `20103`.
4. Go to `Adaptation`, find channel `Developer mode`, and activate it.
5. Reboot the unit with [key combination](/General information/Useful documents/Key combinations and shortcuts/) for your device.

### with Car Scanner ELM OBD2


1. Go to `Coding & Service` .
2. Select platform (In most cases, choose `MQB`, even if the car is on the `MLB` platform).
3. Go to `Mutimedia`.
4. Select `Multimedia developer mode activation` and turn it on.
5. Reboot the unit with [key combination](/General information/Useful documents/Key combinations and shortcuts/) for your device or use `Restart multimedia system` option.

## Audi MMI 2G

## Audi MMI 3G/3G+

## Audi RMC

## More info


:::info
Unit might require reboot for the developer mode to be active.

:::


:::tip
After enabling developer mode, check how to use [button combination](/General information/Useful documents/Key combinations and shortcuts/) in your unit for developer functions.

:::