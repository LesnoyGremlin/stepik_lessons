from .base_page import BasePage
from .locators import BasketPageLocators
from .data_links import Links
from .data_language import LANGUAGES_DICT


class BasketPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.BASKET_PAGE_LINK
        self.browser.implicitly_wait(timeout)

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Product is in the basket, but should not be."

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert LANGUAGES_DICT[self.browser.user_language]['empty_basket'] in message, \
            "Empty basket message is not, but should be."
