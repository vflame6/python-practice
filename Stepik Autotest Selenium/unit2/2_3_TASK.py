from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
  browser = webdriver.Chrome()
  browser.get(link)

  s = str(int(browser.find_element_by_id('num2').text) + int(browser.find_element_by_id('num1').text))
  x = Select(browser.find_element_by_id('dropdown'))
  x.select_by_value(s)

  browser.find_element_by_class_name('btn').click()

finally:
  time.sleep(15)
  browser.quit()
