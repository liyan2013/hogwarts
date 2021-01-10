from test_framework.log import log
from test_framework.page.base_page import BasePage


class CommonPage(BasePage):

    def __getattr__(self, item):
        log.debug(f'__get_attr__{item}')
        self._method_name = item
        return self._po_method

    # 定义通用方法
    def _po_method(self, **kwargs):
        log.debug(f'_po_method {kwargs}')
        self.po_run(self._method_name, **kwargs)

    def login_by_password(self, username, password):
        self.po_run('login_by_password', username=username, password=password)
