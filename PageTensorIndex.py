from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    SILA_SECTION = (By.XPATH, f"//p[text()='Сила в людях']//{BasePage.UP_TO_SECTION}")
    SILA_ABOUT = (By.XPATH, "//p[text()='Сила в людях']//following::a[text()='Подробнее']")


class Navigator(BasePage):
    def check_sila_section(self):
        try:
            self.find_element(Locators.SILA_SECTION)
            return True
        except:
            return False

    def click_on_about(self):
        return self.find_element(Locators.SILA_ABOUT).click()