




import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    trad = vertical(page)
    trad.click_trading_options()

@pytest.mark.smoke
def test_retailEcommerce(page):
    retail = vertical(page)
    retail.click_retailEcommerce()

@pytest.mark.smoke
def test_Healthcare(page):
    health = vertical(page)
    health.click_Healthcare()

@pytest.mark.smoke
def test_fintech(page):
    fintech = vertical(page)
    fintech.click_fintech()

@pytest.mark.smoke
def test_Custom_App(page):
    Custom_App = vertical(page)
    Custom_App.click_Custom_App()



