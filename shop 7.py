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
driver.execute_script("window.scrollBy(0,300);")
driver.find_element(By.CSS_SELECTOR, ".post-182 >.add_to_cart_button").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name"))).send_keys('Johna')
driver.find_element(By.ID, "billing_last_name").send_keys('Volkona')
driver.find_element(By.ID, "billing_email").send_keys('johnvnvn@gmail.com')
driver.find_element(By.ID, "billing_phone").send_keys('79531525353')
driver.find_element(By.ID, "billing_address_1").send_keys('lenovo')
driver.find_element(By.ID, "billing_city").send_keys('taiwan')
driver.find_element(By.ID, "billing_state").send_keys('wantai')
driver.find_element(By.ID, "billing_postcode").send_keys('1234321')
driver.find_element(By.CLASS_NAME, "select2-chosen").click()
driver.find_element(By.CLASS_NAME, "select2-input").send_keys('Russia')
driver.find_element(By.CLASS_NAME, "select2-match").click()
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
driver.find_element(By.ID, "payment_method_cheque").click()
time.sleep(3)
driver.find_element(By.ID, "place_order").click()
wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method >strong"), "Check Payments"))








