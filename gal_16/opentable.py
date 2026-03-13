import subprocess
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
from playsound import playsound

APP_NAME = "opentable"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots", APP_NAME)
XML_DIR = os.path.join(BASE_DIR, "ui_xml", APP_NAME)
LOGCAT_DIR = os.path.join(BASE_DIR, "logcat", APP_NAME)

# OpenTable — check seating popup after selecting time

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "16",
    "appium:deviceName": "R5CX809QS2L",
    "appium:udid": "R5CX809QS2L",
    "appium:appPackage": "com.opentable",
    "appium:automationName": "UiAutomator2",
    #"appium:appActivity": "com.opentable.ui.home.HomeActivity",
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


tap(530, 2450, 3)
tap(750, 1185, 3)
tap(520, 1550, 3)
tap(535, 1550, 3)
tap(530, 2400, 3)
tap(920, 1440, 3)
tap(760, 1530, 3)

existing = glob.glob(os.path.join(SCREENSHOTS_DIR, f"{APP_NAME}_before_*.png"))
instance = len(existing) + 1

subprocess.run(["adb", "-s", "R5CX809QS2L", "logcat", "-c"])

before_xml_path = os.path.join(XML_DIR, f"{APP_NAME}_before_{instance}.xml")
with open(before_xml_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, f"{APP_NAME}_before_{instance}.png"))

with open(os.path.join(LOGCAT_DIR, f"{APP_NAME}_before_{instance}.txt"), "w", encoding="utf-8") as f:
    f.write(subprocess.run(["adb", "-s", "R5CX809QS2L", "logcat", "-d"], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout)

playsound(os.path.join(os.path.dirname(BASE_DIR), 'auto_alarm.mp3'))
print('please close & open phone in a second')
time.sleep(10)

driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, f"{APP_NAME}_after_{instance}.png"))

with open(os.path.join(LOGCAT_DIR, f"{APP_NAME}_after_{instance}.txt"), "w", encoding="utf-8") as f:
    f.write(subprocess.run(["adb", "-s", "R5CX809QS2L", "logcat", "-d"], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout)

after_xml_path = os.path.join(XML_DIR, f"{APP_NAME}_after_{instance}.xml")
with open(after_xml_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()
