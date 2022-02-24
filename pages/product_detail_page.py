from pages.base_page import BasePage
from resources.locators import add_to_cart_button, cart_quick_overview_close_button


class PerfumeDetailPage(BasePage):

    def add_perfume_to_cart(self):
        self.wait_for_element_to_be_located(add_to_cart_button)
        self.click(add_to_cart_button)
        self.wait_for_element_to_be_located(cart_quick_overview_close_button)
        self.click(cart_quick_overview_close_button)
