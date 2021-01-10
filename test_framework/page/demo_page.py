from selenium.webdriver.common.by import By

from test_framework.page.base_page import BasePage


class DemoPage(BasePage):

    _search_button = (By.ID, "home_search")

    def login(self, username, password):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        self.po_run('search', keyword=keyword)
        return self

    def back(self):
        self.po_run('back')
        return self
