from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random


def test_register(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/")
    browser.find_element_by_id('login_link').click()
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
    browser.find_element_by_name('registration-email').send_keys('111'+res+'@222.ru')
    browser.find_element_by_name('registration-password1').send_keys('111@222,ru')
    browser.find_element_by_name('registration-password2').send_keys('111@222,ru')
    browser.find_element_by_name('registration_submit').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'alertinner')))
    assert browser.find_element_by_class_name('icon-signout').text in 'Выход'
    assert 'Спасибо за регистрацию' in browser.find_element_by_class_name('alertinner').text