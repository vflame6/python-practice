from selenium import webdriver
import time, math

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element_by_tag_name('button').click()
	browser.switch_to_window(browser.window_handles[1])

	browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
	browser.find_element_by_tag_name('button').click()

finally:
	alert = browser.switch_to_alert()
	print('\033[04m\033[91m' + alert.text)
	alert.accept()
	time.sleep(5)
	browser.quit()
