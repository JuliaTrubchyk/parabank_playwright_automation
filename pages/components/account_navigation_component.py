from playwright.sync_api import Page

class AccountNavigationComponent:
    def __init__(self, page: Page):
        self.page = page
        self.logout_link = page.get_by_role("link", name="Log Out")
        self.welcome_message = page.locator("#leftPanel p.smallText")
        self.open_new_account_link = page.get_by_role("link", name="Open New Account")
        self.account_overview_link = page.get_by_role("link", name="Accounts Overview")
        self.transfer_funds_link = page.get_by_role("link", name="Transfer Funds")
        self.bill_pay_link = page.get_by_role("link", name="Bill Pay")
        self.find_transactions_link = page.get_by_role("link", name="Find Transactions")
        self.update_contact_info_link = page.get_by_role("link", name="Update Contact Info")
        self.request_loan_link = page.get_by_role("link", name="Request Loan")

    def logout(self):
        self.logout_link.click()

    def open_new_account(self):
        self.open_new_account_link.click()

