import pytest
from pages.home_page import HomePage

@pytest.fixture
def home_page(page):
    return HomePage(page)