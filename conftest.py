import pytest
from playwright.sync_api import sync_playwright

# Setting browser and page as fixtures, to execute on every test.

# This overrides the default 'page' and 'browser' fixtures provided by pytest-playwright.
# Comment them to use the default ones.

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
