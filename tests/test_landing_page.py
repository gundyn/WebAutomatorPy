import pytest
import logging

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
        logging.info('Starting test_page_loads.')
        self.landing_page.load()
        assert self.driver.driver.current_url == LandingPage.URL
