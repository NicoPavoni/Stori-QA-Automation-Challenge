import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

BROWSER_OPTION = "--browser"


def pytest_addoption(parser):
    parser.addoption(BROWSER_OPTION, action="store", default="chrome")


@pytest.fixture
def browser(request):
    browser_choice = request.config.getoption(BROWSER_OPTION)

    if browser_choice.lower() == "firefox":
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    elif browser_choice.lower() == "opera":
        browser = webdriver.Opera(service=Service(OperaDriverManager().install()))

    else:  # Make Chrome to default if the parameter browser it's not recognized
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return browser


@pytest.fixture
def driver(browser):
    browser.get('https://rahulshettyacademy.com/AutomationPractice/')
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()
