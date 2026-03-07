import time
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Desired capabilities for Retro64 app
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "RFCT70XTZQM",
    "appium:udid": "RFCT70XTZQM",
    "appium:appPackage": "nes.snes.gba.fcemulator.n64",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "org.cocos2dx.cpp.AppActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Start Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Wait before first action
time.sleep(5)

# Deny permissions to move to the next activity
driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button").click()

# Tap sequence
def tap(x, y, delay=5):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(delay)

# Reproduce sequence to start a game
tap(1803, 368)
tap(1707, 458)
tap(1984, 271)
tap(525, 253)
tap(1496, 368)
tap(1490, 356)

# GUI capture before unfolding event
before_path = os.path.join(os.getcwd(), "before.xml")
with open(before_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Allow time for manual unfolding
time.sleep(10)

# GUI capture after unfolding event
after_path = os.path.join(os.getcwd(), "after.xml")
with open(after_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# End session
driver.quit()

