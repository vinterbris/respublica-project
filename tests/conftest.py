import allure
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import project
from respublica_tests.application import app
from respublica_tests.utils import attach


def pytest_addoption(parser):
    parser.addoption('--browser_version', default='124.0')
    parser.addoption('--selenoid', default=False)
    parser.addoption('--selenoid_url', default='http://localhost:4444')
    parser.addoption('--selenoid_ui_url', default='http://localhost:8080')


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    run_selenoid = request.config.getoption('--selenoid')
    selenoid_url = request.config.getoption('--selenoid_url')
    selenoid_ui_url = request.config.getoption('--selenoid_ui_url')

    browser.config.timeout = project.config.timeout
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.base_url = project.config.base_url

    options = Options()
    options.page_load_strategy = 'eager'

    if run_selenoid:
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-application-cache')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        selenoid_capabilities = {
            "browserName": 'chrome',
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=selenoid_url + "/wd/hub", options=options
        )

        browser.config.driver = driver
    else:
        browser.config.driver_options = options

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, selenoid_ui_url)

    browser.quit()


@pytest.fixture(scope='function')
def clear_cart_when_finished():
    '''
    Очищает корзину - используется только когда происходит логин
    :return:
    '''
    yield

    with allure.step('Очистить корзину и подвердить очищение'):
        if app.cart_page.cart_has_items():
            app.clear_cart()
            app.cart_page.check_is_cart_empty()
