from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()
