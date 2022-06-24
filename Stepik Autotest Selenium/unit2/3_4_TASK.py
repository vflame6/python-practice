from selenium import webdriver
import time, math

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element_by_tag_name('button').click()
	confirm = browser.switch_to.alert
	confirm.accept()
	s = calc(browser.find_element_by_id('input_value').text)
	browser.find_element_by_id('answer').send_keys(s)
	button = browser.find_element_by_tag_name("button").click()

	alert = browser.switch_to_alert()
	print(alert.text)
	alert.accept()
	# prompt.send_keys("My answer")
	# confirm.dismiss()


finally:
	time.sleep(5)
	browser.quit()
