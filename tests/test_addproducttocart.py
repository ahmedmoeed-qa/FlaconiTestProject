import pytest
from pages.home_page import HomePage
from pages.perfume_page import PerfumesPage
from pages.product_detail_page import PerfumeDetailPage
from pages.cart_page import CartPage
from resources.locators import invalid_voucher_code


@pytest.mark.usefixtures("browser")
class TestAddProductToCart:

    def test_add_product(self):
        self.home_page = HomePage(self.driver)
        self.perfumes_page = PerfumesPage(self.driver)
        self.perfumes_detail_page = PerfumeDetailPage(self.driver)
        self.cart_page = CartPage(self.driver)
        # Test
        self.home_page.open_perfumes_page()
        self.perfumes_page.click_on_random_perfume_product()
        self.perfumes_detail_page.add_perfume_to_cart()
        self.cart_page.go_to_cart()
        self.cart_page.enter_voucher_code()

        assert self.cart_page.get_invalid_voucher_code_error_message() == invalid_voucher_code
