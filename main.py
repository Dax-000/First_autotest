from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


UP_TO_SECTION = "ancestor::div[contains(@class, 'tensor_ru-container tensor_ru-section')]"


def sizes_is_equal(*web_elements):
    return len({tuple(e.size.values()) for e in web_elements}) == 1


driver = webdriver.Chrome()
driver.get("https://sbis.ru/")
contacts = driver.find_element(By.LINK_TEXT, "Контакты")
contacts.click()

tensor = driver.find_element(By.XPATH, "//a[@title='tensor.ru']")
assert tensor.get_attribute("href") == "https://tensor.ru/"
tensor.click()
sleep(2.5)

driver.switch_to.window(driver.window_handles[1])
block4_section = driver.find_element(By.XPATH, f"//p[text()='Сила в людях']//{UP_TO_SECTION}")
block4_about = driver.find_element(By.XPATH, "//p[text()='Сила в людях']//following::a[text()='Подробнее']")
assert block4_about.get_attribute("href") == "https://tensor.ru/about"
driver.execute_script("arguments[0].click();", block4_about)    # ссылка делала мозг с обычным кликом

# Секция "Работаем"
image_wrappers = driver.find_elements(By.XPATH, f"//h2[text()='Работаем']//{UP_TO_SECTION}//img/..")
assert sizes_is_equal(*image_wrappers)

driver.close()
