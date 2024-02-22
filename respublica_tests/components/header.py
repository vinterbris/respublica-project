import os

from selene import browser, be, have


class Header:

    def __init__(self):
        self._cart_item_counter = browser.element('.nr-header__badge')
        self._button_cart = browser.element('[title="Корзина"]')
        self._field_search = browser.element('.nr-header__search-input')
        self._button_profile_panel = browser.element('.nr-avatar')
        self._button_signin = browser.element('.sign-in-button')
        self._field_login_password = browser.element('#sign-in-password')
        self._field_login_name = browser.element('#sign-in-login')
        self._button_authorisation = browser.element('[title=Авторизоваться]')
        self._button_profile = browser.element('[title=Профиль]')

    def login_initial(self):
        browser.open('/')
        self._button_authorisation.with_(timeout=20.0).click()
        self._field_login_name.type(os.getenv('LOGIN'))
        self._field_login_password.type(os.getenv('PASSWORD'))
        self._button_signin.click()

    def login_if_not_logged_in(self):
        if self._button_profile.matching(be.absent):
            self.login_initial()

    def open_profile_panel(self):
        self._button_profile_panel.click()

    def search(self, search_name):
        self._field_search.type(search_name).press_enter()

    def go_to_cart(self):
        self._button_cart.click()

    def check_is_cart_empty(self):
        self._cart_item_counter.should(have.text('0'))
