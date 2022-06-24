from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_CART), \
            "Cart is not empty"


    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), \
            "No empty cart message"