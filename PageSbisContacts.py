from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    TENSOR = (By.XPATH, "//a[@title='tensor.ru']")


class Navigator(BasePage):
    def click_on_tensor(self):
        return self.find_element(Locators.TENSOR).click()
