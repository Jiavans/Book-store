import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.find_element(By.XPATH, "//*[text()='My Account']").click()
driver.find_element(By.ID, "reg_email").send_keys('johnvnvn@gmail.com')
time.sleep(4)
driver.find_element(By.ID, "reg_password").send_keys('9271531Azx')
time.sleep(4)
driver.find_element(By.NAME, "register").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[text()='My Account']").click()
driver.find_element(By.ID, "username").send_keys('johnvnvn@gmail.com')
time.sleep(4)
driver.find_element(By.ID, "password").send_keys('9271531Azx')
time.sleep(4)
driver.find_element(By.NAME, "login").click()