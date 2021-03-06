import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data_language


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="None",
                     help="Choose language: ru, en-GB, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language not in data_language.LANGUAGES_DICT.keys():
        raise pytest.UsageError("Test run should contain language for test")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.user_language = user_language
    yield browser
    print("\nquit browser..")
    browser.quit()
