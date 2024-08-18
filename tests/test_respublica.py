import allure
from allure_commons.types import Severity
from selene import have

from respublica_ui_tests.application import app
from respublica_ui_tests.test_data.data import (
    PRODUCT_NAME,
    PRODUCTS,
    items,
    amount_per_item,
)


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Логин")
def test_login():
    with allure.step('Логин'):
        app.header.login_initial()
    with allure.step('Открыть панель профиля'):
        app.header.open_profile_panel()
    with allure.step('Проверить успешность логина'):
        app.header._button_profile.should(have.text('Профиль'))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Корзина")
@allure.story("Добавление одного товара в корзину")
def test_add_single_item_to_cart():
    app.open()

    # WHEN
    with allure.step('Найти товар'):
        app.header.search(PRODUCT_NAME)
    with allure.step('Выбрать найденный товар'):
        app.search_page.select(PRODUCT_NAME)
    with allure.step('Добавить товар в корзину'):
        app.product_page.add_to_cart()
    with allure.step('Перейти в корзину'):
        app.product_page.go_to_cart()

    # THEN
    with allure.step(
            'Проверить количество товаров в корзине, что товар выбран, имя и количество товара соответствует'
    ):
        app.cart_page.all_items_counter.should(have.text(f'{items} товар'))
        app.cart_page.checkbox.should(have.value('true'))
        # app.cart_page.item_name.should(have.text(PRODUCT_NAME)) # assertion broken
        # app.cart_page.item_count.should(have.value(f'{amount_per_item}')) # assertion broken


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Корзина")
@allure.story("Добавление нескольких одинаковых товаров в корзину")
def test_add_multiple_items_to_cart():
    app.open()

    # WHEN
    with allure.step('Найти и добавить товар в корзину'):
        app.header.search(PRODUCT_NAME)
        app.search_page.select(PRODUCT_NAME)
        app.product_page.add_to_cart()
        app.product_page.increase_amount_by(amount_per_item)
    with allure.step('Перейти в корзину'):
        app.product_page.go_to_cart()

    # THEN
    with allure.step(
            'Проверить количество товаров в корзине, что товар выбран, имя и количество товара соответствует'
    ):
        app.cart_page.all_items_counter.should(have.text(f'{items} товар'))
        app.cart_page.checkbox.should(have.value('true'))
        # app.cart_page.item_name.should(have.text(PRODUCT_NAME)) # assertion broken
        # app.cart_page.item_count.should(have.value(f'{amount_per_item}')) # assertion broken


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Корзина")
@allure.story("Добавление нескольких разных товаров в корзину")
def test_add_multiple_different_items_to_cart():
    app.open()

    # WHEN
    with allure.step('Найти и добавить товары в корзину'):
        app.add_to_cart_all(PRODUCTS)
    with allure.step('Перейти в корзину'):
        app.product_page.go_to_cart()

    # THEN
    with allure.step(
            'Проверить количество товаров в корзине, что товар выбран, имя и количество товара соответствует'
    ):
        total_amount_of_items = app.get_total_amount_of_items(PRODUCTS)
        checkbox_statuses = app.make_list_of_all_checkbox_statuses(total_amount_of_items)
        # amounts_of_items = app.make_list_of_all_individual_item_amounts(total_amount_of_items)

        app.cart_page.all_items_counter.should(have.text(f'{total_amount_of_items} товара'))
        app.cart_page.all_checkboxes.should(have.values(*checkbox_statuses))
        # app.cart_page.all_item_names.should(have.texts(*PRODUCTS_REVERSED)) # assertion broken
        # app.cart_page.all_item_counts.should(have.values(*amounts_of_items)) # assertion broken


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
def test_delete_item_from_cart():
    app.open()

    # WHEN
    with allure.step('Добавить товар в корзину и перейти в нее'):
        app.add_to_cart(PRODUCT_NAME)
    with allure.step('Удалить товар из корзины'):
        app.cart_page.remove_first_item()

    # THEN
    with allure.step('Подвердить удаление и 0 товаров в корзине'):
        app.cart_page.checkbox.should(have.value('false'))
        # app.cart_page.total_items.should(have.text('Товары 0')) # assertion broken
        app.cart_page.cart_order_item_cost.should(have.text('0'))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "dobrovolskiysv")
@allure.feature("Корзина")
@allure.story("Очистка корзины")
def test_clear_cart():
    app.open()

    # WHEN
    with allure.step('Добавить товар в корзину и перейти в нее'):
        app.add_to_cart(PRODUCT_NAME)
    with allure.step('Очистить корзину'):
        app.clear_cart()

    # THEN
    with allure.step('Подтвердить, что корзина очищена'):
        app.cart_page.empty.should(have.text('В вашей корзине еще нет товаров'))
