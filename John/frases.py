# This script is intended to access the Wishes and blessings app via Appium

import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:platformVersion": "14",
	"appium:deviceName": "192.168.1.205:5555", # This is to access the device via wifi, ensure wifi debugging is enabled on the device.
	"appium:appPackage": "com.frasesyreflexiones.saludosparatodaocasion",
	"appium:automationName": "UiAutomator2",
	"appium:appActivity": "com.frasesyreflexiones.saludosparatodaocasion.activities.ActivitySplash",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Disallow notifications
el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
el1.click()

# Adding a 10 seconds delay between actions. Sometimes ads are played which requires an extended delay
time.sleep(10)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(705, 634)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 10 seconds delay between actions
time.sleep(10)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(495, 1430)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 5 seconds delay between actions
time.sleep(5)

# An attempt to share an image is made. This -sometimes- causes state loss after unfolding the device in the middle of sharing
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(270, 1943)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# GUI capture before unfolding event
driver.get_screenshot_as_file("home/Documents/NJIT_Research/Appium_Scripts/Frases_y_Reflexiones/before.png")

# Adding a 5 seconds delay to allow for the device to be unfolded
time.sleep(5)

# GUI capture after unfolding event
driver.get_screenshot_as_file("home/Documents/NJIT_Research/Appium_Scripts/Frases_y_Reflexiones/after.png")

# Script is completed
driver.quit()
