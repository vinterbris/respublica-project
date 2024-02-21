import pytest
from selene import browser

from respublica_tests.pages.cart_page import CartPage
from utils import attach

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
    #     "browserVersion": '110.0',
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
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
    cart_page = CartPage()

    yield

    if cart_page.cart_has_items():
        cart_page.clear_cart()
        cart_page.check_is_cart_empty()
