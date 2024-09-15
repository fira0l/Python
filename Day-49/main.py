import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

JOB_URL = "https://www.linkedin.com/jobs/search/?currentJobId=4022478261&distance=25&f_AL=true&geoId=100212432&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"
URL = "https://www.linkedin.com/"

ACCOUNT_EMAIL = os.environ.get("USER_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("USER_PASS")

driver.get(URL)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
