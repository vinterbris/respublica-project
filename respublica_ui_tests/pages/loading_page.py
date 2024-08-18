from selene import browser, be


class LoadingPage:
    def wait_until_finished(self):
        browser.element('loading-page').matching(be.absent)
