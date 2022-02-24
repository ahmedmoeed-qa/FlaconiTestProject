import random
from pages.base_page import BasePage
from resources.locators import list_of_products


class PerfumesPage(BasePage):

    def click_on_random_perfume_product(self):
        elements = self.find_all_elements(list_of_products)
        element = elements[random.randint(0, len(elements) - 1)]
        self.scroll_to_element(element)
        element.click()
