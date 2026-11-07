from playwright.sync_api import expect
import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
import uuid
import re

pytestmark = pytest.mark.ui_tests

def test_user_register(home_page: HomePage, register_page: RegisterPage):
    home_page.open()
    home_page.register_link.click()
    expect(register_page.page).to_have_url(re.compile(r"http://localhost:8080/parabank/register\.htm"))
    expect(register_page.page_title).to_be_visible()

    user_data = {
        "first_name": "John",
        "last_name": "Smith",
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345",
        "phone": "123-456-7890",
        "ssn": "123-45-6789",
        "username": f"testuser_{uuid.uuid4().hex[:8]}",
        "password": "Test123!",
        "confirm_password": "Test123!"
    }

    register_page.register_user(user_data)
    expect(register_page.success_message).to_be_visible()
    expect(register_page.welcome_heading(user_data['username'])).to_be_visible()

