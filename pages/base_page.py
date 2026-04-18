from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    
    yandex_logo = [By.XPATH, ".//div[contains(@class,'Header_Logo')]/a[contains(@class,'Header_LogoYandex')]"]
    samokat_logo = [By.XPATH,".//div[contains(@class,'Header_Logo')]/a[contains(@class,'Header_LogoScooter')]"]

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url_page):
        self.driver.get(url_page)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element_by_locator(self,locator):
        return self.driver.find_element(*locator)

    def wait_for_element_is_clickable(self, locator_or_element):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator_or_element))

    def wait_and_click_element(self, locator_or_element):
        element = self.wait_for_element_is_clickable(locator_or_element)
        element.click()

    def wait_and_fill_element(self, locator_or_element, text_value):
        element = self.wait_for_element_is_clickable(locator_or_element)
        element.send_keys(text_value)

    def wait_for_element_is_visible(self, locator_or_element):
        if isinstance(locator_or_element, WebElement):
            return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(locator_or_element))
        else:
            return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator_or_element))

    def scroll_to_element(self, locator_or_element):
        element = self.wait_for_element_is_visible(locator_or_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_text(self, locator_or_element):
        element = self.wait_for_element_is_visible(locator_or_element)
        return element.text

    def wait_for_yandex_logo_is_clickable(self):
        self.wait_for_element_is_clickable(self.yandex_logo)

    def yandex_logo_click(self):
        self.wait_and_click_element(self.yandex_logo)

    def return_current_url(self):
        return self.driver.current_url

    def new_tab_switch(self, tabs):
        WebDriverWait(self.driver, 30).until(expected_conditions.number_of_windows_to_be(tabs))
        #Переключаемся на вторую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

    def return_tab(self, original_window):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def wait_for_samokat_logo_is_clickable(self):
        self.wait_for_element_is_clickable(self.samokat_logo)

    def samokat_logo_click(self):
        self.wait_and_click_element(self.samokat_logo)
