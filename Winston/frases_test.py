import time
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Setup Appium options
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "192.168.1.205:5555",  # Ensure Wi-Fi debugging is enabled
    "appium:appPackage": "com.frasesyreflexiones.saludosparatodaocasion",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.frasesyreflexiones.saludosparatodaocasion.activities.ActivitySplash",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Connect to Appium server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Disallow notification permissions popup
el1 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_deny_button")
el1.click()

# Wait to allow ads or splash screens to finish
time.sleep(10)

# Helper for tap actions
def tap(x, y, delay=10):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(delay)

# App navigation sequence
tap(705, 634)     # Open a greeting category
tap(495, 1430)    # Select a specific greeting
tap(270, 1943, delay=5)  # Tap share (affected by fold state)

# GUI capture before folding event
before_path = os.path.join(os.getcwd(), "before.xml")
with open(before_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Simulate folding/unfolding action (externally or manually)
time.sleep(5)

# GUI capture after unfolding event
after_path = os.path.join(os.getcwd(), "after.xml")
with open(after_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# End of script
driver.quit()

