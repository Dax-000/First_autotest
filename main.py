from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://sbis.ru/")
driver.close()
