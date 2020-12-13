from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span a.btn.btn-default")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_WAS_ADDED_SUCCESS_ALERT = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
    PRODUCT_WAS_ADDED_INFO_ALERT = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main p.price_color")
