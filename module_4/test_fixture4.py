import pytest
from selenium import webdriver


"""
В отличии от предыдущего здесь браузер запускается один раз для всех тестов и закрывается по окончании тестов
"""
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="module")  # scope задает выполнится один раз для всего модуля
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".basket-mini .btn-group > a")
