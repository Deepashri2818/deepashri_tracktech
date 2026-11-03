import pytest

from pages.contactus import contactus


@pytest.mark.smoke
def test_contactus(page):
    contactus_obj = contactus(page)
    contactus_obj.fill_contact_us_form("Swati", "swatisuman170@gmail.com", "Company", "757123213")



