def test_browser_name(browser):
    print(f"\n Running test on browser: {browser}")
    assert browser in ["chrome", "firefox", "safari", "edge"]
