from BaseApp import BasePage
from selenium.webdriver.common.by import By


def sizes_is_equal(*web_elements):
    return len({tuple(e.size.values()) for e in web_elements}) == 1


class Locators:
    PAbOTAEM_IMAGE_WRAPPERS = (By.XPATH, f"//h2[text()='Работаем']//{BasePage.UP_TO_SECTION}//img/..")


class TensorAbout(BasePage):
    def check_size_equality(self):
        image_wrappers = self.find_elements(Locators.PAbOTAEM_IMAGE_WRAPPERS)
        return sizes_is_equal(*image_wrappers)
