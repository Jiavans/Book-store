import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.find_element(By.ID, "menu-item-40").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".cat-item.cat-item-19 :nth-child(1)").click()
items_count = driver.find_elements(By.CLASS_NAME, "product")
if len(items_count) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))