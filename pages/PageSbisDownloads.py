from BaseApp import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Locators:
    TAB_PLUGIN = (By.XPATH, "//div[@name='TabButtons']//div[text()='СБИС Плагин']")
    DOWNLOAD_PLUGIN = (By.XPATH, "//div[contains(@class, 'sbis_ru-DownloadNew-block')]//*[text()='Веб-установщик ']"
                                 "//following::a[starts-with(text(), 'Скачать')]")


class SbisDownloads(BasePage):
    def click_on_tab_plugin(self):
        sleep(2)
        self.click(self.find_element(Locators.TAB_PLUGIN))

    def get_plugin_download_data(self):
        a = self.find_element(Locators.DOWNLOAD_PLUGIN)
        url = a.get_attribute('href')
        MBs = float(a.text.split()[-2])
        return url, MBs
