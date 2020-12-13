import pytest

from pytest01.calculator import Calculator


def setup_module():
    print("Setup Module")


def teardown_module():
    print("Teardown module")


class TestCalc:

    def setup_class(self):
        print("Setup class")

    def teardown_class(self):
        print("Teardown class")

    @pytest.mark.parametrize("a,b,expected",
                             [
                                 (1, 1, 2),
                                 (1.1, 1.2, 2.3),
                                 (-1, -1, -2),
                                 (-1.3, -1.3, -2.6),
                                 (1, -1, 0)
                             ])
    def test_add(self, a, b, expected):
        cal = Calculator()
        print("开始计算")
        actual = cal.add(a, b)
        print("计算结束")
        assert actual == expected

    @pytest.mark.parametrize("a,b,expected",
                             [
                                 (1, 1, 1),
                                 (0, 1, 0),
                                 (-1, 1, -1),
                                 (-1.3, -1.3, 1),
                                 (1, 2, 0.5)
                             ])
    def test_div(self, a, b, expected):
        cal = Calculator()
        print("开始计算")
        actual = cal.div(a, b)
        print("计算结束")
        assert actual == expected