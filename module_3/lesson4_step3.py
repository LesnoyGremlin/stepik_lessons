from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id('num1')
    x1 = x1_element.text
    x2_element = browser.find_element_by_id('num2')
    x2 = x2_element.text
    y = int(x1) + int(x2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
