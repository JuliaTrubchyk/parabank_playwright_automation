import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def register_page(page):
    return RegisterPage(page)