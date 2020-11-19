from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/ru")

    search = browser.find_element_by_id("id_q")
    search.clear()
    search.send_keys("The shellcoder's handbook")

    search_button = browser.find_element_by_css_selector("input.btn.btn-default").click()

    search_result = browser.find_element_by_link_text("The shellcoder's handbook")
    search_title = browser.find_element_by_tag_name("h1")
    search_title = search_title.text
    assert "The shellcoder's handbook" in search_title

finally:
    time.sleep(5)
    browser.quit()
