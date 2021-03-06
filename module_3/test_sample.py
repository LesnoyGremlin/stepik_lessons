#!/usr/bin/env python3
"""
Домашнее задание по модулю 3, окончательное
- Заранее создан пользователь starodubtseva_test@test.tst, который используется в тестах
 (в первой версии пользователь создавался и удалялся в каждом тесте).
- Добавлена проверка входа пользователя по наличию ссылок на "Аккаунт" или "Войти"
"""

from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
login_or_register_locator = "[id='login_link']"

valid_email = "starodubtseva_test@test.tst"
valid_password = "mjnhbg1357"

success_user_login_alert = "Рады видеть вас снова"
wrong_user_data_alert = "введите правильные имя пользователя и пароль"

login_email_locator = "input[name='login-username']"
login_password_locator = "input[name='login-password']"
login_button_locator = "button[name='login_submit']"
login_alert_success_path_locator = f"//div[@id='messages']/div[contains(., '{success_user_login_alert}')]"
login_alert_danger_locator = ".alert-danger"
alert_wrong_email_or_password_path_locator = f"//form/div[contains(., '{wrong_user_data_alert}')]"
account_profile_locator = "a[href$='accounts/']"


def test_login_valid_email_and_valid_password():
    # Data
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
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
        assert len(browser.find_elements_by_css_selector(account_profile_locator)) > 0, \
            "Error login: not registered with valid email and valid password"
        # Assert
        assert len(browser.find_elements_by_xpath(login_alert_success_path_locator)) > 0, \
            "Error login: registered, but no welcome message with valid email and valid password"

    finally:
        browser.quit()


def test_login_valid_email_and_wrong_password():
    # Data
    wrong_password = "tratata"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
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
        assert len(browser.find_elements_by_css_selector(login_or_register_locator)) > 0, \
            "Error login: registered with wrong email and password"
        assert len(browser.find_elements_by_xpath(alert_wrong_email_or_password_path_locator)) > 0, \
            "Error login: not registered, but no warning about wrong email and password"

    finally:
        browser.quit()


test_login_valid_email_and_valid_password()
test_login_valid_email_and_wrong_password()
