# WebAutomatorPy

Automating web interactions using Python and Selenium

## Motivation

The purpose of this project is to automate web interactions using Python and Selenium. By utilizing the Selenium WebDriver, we can simulate user actions such as clicking buttons, filling forms, and scraping data from web pages. This automation can save time and effort in repetitive tasks, improve efficiency, and enable testing of web applications.

## Method and Results

The project utilizes the Selenium WebDriver in Python to automate web interactions. It includes a custom `WebDriver` class that manages the WebDriver instance, provides setup and teardown methods, and offers utility functions such as waiting for elements to appear and taking screenshots.

The `test_landing_page.py` file contains test cases for the landing page of a website. The test cases demonstrate the usage of the `WebDriver` class and validate the functionality of the landing page. They include checks for page loading, element presence, and capturing screenshots on successful load or failure.

The project has been successfully tested, and all test cases pass, ensuring that the WebDriver and landing page functionality work as intended.

## Repository Overview

The repository has the following directory structure:

```
├── drivers
│ └── chromedriver
│ └── LICENSE.chromedriver
├── logs
│ └── test.log
├── screenshots
│ └── successful_load.png
├── src
│ ├── webdriver.py
│ ├── landing_page.py
├── tests
│ └── test_landing_page.py
├── utils
│ └── logger.py
└── README.md
```

- The `drivers` directory contains the ChromeDriver executable file (`chromedriver`) and its license file (`LICENSE.chromedriver`).
- The `logs` directory contains the log file (`test.log`).
- The `screenshots` directory contains the screenshot file (`successful_load.png`).
- The `src` directory contains the main source code files of the project, including `webdriver.py` for managing the Selenium WebDriver, `landing_page.py` for interacting with the landing page, and the `utils` directory with the `logger.py` utility module.
- The `tests` directory contains the test file (`test_landing_page.py`) for testing the landing page functionality.
- The `utils` directory contains the README file (`README.md`) specific to the `utils` directory.
- The root directory also contains the main README file (`README.md`) for the entire project.

Please update this code box with your actual file structure as needed.

## Running Instructions

To run the project and replicate the workflow, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/WebAutomatorPy.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Download the appropriate ChromeDriver executable and update the `CHROMEDRIVER_PATH` variable in `test_landing_page.py` and `webdriver.py` with the correct path.
4. Execute the test cases: `pytest`

Make sure you have Python and Chrome installed on your system before running the project.

## More Resources

For more information and documentation on Selenium WebDriver and Python, refer to the following resources:

- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/en/webdriver/)
- [Python Documentation](https://docs.python.org/)

## About

This project is a personal undertaking by Nathan T. Gundy. It aims to showcase web automation and testing skills using Python and Selenium.
