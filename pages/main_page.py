import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_question_list(self):
        self.wait_for_element(MainPageLocators.QUESTIONS)

    @allure.step("Открыть вопрос по индексу")
    def click_on_question(self, question_number):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.wait_for_clickable_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Получить ответ по индексу")
    def get_answer_text(self, index):
        answer_locator = MainPageLocators.answer_number(index)
        answer_element = self.get_text_of_element(answer_locator)
        return answer_element


    @allure.step("Кликнуть на кнопку Заказать")
    def click_order_button_upper(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_UPPER)

    @allure.step("Кликнуть на логотип Самокат")
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Перейти на страницу Дзен")
    def switch_to_dzen(self):
        self.switch_to_last_tab()
        self.wait_for_element(MainPageLocators.DZEN_LOGO)
