import os
import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
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

# Connect to Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Step-by-step interaction sequence
driver.find_element(by=AppiumBy.ID, value="com.google.android.gms:id/continue_button").click()

time.sleep(5)
driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button").click()

time.sleep(5)
driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button").click()

time.sleep(5)
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(2)").click()

time.sleep(3)
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"New York Mets\")").click()

time.sleep(3)
driver.find_element(by=AppiumBy.ID, value="com.bamnetworks.mobile.android.ballpark:id/footer_button").click()

time.sleep(3)
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.Button\").instance(0)").click()

time.sleep(3)
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.bamnetworks.mobile.android.ballpark:id/green_ticket_image\").instance(0)").click()

# Touch action 1
time.sleep(3)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(421, 1851)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Confirm ticket
time.sleep(3)
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"OK\")").click()

# Touch action 2
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(471, 1330)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Touch action 3
time.sleep(3)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(456, 1321)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Touch action 4
time.sleep(3)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(628, 1972)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Touch action 5
time.sleep(3)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(471, 1425)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

# GUI capture before unfolding event (as XML)
before_path = os.path.join(os.getcwd(), "before.xml")
with open(before_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Unfolding device manually
time.sleep(5)

# GUI capture after unfolding event (as XML)
after_path = os.path.join(os.getcwd(), "after.xml")
with open(after_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# End session
driver.quit()

