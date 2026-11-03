

import pytest

from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    trading_obj = vertical(page)
    trading_obj.trading_options_clicking()

@pytest.mark.smoke
def test_retail_ecommerce(page):
    retail_obj = vertical(page)
    retail_obj.retail_options_selection()

@pytest.mark.smoke
def test_healthcare(page):
    healthcare_obj = vertical(page)
    healthcare_obj.healthcare_options_selection()


