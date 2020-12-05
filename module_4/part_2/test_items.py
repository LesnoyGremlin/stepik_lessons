link = "http://selenium1py.pythonanywhere.com/"

valid_email = "starodubtseva_new_user@test.tst"
valid_password = "qwer4321rewq"

login_or_register_locator = "[id='login_link']"
register_email_locator = "input[name='registration-email']"
register_password_locator = "input[name='registration-password1']"
register_confirm_password_locator = "input[name='registration-password2']"
register_button_locator = "button[name='registration_submit']"

account_logout_locator = "a[href$='accounts/logout/']"
account_profile_locator = "a[href$='accounts/']"
account_delete_locator = "a[id='delete_profile']"
account_delete_password_locator = "input[name='password']"
account_button_delete_locator = "[id='delete_profile_form'] button"


def test_new_user_registration_with_valid_data(browser):
    # Act
    browser.get(link)
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

    # Assert
    account_logout = browser.find_elements_by_css_selector(account_logout_locator)
    assert len(account_logout) > 0, \
        "Not registration with valid data"

    # Delete new user
    browser.find_element_by_css_selector(account_profile_locator).click()
    browser.find_element_by_css_selector(account_delete_locator).click()
    password_input = browser.find_element_by_css_selector(account_delete_password_locator)
    password_input.clear()
    password_input.send_keys(valid_password)
    browser.find_element_by_css_selector(account_button_delete_locator).click()
