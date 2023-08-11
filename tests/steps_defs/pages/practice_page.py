from selenium.webdriver.common.by import By

from tests.steps_defs.pages.base_page import BasePage


class PracticePage(BasePage):

    """
            Page Object for the stori Practice Page.

            Contains methods to interact with the screen elements.

            Attributes:
                driver (WebDriver): The WebDriver instance used to interact with the web application.

            Methods:
                This class contains methods to search for its elements. These functions use driver decorators
                (find_element_by_id, find_element_by_xpath) to centralize the search code, avoid writing waiting
                conditions throughout the test suite, and simplify the implementation.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    COUNTRIES_INPUT = (By.XPATH, '/html/body/div[1]/div[2]/fieldset/input')
    SELECT_DROPDOWN = (By.XPATH, '/html/body/div[1]/div[3]/fieldset/select')
    OPEN_WINDOW_BTN = (By.XPATH, '/html/body/div[2]/div[1]/fieldset/button')
    SWITCH_TO_ALERT_INPUT = (By.XPATH, '/html/body/div[2]/div[3]/fieldset/input[1]')
    ALERT_BTN = (By.ID, 'alertbtn')
    CONFIRM_BTN = (By.ID, 'confirmbtn')
    SWITCH_WINDOW_BTN = (By.XPATH, '//*[@id="openwindow"]')

    def get_country_input(self):
        return self.driver.find_element(*self.COUNTRIES_INPUT)

    def get_dropdown(self):
        return self.driver.find_element(*self.SELECT_DROPDOWN)

    def get_alert_input(self):
        return self.driver.find_element(*self.SWITCH_TO_ALERT_INPUT)

    def get_alert_btn(self):
        return self.driver.find_element(*self.ALERT_BTN)

    def get_confirm_btn(self):
        return self.driver.find_element(*self.CONFIRM_BTN)

    def get_switch_window_btn(self):
        return self.driver.find_element(*self.SWITCH_WINDOW_BTN)

    def get_country_option(self, country):
        locator = (By.XPATH, '//li/div[text()="{}"]'.format(country))
        return self.find_visible_element(locator)

    def enter_text_country(self, country):
        country_input = self.get_country_input()
        country_input.send_keys(country)

    def select_option_from_dropdown(self, country):
        option = self.get_country_option(country)
        option.click()

    def enter_alert_text(self, text):
        alert_input = self.get_alert_input()
        alert_input.click()
        alert_input.send_keys(text)

    def click_alert_btn(self):
        self.get_alert_btn().click()

    def click_confirm_btn(self):
        self.get_confirm_btn().click()

    def click_switch_window_btn(self):
        self.get_switch_window_btn().click()

    def get_alert(self):
        return self.driver.switch_to.alert
