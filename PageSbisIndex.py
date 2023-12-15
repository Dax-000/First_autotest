from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    CONTACTS = (By.LINK_TEXT, "Контакты")


class SbisIndex(BasePage):
    def click_on_contacts(self):
        return self.click(self.find_element(Locators.CONTACTS))
