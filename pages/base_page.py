from playwright.sync_api import Page
# A Page is a Playwright object representing a browser tab. It provides methods such as goto(), locator(), and get_by_role()

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_url(self) -> str:
        return self.page.url