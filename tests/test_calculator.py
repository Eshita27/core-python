import pytest
from src.basics.calculator import add,subtract,multiply,divide

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (10, 0, 10)
    ]
)

def test_add(a,b,expected):
    assert add(a,b) == expected

def test_subtract():
    assert subtract(9,2) == 7

def test_add_negative_numbers():
    assert add(-4,-2) == -6

def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)

def test_multiply():
    assert multiply(2,3) == 6

def test_multiply_by_zero():
        multiply(9,0)