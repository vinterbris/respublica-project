import os

from selene import browser


class Header:

    def __init__(self):
        self.profile = browser.element('[title=Профиль]')

    def login(self):
        browser.open('/')
        browser.element('[title=Авторизоваться]').with_(timeout=20.0).click()
        browser.element('#sign-in-login').type(os.getenv('LOGIN'))
        browser.element('#sign-in-password').type(os.getenv('PASSWORD'))
        browser.element('.sign-in-button').click()

    def open_profile_panel(self):
        browser.element('.nr-avatar').click()

    def search(self, search_name):
        browser.element('.nr-header__search-input').type(search_name).press_enter()

    def go_to_cart(self):
        browser.element('[title="Корзина"]').click()
