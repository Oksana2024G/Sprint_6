import pytest
import allure
import data
from pages.main_page import MainPage

class TestAnswersToQuestions:
    @allure.title("Текст ответа на вопрос")
    @pytest.mark.parametrize('question_number, expected_text', data.Data.answers_to_questions)
    def test_answers_to_questions(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.wait_for_question_list()
        main_page.click_on_question(question_number)
        answer_text = main_page.get_answer_text(question_number)

        assert answer_text == expected_text
