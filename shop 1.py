import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.find_element(By.XPATH, "//*[text()='My Account']").click()
driver.find_element(By.ID, "username").send_keys('johnvnvn@gmail.com')
time.sleep(4)
driver.find_element(By.ID, "password").send_keys('9271531Azx')
time.sleep(4)
driver.find_element(By.NAME, "login").click()
driver.find_element(By.ID, "menu-item-40").click()
driver.find_element(By.XPATH, "//*[text()='HTML5 Forms']").click()
element = driver.find_element(By.CSS_SELECTOR, ".product_title.entry-title")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
if element_get_text == "HTML4 Forms":
    print("Текст соответствующий")
else:
    print("Текст другой")