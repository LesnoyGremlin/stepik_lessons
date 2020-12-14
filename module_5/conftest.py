import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.data_language import LANGUAGES_DICT
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru, en-GB, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language not in LANGUAGES_DICT.keys():
        raise pytest.UsageError("Test run should contain language for test")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.user_language = user_language

    yield browser
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    print("\nquit browser..")
    browser.quit()
