from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import logging


class BasePage:
    UP_TO_SECTION = "ancestor::div[contains(@class, 'tensor_ru-container tensor_ru-section')]"

    def __init__(self, driver, logger):
        self.logger = logger
        self.driver = driver

    def find_element(self, locator, time=2.5):
        try:
            web_element = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))
            self.logger.info(f"Find element by locator {locator}")
            return web_element
        except TimeoutException as _:
            self.logger.error(f"Can't find element by locator {locator}", exc_info=True)
            return None

    def find_elements(self, locator, time=2.5):
        try:
            web_elements = WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator))
            self.logger.info(f"Find elements by locator {locator}")
            return web_elements
        except TimeoutException as _:
            self.logger.error(f"Can't find elements by locator {locator}", exc_info=True)
            return None

    def go_to_site(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Visit url {url}")
        except WebDriverException as _:
            self.logger.error(f"Can't visit url {url}", exc_info=True)

    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
        self.logger.info(f"Switched to window {index}")

    def get_url(self):
        return self.driver.current_url

    def click(self, web_element):
        try:
            self.driver.execute_script("arguments[0].click();", web_element)
            self.logger.info(f"Click on {web_element.id}")
        except WebDriverException as _:
            self.logger.error(f"Can`t click on {web_element.id}", exc_info=True)
