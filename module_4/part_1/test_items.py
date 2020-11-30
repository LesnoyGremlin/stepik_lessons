link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
languages_dict = {'ru': 'Добавить в корзину', 'en-GB': 'Add to basket',\
                  'es': 'Añadir al carrito', 'fr': 'Ajouter au panier'}
button_add_to_basket_locator = "button.btn-add-to-basket"


def test_button_add_to_basket_text(browser):
    browser.get(link)
    text_button = browser.find_element_by_css_selector(button_add_to_basket_locator).text
    # Assert
    assert text_button == languages_dict[browser.user_language], \
        "Error: текст не совпадает"
