from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

""" ДЗ 4 часть 2   задание
Создайте тест для регистрации нового пользователя на сайте http://selenium1py.pythonanywhere.com/:

в виде отдельного файла-теста на Python с помощью Selenium+Pytest  - это этот файл
с помощью Codeless-рекордера (Selenium IDE или Katalon automation recorder на выбор). - это файл register.side"""
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