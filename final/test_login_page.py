import pytest
from .pages.login_page import LoginPage


class TestBasketPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()

    @pytest.mark.parametrize('wrong_email', ["testtest.tst",
                                             "test@test@tst"])
    def test_cant_wrong_email_for_login(self, browser, wrong_email):
        # Act
        login_page = LoginPage(browser)
        login_page.send_login_email(wrong_email)

        # Assert
        login_page.should_be_wrong_user_email_alert()
