from selenium.webdriver.common.by import By


class CommonLocators():
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href$='accounts/']")
    LANGUAGE_SELECTOR = (By.CSS_SELECTOR, "#language_selector")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")


class BasePageLocators(CommonLocators):
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(CommonLocators):
    None


class LoginPageLocators(CommonLocators):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")


class BasketPageLocators(CommonLocators):
    CHANGE_NUMBER_OF_PRODUCT = (By.CSS_SELECTOR, "div.basket-items #id_form-0-quantity")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items h3 a")
    PRODUCT_TOTAL_PRICE = (By.CSS_SELECTOR, "div.basket-items .col-sm-2 p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    REMOVE_FROM_BASKET_BTN = (By.CSS_SELECTOR, "div.basket-items a.inline")
    UPDATE_NUMBER_IN_BASKET_BTN = (By.CSS_SELECTOR, "div.basket-items button")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_WAS_ADDED_INFO_ALERT = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    PRODUCT_WAS_ADDED_SUCCESS_ALERT = (By.CSS_SELECTOR, "#messages .alert-success .alertinner")
