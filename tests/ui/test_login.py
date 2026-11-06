from pages.home_page import HomePage
from playwright.sync_api import expect

# Positive test case for login with valid credentials
def test_login_with_valid_credentials(home_page: HomePage, registered_user):
    home_page.account_navigation.logout_link.click()

    home_page.login_component.login(
        registered_user["username"],
        registered_user["password"]
    )

    expected_name = f"{registered_user['first_name']} {registered_user['last_name']}"

    expect(home_page.account_navigation.welcome_message).to_contain_text(f"Welcome {expected_name}")
    expect(home_page.account_navigation.logout_link).to_be_visible()


# Negative test case for login with invalid credentials
def test_login_with_invalid_password(home_page: HomePage, registered_user):
    home_page.account_navigation.logout_link.click()

    home_page.login_component.login(
        registered_user["username"],
        "invalid_password"
    )
        
    expect(home_page.login_component.error_message).to_contain_text("The username and password could not be verified.")
    expect(home_page.account_navigation.logout_link).to_be_hidden()

def test_login_with_invalid_username(home_page: HomePage, registered_user):
    home_page.account_navigation.logout_link.click()

    home_page.login_component.login(
        "invalid_username",
        registered_user["password"]
    )

    expect(home_page.login_component.error_message).to_contain_text("The username and password could not be verified.")
    expect(home_page.account_navigation.logout_link).to_be_hidden()

def test_login_with_empty_fields(home_page: HomePage):
    home_page.account_navigation.logout_link.click()

    home_page.login_component.login("", "")
    expect(home_page.login_component.error_message).to_contain_text("Please enter a username and password.")
    expect(home_page.account_navigation.logout_link).to_be_hidden()

