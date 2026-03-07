import time
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# Configure Appium options
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "14",
    "appium:deviceName": "192.168.1.205:5555",
    "appium:appPackage": "com.aspyr.civvi",
    "appium:automationName": "UiAutomator2",
    "appium:appActivity": "com.aspyr.civvi.BootstrapActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

# Start Appium session
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Wait for app to load
time.sleep(40)

# Define helper for tap actions
def tap(x, y, delay=10):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(delay)

# Perform tap sequence to navigate to a new game area
tap(682, 428)   # Sign-in
tap(1158, 633)  # First UI element
tap(1176, 645)  # Second UI element
tap(1116, 356)
tap(1080, 320)
tap(1279, 398)
tap(1755, 760, delay=20)  # Start game

# Allow game to settle
time.sleep(10)

# Dump GUI hierarchy before folding
before_path = os.path.join(os.getcwd(), "before.xml")
with open(before_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Simulate folding/unfolding event externally (manual or automated)
time.sleep(20)

# Dump GUI hierarchy after unfolding
after_path = os.path.join(os.getcwd(), "after.xml")
with open(after_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

# Close session
driver.quit()

