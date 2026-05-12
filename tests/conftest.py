import pytest


@pytest.fixture(scope="module")
def sample_numbers():
    print("\n Setting up sample numbers")
    yield 10, 5
    print("\n Cleaning up sample numbers")

@pytest.fixture()
def students():
    return {
        "Eshita":"A",
        "Rahul":"B",
        "Priya":"A+"
    }