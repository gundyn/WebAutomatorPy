# WebAutomatorPy/src/webdriver.py
from selenium import webdriver

class WebDriver:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        self.driver.maximize_window()
        
    def teardown(self):
        if self.driver:
            self.driver.quit()
