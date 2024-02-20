import os

from selene import browser, have


# os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD')

class Header:

    def login(self):
        browser.open('/')
        browser.element('[title=Авторизоваться]').click()
        browser.element('#sign-in-login').type(os.getenv('LOGIN'))
        browser.element('#sign-in-password').type(os.getenv('PASSWORD'))
        browser.element('.sign-in-button').click()

    def open_profile_panel(self):
        browser.element('.nr-avatar').click()

    def search(self, search_name):
        browser.element('.nr-header__search-input').type(search_name).press_enter()


class SearchPage:
    def select_product(self, product_name):
        browser.element(f"[title='{product_name}']").click()


class ProductPage:

    def add_to_cart(self):
        browser.element('.buy').click()

    def go_to_cart(self):
        browser.element('.buy.isActive').click()

    def increase_amount_by(self, amount):
        for _ in range(amount):
            browser.element('[title="Увеличить количество товара"]').click()


class CartPage:
    def clear_cart(self):
        browser.element('[title=Корзина]').click()
        browser.element('.delete-selected').click()
        browser.element('.deleted-button').click()


def test_login():
    header = Header()

    header.login()
    header.open_profile_panel()

    browser.element('[title=Профиль]').should(have.text('Профиль'))


def test_add_single_item_to_cart(clear_cart_when_finished):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()

    amount_of_items = 1
    search_name = 'leuchttrum master classic'
    product_name = 'Блокнот нелинованный \"Master Classic\" черный A4+'

    # WHEN
    header.login()
    header.search(search_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.go_to_cart()

    # THEN
    browser.element('.cart-count').should(have.text(f'({amount_of_items} товар)'))
    browser.element('[type=checkbox]').should(have.value('true'))
    browser.element('.item-name').should(have.text(product_name))
    browser.element('.count-input').should(have.value(f'{amount_of_items}'))


def test_add_multiple_items_to_cart(clear_cart_when_finished):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()

    amount_of_items = 3
    search_name = 'leuchttrum master classic'
    product_name = 'Блокнот нелинованный \"Master Classic\" черный A4+'

    # WHEN
    header.login()
    header.search(search_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.increase_amount_by(amount_of_items - 1)
    product_page.go_to_cart()

    # THEN
    browser.element('.cart-count').should(have.text(f'({amount_of_items} товар)'))
    browser.element('[type=checkbox]').should(have.value('true'))
    browser.element('.item-name').should(have.text(product_name))
    browser.element('.count-input').should(have.value(f'{amount_of_items}'))


def test_add_multiple_different_items_to_cart(clear_cart_when_finished):
    pass


def test_delete_item_from_cart():
    pass


def test_clear_cart():
    pass


def test_add_to_favorites():
    pass


def test_remove_from_favorites():
    pass
