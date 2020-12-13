from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .data_language import LANGUAGES_DICT


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()

    def check_alert_add_to_basket_name(self, expected_text_with_name):
        alerts_list = self.browser.find_elements(*ProductPageLocators.PRODUCT_WAS_ADDED_SUCCESS_ALERT)
        assert len(alerts_list) > 0, "Error. Not alerts about basket."
        alerts_text = [x.text.rstrip() for x in alerts_list]
        assert expected_text_with_name in alerts_text, "Wrong name or message about adding in basket."

    def check_alert_add_to_basket_price(self, expected_price):
        alert = self.browser.find_element(*ProductPageLocators.PRODUCT_WAS_ADDED_INFO_ALERT).text
        assert expected_price in alert, "Wrong price or message about adding in basket."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_WAS_ADDED_SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_WAS_ADDED_SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def product_name_on_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text

    def product_price_on_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE).text
