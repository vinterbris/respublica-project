from selene import browser

from respublica_ui_tests.pages.loading_page import LoadingPage

loading_page = LoadingPage()


class SearchPage:

    def add_to_cart(self, products):
        for product_id in products:
            browser.element(f'{product_id} [title="Добавить в корзину"]')

    def select(self, product_name):
        browser.element(f"[title='{product_name}']").click()
        loading_page.wait_until_finished()
