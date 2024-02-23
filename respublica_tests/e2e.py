from respublica_tests.application import app


def add_item_to_cart(product_name):
    app.header.login_if_not_logged_in()
    app.header.search(product_name)
    app.search_page.select_product(product_name)
    app.product_page.add_to_cart()
    app.product_page.go_to_cart()
