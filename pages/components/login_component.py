from playwright.sync_api import Page

class LoginComponent:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = self.page.locator("input[name=\"username\"]")
        self.password_input = self.page.locator("input[name=\"password\"]")
        self.login_button = self.page.get_by_role("button", name="Log In")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

