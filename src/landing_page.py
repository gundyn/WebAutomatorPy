import logging

class LandingPage:
    """Interactions with the landing page."""

    URL = 'https://ultimateqa.com/fake-landing-page'

    def __init__(self, driver):
        """Initialize with the WebDriver instance."""
        self.driver = driver

    def load(self):
        """Load the landing page."""
        logging.info('Loading landing page.')
        self.driver.driver.get(self.URL)

    # Other methods for interacting with the landing page
