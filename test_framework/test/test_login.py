import pytest

from test_framework.page.demo_page import DemoPage
from test_framework.util import fileutil


class TestLogin:

    data = fileutil.from_file('tet_search.yaml')

    def setup_class(self):
        self.demo = DemoPage()
        self.demo.start()

    def setup(self):
        pass

    def teardown(self):
        self.demo.back()

    def teardown_class(self):
        self.demo.stop()

    @pytest.mark.parametrize('username, password', [
        ('user1', 'password1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        self.demo.login(username, password)
        assert 1 == 1

    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.demo.search(keyword)
