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

@pytest.mark.smoke
@pytest.mark.unit
def test_add(a,b,expected):
    assert add(a,b) == expected

@pytest.mark.unit
def test_subtract():
    assert subtract(9,2) == 7

@pytest.mark.regression
def test_add_negative_numbers():
    assert add(-4,-2) == -6

@pytest.mark.integration
def test_divide():
    assert divide(10,2) == 5

@pytest.mark.unit
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)

@pytest.mark.regression
def test_multiply():
    assert multiply(2,3) == 6

@pytest.mark.integration
def test_multiply_by_zero():
        assert multiply(9,0) == 0

@pytest.mark.regression
def test_subtract_using_fixture(sample_numbers):
    a,b = sample_numbers
    assert subtract(a,b) == 5