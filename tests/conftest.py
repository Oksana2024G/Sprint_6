import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

from curl import *


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()

    options.add_argument("--windows-size=1200,600")
    driver = webdriver.Firefox(options = options)
    driver.get(main_site)
    yield driver
    driver.quit()
