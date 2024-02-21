from respublica.pages.header import Header
from respublica.pages.product_page import ProductPage
from respublica.pages.search_page import SearchPage


def add_item_to_cart(product_name):
    header = Header()
    search_page = SearchPage()
    product_page = ProductPage()

    header.login()
    header.search(product_name)
    search_page.select_product(product_name)
    product_page.add_to_cart()
    product_page.go_to_cart()
