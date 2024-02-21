from selene import browser


class ProductPage:

    def __init__(self):
        self.checkout = browser.element('.buy.isActive')

    def add_to_cart(self):
        browser.element('.buy').click()

    def go_to_cart(self):
        browser.element('.buy.isActive').click()

    def increase_amount_by(self, amount):
        for _ in range(amount):
            browser.element('[title="Увеличить количество товара"]').click()
