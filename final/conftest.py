import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.data_language import LANGUAGES_DICT
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language not in LANGUAGES_DICT.keys():
        raise pytest.UsageError("Test run should contain language for test")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=profile)

    browser.user_language = user_language

    yield browser
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    print("\nquit browser..")
    browser.quit()
