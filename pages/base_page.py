from playwright.sync_api import Page
# A Page is a Playwright object representing a browser tab. It provides methods such as goto(), locator(), and get_by_role()
from pages.components.login_component import LoginComponent
from pages.components.account_navigation_component import AccountNavigationComponent

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_component = LoginComponent(page)
        self.account_navigation = AccountNavigationComponent(page)
        self.register_link = self.page.get_by_role("link", name="Register")

    def get_url(self) -> str:
        return self.page.url