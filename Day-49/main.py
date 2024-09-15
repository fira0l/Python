import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

JOB_URL = ("https://www.linkedin.com/jobs/search/?currentJobId=4022478261&distance=25&f_AL=true&geoId=100212432&keywords"
           "=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")
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

driver.get(JOB_URL)
time.sleep(15)
easyapply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
easyapply.click()

time.sleep(30)
mobileNumber = driver.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-app"
                                                    "lyformcommon-easyApplyFormElement-4022478261-4243406098594063401-"
                                                    "phoneNumber-nationalNumber")
mobileNumber.send_keys("+251940239847")
mobileNumber.send_keys(Keys.TAB)

email = driver.find_element(By.CSS_SELECTOR, "#text-entity-list-form-component-formElement-urn-li-jobs-applyform"
                                             "common-easyApplyFormElement-4022478261-3571792469076367172-multipleChoice")
email.send_keys(Keys.TAB)


next_link = driver.find_element(By.CSS_SELECTOR, "footer button")
next_link.click()
time.sleep(10)
reviewButton = driver.find_elements(By.CSS_SELECTOR, "footer button")
review = reviewButton[1]
review.click()
time.sleep(10)

submit = driver.find_elements(By.CSS_SELECTOR, "footer div")
submitt = submit[2]
submitt.click()
submitt.send_keys(Keys.ENTER)



