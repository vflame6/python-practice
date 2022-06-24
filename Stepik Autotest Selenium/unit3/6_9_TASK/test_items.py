import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button_is_located(browser):
    browser.get(link)
    x_testing = browser.find_elements_by_class_name('btn-add-to-basket')
    assert (x_testing is not None and len(x_testing) == 1), "Can't locate unique element: ADD_TO_BASKET_BUTTON"
    time.sleep(15)