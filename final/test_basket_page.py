from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
from .pages.login_page import LoginPage
from .pages.data import ProductTest
from .pages.data import UserDate
import time


# @pytest.mark.guest_change_basket
class TestGuestChangeBasketPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_to_basket()

    @pytest.mark.xfail
    def test_guest_can_remove_product_from_basket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.remove_from_basket()

        # Assert
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_guest_can_reduce_number_of_product_in_basket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.reduce_in_basket()

        # Assert
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_guest_can_increase_number_of_product_in_basket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.increase_in_basket()
        total_price_product = str(float(ProductTest.PRODUCT_PRICE) * 2)

        # Assert
        basket_page.should_be_product_in_basket(ProductTest.PRODUCT_NAME)
        basket_page.check_total_price_product_in_basket(total_price_product)

    def test_guest_cant_add_more_product_than_available(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.add_number_of_product_in_basket(ProductTest.PRODUCT_IN_STOCK + 1)

        # Assert
        basket_page.should_not_add_too_much_product()
#        basket_page.should_be_too_much_product_alert()


# @pytest.mark.user_change_basket
class TestUserChangeBasketPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        print(email)
        page.register_new_user(email, UserDate.VALID_PASSWORD)
        page.should_be_authorized_user()

        page = ProductPage(browser)
        page.open()
        page.add_to_basket()

    @pytest.mark.xfail
    def test_user_can_remove_product_from_basket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.remove_from_basket()

        # Assert
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_user_can_reduce_number_of_product_in_basket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.reduce_in_basket()

        # Assert
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()

    def test_user_can_increase_number_of_product_in_basket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.increase_in_basket()
        total_price_product = str(float(ProductTest.PRODUCT_PRICE) * 2)

        # Assert
        basket_page.should_be_product_in_basket(ProductTest.PRODUCT_NAME)
        basket_page.check_total_price_product_in_basket(total_price_product)

    def test_user_cant_add_more_product_than_available(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.add_number_of_product_in_basket(ProductTest.PRODUCT_IN_STOCK + 1)

        # Assert
        basket_page.should_not_add_too_much_product()
#        basket_page.should_be_too_much_product_alert()
