import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def init_browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
