import time
import glob
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

APP_NAME = "yelp"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots", APP_NAME)
XML_DIR = os.path.join(BASE_DIR, "ui_xml", APP_NAME)

# Yelp
# Note: need login — no close/open

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "15",
    "appium:deviceName": "ZY22HS5QFQ",
    "appium:udid": "ZY22HS5QFQ",
    "appium:appPackage": "com.yelp.android",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.yelp.android.home.ui.RootSingleActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(3)

def tap(x, y, delay=2):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    if delay > 0:
        time.sleep(delay)

tap(530, 2222, 2)
tap(750, 1185, 2)
tap(520, 1550, 2)
tap(550, 1550, 2)
tap(650, 1530, 3)

# Note: need login — no close/open

driver.quit()
