from .base_page import BasePage
from .data import Links


class MainPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.MAIN_PAGE_LINK
        self.browser.implicitly_wait(timeout)
