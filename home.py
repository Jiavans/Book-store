import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0,600);")
driver.find_element(By.XPATH, "//a[text()='Read more']").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Reviews')]").click()
driver.find_element(By.CLASS_NAME, "star-5").click()
driver.find_element(By.ID, "comment").send_keys("Nice Book!")
driver.find_element(By.ID, "author").send_keys("Ivan")
driver.find_element(By.ID, "email").send_keys("johnvnvn@gmail.com")
driver.find_element(By.ID, "submit").click()