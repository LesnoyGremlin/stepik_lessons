from selenium import webdriver
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)
            # заполняем обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block .first_class input")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second_class input")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third_class input")
            input3.send_keys("ivan@test.test")
            # Отправляем заполненную форму
            button = browser.find_element_by_tag_name("button")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", \
            "Registration failed")
        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)
            # заполняем обязательные поля
            input1 = browser.find_element_by_css_selector(".first_block .first_class input")
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_css_selector(".first_block .second_class input")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_css_selector(".first_block .third_class input")
            input3.send_keys("ivan@test.test")
            # Отправляем заполненную форму
            button = browser.find_element_by_tag_name("button")
            button.click()
            # Проверяем, что смогли зарегистрироваться
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", \
            "Registration failed")
        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
