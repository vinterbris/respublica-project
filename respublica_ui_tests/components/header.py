import os
import time

from selene import browser, be, have

import project
from respublica_ui_tests.pages.loading_page import LoadingPage


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
        time.sleep(2)
        self._button_authorisation.click()  # flaky trash that doesn't accept proper explicit waits
        self._field_login_name.type(project.config.login)
        self._field_login_password.type(project.config.password)
        self._button_signin.click()

    def login_if_not_logged_in(self):
        if self._button_profile.matching(be.absent):
            self.login_initial()

    def open_profile_panel(self):
        self._button_profile_panel.click()

    def search(self, search_name):
        self._field_search.type(search_name).press_enter()
        loading_page = LoadingPage()
        loading_page.wait_until_finished()

    def go_to_cart(self):
        self._button_cart.click()
        loading_page = LoadingPage()
        loading_page.wait_until_finished()

    def check_is_cart_empty(self):
        self._cart_item_counter.should(have.text('0'))
