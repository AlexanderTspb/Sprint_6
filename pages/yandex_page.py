from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class YandexPage:

    yandex_search_placeholder = [By.XPATH, ".//form[contains(@data-params,'Поиск Яндекса')]"]

    def __init__(self, driver):
        self.driver = driver

    def return_current_url(self):
        return self.driver.current_url

    def wait_yandex_search_placeholder_is_visible(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.yandex_search_placeholder))
