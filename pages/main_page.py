from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class SamokatHomePage(BasePage):

    questions = [By.CSS_SELECTOR,".accordion__button"]
    answers = [By.CSS_SELECTOR,".accordion__panel"]
    main_page_title = [By.XPATH,".//div[contains(@class,'Home_Header') and contains(text(), 'Самокат')]"]
    cookie_accept_button = [By.CSS_SELECTOR,'#rcc-confirm-button']
    faq_div = [By.XPATH,".//div[contains(@class,'Home_FAQ')]"]
    order_button_header = [By.XPATH, ".//div[contains(@class,'Header')]/button[text()='Заказать']"]
    order_button_roadmap = [By.XPATH,".//div[contains(@class,'Home_FinishButton')]/button[contains(text(),'Заказать')]"]

    def __init__(self, driver):
        super().__init__(driver)

    def click_cookie_accept_button(self):
        try:
            self.wait_and_click_element(self.cookie_accept_button)
        except TimeoutException:
            print("cookie_accept_button не стала кликабельной")

    def wait_for_load_main_page(self):
        self.wait_for_element_is_visible(self.main_page_title)

    def scroll_to_faq_question(self, index):
        element = self.find_elements_by_locator(self.questions)[index]
        self.scroll_to_element(element)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def get_description_question(self, index):
        element = self.find_elements_by_locator(self.questions)[index]
        return self.get_element_text(element)
    
    def click_question(self, index):
        element = self.find_elements_by_locator(self.questions)[index]
        self.wait_and_click_element(element)

    def get_answer_question(self, index):
        element = self.find_elements_by_locator(self.answers)[index]
        return self.get_element_text(element)
    
    def scroll_to_order_button(self, button):
        element = self.find_element_by_locator(button)
        self.scroll_to_element(element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform() 

    def order_button_click(self, element):
        self.wait_and_click_element(element)
