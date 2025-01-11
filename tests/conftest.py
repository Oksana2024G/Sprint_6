import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

from curl import *


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    options.add_argument("--windows-size=1200,600")
    service = Service("C:/WebDriver/bin/geckodriver.exe")
    driver = webdriver.Firefox(options = options, service = service)
    driver.get(main_site)
    yield driver
    driver.quit()
