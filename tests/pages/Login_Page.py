
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.page = page

    def login(self, username, password,url):
        self.page.goto(url)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


