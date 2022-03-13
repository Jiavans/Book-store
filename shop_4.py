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
driver.find_element(By.XPATH, "//*[text()='Android Quick Start Guide']").click()
price_old = driver.find_element(By.CSS_SELECTOR, ".price :nth-child(1) .woocommerce-Price-amount")
priceold_get_text = price_old.text
assert priceold_get_text == "₹600.00"
price_new = driver.find_element(By.CSS_SELECTOR, ".price :nth-child(2) .woocommerce-Price-amount")
pricenew_get_text = price_new.text
assert pricenew_get_text == "₹450.00"
wait = WebDriverWait(driver, 10)
imageandro = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single.size-shop_single.wp-post-image")) ).click()
shutwindow = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) ).click()