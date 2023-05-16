import pytest
from utils.logger import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.webdriver import WebDriver
from src.landing_page import LandingPage

CHROMEDRIVER_PATH = "path/to/chromedriver"

@pytest.fixture(scope='class', autouse=True)
def setup(request):
    """Set up the WebDriver instance and landing page."""
    driver = WebDriver(CHROMEDRIVER_PATH)
    driver.setup()
    lp = LandingPage(driver)
    request.cls.driver = driver
    request.cls.landing_page = lp
    yield
    driver.teardown()


class TestLandingPage:
    """Test class for the landing page."""

    def test_page_loads(self):
        """Test the landing page load."""
        logger.info('Starting test_page_loads.')
        print('Log message:', 'Starting test_page_loads.')  
        self.landing_page.load()
        assert self.driver.driver.current_url == LandingPage.URL

        # Capture a screenshot on successful load or failure
        if self.driver.driver.current_url == LandingPage.URL:
            logger.info('Page loaded successfully.')
            self.driver.save_screenshot('successful_load.png')
        else:
            logger.error('Page did not load successfully.')
            self.driver.save_screenshot('failure_load.png')

    def test_button_exists(self):
        """Test if the button with class name 'et_pb_button_1' exists."""
        logger.info('Starting test_button_exists.')
        self.landing_page.load()
        
        wait = WebDriverWait(self.driver.driver, 10)  # Wait for a maximum of 10 seconds
        button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'et_pb_button_1')))
        
        assert button is not None
