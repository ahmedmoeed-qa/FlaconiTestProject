import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures("browser")
class TestStatusOfAllLinks:
    def test_makeup_navigation_sub_links(self):
        self.home_page = HomePage(self.driver)
        # Test
        self.home_page.hover_to_make_up_menu()
        self.home_page.get_all_makeup_links_status_code()
