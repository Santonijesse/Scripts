# Appium Capabilities Reference — Food & Delivery Apps

## Scripts requiring login (no capture block)

The following scripts are stubs — they cannot complete the before/after fold sequence without an account:

- dunkin.py — can't download policies
- earnify.py — needs login
- edgeaura.py -- How to work around ads
- freecash.py — needs Gmail
- instacart.py — needs login
- instagream -- won't load
- mcdonalds.py — needs login
- nextdoor.py — needs Gmail account
- nytimes.py — needs login
- reddit.py — needs Gmail account
- substack.py — needs an account
- toogoodtogo.py — needs login
- ubereats.py — needs login
- whatnot.py — needs Gmail
- x_twitter.py — needs an account
- yelp.py — needs login

---

This document provides `load_capabilities` blocks for 20 Android food/delivery apps.
Replace `<PLATFORM_VERSION>`, `<DEVICE_NAME_OR_IP>`, and `<UDID>` with your device's actual values.

> **Tip:** To find the correct `appActivity` for any installed app, run:
> ```
> adb shell dumpsys package <appPackage> | grep -i activity
> ```

---

## DoorDash

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.dd.doordash",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.dd.doordash.ux.launcher.LauncherActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## McDonald's

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.mcdonalds.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.mcdonalds.mcdcoreapp.common.activity.SplashActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Uber Eats

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.ubercab.eats",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.ubercab.eats.core.activity.LauncherActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Starbucks

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.starbucks.mobilecard",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.starbucks.mobilecard.main.activity.LandingPageActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Taco Bell

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.tacobell.ordering",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.tacobell.ordering.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## OpenTable

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.opentable",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.opentable.ui.home.HomeActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Instacart

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.instacart.client",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.instacart.client.browse.ICBrowseActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Too Good To Go

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.app.tgtg",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.app.tgtg.feature.login.SplashActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Domino's

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.dominospizza",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.dominospizza.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Yelp

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.yelp.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.yelp.android.home.ui.RootSingleActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Dunkin'

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.dunkinbrands.otgo",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.cardfree.android.dunkindonuts.activities.LauncherActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Recime

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.recime.app",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.recime.app.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Chick-fil-A

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.chickfila.cfaflagship",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".activities.InitialLoadActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Dutch Bros

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.dutchbros.loyalty",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.dutchbros.loyalty.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Chipotle

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.chipotle.ordering",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.chipotle.ordering.view.activity.SplashActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Subway

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.subway.mobile.subwayapp03",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.subway.mobile.subwayapp03.activity.HomeActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Little Caesars

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.littlecaesars",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.littlecaesars.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Wingstop

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.wingstop.mobile",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.wingstop.mobile.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Buffalo Wild Wings

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.buffalowildwings.blazinrewards",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.buffalowildwings.ordering.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Crumbl

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.crumbl.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.crumbl.app.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## DoorDash Driver

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.doordash.driverapp",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.doordash.driverapp.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# Maps, Navigation & Parking

---

## Google Maps

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.google.android.apps.maps",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Waze

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.waze",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".FreeMapAppActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Organic Maps

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.organicmaps",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## ParkMobile

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.parkmobile.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Transit

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.thetransitapp.droid",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".shared.activity.SplashActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## MapXplorer

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.mapxplorer.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## SpotHero

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.spothero.spothero",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.spothero.android.activity.HomeActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Shell Motorist

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.shell.sitibv.motorist",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## ParkWhiz

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.parkwhiz",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Metropolis Parking

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.metropolis.parking",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## onX Hunt

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.onxmaps.hunt",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## onX Offroad

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.onxmaps.offroad",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## MTA TraIT

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.mta.trait",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Neshan Maps

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.neshan.maps",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Coulomb Tech

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.coulombtech",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Simple Speedometer

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.speedometer.simple",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## BPme

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.bp.app.bpme.global.ros",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.bp.bpme.global.ros.ui.LandingScreenActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Citymapper

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.citymapper.app.release",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.citymapper.app.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## TranzMate

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.tranzmate",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.moovit.app.home.HomeActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## AutoNavi (Amap)

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.autonavi.minimap",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# Social & News

---

## X (Twitter)

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.twitter.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".StartActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Substack

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.substack.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Reddit

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.reddit.frontpage",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "launcher.default",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Crime Radar

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.crimeradar.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Nextdoor

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.nextdoor",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## NewsBreak

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.particlenews.newsbreak",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## New York Times

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.nytimes.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## SpotCrime

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.spotcrime.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Police Scanner Radio

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.police.scanner.radio",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## TrueShort

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.trueshort.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Checkitt

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.checkitt",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "vc.ucic.SplashActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Fizz

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.fizz.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## AP News

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.apnews",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Wall Street Journal

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.wsj.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## The Pour Over

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.thepourover.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Podcasts

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.podcast.podcasts",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "fm.castbox.ui.main.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Clubhouse

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.clubhouse.app",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Police Scanner (Broadcastify)

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.bstore.android.policescanner",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Ring Neighbors

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.ring.neighbors",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Fox News

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.foxnews.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Instagram

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.instagram.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.instagram.android.activity.MainTabActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## WhatsApp

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.whatsapp",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".Main",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Facebook

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.facebook.katana",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".LoginActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## TikTok

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.ss.android.ugc.trill",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.ss.android.ugc.trill.splash.SplashActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## TikTok Lite

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.zhiliaoapp.musically.go",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.zhiliaoapp.musically.go.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Threads

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.instagram.barcelona",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".mainactivity.BarcelonaActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# AI & Productivity

---

## Microsoft Copilot

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.microsoft.copilot",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.microsoft.copilot.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## ChatGPT

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.openai.chatgpt",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.openai.chatgpt.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# Shopping

---

## Temu

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.einnovation.temu",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.baogong.splash.activity.MainFrameActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## SHEIN

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.zzkko",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.shein.welcome.WelcomeActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Whatnot

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.whatnot_mobile",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.whatnot_mobile.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# Entertainment & Streaming

---

## Peacock

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.peacocktv.peacockandroid",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.peacocktv.peacockandroid.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Tubi

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.tubitv",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.tubitv.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## CapCut

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.lemon.lvoverseas",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.lemon.lvoverseas.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# Finance & Payments

---

## PayPal

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.paypal.android.p2pmobile",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": ".startup.activities.StartupActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Cash App

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.squareup.cash",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.squareup.cash.ui.LaunchActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## FreeCash

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.freecash.app2",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.freecash.app2.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

# Utilities & Other

---

## Edge Aura

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.wallpaper.edge.aura",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.wallpaper.edge.aura.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```

---

## Victor

```python
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "<PLATFORM_VERSION>",
    "appium:deviceName": "<DEVICE_NAME_OR_IP>",
    "appium:udid": "<UDID>",
    "appium:appPackage": "com.newleaf.app.android.victor",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.newleaf.app.android.victor.MainActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})
```
