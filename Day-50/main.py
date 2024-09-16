import os

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

USERPHONE = os.environ.get("PHONE")
USERPASS = os.environ.get("PASS")

URL = "https://www.tinder.com/"
driver.get(URL)

time.sleep(15)

login_button = driver.find_element(By.XPATH, '//*[@id="s-1722817178"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                             'div/header/div/div[2]/div[2]/a/div[2]')
login_button.click()

time.sleep(20)

facebooksignin = driver.find_element(By.XPATH, '//*[@id="s843769042"]/div/div/div/div[1]/div/div/div[2]/div[2]'
                                               '/span/div[2]/button/div[2]/div[2]')
facebooksignin.click()
time.sleep(30)

handles = driver.window_handles
fb_window = handles[1]

driver.switch_to.window(fb_window)

email = driver.find_element(By.NAME, "email")
email.send_keys(USERPHONE)
password = driver.find_element(By.NAME, "pass")
password.send_keys(USERPASS)
password.submit()

time.sleep(15)
logginas = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Lm"]/div/div/div/div/div/div/div[1]/div[3]/div/div/'
                                         'div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div')
logginas.click()

