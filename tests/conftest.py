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

@pytest.fixture()
def db_connection():
    print("\n Connecting to database")
    yield "DB Connection"
    print("\n Closing database connection")

@pytest.fixture()
def user(db_connection):
    print("\n Creating user")
    return {
        "username": "Eshita"
    }

@pytest.fixture(scope="session")
def app_config():
    print("\n Loading app config")
    return {
        "env":"QA",
        "browser":"Chrome"
    }

@pytest.fixture(params=["chrome","firefox","safari","edge"])
def browser(request):
    return request.param