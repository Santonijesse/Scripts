# This script is intended to access a game on the Retro64 Emulator Android app, a feature that presents state loss after unfolding events

import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Desired capabilities
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

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Adding a 5 seconds delay before the first action
time.sleep(5)

el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
el1.click()

# Adding a 5 seconds delay between actions
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1803, 368)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 5 seconds delay between actions
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1707, 458)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 5 seconds delay between actions
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1984, 271)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 5 seconds delay between actions
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(525, 253)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 5 seconds delay between actions
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1496, 368)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 5 seconds delay between actions
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(1490, 356)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# GUI capture before unfolding event
driver.get_screenshot_as_file("home/Documents/NJIT_Research/Appium_Scripts/Retro_64_Games/before.png")

# Adding a 10 seconds delay before ending, the unfolding event is performed here
time.sleep(10)

# GUI capture after folding event
driver.get_screenshot_as_file("home/Documents/NJIT_Researcg/Appium_Scripts/Retro_64_Games/after.png")

# Finishing the session
driver.quit()
