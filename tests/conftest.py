import os

import pytest
from selene import browser
from selenium import webdriver

from respublica_tests.application import app
from respublica_tests.pages.cart_page import CartPage
from utils import attach
from selenium.webdriver.chrome.options import Options

WEB_URL = "https://www.respublica.ru"


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.timeout = 8.0
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.base_url = WEB_URL

    # driver_options = webdriver.ChromeOptions()
    # driver_options.page_load_strategy = 'eager'
    # browser.config.driver_options = driver_options

    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": 'chrome',
    #     "browserVersion": '100.0',
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    # login = os.getenv('SELENOID_LOGIN')
    # password = os.getenv('SELENOID_PASSWORD')
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )
    #
    # browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def clear_cart_when_finished():

    yield

    if app.cart_page.cart_has_items():
        app.cart_page.clear_cart()
        app.cart_page.check_is_cart_empty()
