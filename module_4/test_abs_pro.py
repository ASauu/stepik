import unittest
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def steps(self):
        input1 = self.browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Smolensk")
        input4 = self.browser.find_element_by_css_selector('.second_block .first')
        input4.send_keys("Russia")
        input5 = self.browser.find_element_by_css_selector('.second_block .second')
        input5.send_keys("Russia")
        self.browser.find_element_by_css_selector('.btn-default').click()

    def test_first(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.steps()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt, "тест 1 не прошел")

    def test_second(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.steps()
        welcome_text_elt = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt, "тест 2 не прошел")


if __name__ == "__main__":
    unittest.main()