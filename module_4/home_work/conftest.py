import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

""" ДЗ 4 часть 1  
конфиг для test_items.py  и register_python.py"""
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(options=options)
    # if browser_name == "chrome":
    #     print("\nstart chrome browser for test..")
    #     browser = webdriver.Chrome()
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     browser = webdriver.Firefox()
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()