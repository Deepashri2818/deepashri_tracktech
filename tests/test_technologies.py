import pytest
from pages.technologies import technologies

@pytest.mark.smoke
def test_ecom_development(page):
    technologies_obj = technologies(page)

    technologies_obj.ecom_development_selection()

@pytest.mark.smoke
def test_mobile_app_development(page):
    technol_obj = technologies(page)
    technol_obj.mobile_app_selection()


