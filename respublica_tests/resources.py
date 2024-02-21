from respublica_tests.pages.header import Header
from respublica_tests.pages.product_page import ProductPage
from respublica_tests.pages.search_page import SearchPage


def add_item_to_cart(product_name):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()

    header.login_if_not_logged_in()
    header.search(product_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.go_to_cart()
