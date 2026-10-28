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

    def fill_personal_info(self, user_data: dict):
        self.first_name_input.fill(user_data["first_name"])
        self.last_name_input.fill(user_data["last_name"])
        self.address_street_input.fill(user_data["street"])
        self.city_input.fill(user_data["city"])
        self.state_input.fill(user_data["state"])
        self.zip_code_input.fill(user_data["zip_code"])
        self.phone_number_input.fill(user_data["phone"])
        self.ssn_input.fill(user_data["ssn"])

    def fill_credentials(self, user_data: dict):
        self.username_input.fill(user_data["username"])
        self.password_input.fill(user_data["password"])
        self.confirm_password_input.fill(user_data["confirm_password"])

    def submit_registration(self):
        self.register_button.click()

    def register_user(self, user_data: dict):
        self.fill_personal_info(user_data)
        self.fill_credentials(user_data)
        self.submit_registration()


    


