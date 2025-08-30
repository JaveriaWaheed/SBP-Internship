from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# setup chromedriver path 
chrome_driver_path = "C:/Users/User/Desktop/chromedriver/chromedriver.exe"

service = Service(executable_path=chrome_driver_path) 

driver = webdriver.Chrome(service=service)

# go to login page
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)

#locate username and password fields
username_field = driver.find_element(By.ID,"username")
password_field = driver.find_element(By.ID,"password")
time.sleep(5)
#enter credentials 
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
time.sleep(10)

#click login 
login_button = driver.find_element(By.CLASS_NAME,"radius")
login_button.click()

time.sleep(10)
driver.quit()