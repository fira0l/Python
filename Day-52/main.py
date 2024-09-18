import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

Username = os.environ.get("USERNAME")
Password = os.environ.get("PASSWORD")

URL = "https://www.instagram.com"

driver.get(URL)
time.sleep(30)

username = driver.find_element(By.NAME, "username")
username.send_keys(Username)
password = driver.find_element(By.NAME, "password")
password.send_keys(Password)
password.send_keys(Keys.ENTER)

time.sleep(45)

button = driver.find_element(By.CSS_SELECTOR,"div button")
button.click()

time.sleep(15)





