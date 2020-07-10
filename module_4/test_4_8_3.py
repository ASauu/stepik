import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link',
                         [#'https://stepik.org/lesson/236895/step/1',
                         # 'https://stepik.org/lesson/236896/step/1',
                        #  'https://stepik.org/lesson/236897/step/1',
                        #  'https://stepik.org/lesson/236898/step/1',
                        #  'https://stepik.org/lesson/236899/step/1',
                        #  'https://stepik.org/lesson/236903/step/1',
                          'https://stepik.org/lesson/236904/step/1'#,
                     #     'https://stepik.org/lesson/236905/step/1'
                         ])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[id^="ember"]')))
    browser.find_element_by_css_selector('textarea[id^="ember"]').send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    assert browser.find_element_by_css_selector(".smart-hints__hint").text == 'Correct!', f' некоррекная буква: {browser.find_element_by_css_selector(".smart-hints__hint").text}'
