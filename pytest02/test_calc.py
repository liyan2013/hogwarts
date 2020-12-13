import pytest

from pytest01.calculator import Calculator


class TestCalc:

    cal = Calculator()

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
    def test_01_add(self, a, b, expected, config_test):
        actual = self.cal.add(a, b)
        assert actual == expected

    @pytest.mark.parametrize("a,b,expected",
                             [
                                 (1, 1, 0),
                                 (1.1, 1.2, -0.1),
                                 (-1, 1, -2),
                                 (-1.3, -1.3, 0),
                                 (1, -1, 2)
                             ])
    def test_02_sub(self, a, b, expected, config_test):
        actual = self.cal.sub(a, b)
        assert actual == expected

    @pytest.mark.parametrize("a,b,expected",
                             [
                                 (2, 2, 4),
                                 (1.1, 1.1, 1.21),
                                 (-1, -1, 1),
                                 (-1, 0, 0),
                                 (1, -1, -1)
                             ])
    def test_03_mul(self, a, b, expected, config_test):
        actual = self.cal.mul(a, b)
        assert actual == expected

    @pytest.mark.parametrize("a,b,expected",
                             [
                                 (1, 1, 1),
                                 (0, 1, 0),
                                 (1, 0, 0),
                                 (-1, 1, -1),
                                 (-1.3, -1.3, 1),
                                 (1, 2, 0.5)
                             ])
    def test_04_div(self, a, b, expected, config_test):
        actual = self.cal.div(a, b)
        assert actual == expected
