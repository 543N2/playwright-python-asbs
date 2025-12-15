import pytest
from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert page.title() == "Google"
        print("Page title: ", page.title())
        browser.close()
        