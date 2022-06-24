from selenium import webdriver
import time, math

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))

link = ''

try:
	browser = webdriver.Chrome()
	browser.get(link)

	alert = browser.switch_to_alert()
	print('\033[04m\033[91m' + alert.text)
	alert.accept()
finally:

	time.sleep(5)
	browser.quit()
