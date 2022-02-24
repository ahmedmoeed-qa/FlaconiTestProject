from requests import get
from pages.base_page import BasePage
from resources.locators import perfume_menu, makeup_menu, makeup_menu_sub_section_links, link_attribute, anchor_tag


class HomePage(BasePage):

    def open_perfumes_page(self):
        self.move_to_and_click(perfume_menu)

    def hover_to_make_up_menu(self):
        self.hover_to(makeup_menu)

    def get_all_makeup_links_status_code(self):
        sub_menu_category_links = self.find_all_elements(makeup_menu_sub_section_links)

        for link in sub_menu_category_links:
            href = link.get_attribute(link_attribute)
            request = get(href)
            if not request.status_code == 200:
                raise Exception(f'"{href}" not found')
