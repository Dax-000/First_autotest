from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    UP_TO_SECTION = "ancestor::div[contains(@class, 'tensor_ru-container tensor_ru-section')]"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=2.5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=2.5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url):
        return self.driver.get(url)
