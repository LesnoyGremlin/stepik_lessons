from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
login_or_register_locator = "[id='login_link']"

register_email_locator = "input[name='registration-email']"
register_password_locator = "input[name='registration-password1']"
register_confirm_password_locator = "input[name='registration-password2']"
register_button_locator = "button[name='registration_submit']"

valid_email = "starodubtseva_test@test.tst"
valid_password = "mjnhbg1357"


def account_registration():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

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
        print("Создан пользователь с адресом: ", valid_email)

    finally:
        browser.quit()


account_registration()
