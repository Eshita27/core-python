def test_one(demo_fixture):
    print("\n Running test one")
def test_two(demo_fixture):
    print("\n Running test two")
def test_env(app_config):
    assert app_config["env"] == "QA"
def test_browser(app_config):
    assert app_config["browser"].lower() == "chrome"