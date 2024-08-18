from selene import browser, be

from respublica_ui_tests.components.header import Header
from respublica_ui_tests.pages.cart_page import CartPage
from respublica_ui_tests.pages.loading_page import LoadingPage
from respublica_ui_tests.pages.product_page import ProductPage
from respublica_ui_tests.pages.search_page import SearchPage


class Application:
    def __init__(self):
        self.header = Header()
        self.search_page = SearchPage()
        self.product_page = ProductPage()
        self.cart_page = CartPage()
        self.loading_page = LoadingPage()

    def open(self):
        browser.open('/')

    def add_to_cart(self, product_name):
        app.header.search(product_name)
        app.search_page.select(product_name)
        app.product_page.add_to_cart()
        app.product_page.go_to_cart()

    def clear_cart(self):
        self.header.go_to_cart()
        self.cart_page.button_clear_cart.click()
        self.cart_page.confirm_clear_cart.click()

    @staticmethod
    def get_total_amount_of_items(PRODUCTS):
        return len(PRODUCTS)

    @staticmethod
    def make_list_of_all_checkbox_statuses(total_amount_of_items):
        return ['true' for _ in range(total_amount_of_items)]

    # def make_list_of_all_individual_item_amounts(self, total_amount_of_items):
    #     return ['1' for _ in range(total_amount_of_items)]

    def add_to_cart_all(self, PRODUCTS):
        for product in PRODUCTS:
            app.header.search(product)
            app.search_page.select(product)
            app.product_page.add_to_cart()
            app.product_page.checkout.wait_until(be.visible)


app = Application()
