from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class SamokatHomePage:

    questions = [By.CSS_SELECTOR,".accordion__button"]
    answers = [By.CSS_SELECTOR,".accordion__panel"]
    main_page_title = [By.XPATH,".//div[contains(@class,'Home_Header') and contains(text(), 'Самокат')]"]
    cookie_accept_button = [By.CSS_SELECTOR,'#rcc-confirm-button']
    faq_div = [By.XPATH,".//div[contains(@class,'Home_FAQ')]"]
    order_button_header = [By.XPATH, ".//div[contains(@class,'Header')]/button[text()='Заказать']"]
    order_button_roadmap = [By.XPATH,".//div[contains(@class,'Home_FinishButton')]/button[contains(text(),'Заказать')]"]

    def __init__(self, driver):
        self.driver = driver

    def click_cookie_accept_button(self):
        try:
            button = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(self.cookie_accept_button))
            button.click()
        except TimeoutException:
            print("cookie_accept_button не стала кликабельной")

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.main_page_title))

    def scroll_to_faq_question(self, index):
        element = self.driver.find_elements(*self.questions)[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_description_question(self, index):
        return self.driver.find_elements(*self.questions)[index].text
    
    def click_question(self, index):
        element = self.driver.find_elements(*self.questions)[index]
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element))
        element.click()

    def get_answer_question(self, index):
        return self.driver.find_elements(*self.answers)[index].text
    
    def scroll_to_order_button(self, button):
        element = self.driver.find_element(*button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element))
    
    def order_button_click(self, element):
        self.driver.find_element(*element).click()
