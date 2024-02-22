from selene import browser


class ProductPage:

    def __init__(self):
        self._button_increase_amount = browser.element('[title="Увеличить количество товара"]')
        self._button_buy = browser.element('.buy')
        self.checkout = browser.element('.buy.isActive')

    def add_to_cart(self):
        self._button_buy.click()

    def go_to_cart(self):
        self.checkout.click()

    def increase_amount_by(self, amount):
        for _ in range(amount):
            self._button_increase_amount.click()
