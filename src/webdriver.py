import os

from utils.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebDriver:
    """A utility class for managing a Selenium WebDriver."""
    
    def __init__(self, driver_path):
        """Initialize the WebDriver utility with the path to the driver executable."""
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        """Setup the WebDriver with Chrome options and maximize the window."""
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        
    def teardown(self):
        """Close the browser and quit the WebDriver."""
        if self.driver:
            self.driver.quit()

    def save_screenshot(self, filename):
        """Save a screenshot of the current browser window to the specified file."""
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, filename)

        # Delete the existing file if it exists
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        self.driver.save_screenshot(screenshot_path)


    def wait(self, locator):
        """Wait for an element with the specified locator."""
        logger.info('Waiting for element with locator: %s', locator)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator))
