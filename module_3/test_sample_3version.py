# Потренируюсь писать разные тесты, то есть больше, чем отправлено в дз
# тесты по проверке входа в аккаунт
from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

valid_email = "starodubtseva_test@test.tst"
valid_password = "mjnhbg1357"

success_user_login_alert = "Рады видеть вас снова"
wrong_user_data_alert = "введите правильные имя пользователя и пароль"
not_valid_email_alert = "Введите корректный адрес электронной почты"
password_recovery_text = "Восстановление пароля"

login_or_register_locator = "[id='login_link']"
login_email_locator = "input[name='login-username']"
login_password_locator = "input[name='login-password']"
login_button_locator = "button[name='login_submit']"
login_alert_success_path_locator = f"//div[@id='messages']/div[contains(., '{success_user_login_alert}')]"
login_alert_danger_locator = ".alert-danger"
alert_wrong_email_or_password_path_locator = f"//form/div[contains(., '{wrong_user_data_alert}')]"
alert_not_valid_email_path_locator = f"//span[contains(., '{not_valid_email_alert}')]"
password_recovery_locator = "a[href$='/password-reset/']"
page_password_recovery_path_locator = f"//h1[contains(., '{password_recovery_text}')]"


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
        assert len(browser.find_elements_by_xpath(login_alert_success_path_locator)) > 0, \
            "Error login: not registered with valid email and valid password"

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
        assert len(browser.find_elements_by_xpath(alert_wrong_email_or_password_path_locator)) > 0, \
            "Error login: no warning about wrong email and password"

    finally:
        browser.quit()


def test_login_not_valid_email():
    # Data
    not_valid_email = "starodubtseva_test@test"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_css_selector(login_or_register_locator).click()

        # Act
        email_input = browser.find_element_by_css_selector(login_email_locator)
        email_input.clear()
        email_input.send_keys(not_valid_email)
        password_input = browser.find_element_by_css_selector(login_password_locator)
        password_input.clear()
        password_input.send_keys(valid_password)
        browser.find_element_by_css_selector(login_button_locator).click()

        # Assert
        assert len(browser.find_elements_by_xpath(alert_not_valid_email_path_locator)) > 0, \
            "Error login: no warning about not valid email"

    finally:
        browser.quit()


def test_forgotten_password():
    # Data
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_css_selector(login_or_register_locator).click()

        # Act
        browser.find_element_by_css_selector(password_recovery_locator).click()

        # Assert
        assert len(browser.find_elements_by_xpath(page_password_recovery_path_locator)) > 0, \
            "Error login: failed to go to the password recovery page"

    finally:
        browser.quit()


test_login_valid_email_and_valid_password()
test_login_valid_email_and_wrong_password()
test_login_not_valid_email()
test_forgotten_password()
