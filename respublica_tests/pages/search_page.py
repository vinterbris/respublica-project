from selene import browser

from respublica_tests.pages.loading_page import LoadingPage


class SearchPage:
    def select_product(self, product_name):
        browser.element(f"[title='{product_name}']").click()
        loading_page = LoadingPage()
        loading_page.wait_until_finished()

    def add_to_cart(self, products):
        for product_id in products:
            browser.element(f'{product_id} [title="Добавить в корзину"]')
