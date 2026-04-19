from pages.main_page import SamokatHomePage
from pages.order_page import OrderPage
from pages.yandex_page import YandexPage
from url import Urls
from data import OrderData
import pytest
import allure

class TestSamokatOrder:

    @allure.title('Проверка сценария заказа самоката')
    @allure.description('Проверяем весь путь от клика на кнопку заказать до появления окна об успешном заказе.'
    'При этом проверяем обе точки входа через разные кнопки "Заказать", с разными наборами данных')
    @pytest.mark.parametrize(
        'order_button, userdata',            
        [
            [SamokatHomePage.order_button_header, OrderData.userdata_1],
            [SamokatHomePage.order_button_roadmap, OrderData.userdata_2],
            [SamokatHomePage.order_button_roadmap, OrderData.userdata_3]
        ]
    )
    def test_order(self, init_browser, order_button, userdata):
        
        main_page = SamokatHomePage(init_browser)
        main_page.open_page(Urls.main_page_url)
        main_page.wait_for_load_main_page()
        main_page.click_cookie_accept_button()
        main_page.scroll_to_order_button(order_button)
        main_page.order_button_click(order_button)
        order_page = OrderPage(init_browser)
        order_page.wait_for_load_order_page()
        order_page.set_first_name(userdata.get('firstname'))
        order_page.set_second_name(userdata.get('secondname'))
        order_page.set_adress(userdata.get('adress'))
        order_page.set_metro(userdata.get('station'))
        order_page.set_phone_number(userdata.get('phone'))
        order_page.order_next_button_click()
        order_page.wait_for_load_next_order_page()
        order_page.set_date()
        order_page.set_rental_period(userdata.get('rental_period'))
        order_page.set_color(userdata.get('color'))
        order_page.set_comment(userdata.get('comment'))
        order_page.order_form_order_button_click()
        order_page.wait_order_form_order_confirm_window_title()
        order_page.order_form_confirm_order_button_click()
        order_page.wait_order_form_order_succeed()
        order_text = order_page.get_order_form_order_succeed_text()
        assert OrderData.order_number in order_text

class TestHeaderLogoLinks:

    @allure.title('Проверка открытия новых страниц при нажатии на логотипы в хэдере страниц')
    @allure.description('Проверяем открытие страницы Дзена при нажатии на логотип Яндекса'
    ' и открытие главной страницы Самоката при нажатии на логотип Самоката')
    def test_logo_click_navigation(self, init_browser):
        order_page = OrderPage(init_browser)
        order_page.open_page(Urls.order_page_url)
        order_page.wait_for_yandex_logo_is_clickable()
        #Сохраняем текущую вкладку
        original_window = init_browser.current_window_handle
        order_page.yandex_logo_click()
        order_page.new_tab_switch(2)
        yandex_page = YandexPage(init_browser)
        yandex_page.wait_yandex_search_placeholder_is_visible()
        assert Urls.yandex_page_url in yandex_page.return_current_url()
        yandex_page.return_tab(original_window)
        yandex_page.wait_for_samokat_logo_is_clickable()
        yandex_page.samokat_logo_click()
        main_page = SamokatHomePage(init_browser)
        main_page.wait_for_load_main_page()
        assert Urls.main_page_url == yandex_page.return_current_url() 
