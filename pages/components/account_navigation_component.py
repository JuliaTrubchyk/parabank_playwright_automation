from playwright.sync_api import Page

class AccountNavigationComponent:
    def __init__(self, page: Page):
        self.page = page
        self.logout_link = page.get_by_role("link", name="Log Out")
        self.welcome_message = page.locator("#leftPanel p.smallText")
