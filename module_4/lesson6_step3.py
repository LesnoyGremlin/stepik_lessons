# задачка про инопланетян
import pytest
from selenium import webdriver
import time
import math


push_answer_locator = ".textarea.string-quiz__textarea.ember-text-area.ember-view" #".quiz-component"
answer_locator = ".smart-hints__hint"
button_answer_locator = "button.submit-submission"
good_answer_text = "Correct!"


aliens_for_me = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_from_alien(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    print('\n', link)
    answer = math.log(int(time.time()))
    push_answer = browser.find_element_by_css_selector(push_answer_locator)
    push_answer.send_keys(str(answer))
    time.sleep(2)
    button = browser.find_element_by_css_selector(button_answer_locator)
    button.click()
    answer_alien = browser.find_element_by_css_selector(answer_locator)
    answer_alien_text = answer_alien.text
    time.sleep(2)
    assert answer_alien_text == good_answer_text

    print("\n Ответ от инопланетян: ", aliens_for_me)
# The owls are not what they seem! OvO
