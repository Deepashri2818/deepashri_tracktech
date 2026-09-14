import pytest

from pages.contact import contacts

@pytest.mark.smoke
def test_fill_contact_details(page):
    con = contacts(page)
    con.fill_contact_details()

@pytest.mark.smoke
def test_Web_Devlopment(page):
    con = contacts(page)
    con.click_Web_Devlopment()

@pytest.mark.smoke
def test_App_devlopment(page):
    con = contacts(page)
    con.click_App_devlopment()

@pytest.mark.smoke
def test_graphic_design(page):
    con = contacts(page)
    con.click_graphic_design()

@pytest.mark.smoke
def test_UI_UX(page):
    con = contacts(page)
    con.click_UI_UX()

@pytest.mark.smoke
def test_follow_us(page):
    con = contacts(page)
    con.socialmediapageclick()