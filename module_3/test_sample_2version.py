# Вторая версия теста. Просматриваем все алерты и проверяем, есть ли алерт об ошибке имени и пароле
# реализована функция поиска нужного алерта из массива алертов
from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
login_or_register_locator = "[id='login_link']"

login_email_locator = "input[name='login-username']"
login_password_locator = "input[name='login-password']"
login_button_locator = "button[name='login_submit']"
login_alert_success_locator = ".alert-success"
login_alert_danger_locator = ".alert-danger"

wrong_user_data_alert = 'введите правильные имя пользователя и пароль'

valid_email = "starodubtseva_test@test.tst"
valid_password = "mjnhbg1357"


def is_alert_in_alerts(alerts_array, alert):
    for i_alert in alerts_array:
        if i_alert.text.find(alert) != -1:
            return True
    return False


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
        assert len(browser.find_elements_by_css_selector(login_alert_success_locator)) > 0, \
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
        password_input.send_keys(valid_password)
        browser.find_element_by_css_selector(login_button_locator).click()

#// form / div[contains(., "имя")]
        # Assert
        alerts = browser.find_elements_by_css_selector(login_alert_danger_locator)
        assert is_alert_in_alerts(alerts, wrong_user_data_alert), \
            "Error login: no warning about wrong email and password"

    finally:
        browser.quit()


test_login_valid_email_and_valid_password()
test_login_valid_email_and_wrong_password()
