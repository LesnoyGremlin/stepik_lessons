from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';")
    browser.execute_script("alert('Robots at work');")
#   или так задать две команды
#    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
