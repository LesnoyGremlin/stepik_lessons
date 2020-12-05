import data_language


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button_add_to_basket_locator = "button.btn-add-to-basket"


def test_button_add_to_basket_text(browser):
    # Act
    browser.get(link)
    text_button = browser.find_element_by_css_selector(button_add_to_basket_locator).text
    # Assert
    assert text_button == data_language.LANGUAGES_DICT[browser.user_language], \
        "Error: The label on the button doesn't match with expected value."
