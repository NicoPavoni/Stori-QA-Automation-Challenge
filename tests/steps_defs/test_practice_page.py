import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .pages.practice_page import PracticePage


def test_select_country_mexico(driver):
    page = PracticePage(driver)
    country = 'Mexico'
    page.enter_text_country('Me')
    page.select_option_from_dropdown(country)
    assert country == page.get_country_input().get_attribute('value')


def test_dropdown_option_updates(driver):
    page = PracticePage(driver)
    dropdown = page.get_dropdown()
    select = Select(dropdown)
    select.select_by_value('option2')
    assert 'option2' == dropdown.get_attribute('value')
    time.sleep(5)
    select.select_by_value('option3')
    assert 'option3' == dropdown.get_attribute('value')
    time.sleep(5)


def test_switch_window_example(driver):
    page = PracticePage(driver)
    text = '30 day money back guarantee'
    page.click_switch_window_btn()
    driver.switch_to.window(driver.window_handles[-1])
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text))
        print("Expected text is showing in the page")
    except TimeoutException:
        print(" Test failed. The expected text was not found in the popup window.")
    driver.close()
    time.sleep(5)


def test_alert_pops_up(driver):
    page = PracticePage(driver)
    page.enter_alert_text("Stori Card")
    page.click_alert_btn()
    time.sleep(5)
    alert = page.get_alert()
    assert "Hello Stori Card, share this practice page and share your knowledge" == alert.text
    print(alert.text)
    alert.accept()


def test_alert_pops_up_and_confirm_it(driver):
    page = PracticePage(driver)
    page.enter_alert_text("Stori Card")
    time.sleep(3)
    page.click_confirm_btn()
    alert = page.get_alert()
    time.sleep(3)
    print(alert.text)
    assert "Hello Stori Card, Are you sure you want to confirm?" == alert.text
    alert.accept()
