from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://sbis.ru/")
contacts = driver.find_element(By.LINK_TEXT, "Контакты")
contacts.click()
tensor = driver.find_element(By.XPATH, "//a[@title='tensor.ru']")
tensor.click()

driver.close()

