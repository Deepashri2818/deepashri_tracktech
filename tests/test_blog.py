

import pytest

from pages.blog import blogs



@pytest.mark.smoke
def test_Categories(page):
    cat = blogs(page)
    cat.click_Categories()
