import os

from selene import browser, have, be


# os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD')

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


class SearchPage:
    def select_product(self, product_name):
        browser.element(f"[title='{product_name}']").click()

    def add_to_cart(self, products):
        for product_id in products:
            browser.element(f'{product_id} [title="Добавить в корзину"]')


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


class CartPage:
    def __init__(self):
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

    def all_checkboxes(self, i):
        return browser.all('[type=checkbox]')[i]

    def all_item_counts(self, i):
        return browser.element('.count-input')


def test_login():
    header = Header()

    header.login()
    header.open_profile_panel()

    header.profile.should(have.text('Профиль'))


def test_add_single_item_to_cart(clear_cart_when_finished):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()
    cart_page = CartPage()

    items = 1
    amount_of_item = 1
    product_name = 'Блокнот нелинованный \"Master Classic\" черный A4+'

    # WHEN
    header.login()
    header.search(product_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.go_to_cart()

    # THEN
    cart_page.all_items_counter.should(have.text(f'({items} товар)'))
    cart_page.checkbox.should(have.value('true'))
    cart_page.item_name.should(have.text(product_name))
    cart_page.item_count.should(have.value(f'{amount_of_item}'))


def test_add_multiple_items_to_cart(clear_cart_when_finished):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()
    cart_page = CartPage()

    items = 1
    amount_of_item = 4
    product_name = 'Блокнот нелинованный \"Master Classic\" черный A4+'

    # WHEN
    header.login()
    header.search(product_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.increase_amount_by(amount_of_item - 1)
    product_page.go_to_cart()

    # THEN
    cart_page.all_items_counter.should(have.text(f'({items} товар)'))
    cart_page.checkbox.should(have.value('true'))
    cart_page.item_name.should(have.text(product_name))
    cart_page.item_count.should(have.value(f'{amount_of_item}'))


def test_add_multiple_different_items_to_cart(clear_cart_when_finished):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()
    cart_page = CartPage()

    products = (
        'Блокнот нелинованный \"Master Classic\" черный A4+',
        'Блокнот \"Master Classic\" A4+, 117 листов, в линейку, черный',
        'Блокнот Leuchtturm1917 Medium, A5, 125л, без линовки, Лобстер'
    )
    items = len(products)
    amount_of_item = 1

    # WHEN
    header.login()
    for product in products:
        header.search(product)
        search_page.select_product(product)
        product_page.add_to_cart()
        product_page.checkout.wait_until(be.visible)
    product_page.go_to_cart()

    # THEN
    cart_page.all_items_counter.should(have.text(f'({items} товара)'))
    cart_page.checkbox.should(have.value('true'))
    for i in range(items):
        cart_page.all_checkboxes(i).should(have.value('true'))
    cart_page.all_item_names.should(have.texts(*reversed(products)))
    for i in range(items):
        cart_page.all_item_counts(i).should(have.value(f'{amount_of_item}'))


def test_delete_item_from_cart():
    pass


def test_clear_cart():
    pass


def test_add_to_favorites():
    pass


def test_remove_from_favorites():
    pass
