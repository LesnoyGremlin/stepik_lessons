from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
from .pages.data_language import LANGUAGES_DICT
from .pages.login_page import LoginPage

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

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser)

        # Assert
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()


    @pytest.mark.skip
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.skip
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()
