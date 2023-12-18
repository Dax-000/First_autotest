from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    PARTNERS = (By.XPATH, "//div[@id='contacts_clients']//div[@data-qa='items-container']//div[@data-qa='item'][position()>1]")
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

    def get_partners_item_keys(self, count=99):
        items = self.find_elements((Locators.PARTNERS[0], Locators.PARTNERS[1]+f"[position()<{count+1}]"))
        item_keys = {item.get_attribute("item-key") for item in items}
        self.logger.info(f"Got item keys {item_keys}")
        return item_keys

    def change_region(self, region):
        self.click(self.find_element(Locators.REGION))
        region_button = self.find_element((By.XPATH, f"//span[@title='{region}']"))
        region_code = int(region_button.text[:2])
        self.click(region_button)
        return region_code
