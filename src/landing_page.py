import logging

from selenium.webdriver.common.by import By

class LandingPage:
    """Interactions with the landing page."""

    URL = 'https://ultimateqa.com/fake-landing-page'
    CTA_BUTTON = (By.ID, 'et_pb_contact_submit_0')

    def __init__(self, driver):
        """Initialize with the WebDriver instance."""
        self.driver = driver

    def load(self):
        """Load the landing page."""
        logging.info('Loading landing page.')
        self.driver.get(self.URL)

    def cta_button_is_displayed(self):
        """Check if the CTA button is displayed."""
        button_displayed = self.driver.find_element(*self.CTA_BUTTON).is_displayed()
        if button_displayed:
            logging.info('CTA button is displayed.')
        else:
            logging.warning('CTA button is not displayed.')
        return button_displayed
