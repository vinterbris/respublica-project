from selene import have, be, browser

from respublica.pages.cart_page import CartPage
from respublica.pages.header import Header
from respublica.pages.product_page import ProductPage
from respublica.pages.search_page import SearchPage


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

    list_of_all_checkbox_statuses = ['true' for _ in range(items)]
    cart_page.all_checkboxes.should(have.values(*list_of_all_checkbox_statuses))

    cart_page.all_item_names.should(have.texts(*reversed(products)))

    list_of_all_individual_item_amounts = ['1' for _ in range(items)]
    cart_page.all_item_counts.should(have.values(*list_of_all_individual_item_amounts))


def test_delete_item_from_cart():
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()
    cart_page = CartPage()

    items = 1
    amount_of_item = 1
    product_name = 'Блокнот нелинованный \"Master Classic\" черный A4+'

    # WHEN
    add_item_to_cart(header, product_name, product_page, search_page)
    cart_page.remove_first_item()

    # THEN
    cart_page.checkbox.should(have.value('false'))
    cart_page.total_items.should(have.text('Товары (0)'))


def add_item_to_cart(header, product_name, product_page, search_page):
    header.login()
    header.search(product_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.go_to_cart()


def test_clear_cart():
    pass


def test_add_to_favorites():
    pass


def test_remove_from_favorites():
    pass
