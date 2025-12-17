from playwright.sync_api import expect, Page

# This test is not using POM

def test_example(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("button", name="Upgrade")).to_be_visible()
    page.get_by_role("link", name="Performance").click()
    page.get_by_role("link", name="Dashboard").click()
    