import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнить форму Для кого самокат")
    def fill_form_for_whom_scooter(self, first_name, last_name, address, phone_number):
        self.send_keys_to_input(OrderPageLocators.FIRST_NAME_FIELD, first_name)
        self.send_keys_to_input(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_on_element(OrderPageLocators.METRO_STATION_FIELD)
        self.click_on_element(OrderPageLocators.METRO_STATION_DROPDOWN)
        self.send_keys_to_input(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму Про аренду")
    def fill_rental_form(self, date, period, comment):
        self.click_on_element(OrderPageLocators.DELIVERY_DATE_FIELD)
        self.click_on_element(OrderPageLocators.SPECIFIC_DATE)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        period_locator = OrderPageLocators.specific_period(period)
        self.click_on_element(period_locator)
        self.click_on_element(OrderPageLocators.COLOR_CHECKBOX)
        self.send_keys_to_input(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Кликнуть на кнопку Заказать")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку подтверждения заказа")
    def click_confirm_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step("Проверить текст сообщения о заказе")
    def check_success_message(self):
        actual_text = self.get_text_of_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
        return "Заказ оформлен" in actual_text
