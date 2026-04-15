from selenium import webdriver
from pages.main_page import SamokatHomePage
from data import questionData
from data import answerData
from url import Urls
import pytest
import allure

class TestFaqQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка открытия вопросов и ответов из раздела Вопросы о важном')
    @allure.description('На странице поочередно прокликиваем вопросы, сравниваем текст вопроса, сравниваем текст ответа')
    @pytest.mark.parametrize(
        'index, expected_text_question, expected_text_answer',            
        [
            [0, questionData.question_0, answerData.answer_0],
            [1, questionData.question_1, answerData.answer_1],
            [2, questionData.question_2, answerData.answer_2],
            [3, questionData.question_3, answerData.answer_3],
            [4, questionData.question_4, answerData.answer_4],
            [5, questionData.question_5, answerData.answer_5],
            [6, questionData.question_6, answerData.answer_6],
            [7, questionData.question_7, answerData.answer_7],
        ]
    )
    def test_get_description_questions(self, index, expected_text_question, expected_text_answer):

        self.driver.get(Urls.main_page_url)
        main_page = SamokatHomePage(self.driver)
        main_page.wait_for_load_main_page()
        main_page.click_cookie_accept_button()
        main_page.scroll_to_faq_question(index)
        main_page.click_question(index)
        description = main_page.get_description_question(index)
        assert description == expected_text_question
        answer = main_page.get_answer_question(index)
        assert answer == expected_text_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
