import pytest
import time
import logging

from src.webdriver import WebDriver
from src.landing_page import LandingPage

# This is the path to your chromedriver executable. Update it if necessary.
CHROMEDRIVER_PATH = "drivers/chromedriver/chromedriver"

class TestLandingPage:
    @pytest.fixture(scope='class', autouse=True)
    def driver_setup(self):
        self.driver = WebDriver(CHROMEDRIVER_PATH)
        self.driver.setup()
        self.landing_page = LandingPage(self.driver.driver)
        yield
        self.driver.teardown()

    def test_page_loads(self):
        start_time = time.time()
        logging.info('Starting test_page_loads.')
        self.landing_page.load()
        if 'Fake Landing Page' in self.driver.driver.title:
            logging.info('Page loaded successfully.')
            assert True
        else:
            logging.error('Page did not load successfully.')
            assert False
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f'Finished test_page_loads. Elapsed time: {elapsed_time} seconds.')

    def test_cta_button_present(self):
        start_time = time.time()
        logging.info('Starting test_cta_button_present.')
        self.landing_page.load()
        button_displayed = self.landing_page.cta_button_is_displayed()
        assert button_displayed
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f'Finished test_cta_button_present. Elapsed time: {elapsed_time} seconds.')
