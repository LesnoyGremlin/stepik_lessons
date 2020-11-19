from selenium import webdriver
import time


def test_item_search():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/ru")

        search_input = browser.find_element_by_id("id_q")
        search_input.clear()

        # Act
        search_input.send_keys("The shellcoder's handbook")
        browser.find_element_by_css_selector("input.btn.btn-default").click()

        # Assert
        search_title = browser.find_element_by_tag_name("h1")
        assert "The shellcoder's handbook" in search_title.text

    finally:
        time.sleep(5)
        browser.quit()


test_item_search()
