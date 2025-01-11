from selenium.webdriver.common.by import  By

class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_DROPDOWN = (By.XPATH, "//ul[@class='select-search__options']/li")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SPECIFIC_DATE = (By.XPATH, "//div[@class='react-datepicker__week']/div[@class='react-datepicker__day react-datepicker__day--015']")
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_DROPDOWN_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']/div")
    COLOR_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    ORDER_CONFIRMATION_BUTTON = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']/div[@class='Order_Buttons__1xGrp']/button[text()='Да']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, ".//*[text()='Заказ оформлен']")

    @staticmethod
    def specific_period(period):
        return By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{period}']"
