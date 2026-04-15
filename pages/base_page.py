from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    
    yandex_logo = [By.XPATH, ".//div[contains(@class,'Header_Logo')]/a[contains(@class,'Header_LogoYandex')]"]
    samokat_logo = [By.XPATH,".//div[contains(@class,'Header_Logo')]/a[contains(@class,'Header_LogoScooter')]"]

    def __init__(self, driver):
        self.driver = driver

    def wait_for_yandex_logo_is_clickable(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(self.yandex_logo))

    def yandex_logo_click(self):
        self.driver.find_element(*self.yandex_logo).click()

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
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(self.samokat_logo))

    def samokat_logo_click(self):
        self.driver.find_element(*self.samokat_logo).click()
