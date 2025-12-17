from playwright.sync_api import Page
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_home_page import HomePage

# This test is using POM

def test_example(page: Page):
    
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
    
    