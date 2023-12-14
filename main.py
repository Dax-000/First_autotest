from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://sbis.ru/")
contacts = driver.find_element(By.LINK_TEXT, "Контакты")
contacts.click()

tensor = driver.find_element(By.XPATH, "//a[@title='tensor.ru']")
assert tensor.get_attribute("href") == "https://tensor.ru/"
tensor.click()
sleep(2.5)

driver.switch_to.window(driver.window_handles[1])
block4_section = driver.find_element(By.XPATH, "//p[text()='Сила в людях']//ancestor::div[contains(@class, 'tensor_ru-container tensor_ru-section')]")
block4_about = driver.find_element(By.XPATH, "//p[text()='Сила в людях']//following::a[text()='Подробнее']")
assert block4_about.get_attribute("href") == "https://tensor.ru/about"
driver.execute_script("arguments[0].click();", block4_about)    # ссылка делала мозг с обычным кликом


driver.close()

