import pytest

from pages.portfolio import portfolio

@pytest.mark.smoke
def test_portfolio_select(page):
    portfolio_obj = portfolio(page)

    portfolio_obj.portfolio_selection()

