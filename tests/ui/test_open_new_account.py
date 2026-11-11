import pytest
from pages.home_page import HomePage
from pages.open_new_account_page import OpenNewAccountPage
from playwright.sync_api import expect

pytestmark = pytest.mark.ui_tests


def test_open_checking_account_with_default_settings(
    home_page: HomePage,
    open_new_account_page: OpenNewAccountPage,
    registered_user
):
    # Navigate to Open New Account
    home_page.account_navigation.open_new_account()

    # Submit the form using default settings
    open_new_account_page.submit_open_account()

    expect(open_new_account_page.success_heading).to_be_visible()
    expect(open_new_account_page.success_message).to_be_visible()

