from selenium import webdriver
import time, os

link = 'http://suninjuly.github.io/file_input.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x = 'lol'
	fi = os.path.join('C:/Users/multi/Desktop/stepik/Автоматизация тестирования с помощью Selenium и Python/2', '2-8.txt')

	for i in browser.find_elements_by_tag_name('input'):
		if i.get_attribute('id') == 'file':
			i.send_keys(fi)
		else:
			i.send_keys(x)

	browser.find_element_by_tag_name('button').click()

finally:
	time.sleep(15)
	browser.quit()
