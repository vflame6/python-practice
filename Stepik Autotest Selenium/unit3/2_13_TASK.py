from selenium import webdriver
import unittest, time



class TestAbs(unittest.TestCase):
    global link1, link2, browser
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()

    def test1(self):
        browser.get(link1)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys('lol')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys('lol')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys('lol')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        self.assertEqual(welcome_text_elt.text, "Congratulations! You have successfully registered!", "Error")

    def test2(self):
        browser.get(link2)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys('lol')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys('lol')
        browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys('lol')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        self.assertEqual(welcome_text_elt.text, "Congratulations! You have successfully registered!", "Error")

    def stopbrowser(self):
        browser.quit()

if __name__ == "__main__":
    unittest.main()