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
driver.execute_script("window.scrollBy(0,500);")
driver.find_element(By.CSS_SELECTOR, ".post-182 >.add_to_cart_button").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".post-180 >.add_to_cart_button").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@data-product_id='182']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".woocommerce-message >a").click()
driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(2) .input-text").clear()
driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(2) .input-text").send_keys(3)
driver.find_element(By.XPATH, "//*[@name='update_cart']").click()
quantks = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(2) .quantity .input-text")
quantks_check = quantks.get_attribute("value")
print(quantks_check)
assert quantks_check == "3"
time.sleep(2)
driver.find_element(By.XPATH, "//*[@name='apply_coupon']").click()
wait = WebDriverWait(driver, 10)
textelen = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
driver.quit()
