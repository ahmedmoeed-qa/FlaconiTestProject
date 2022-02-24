from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger("BasePage")

    # Move to the page element and click on it
    def move_to_and_click(self, locator):
        self.wait_for_element_to_be_located(locator)
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        element_click = actions.move_to_element(element).click()
        element_click.perform()

    # Hover to the element
    def hover_to(self, locator):
        self.wait_for_element_to_be_located(locator)
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    # Click on the element
    def click(self, locator):
        self.wait_for_element_to_be_located(locator)
        element = self.driver.find_element(*locator)
        self.logger.info("Tap " + element.text)
        element.click()

    # Wait for element to be located on the page
    def wait_for_element_to_be_located(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    # Enter the text in the input field
    def enter_text(self, locator, text):
        self.wait_for_element_to_be_located(locator)
        self.driver.find_element(*locator).send_keys(text)

    # Scroll to the particular element on the page
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Find Element on the page
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # Find list of elements on the page
    def find_all_elements(self, locator):
        self.wait_for_element_to_be_located(locator)
        return self.driver.find_elements(*locator)

    # Get the visible text of the element
    def get_element_text(self, locator):
        self.wait_for_element_to_be_located(locator)
        element = self.find_element(locator)
        return element.text

    # Get the tag of the element
    def get_element_by_tag(self, tag):
        return self.driver.find_element(By.TAG_NAME, tag)
