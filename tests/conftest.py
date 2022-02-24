import time

import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from resources.locators import config_path, accept_cookies


@pytest.fixture(scope='session')
def config(request):
    with open(config_path) as config_data:
        data = json.load(config_data)
    return data


@pytest.fixture(scope='session')
def browser_name(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['timeout'] if 'timeout' in config else 5


@pytest.fixture(scope='session')
def base_url(config):
    return config['base_url']


@pytest.fixture(scope='session')
def cookie_selector():
    return accept_cookies


@pytest.fixture(scope="function")
def browser(request, config, browser_name, config_wait_time, base_url, cookie_selector):
    if browser_name == 'chrome':
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(base_url)
    else:
        raise Exception(f'"{browser_name}" is not a supported browser')

    # Wait till the JS is loaded completely and cookies pop up is displayed
    time.sleep(10)
    # Handle cookies
    driver.execute_script(
        "document.querySelector('#usercentrics-root').shadowRoot.querySelector('" + accept_cookies + "').click()")
    request.cls.driver = driver
    yield

    driver.close()
    driver.quit()
