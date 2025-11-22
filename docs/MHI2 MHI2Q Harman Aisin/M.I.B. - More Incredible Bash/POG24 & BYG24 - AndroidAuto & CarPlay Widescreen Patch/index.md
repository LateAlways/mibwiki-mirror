# POG24 & BYG24 - AndroidAuto & CarPlay Widescreen Patch

:::info
The patch is integrated into [M.I.B](/MHI2 MHI2Q Harman Aisin/M.I.B. - More Incredible Bash/)

:::


:::tip
Any `*.jar` file placed in `/net/mmx/mnt/app/eso/hmi/lsd/jars/`is loaded during the boot of the unit.

:::

## Java Code

```javascript
package de.audi.app.terminalmode.pgen2;

import de.audi.app.terminalmode.AbstractTerminalModeConfiguration;
import de.audi.atip.base.IFrameworkAccess;

public class PGen2TMConfiguration
extends AbstractTerminalModeConfiguration {
    private final int screenOffsetX = Integer.parseInt(System.getProperty("terminalmode.screenoffsetx", this.isRightHandDrive() ? "506" : "134"));
    private final int screenOffsetY = Integer.parseInt(System.getProperty("terminalmode.screenoffsety", "55"));
    private final int touchpadX = Integer.parseInt(System.getProperty("terminalmode.touchpadx", "1440"));
    private final int touchpadY = Integer.parseInt(System.getProperty("terminalmode.touchpady", "540"));

    public PGen2TMConfiguration(IFrameworkAccess iFrameworkAccess) {
        super(iFrameworkAccess);
    }

    public boolean hasKnob() {
        return true;
    }

    public boolean hasTouchscreenHigh() {
        return true;
    }

    public String getScreenName() {
        return "Porsche";
    }

    public boolean isAutoConnect() {
        return false;
    }

    public boolean getStoreUserAcceptState() {
        return false;
    }

    public boolean shouldShowDisclaimerAtLeastOnce() {
        return true;
    }

    public boolean isKnobDirectionInverted() {
        return true;
    }

    public boolean usesOldMediaConnector() {
        return true;
    }

    public int getScreenOffsetX() {
        return this.isRightHandDrive() ? 0 : 114;
    }

    public int getScreenOffsetY() {
        return 55;
    }

    public int getScreenResolutionX() {
        return 1440;
    }

    public int getScreenResolutionY() {
        return 540;
    }

    public int getWindowResolutionX() {
        return 1326;
    }

    public int getWindowResolutionY() {
        return 480;
    }

    public int getTMWindowResolutionInXAxis() {
        return 1326;
    }

    public int getPhysicalDisplayHeight() {
        return 110;
    }

    public int getPhysicalDisplayWidth() {
        return 295;
    }

    public int getTouchPadResolutionX() {
        return this.touchpadX;
    }

    public int getTouchPadResolutionY() {
        return this.touchpadY;
    }

    public boolean isTouchScreenInputWidget() {
        return true;
    }

    public boolean hasBothPhoneMFLKeys() {
        return true;
    }

    public boolean supportsDeletionOfConnectedDevices() {
        return true;
    }

    public int getDSICarPlayScreenResolution() {
        return 3;
    }

    public int getCarPlayPhysicalDisplayHeight() {
        return 110;
    }

    public int getCarPlayPhysicalDisplayWidth() {
        return 295;
    }

    public boolean hasTwoVirtualButtonModels() {
        return false;
    }

    public boolean useDSIAndroidAuto2() {
        return true;
    }
}
```

## Compiled jar

[g24ws.jar 1672](attachments/68032750-ce81-4576-b0ad-f8239bd15a49.jar)


## Porsche POG24 - AndroidAuto

 ![](attachments/ca41c710-2278-4706-b28b-a32fea0900f1.png)

## Porsche POG24 - CarPlay

 ![](attachments/7c6ba198-c49e-4f67-94dc-24eb1a26ff5a.png)

## Bentley BYG24 - CarPlay

 ![](attachments/1324b290-95a0-4fcd-8a02-2c4b6ab53f70.png)

## Bentley BYG24 - AndroidAuto

Nobody tested but the jar should work there too.