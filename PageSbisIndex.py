from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    CONTACTS = (By.LINK_TEXT, "Контакты")
    DOWNLOAD = (By.LINK_TEXT, "Скачать СБИС")


class SbisIndex(BasePage):
    def click_on_contacts(self):
        self.click(self.find_element(Locators.CONTACTS))

    def click_on_download_page(self):
        self.click(self.find_element(Locators.DOWNLOAD))
