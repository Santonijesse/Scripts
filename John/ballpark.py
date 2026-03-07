# This script is intended to place tickets in the shopping cart of the MLB Ballpark Android app

import os
import subprocess
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
	"appium:appPackage": "com.bamnetworks.mobile.android.ballpark",
	"appium:automationName": "UiAutomator2",
	"appium:appActivity": "com.bamnetworks.mobile.android.ballpark.activity.MainActivity",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Function to capture the device's GUI and save it
def capture_screenshot(filename):
        expanded_filename = os.path.expanduser(filename)
        subprocess.run(f"adb exec-out screencap -p > {expanded_filename}", shell=True)

# Adding a 10 seconds delay before the first action
time.sleep(10)

el1 = driver.find_element(by=AppiumBy.ID, value="com.google.android.gms:id/continue_button")
el1.click()

# Adding a 5 seconds delay before the second action
time.sleep(5)

el2 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
el2.click()
package_name = driver.execute_script('mobile: getCurrentPackage')
desired_caps = driver.desired_capabilities()

# Adding a 5 seconds delay before the third action
time.sleep(5)

el3 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
el3.click()

# Adding a 5 seconds delay before the fourth action
time.sleep(5)

el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(2)")
el4.click()

# Adding a 3 seconds delay before the fifth action
time.sleep(3)

el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"New York Mets\")")
el5.click()

# Adding a 3 seconds delay before the sixth action
time.sleep(3)

el6 = driver.find_element(by=AppiumBy.ID, value="com.bamnetworks.mobile.android.ballpark:id/footer_button")
el6.click()

# Adding a 3 seconds delay before the seventh action
time.sleep(3)

el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(0)")
el7.click()

# Adding a 3 seconds delay before the eighth action
time.sleep(3)

el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.bamnetworks.mobile.android.ballpark:id/green_ticket_image\").instance(0)")
el8.click()

# Adding a 3 seconds delay before the pointer action
time.sleep(3)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(421, 1851)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 3 seconds delay before the tenth action
time.sleep(3)

el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"OK\")")
el9.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(471, 1330)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 3 seconds delay before the pointer action
time.sleep(3)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(456, 1321)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 3 seconds delay before the pointer action
time.sleep(3)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(628, 1972)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Adding a 3 seconds delay before the pointer action
time.sleep(3)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(471, 1425)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# GUI capture before unfolding event
capture_screenshot("before.jpg")

# Adding a 5 seconds delay after the screenshot is taken
time.sleep(5)

# Unfolding event is performed here

# GUI capture after folding event
capture_screenshot("after.jpg")


driver.quit()
