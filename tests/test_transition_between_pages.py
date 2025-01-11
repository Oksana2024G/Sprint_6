import pytest
import allure
from pages.main_page import MainPage
from curl import *

class TestTransitionBetweenPages:
    @allure.title("Тест перехода по логотипу Самокат на главную страницу")
    def test_click_scooter_logo_return_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == main_site

    @allure.title("Тест перехода по логотипу Яндекс на страницу Дзен")
    def test_click_yandex_logo_open_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_dzen()
        current_url = main_page.get_current_url()

        assert current_url == dzen_site
