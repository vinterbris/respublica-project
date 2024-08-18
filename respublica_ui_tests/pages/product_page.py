import time

from selene import browser

from respublica_ui_tests.pages.loading_page import LoadingPage


class ProductPage:

    def __init__(self):
        self._button_increase_amount = browser.element(
            '[title="Увеличить количество товара"]'
        )
        self._button_buy = browser.element('.buy')
        self.checkout = browser.element('.buy.isActive')

    def add_to_cart(self):
        time.sleep(2)
        self._button_buy.click()

    def go_to_cart(self):
        self.checkout.click()
        loading_page = LoadingPage()
        loading_page.wait_until_finished()

    def increase_amount_by(self, amount):
        for _ in range(amount - 1):
            self._button_increase_amount.click()
