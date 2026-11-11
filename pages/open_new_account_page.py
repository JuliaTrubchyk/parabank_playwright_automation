from pages.base_page import BasePage
from playwright.sync_api import Page

class OpenNewAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.open_account_button = page.get_by_role("button", name="Open New Account")
        self.account_type_dropdown = page.locator("#type")
        self.from_account_dropdown = page.locator("#fromAccountId")
        self.success_heading = page.locator("#openAccountResult h1")
        self.success_message = page.locator("#openAccountResult p").first


    # SAVINGS or CHECKING
    def select_account_type(self, account_type: str):
        self.account_type_dropdown.select_option(label=account_type)

    def select_source_account(self, index: int = 0):
        self.from_account_dropdown.select_option(index=index)

    def submit_open_account(self):
        self.open_account_button.click()