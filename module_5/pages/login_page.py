from .base_page import BasePage
from .locators import LoginPageLocators
from .data import Links


class LoginPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.LOGIN_PAGE_LINK
        self.browser.implicitly_wait(timeout)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert "login" in url, "Incorrect url for registration page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
