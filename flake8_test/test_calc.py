from calc import add, subtract, multiply, divide
import pytest
def test_add():
    assert add(2, 3) == 5
def test_add_positive():
    assert add(10, 5) == 15


def test_add_negative():
    assert add(-2, -3) == -5
def test_subtract():
    assert subtract(10, 3) == 7
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0

def test_divide__by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0) == 2
