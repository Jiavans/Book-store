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
driver.find_element(By.CSS_SELECTOR, ".post-182 >.add_to_cart_button").click()
time.sleep(4)
amount = driver.find_element(By.CLASS_NAME, "cartcontents")
amount_check = amount.text
assert amount_check == "1 Item"
price = driver.find_element(By.CLASS_NAME, "amount")
price_check = price.text
assert price_check == '₹180.00'
driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
wait = WebDriverWait(driver, 10)
subtot = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "180.00"))
totot = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "189.00"))
time.sleep(2)
driver.quit()