from src.basics.calculator import add,subtract

def test_add():
    assert add(4,7) == 11

def test_subtract():
    assert subtract(9,2) == 7

def test_add_negative_numbers():
    assert add(-4,-2) == -6