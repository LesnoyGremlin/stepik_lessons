from selenium import webdriver


main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
login_or_register_locator = "[id='login_link']"

login_email_locator = "input[name='login-username']"
login_password_locator = "input[name='login-password']"
login_button_locator = "button[name='login_submit']"

account_logout_locator = "a[href$='accounts/logout/']"
account_profile_locator = "a[href$='accounts/']"
account_delete_locator = "a[id='delete_profile']"
account_delete_password_locator = "input[name='password']"
account_button_delete_locator = "[id='delete_profile_form'] button"


valid_email = "starodubtseva_test@test.tst"
valid_password = "mjnhbg1357"


def account_delete():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        account_logout = browser.find_elements_by_css_selector(account_logout_locator)
        if len(account_logout) == 0:
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
        print("Удален пользователь с адресом: ", valid_email)

    finally:
        browser.quit()


account_delete()
