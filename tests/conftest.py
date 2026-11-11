import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.open_new_account_page import OpenNewAccountPage
import uuid

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def register_page(page):
    return RegisterPage(page)

@pytest.fixture
def registered_user(home_page: HomePage, register_page: RegisterPage):
    home_page.open()
    home_page.register_link.click()
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
    return user_data

@pytest.fixture
def open_new_account_page(page):
    return OpenNewAccountPage(page)