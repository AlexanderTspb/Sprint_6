from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from helpers import DateFormatter
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):

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
        super().__init__(driver)

    @allure.step('Ожидаем видимость заголовка страницы заказа Для кого самокат')
    def wait_for_load_order_page(self):
        self.wait_for_element_is_visible(self.order_form_title)
    
    @allure.step('Получаем текст заголовка страницы заказа Для кого самокат')
    def get_order_form_title_text(self):
        return self.get_element_text(self.order_form_title)
    
    @allure.step('Заполняем поле Имя значением {first_name}')
    def set_first_name(self, first_name):
        self.wait_and_fill_element(self.order_form_input_first_name, first_name)

    @allure.step('Заполняем поле Фамилия значением {second_name}')
    def set_second_name(self, second_name):
        self.wait_and_fill_element(self.order_form_input_second_name, second_name)

    @allure.step('Заполняем поле Адрес значением {adress}')
    def set_adress(self, adress):
        self.wait_and_fill_element(self.order_form_input_adress, adress)
    
    @allure.step('Заполняем поле Станция метро значением {metro_name}')
    def set_metro(self, metro_name):
        self.wait_and_fill_element(self.order_form_input_metro, metro_name)
        order_form_input_li_xpath = f".//li[contains(@class,'select-search')]//div[contains(text(),'{metro_name}')]"
        order_form_input_metro_li = [By.XPATH, order_form_input_li_xpath]
        self.wait_and_click_element(order_form_input_metro_li)

    @allure.step('Заполняем поле Телефон значением {phone_number}')
    def set_phone_number(self, phone_number):
        self.wait_and_fill_element(self.order_form_input_phone, phone_number)

    @allure.step('Выполняем клик по кнопке Далее')
    def order_next_button_click(self):
        self.wait_and_click_element(self.order_next_button)

    @allure.step('Ожидаем видимость заголовка второй страницы заказа Про Аренду')
    def wait_for_load_next_order_page(self):
        self.wait_for_element_is_visible(self.order_form_next_title)
    
    @allure.step('Выполняем клик по полю Когда привезти самокат')
    def order_form_input_date_click(self):
        self.wait_and_click_element(self.order_form_input_date)

    @allure.step('Заполняем поле Когда привезти самокат')
    def set_date(self):
        current_date = datetime.now()
        current_date_next_day = current_date + timedelta(days=1)
        date_for_aria_label = DateFormatter.format_date(current_date_next_day)
        order_form_calendar_day_xpath = f".//div[contains(@class,'react-datepicker__day') and @role='button' and contains(@aria-label,'{date_for_aria_label}')]"
        order_form_calendar_day = [By.XPATH, order_form_calendar_day_xpath]
        self.order_form_input_date_click()
        self.wait_and_click_element(order_form_calendar_day)

    @allure.step('Ожидаем видимость выпадающего меню поля Срок аренды')
    def wait_for_load_rental_period_dropdown_menu(self):
        self.wait_for_element_is_visible(self.order_form_input_rental_period_dropdown_menu)

    @allure.step('Заполняем поле Срок аренды значением {period}')
    def set_rental_period(self, period):
        self.wait_and_click_element(self.order_form_input_rental_period)
        self.wait_for_load_rental_period_dropdown_menu()
        order_form_rental_period_dropdown_option_xpath = f".//div[contains(@class, 'Dropdown-option') and contains(text(), '{period}')]"
        order_form_rental_period_dropdown_option = [By.XPATH, order_form_rental_period_dropdown_option_xpath]
        self.wait_and_click_element(order_form_rental_period_dropdown_option)

    @allure.step('Заполняем поле Цвет самоката значением {color}')
    def set_color(self, color):
        order_form_checkbox_color_xpath = f".//input[@id='{color}' and @type='checkbox']"
        order_form_checkbox_color = [By.XPATH, order_form_checkbox_color_xpath]
        self.wait_and_click_element(order_form_checkbox_color)

    @allure.step('Заполняем поле Комментарий для курьера значением {comment}')
    def set_comment(self, comment):
        self.wait_and_fill_element(self.order_form_input_comment, comment)

    @allure.step('Выполняем клик по кнопке Заказать на второй странице заказа Про Аренду')
    def order_form_order_button_click(self):
        self.wait_and_click_element(self.order_form_order_button)

    @allure.step('Ожидаем видимость заголовка окна подтверждения заказа')
    def wait_order_form_order_confirm_window_title(self):
        self.wait_for_element_is_visible(self.order_form_order_confirm_window_title)

    @allure.step('Выполняем клик по кнопке Да в окне подтверждения заказа')
    def order_form_confirm_order_button_click(self):
        self.wait_and_click_element(self.order_form_confirm_order_button)

    @allure.step('Ожидаем видимость заголовка окна об успешном оформлении заказа')
    def wait_order_form_order_succeed(self):
        self.wait_for_element_is_visible(self.order_form_order_succeed)

    @allure.step('Получаем текст заголовка окна об успешном оформлении заказа')
    def get_order_form_order_succeed_text(self):
        return self.get_element_text(self.order_form_order_succeed_text)
