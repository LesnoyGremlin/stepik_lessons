from .base_page import BasePage
from .locators import BasketPageLocators
from .data import Links
from .data import ProductTest
from .data_language import LANGUAGES_DICT
from selenium.webdriver.common.keys import Keys


class BasketPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.BASKET_PAGE_LINK
        self.browser.implicitly_wait(timeout)

    def add_number_of_product_in_basket(self, number_product):
        number = self.browser.find_element(*BasketPageLocators.CHANGE_NUMBER_OF_PRODUCT)
        number.clear()
        number.send_keys(str(number_product) + Keys.RETURN)

    def check_total_price_product_in_basket(self, product_price):
        price = self.browser.find_element(*BasketPageLocators.PRODUCT_TOTAL_PRICE).text
        price = price.replace(',', '.')
        print(product_price, price)
        assert product_price in price, \
            "Total price for product is wrong."

    def increase_in_basket(self):
        number = self.browser.find_element(*BasketPageLocators.CHANGE_NUMBER_OF_PRODUCT)
        number.send_keys(Keys.UP)
        button = self.browser.find_element(*BasketPageLocators.UPDATE_NUMBER_IN_BASKET_BTN)
        button.click()

    def reduce_in_basket(self):
        number = self.browser.find_element(*BasketPageLocators.CHANGE_NUMBER_OF_PRODUCT)
        number.send_keys(Keys.DOWN)
        button = self.browser.find_element(*BasketPageLocators.UPDATE_NUMBER_IN_BASKET_BTN)
        button.click()

    def remove_from_basket(self):
        button = self.browser.find_element(*BasketPageLocators.REMOVE_FROM_BASKET_BTN)
        button.click()

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert LANGUAGES_DICT[self.browser.user_language]['empty_basket'] in message, \
            "Empty basket message is not, but should be."

    def should_be_product_in_basket(self, product_name):
        product = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name in product, \
            "Product is not in the basket, but should be."

    def should_be_too_much_product_alert(self):
        input_number = self.browser.find_element(*BasketPageLocators.CHANGE_NUMBER_OF_PRODUCT)
        alert = input_number.get_attribute("validationMessage")
        assert len(alert) > 0, \
            "Not message about more product than available in basket."

    def should_not_add_too_much_product(self):
        price = self.browser.find_element(*BasketPageLocators.PRODUCT_TOTAL_PRICE).text
        price = price.replace(',', '.')
        print(ProductTest.PRODUCT_PRICE, price)
        assert ProductTest.PRODUCT_PRICE in price, \
            "Can add more product than available, but should not be."

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Product is in the basket, but should not be."
