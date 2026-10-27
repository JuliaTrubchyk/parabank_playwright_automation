
from pages.home_page import HomePage

def test_homepage_opens(home_page: HomePage):
    home_page.open()
    assert home_page.get_url() == "http://localhost:8080/parabank/index.htm"