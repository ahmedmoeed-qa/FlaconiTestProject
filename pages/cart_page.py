from pages.base_page import BasePage
from resources.locators import cart_icon, voucher_code, submit_voucher_button, voucher_code_message


class CartPage(BasePage):

    def go_to_cart(self):
        self.wait_for_element_to_be_located(cart_icon)
        self.click(cart_icon)

    def enter_voucher_code(self):
        self.wait_for_element_to_be_located(voucher_code)
        self.enter_text(voucher_code, 'abc123')
        self.click(submit_voucher_button)

    def get_invalid_voucher_code_error_message(self):
        return self.get_element_text(voucher_code_message)
