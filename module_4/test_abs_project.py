import unittest
from selenium import webdriver
import time



class TestAbs(unittest.TestCase):

    def test_1(self):
        browser = webdriver.Chrome()
        self.test1 = browser.get("http://suninjuly.github.io/registration1.html")
        input1 = self.test1.find_element_by_css_selector('.first')
        input1.send_keys("Ivan")
        input2 = self.test1.find_element_by_css_selector('.third')
        input2.send_keys("Petrov")
        input3 = self.test1.find_element_by_css_selector('[placeholder="Input your phone:"]')
        input3.send_keys("Smolensk")
        input4 = self.test1.find_element_by_css_selector('.second')
        input4.send_keys("Russia")
        self.test1.find_element_by_css_selector('.btn-default').click()
        self.assertEqual("Congratulations! You have successfully registered!", browser.find_element_by_css_selector('h1').text, "Should be absolute value of a number")
        self.test1.quit()

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()