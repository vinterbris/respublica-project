from respublica_tests.pages.cart_page import CartPage
from respublica_tests.components.header import Header
from respublica_tests.pages.product_page import ProductPage
from respublica_tests.pages.search_page import SearchPage


class Application:
    def __init__(self):
        self.header = Header()
        self.search_page = SearchPage()
        self.product_page = ProductPage()
        self.cart_page = CartPage()


app = Application()
