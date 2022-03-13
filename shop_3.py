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
order = driver.find_element(By.NAME, "orderby")
check_element = order.get_attribute('value')
if check_element == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Другая сортировка")
element = driver.find_element(By.NAME, "orderby")
select = Select(element)
select.select_by_value("price-desc")
element2 = driver.find_element(By.NAME, "orderby")
check_element2 = element2.get_attribute('value')
if check_element2 == "price-desc":
    print("Выбрана сортировка по убыванию цены")
else:
    print("Другая сортировка")
