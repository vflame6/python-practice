from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()


    def should_be_product_added_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_IN_A_BASKET_NAME).text, \
            "Product name not equals basket price"


    def should_be_product_price_in_a_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_IN_A_BASKET_PRICE).text, \
            "Product price not equals basket price"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_A_BASKET_NAME), \
            "Success message is presented, but should not be"


    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_A_BASKET_NAME), \
            "Success message did not dissapear"
