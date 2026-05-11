from src.basics.list_utils import get_even_numbers

def test_get_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    result = get_even_numbers(numbers)

    assert result == [2, 4, 6]