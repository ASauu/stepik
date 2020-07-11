import random

import allure
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import string


def is_element_present(driver, how, what):
    try:
        driver.find_element(how, what)
    except (NoSuchElementException):
        return False
    return True

@allure.testcase('Тест проверки авторизации')
def test_registration(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    browser.get(link)
    allure.step('Открыть страницу браузера')
    browser.find_element_by_id('login_link').click()
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    browser.find_element_by_name('registration-email').send_keys('111' + res + '@222.ru')
    browser.find_element_by_name('registration-password1').send_keys('111@222,ru')
    browser.find_element_by_name('registration-password2').send_keys('111@222,ru')
    browser.find_element_by_name('registration_submit').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alertinner')))
    assert is_element_present(driver=browser, how=By.CSS_SELECTOR, what='#logout_link')
