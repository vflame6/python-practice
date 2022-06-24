from selenium import webdriver
import time, math

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)
	s = calc(browser.find_element_by_id('input_value').text)
	browser.find_element_by_id('answer').send_keys(s)
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	browser.find_element_by_id('robotCheckbox').click()
	browser.find_element_by_id('robotsRule').click()
	button.click()

finally:
	time.sleep(30)
	browser.quit()
