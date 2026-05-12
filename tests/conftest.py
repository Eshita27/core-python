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

@pytest.fixture(scope="module")
def demo_fixture():
    print("\n Creating fixture")
    yield "fixture_data"
    print("\n Destroying fixture")

@pytest.fixture(autouse=True)
def auto_logger():
    print("\n Before every test")
    yield
    print("\n After every test")