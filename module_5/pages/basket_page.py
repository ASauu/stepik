from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def go_to_basket(self):
        batton = self.browser.find_element(*BasePageLocators.BASKET)
        batton.click()