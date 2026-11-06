from pages.home_page import HomePage
from playwright.sync_api import expect


def test_login_with_valid_credentials(home_page: HomePage, registered_user):
    home_page.account_navigation.logout_link.click()

    home_page.login_component.login(
        registered_user["username"],
        registered_user["password"]
    )

    expected_name = f"{registered_user['first_name']} {registered_user['last_name']}"

    expect(home_page.account_navigation.welcome_message).to_contain_text(f"Welcome {expected_name}")
    expect(home_page.account_navigation.logout_link).to_be_visible()




        
