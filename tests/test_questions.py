from pages.main_page import SamokatHomePage
from data import QuestionData
from data import AnswerData
from url import Urls
import pytest
import allure

class TestFaqQuestions:

    @allure.title('Проверка открытия вопросов и ответов из раздела Вопросы о важном')
    @allure.description('На странице поочередно прокликиваем вопросы, сравниваем текст вопроса, сравниваем текст ответа')
    @pytest.mark.parametrize(
        'index, expected_text_question, expected_text_answer',            
        [
            [0, QuestionData.QUESTION_0, AnswerData.ANSWER_0],
            [1, QuestionData.QUESTION_1, AnswerData.ANSWER_1],
            [2, QuestionData.QUESTION_2, AnswerData.ANSWER_2],
            [3, QuestionData.QUESTION_3, AnswerData.ANSWER_3],
            [4, QuestionData.QUESTION_4, AnswerData.ANSWER_4],
            [5, QuestionData.QUESTION_5, AnswerData.ANSWER_5],
            [6, QuestionData.QUESTION_6, AnswerData.ANSWER_6],
            [7, QuestionData.QUESTION_7, AnswerData.ANSWER_7],
        ]
    )
    def test_get_description_questions(self, init_browser, index, expected_text_question, expected_text_answer):

        main_page = SamokatHomePage(init_browser)
        main_page.open_page(Urls.main_page_url)
        main_page.wait_for_load_main_page()
        main_page.click_cookie_accept_button()
        main_page.scroll_to_faq_question(index)
        main_page.click_question(index)
        description = main_page.get_description_question(index)
        assert description == expected_text_question
        answer = main_page.get_answer_question(index)
        assert answer == expected_text_answer
