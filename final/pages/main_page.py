from .base_page import BasePage
from .data import Links


class MainPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.MAIN_PAGE_LINK
        self.browser.implicitly_wait(timeout)

"""
Перенесли эти функции в класс BasePage
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
"""
