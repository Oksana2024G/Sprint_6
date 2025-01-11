import pytest
import allure
import data
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderScooter:
    @allure.title("Тест сообщения об успешном создании заказа")
    @pytest.mark.parametrize('first_name, last_name, address, phone_number, date, period, comment', data.DetailsForOrdering.details_for_ordering)
    def test_order_scooter(self, driver, first_name, last_name, address, phone_number, date, period, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_upper()
        order_page.fill_form_for_whom_scooter(first_name, last_name, address, phone_number)
        order_page.click_next_button()
        order_page.fill_rental_form(date, period, comment)
        order_page.click_order_button()
        order_page.click_confirm_order_button()

        assert order_page.check_success_message()
