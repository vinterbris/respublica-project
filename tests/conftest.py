import os

import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

from respublica_tests.application import app
from utils import attach

WEB_URL = "https://www.respublica.ru"


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='120.0')
    parser.addoption('--selenoid', default=False)
    parser.addoption('--selenoid_url', default='http://localhost:4444')
    parser.addoption('--selenoid_ui_url', default='http://localhost:8080')


'''
using https://localtunnel.github.io to forward selenoid on localhost to the internet

Install Localtunnel globally (requires NodeJS) to make it accessible anywhere:

npm install -g localtunnel

Start a webserver on some local port (eg http://localhost:4444) 
and use the command line interface to request a tunnel to your local server:

lt --port 8000

You will receive a url, for example https://gqgh.localtunnel.me, 
that you can share with anyone for as long as your local instance of lt remains active. 
Any requests will be routed to your local service at the specified port.
'''


@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    run_selenoid = request.config.getoption('--selenoid')
    selenoid_url = request.config.getoption('--selenoid_url')
    selenoid_ui_url = request.config.getoption('--selenoid_ui_url')

    browser.config.timeout = 10.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = WEB_URL

    if run_selenoid:
        options = Options()
        options.add_argument("bypass-tunnel-reminder=True")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        selenoid_capabilities = {
            "browserName": 'chrome',
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=selenoid_url + "/wd/hub/",
            options=options
        )

        # login = os.getenv('SELENOID_LOGIN')
        # password = os.getenv('SELENOID_PASSWORD')
        # driver = webdriver.Remote(
        #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        #     options=options
        # )

        browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, selenoid_ui_url)

    browser.quit()


@pytest.fixture(scope='function')
def clear_cart_when_finished():
    yield

    if app.cart_page.cart_has_items():
        app.cart_page.clear_cart()
        app.cart_page.check_is_cart_empty()
