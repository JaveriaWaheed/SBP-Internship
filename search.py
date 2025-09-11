from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to chromedriver
chrome_driver_path = "C:/Users/User/Desktop/chromedriver/chromedriver.exe"

# Setup service
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open DuckDuckGo
driver.get("https://www.duckduckgo.com")
time.sleep(2)

# Find search box and enter query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")
search_box.send_keys(Keys.RETURN)

# Wait for results
time.sleep(3)

# Print page title and URL
print("Page Title:", driver.title)
print("URL:", driver.current_url)

# Wait before quitting
time.sleep(5)
driver.quit()
