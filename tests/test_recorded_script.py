import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    expect(page.get_by_role("search")).to_contain_text("Voy a tener suerte")
    page.get_by_role("button", name="Voy a tener suerte").click()
    expect(page.get_by_text("This site is protected by")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
