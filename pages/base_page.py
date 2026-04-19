from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import allure

class BasePage:
    
    yandex_logo = [By.XPATH, ".//div[contains(@class,'Header_Logo')]/a[contains(@class,'Header_LogoYandex')]"]
    samokat_logo = [By.XPATH,".//div[contains(@class,'Header_Logo')]/a[contains(@class,'Header_LogoScooter')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url_page}')
    def open_page(self, url_page):
        self.driver.get(url_page)

    @allure.step('находим элементы по локатору {locator}')
    def find_elements_by_locator(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step('находим элемент по локатору {locator}')
    def find_element_by_locator(self,locator):
        return self.driver.find_element(*locator)

    @allure.step('ожидаем кликабельность элемента {locator_or_element}')
    def wait_for_element_is_clickable(self, locator_or_element):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator_or_element))

    @allure.step('выполняем клик по элементу {locator_or_element}')
    def wait_and_click_element(self, locator_or_element):
        element = self.wait_for_element_is_clickable(locator_or_element)
        element.click()

    @allure.step('заполняем элемент {locator_or_element} значением {text_value}')
    def wait_and_fill_element(self, locator_or_element, text_value):
        element = self.wait_for_element_is_clickable(locator_or_element)
        element.send_keys(text_value)

    @allure.step('ожидаем видимость элемента {locator_or_element}')
    def wait_for_element_is_visible(self, locator_or_element):
        if isinstance(locator_or_element, WebElement):
            return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(locator_or_element))
        else:
            return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator_or_element))

    @allure.step('выполняем прокрут к элементу {locator_or_element}')
    def scroll_to_element(self, locator_or_element):
        element = self.wait_for_element_is_visible(locator_or_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('получаем текст элемента {locator_or_element}')
    def get_element_text(self, locator_or_element):
        element = self.wait_for_element_is_visible(locator_or_element)
        return element.text

    @allure.step('Ожидаем кликабельность Яндекс логотипа')
    def wait_for_yandex_logo_is_clickable(self):
        self.wait_for_element_is_clickable(self.yandex_logo)

    @allure.step('Выполняем клик по Яндекс логотипу')
    def yandex_logo_click(self):
        self.wait_and_click_element(self.yandex_logo)

    @allure.step('Возвращаем url текущей страницы')
    def return_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаемся на новую вкладку номер {tabs}')
    def new_tab_switch(self, tabs):
        WebDriverWait(self.driver, 30).until(expected_conditions.number_of_windows_to_be(tabs))
        #Переключаемся на вторую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Возращаемся к изначальной вкладке')
    def return_tab(self, original_window):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    @allure.step('Ожидаем кликабельность Cамокат логотипа')
    def wait_for_samokat_logo_is_clickable(self):
        self.wait_for_element_is_clickable(self.samokat_logo)

    @allure.step('Выполняем клик по Cамокат логотипу')
    def samokat_logo_click(self):
        self.wait_and_click_element(self.samokat_logo)
