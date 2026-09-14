
import pytest

from pages.technology import technologies


@pytest.mark.smoke
def test_eCommerce_Development(page):
    ecom = technologies(page)
    ecom.click_eCommerce_Development()

@pytest.mark.smoke
def test_Mobile_Devlopment(page):
    mobile = technologies(page)
    mobile.click_Mobile_App_Development()

@pytest.mark.smoke
def test_AI(page):
    ai = technologies(page)
    ai.click_AI()



