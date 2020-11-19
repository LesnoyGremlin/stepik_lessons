from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем обязательные поля
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("ivan@test.test")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file = browser.find_element_by_css_selector("[type = 'file']")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
