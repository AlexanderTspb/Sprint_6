from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class YandexPage(BasePage):

    yandex_search_placeholder = [By.XPATH, ".//form[contains(@data-params,'Поиск Яндекса')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем видимость плейсхолдера поисковой строки Яндекса')
    def wait_yandex_search_placeholder_is_visible(self):
        self.wait_for_element_is_visible(self.yandex_search_placeholder)
