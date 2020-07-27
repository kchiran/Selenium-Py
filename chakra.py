# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Establish chrome driver and go to report site URL
url = "https://www.oshoworld.com"
driver = webdriver.Chrome("C:/Users/PC 50/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(url)