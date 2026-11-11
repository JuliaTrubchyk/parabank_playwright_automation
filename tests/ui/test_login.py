import pytest
from pages.home_page import HomePage
from playwright.sync_api import expect

pytestmark = pytest.mark.ui_tests

# Positive test case for login with valid credentials
def test_login_with_valid_credentials(home_page: HomePage, registered_user):
    home_page.account_navigation.logout()

    home_page.login_component.login(
        registered_user["username"],
        registered_user["password"]
    )

    expected_name = f"{registered_user['first_name']} {registered_user['last_name']}"

    expect(home_page.account_navigation.welcome_message).to_contain_text(f"Welcome {expected_name}")
    expect(home_page.account_navigation.logout_link).to_be_visible()


# Negative test case for login with invalid credentials
@pytest.mark.parametrize(
    "username, password, error_message",
    [
        ("valid", "invalid", "The username and password could not be verified."),
        ("invalid_username", "secret_sauce", "The username and password could not be verified."),
        ("", "", "Please enter a username and password."),
    ],
)
def test_invalid_login(home_page: HomePage, registered_user, username, password, error_message):
    home_page.account_navigation.logout()

    if username == "valid":
        username = registered_user["username"]

    if password == "valid":
        password = registered_user["password"]

    home_page.login_component.login(username, password)
    
    expect(home_page.login_component.error_message).to_contain_text(error_message)
    expect(home_page.account_navigation.logout_link).to_be_hidden()

# Logout
def test_logout(home_page: HomePage, registered_user):
    home_page.account_navigation.logout()
    
    expect(home_page.login_component.login_button).to_be_visible()
    expect(home_page.account_navigation.logout_link).to_be_hidden()




