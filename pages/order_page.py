from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime, timedelta
from helpers import DateFormatter

class OrderPage:

    order_form_title = [By.XPATH, ".//div[contains(@class,'Order_Header') and contains(text(), 'Для кого самокат')]"]
    order_form_input_first_name = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    order_form_input_second_name = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    order_form_input_adress = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    order_form_input_metro = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]
    order_form_input_phone = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    order_next_button = [By.XPATH, ".//div[contains(@class,'Order_NextButton')]/button[text()='Далее']"]
    order_form_next_title = [By.XPATH, ".//div[contains(@class,'Order_Header') and contains(text(), 'Про аренду')]"]
    order_form_input_date = [By.XPATH, ".//input[contains(@placeholder,'Когда привезти самокат')]"]
    order_form_input_rental_period = [By.XPATH,".//div[@class='Dropdown-placeholder' and contains(text(), 'Срок аренды')]"]
    order_form_input_rental_period_dropdown_menu = [By.CSS_SELECTOR, "div.Dropdown-menu"]
    order_form_input_color_checkbox = [By.XPATH, ".//input[@id='black' and @type='checkbox']"]
    order_form_input_comment = [By.XPATH, ".//input[contains(@placeholder,'Комментарий')]"]
    order_form_order_button = [By.XPATH,".//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']"]
    order_form_order_confirm_window_title = [By.XPATH,".//div[contains(@class,'Order_ModalHeader') and contains(text(),'Хотите оформить заказ?')]"]
    order_form_confirm_order_button = [By.XPATH,".//div[contains(@class,'Order_Buttons')]/button[text()='Да']"]
    order_form_order_succeed_text = [By.XPATH, ".//div[contains(@class,'Order_Text')]"]
    order_form_order_succeed = [By.XPATH, ".//div[contains(@class,'Order_ModalHeader') and contains(text(),'Заказ оформлен')]"]
    
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.order_form_title))

    def get_order_form_title_text(self):
        return self.driver.find_element(*self.order_form_title).text
    
    def set_first_name(self, first_name):
        self.driver.find_element(*self.order_form_input_first_name).send_keys(first_name)

    def wait_for_order_form_input_first_name_is_clickable(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(self.order_form_input_first_name))

    def set_second_name(self, second_name):
        self.driver.find_element(*self.order_form_input_second_name).send_keys(second_name)

    def set_adress(self, adress):
        self.driver.find_element(*self.order_form_input_adress).send_keys(adress)
    
    def set_metro(self, metro_name):
        self.driver.find_element(*self.order_form_input_metro).send_keys(metro_name)
        order_form_input_li_xpath = f".//li[contains(@class,'select-search')]//div[contains(text(),'{metro_name}')]"
        order_form_input_metro_li = [By.XPATH, order_form_input_li_xpath]
        self.driver.find_element(*order_form_input_metro_li).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.order_form_input_phone).send_keys(phone_number)

    def order_next_button_click(self):
        self.driver.find_element(*self.order_next_button).click()

    def wait_for_load_next_order_page(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.order_form_next_title))

    def wait_for_order_form_input_date_is_clickable(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(self.order_form_input_date))

    def order_form_input_date_click(self):
        self.driver.find_element(*self.order_form_input_date).click()

    def set_date(self):
        current_date = datetime.now()
        current_date_next_day = current_date + timedelta(days=1)
        date_for_aria_label = DateFormatter.format_date(current_date_next_day)
        order_form_calendar_day_xpath = f".//div[contains(@class,'react-datepicker__day') and @role='button' and contains(@aria-label,'{date_for_aria_label}')]"
        order_form_calendar_day = [By.XPATH, order_form_calendar_day_xpath]
        self.order_form_input_date_click()
        self.driver.find_element(*order_form_calendar_day).click()

    def wait_for_load_rental_period_dropdown_menu(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.order_form_input_rental_period_dropdown_menu))

    def set_rental_period(self, period):
        self.driver.find_element(*self.order_form_input_rental_period).click()
        self.wait_for_load_rental_period_dropdown_menu()
        order_form_rental_period_dropdown_option_xpath = f".//div[contains(@class, 'Dropdown-option') and contains(text(), '{period}')]"
        order_form_rental_period_dropdown_option = [By.XPATH, order_form_rental_period_dropdown_option_xpath]
        self.driver.find_element(*order_form_rental_period_dropdown_option).click()

    def set_color(self, color):
        order_form_checkbox_color_xpath = f".//input[@id='{color}' and @type='checkbox']"
        order_form_checkbox_color = [By.XPATH, order_form_checkbox_color_xpath]
        self.driver.find_element(*order_form_checkbox_color).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.order_form_input_comment).send_keys(comment)

    def order_form_order_button_click(self):
        self.driver.find_element(*self.order_form_order_button).click()

    def wait_order_form_order_confirm_window_title(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.order_form_order_confirm_window_title))

    def order_form_confirm_order_button_click(self):
        self.driver.find_element(*self.order_form_confirm_order_button).click()

    def wait_order_form_order_succeed(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.order_form_order_succeed))

    def get_order_form_order_succeed_text(self):
        return self.driver.find_element(*self.order_form_order_succeed_text).text
