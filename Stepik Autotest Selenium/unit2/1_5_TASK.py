import math, time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

try:
  browser = webdriver.Chrome()
  browser.get(link)

  x = browser.find_element_by_id('input_value').text
  browser.find_element_by_id('answer').send_keys(calc(x))
  browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
  browser.find_element_by_css_selector('[for="robotsRule"]').click()
  browser.find_element_by_tag_name('button').click()

finally:
  time.sleep(20)
  browser.quit()

