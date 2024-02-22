from selene import browser, have, be

from respublica_tests.components.header import Header


class CartPage:
    def __init__(self):
        self._confirm_clear_cart = browser.element('.deleted-button')
        self._button_clear_cart = browser.element('.delete-selected')
        self.empty = browser.element('.cart-none-title')
        self.total_items = browser.element('.cart-order-item-title')
        self.all_item_counts = browser.all('.count-input')
        self.all_checkboxes = browser.all('[type=checkbox]')
        self.all_item_names = browser.all('.item-name')
        self.item_count = browser.element('.count-input')
        self.item_name = browser.element('.item-name')
        self.checkbox = browser.element('[type=checkbox]')
        self.all_items_counter = browser.element('.cart-count')

    def clear_cart(self):
        header = Header()

        header.go_to_cart()
        self._button_clear_cart.click()
        self._confirm_clear_cart.click()

    def remove_first_item(self):
        self.checkbox.with_(click_by_js=True).click()

    def check_is_cart_empty(self):
        self.empty.should(have.text('В вашей корзине еще нет товаров'))

    def cart_has_items(self):
        return self.empty.matching(be.absent)
