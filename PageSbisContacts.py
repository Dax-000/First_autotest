from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    TENSOR = (By.XPATH, "//a[@title='tensor.ru']")
    REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")


class SbisContacts(BasePage):
    def click_on_tensor(self):
        tensor = self.click(self.find_element(Locators.TENSOR))
        self.switch_window(-1)
        return tensor

    def get_region(self):
        region = self.find_element(Locators.REGION).text
        self.logger.info(f"Site region: {region}")
        return region
