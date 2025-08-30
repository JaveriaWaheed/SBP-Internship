from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Correct path to your chromedriver
chrome_driver_path = "C:/Users/User/Desktop/chromedriver/chromedriver.exe"

# Set up the Service object
service = Service(executable_path=chrome_driver_path)

# Create the driver using the service
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait 5 seconds
time.sleep(5)

search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys("ChromeDriver")
time.sleep(10)
search_box.submit()
time.sleep(5) 

# Close the browser
driver.quit()
