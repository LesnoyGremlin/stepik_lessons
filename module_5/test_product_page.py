from .pages.product_page import ProductPage
import pytest
from .pages.data_language import LANGUAGES_DICT


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        product_name = page.product_name_on_page()
        product_price = page.product_price_on_page()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        template_name = LANGUAGES_DICT[page.browser.user_language]['add_to_basket_alert_with_name'].format(product_name)

        # Assert
        page.check_alert_add_to_basket_name(template_name)
        page.check_alert_add_to_basket_price(product_price)
