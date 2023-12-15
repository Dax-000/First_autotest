from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    TENSOR = (By.XPATH, "//a[@title='tensor.ru']")


class SbisContacts(BasePage):
    def click_on_tensor(self):
        tensor = self.click(self.find_element(Locators.TENSOR))
        self.switch_window(-1)
        return tensor
