from selene import have, be, browser

from respublica_tests.application import app
from respublica_tests.e2e import add_item_to_cart

PRODUCT_NAME = 'Блокнот нелинованный \"Master Classic\" черный A4+'
PRODUCTS = (
    'Блокнот нелинованный \"Master Classic\" черный A4+',
    'Блокнот \"Master Classic\" A4+, 117 листов, в линейку, черный',
    'Блокнот "Classic" Large, 120 листов, пунктир, 13 х 21 см, синий'
)


def test_login():
    app.header.login_initial()
    app.header.open_profile_panel()

    app.header._button_profile.should(have.text('Профиль'))


def test_add_single_item_to_cart(clear_cart_when_finished):
    items = 1
    amount_per_item = 1

    # WHEN
    app.header.login_if_not_logged_in()
    app.header.search(PRODUCT_NAME)
    app.search_page.select_product(PRODUCT_NAME)
    app.product_page.add_to_cart()
    app.product_page.go_to_cart()

    # THEN
    app.cart_page.all_items_counter.should(have.text(f'({items} товар)'))
    app.cart_page.checkbox.should(have.value('true'))
    app.cart_page.item_name.should(have.text(PRODUCT_NAME))
    app.cart_page.item_count.should(have.value(f'{amount_per_item}'))


def test_add_multiple_items_to_cart(clear_cart_when_finished):
    items = 1
    amount_per_item = 4

    # WHEN
    app.header.login_if_not_logged_in()
    app.header.search(PRODUCT_NAME)
    app.search_page.select_product(PRODUCT_NAME)
    app.product_page.add_to_cart()
    app.product_page.increase_amount_by(amount_per_item - 1)
    app.product_page.go_to_cart()

    # THEN
    app.cart_page.all_items_counter.should(have.text(f'({items} товар)'))
    app.cart_page.checkbox.should(have.value('true'))
    app.cart_page.item_name.should(have.text(PRODUCT_NAME))
    app.cart_page.item_count.should(have.value(f'{amount_per_item}'))


def test_add_multiple_different_items_to_cart(clear_cart_when_finished):
    total_amount_of_items = len(PRODUCTS)

    # WHEN
    app.header.login_if_not_logged_in()
    for product in PRODUCTS:
        app.header.search(product)
        app.search_page.select_product(product)
        app.product_page.add_to_cart()
        app.product_page.checkout.wait_until(be.visible)
    app.product_page.go_to_cart()

    # THEN
    app.cart_page.all_items_counter.should(have.text(f'({total_amount_of_items} товара)'))

    list_of_all_checkbox_statuses = ['true' for _ in range(total_amount_of_items)]
    app.cart_page.all_checkboxes.should(have.values(*list_of_all_checkbox_statuses))

    app.cart_page.all_item_names.should(have.texts(*reversed(PRODUCTS)))

    list_of_all_individual_item_amounts = ['1' for _ in range(total_amount_of_items)]
    app.cart_page.all_item_counts.should(have.values(*list_of_all_individual_item_amounts))


def test_delete_item_from_cart():
    # WHEN
    add_item_to_cart(PRODUCT_NAME)
    app.cart_page.remove_first_item()

    # THEN
    app.cart_page.checkbox.should(have.value('false'))
    app.cart_page.total_items.should(have.text('Товары (0)'))


def test_clear_cart():
    # WHEN
    add_item_to_cart(PRODUCT_NAME)
    app.cart_page.clear_cart()

    # THEN
    app.cart_page.empty.should(have.text('В вашей корзине еще нет товаров'))
