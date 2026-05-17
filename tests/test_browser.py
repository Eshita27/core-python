import pytest

@pytest.mark.regression
def test_browser_name(browser):
    print(f"\n Running test on browser: {browser}")
    normalized_browser = browser.lower()
    assert normalized_browser in ["chrome", "firefox", "safari", "edge"]
