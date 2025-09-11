from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Fix typo here
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:/Users/User/Desktop/chromedriver/chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
wait = WebDriverWait(driver, 10)

# Login
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Navigate to Recruitment > Vacancies
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Recruitment']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Vacancies']"))).click()

# Optional wait to observe the page before quitting
time.sleep(3)

driver.quit()
