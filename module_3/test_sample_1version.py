# 1 версия. Смотрим, есть ли при неправильном пароле сообщения о каких-то ошибках (любых).
from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
login_or_register_locator = "[id='login_link']"

register_email_locator = "input[name='registration-email']"
register_password_locator = "input[name='registration-password1']"
register_confirm_password_locator = "input[name='registration-password2']"
register_button_locator = "button[name='registration_submit']"
login_email_locator = "input[name='login-username']"
login_password_locator = "input[name='login-password']"
login_button_locator = "button[name='login_submit']"
login_alert_success_locator = ".alert-success"
login_alert_danger_locator = ".alert-danger"

account_logout_locator = "a[href$='accounts/logout/']"
account_profile_locator = "a[href$='accounts/']"
account_delete_locator = "a[id='delete_profile']"
account_delete_password_locator = "input[name='password']"
account_button_delete_locator = "[id='delete_profile_form'] button"


valid_email = "usertest@test.tst"
valid_password = "mjnhbg1357"


def account_registration(browser):
    browser.get(main_page_link)
    browser.find_element_by_css_selector(login_or_register_locator).click()
    email_input = browser.find_element_by_css_selector(register_email_locator)
    email_input.clear()
    email_input.send_keys(valid_email)
    password_input = browser.find_element_by_css_selector(register_password_locator)
    password_input.clear()
    password_input.send_keys(valid_password)
    password_input = browser.find_element_by_css_selector(register_confirm_password_locator)
    password_input.clear()
    password_input.send_keys(valid_password)
    browser.find_element_by_css_selector(register_button_locator).click()
    browser.find_element_by_css_selector(account_logout_locator).click()


def account_delete(browser):
    account_logout = browser.find_elements_by_css_selector(account_logout_locator)
    if len(account_logout) > 0:
        account_logout[0].click()
    browser.find_element_by_css_selector(login_or_register_locator).click()
    email_input = browser.find_element_by_css_selector(login_email_locator)
    email_input.clear()
    email_input.send_keys(valid_email)
    password_input = browser.find_element_by_css_selector(login_password_locator)
    password_input.clear()
    password_input.send_keys(valid_password)
    browser.find_element_by_css_selector(login_button_locator).click()
    browser.find_element_by_css_selector(account_profile_locator).click()
    browser.find_element_by_css_selector(account_delete_locator).click()
    password_input = browser.find_element_by_css_selector(account_delete_password_locator)
    password_input.clear()
    password_input.send_keys(valid_password)
    browser.find_element_by_css_selector(account_button_delete_locator).click()


def test_login_valid_email_and_valid_password():
    # Data
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        account_registration(browser)
        browser.get(main_page_link)
        browser.find_element_by_css_selector(login_or_register_locator).click()

        # Act
        email_input = browser.find_element_by_css_selector(login_email_locator)
        email_input.clear()
        email_input.send_keys(valid_email)
        password_input = browser.find_element_by_css_selector(login_password_locator)
        password_input.clear()
        password_input.send_keys(valid_password)
        browser.find_element_by_css_selector(login_button_locator).click()

        # Assert
        assert len(browser.find_elements_by_css_selector(login_alert_success_locator)) > 0, \
            "Error login: not registered with valid email and valid password"

    finally:
        account_delete(browser)
        browser.quit()


def test_login_valid_email_and_wrong_password():
    # Data
    wrong_password = "tratata"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        account_registration(browser)
        browser.get(main_page_link)
        browser.find_element_by_css_selector(login_or_register_locator).click()

        # Act
        email_input = browser.find_element_by_css_selector(login_email_locator)
        email_input.clear()
        email_input.send_keys(valid_email)
        password_input = browser.find_element_by_css_selector(login_password_locator)
        password_input.clear()
        password_input.send_keys(wrong_password)
        browser.find_element_by_css_selector(login_button_locator).click()

        # Assert
        assert len(browser.find_elements_by_css_selector(login_alert_danger_locator)) > 0, \
            "Error login: login with wrong password"

    finally:
        account_delete(browser)
        browser.quit()


test_login_valid_email_and_valid_password()
test_login_valid_email_and_wrong_password()
