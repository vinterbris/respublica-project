import allure
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import project
from respublica_ui_tests.application import app
from respublica_ui_tests.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    selenoid = project.config.selenoid
    browser_version = project.config.browser_version
    selenoid_url = project.config.selenoid_url + '/wd/hub'
    selenoid_ui_url = project.config.selenoid_ui_url

    browser.config.timeout = project.config.timeout
    browser.config.window_width = project.config.window_width
    browser.config.window_height = project.config.window_height
    browser.config.base_url = project.config.base_url

    options = Options()
    options.page_load_strategy = 'eager'

    if selenoid:
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

        driver = webdriver.Remote(command_executor=selenoid_url, options=options)

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
