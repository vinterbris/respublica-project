from selene import browser


class SearchPage:

    def add_to_cart(self, products):
        for product_id in products:
            browser.element(f'{product_id} [title="Добавить в корзину"]')
