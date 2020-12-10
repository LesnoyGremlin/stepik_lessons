from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .data_language import LANGUAGES_DICT


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()

    def was_product_added_in_basket(self, product_name, product_price):
        alerts = self.browser.find_elements(*ProductPageLocators.PRODUCT_WAS_ADDED_ALERTS)
        assert len(alerts) > 0, "Not alerts."
        assert LANGUAGES_DICT[self.browser.user_language] in alerts[0].text, \
            "Not alert product was added."
        product = self.browser.find_elements(*ProductPageLocators.PRODUCT_WAS_ADDED_ALERT)
        assert product_name == product[0].text, "Wrong product was added."
        assert product_price == product[len(product)-1].text, "Wrong price for product was added."

    def product_name_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def product_price_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main p.price_color ").text
