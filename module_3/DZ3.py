
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import string

import random


def setup():
    global browser
    browser = webdriver.Chrome()
    browser.get("http://selenium1py.pythonanywhere.com/ru/")

def teardown():
    browser.close()


def open_catalog():
    browser.find_element_by_class_name('dropdown-toggle').click()
    browser.find_element_by_css_selector('[href="/ru/catalogue/"]').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'page-header')))


try:
#предусловие


#тест 1
    setup()
    browser.find_element_by_id('login_link').click()
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
    browser.find_element_by_name('registration-email').send_keys('111'+res+'@222.ru')
    browser.find_element_by_name('registration-password1').send_keys('111@222,ru')
    browser.find_element_by_name('registration-password2').send_keys('111@222,ru')
    browser.find_element_by_name('registration_submit').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'alertinner')))
    assert browser.find_element_by_class_name('icon-signout').text in 'Выход'
    assert 'Спасибо за регистрацию' in browser.find_element_by_class_name('alertinner').text
    teardown()


#тест 2
    setup()
    select = Select(browser.find_element_by_name("language"))
    select.select_by_index(5)
    browser.find_element_by_css_selector('#language_selector .btn-default').click()
    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#language_selector .btn-default"), "Go"))
    assert browser.find_element_by_css_selector('.pull-right strong').text  == 'Basket total:'
    select = Select(browser.find_element_by_name("language"))
    select.select_by_index(17)
    browser.find_element_by_css_selector('#language_selector .btn-default').click()
    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#language_selector .btn-default"), "Выполнить"))
    assert browser.find_element_by_css_selector('.pull-right strong').text  == 'Всего в корзине:'
    teardown()

#тест 3
    setup()
    open_catalog()
    assert browser.find_element_by_css_selector('[title^="The shellcoder"]').text == 'The shellcoder\'s handbook'
    teardown()

#тест4
    setup()
    open_catalog()
    browser.find_element_by_css_selector('[title^="The shellcoder"]').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "product_main")))
    assert  '9,99' in browser.find_element_by_class_name('price_color').text
    assert browser.find_element_by_class_name('btn-add-to-basket').text == 'Добавить в корзину'
    teardown()

#тест 5
    setup()
    open_catalog()
    browser.find_element_by_css_selector('[title^="The shellcoder"]').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "product_main")))
    browser.find_element_by_class_name('btn-add-to-basket').click()
    browser.find_element_by_css_selector('a[href="/ru/basket/"]').click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "content_inner")))
    assert [ i.text for i in browser.find_elements_by_css_selector('#basket_formset .col-sm-4 h3')][0] in 'The shellcoder\'s handbook'
    teardown()

finally:
    browser.quit()