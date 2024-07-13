import pytest
from main import MyClass

@pytest.mark.parametrize("x, y", [(1, 2), (3, 4)])
class TestMyClass:
    def test_add(self, x, y):
        my_class = MyClass(x, y)
        assert my_class.add() == x+y

    def test_sub(self, x, y):
        my_class = MyClass(x, y)
        assert my_class.sub() == y-x
