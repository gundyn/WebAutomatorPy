from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
