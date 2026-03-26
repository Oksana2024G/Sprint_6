from selenium.webdriver.common.by import  By

class MainPageLocators:
    QUESTIONS = (By.CLASS_NAME, "accordion__heading")
    YANDEX_LOGO = (By.XPATH, "//a[@href='//yandex.ru']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    ORDER_BUTTON_UPPER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    ORDER_BUTTON_LOWER = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    DZEN_LOGO = (By.XPATH, "//a[@class='dzen-layout--desktop-base-header__logoLink-2h']")

    @staticmethod
    def question_number(index):
        return By.XPATH, f'//div[@id="accordion__heading-{index}"]'

    @staticmethod
    def answer_number(index):
        return By.XPATH, f'//div[@id="accordion__panel-{index}"]/p'
