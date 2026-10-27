from pages.home_page import HomePage

def test_homepage_opens(home_page: HomePage):
    home_page.open()
    assert home_page.page.url.startswith("http://localhost:8080/parabank/index.htm")