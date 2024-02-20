import os

from selene import browser, have


# os.getenv('LOGIN'), 'Password': os.getenv('PASSWORD')

def login():
    browser.open('/')
    browser.element('[title=Авторизоваться]').click()
    browser.element('#sign-in-login').type(os.getenv('LOGIN'))
    browser.element('#sign-in-password').type(os.getenv('PASSWORD'))
    browser.element('.sign-in-button').click()


def search(search_name):
    browser.element('.nr-header__search-input').type(search_name).press_enter()


def buy():
    browser.element('.buy').click()
    browser.element('.buy.isActive').click()


def test_login():
    login()

    browser.element('.nr-avatar').click()
    browser.element('[title=Профиль]').should(have.text('Профиль'))


def test_add_single_item_to_cart(clear_cart):
    amount_of_items = 1
    login()
    search_name = 'leuchttrum master classic'
    product_name = 'Блокнот нелинованный \"Master Classic\" черный A4+'
    search(search_name)
    browser.element(f"[title='{product_name}']").click()
    browser.element('.about').should(have.text(product_name))
    buy()
    browser.element('.cart-count').should(have.text(f'({amount_of_items} товар)'))
    browser.element('[type=checkbox]').should(have.value('true'))
    browser.element('.item-name').should(have.text(product_name))
    browser.element('.count-input').should(have.value(f'{amount_of_items}'))


def test_add_multiple_items_to_cart():
    pass


def test_add_multiple_different_items_to_cart():
    pass


def test_delete_item_from_cart():
    pass


def test_clear_cart():
    pass


def test_add_to_favorites():
    pass


def test_remove_from_favorites():
    pass
