from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
value1 = 'input'
value2 = 'last_name'
value3 = 'city'
value4 = 'country'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
