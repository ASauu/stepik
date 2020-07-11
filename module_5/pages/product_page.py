import math
from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):
    def go_to_productpage(self):
        batton = self.browser.find_element(*ProductPageLocator.ADD_BOOK)
        batton.click()

    def get_book(self):
        res = self.browser.find_element(*ProductPageLocator.GET_BOOK)
        return res.text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            w=0
            print('sss')


        except NoAlertPresentException:
            print("No second alert presented")