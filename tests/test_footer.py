import pytest

from pages.footer import footer

@pytest.mark.smoke
def test_footer_selection(page):
    footer_obj = footer(page)

    footer_obj.footer_selection()

@pytest.mark.smoke
def test_social_media(page):
    footer_obj1 = footer(page)
    footer_obj1.social_media_selection()


