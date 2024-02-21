from selene import browser, have

from respublica.pages.header import Header


class CartPage:
    def __init__(self):
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
        # if browser.element('.delete-selected').matching(have.title('Удалить выбранные')):
        browser.element('.delete-selected').click()
        browser.element('.deleted-button').click()

    def remove_first_item(self):
        browser.element('[type=checkbox]').with_(click_by_js=True).click()

    def check_is_cart_empty(self):
        browser.element('.cart-none-title').should(have.text('В вашей корзине еще нет товаров'))
