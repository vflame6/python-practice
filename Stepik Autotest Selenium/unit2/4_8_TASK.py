from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element_by_id('book').click()

    answ = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(answ)
    browser.find_element_by_id('solve').click()

    alert = browser.switch_to_alert()
    print('\033[04m\033[91m' + alert.text)
    alert.accept()
finally:
    time.sleep(10)
    browser.quit()
