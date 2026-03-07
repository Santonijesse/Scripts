from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import os
import time

# For W3C touch actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Setup Appium options
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "16",
    "appium:deviceName": "192.168.1.205:5555",
    "appium:appPackage": "com.wacom.bamboopapertab",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.wacom.bamboopapertab.LauncherActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Connect to Appium server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Step-by-step interaction
driver.find_element(by=AppiumBy.ID, value="com.wacom.bamboopapertab:id/btn_go_next").click()
driver.find_element(by=AppiumBy.ID, value="com.wacom.bamboopapertab:id/privacyPolicyCheckBox").click()
driver.find_element(by=AppiumBy.ID, value="com.wacom.bamboopapertab:id/termsCheckBox").click()
driver.find_element(by=AppiumBy.ID, value="com.wacom.bamboopapertab:id/btn_go_next").click()
driver.find_element(by=AppiumBy.ID, value="com.wacom.bamboopapertab:id/btn_go_next").click()
driver.find_element(by=AppiumBy.ID, value="com.wacom.bamboopapertab:id/ink_space_sign_in_not_now_button").click()

# GUI capture before unfolding
before_path = os.path.join(os.getcwd(), "before.xml")
with open(before_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Simulate unfolding event delay
time.sleep(5)

# GUI capture after unfolding
after_path = os.path.join(os.getcwd(), "after.xml")
with open(after_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# End session
driver.quit()

