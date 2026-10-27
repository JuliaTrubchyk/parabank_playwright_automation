from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.page_title = self.page.get_by_role("heading", name="Signing up is easy!")
        self.first_name_input = self.page.locator('[id="customer.firstName"]')
        self.last_name_input = self.page.locator('[id="customer.lastName"]')
        self.address_street_input = self.page.locator('[id="customer.address.street"]')
        self.city_input = self.page.locator('[id="customer.address.city"]')
        self.state_input = self.page.locator('[id="customer.address.state"]')
        self.zip_code_input = self.page.locator('[id="customer.address.zipCode"]')
        self.phone_number_input = self.page.locator('[id="customer.phoneNumber"]')
        self.ssn_input = self.page.locator('[id="customer.ssn"]')
        self.username_input = self.page.locator('[id="customer.username"]')
        self.password_input = self.page.locator('[id="customer.password"]')
        self.confirm_password_input = self.page.locator("#repeatedPassword")

        self.register_button = self.page.get_by_role("button", name="Register")

    def fill_personal_info(self, first_name: str, last_name: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.address_street_input.fill("123 Main St")
        self.city_input.fill("Anytown")
        self.state_input.fill("CA")
        self.zip_code_input.fill("12345")
        self.phone_number_input.fill("123-456-7890")
        self.ssn_input.fill("123-45-6789")

    def fill_credentials(self, username: str, password: str, confirm_password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)

    def submit_registration(self):
        self.register_button.click()

    def register_user(self, first_name: str, last_name: str, username: str, password: str, confirm_password: str):
        self.fill_personal_info(first_name, last_name)
        self.fill_credentials(username,password, confirm_password)
        self.submit_registration()


    


