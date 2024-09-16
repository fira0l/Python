from selenium import webdriver
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


URL = "https://www.tinder.com/"
driver.get(URL)

time.sleep(15)

login_button = driver.find_element(By.XPATH, '//*[@id="s-1722817178"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                             'div/header/div/div[2]/div[2]/a/div[2]')
login_button.click()

time.sleep(20)

google_signup = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/span[1]')
google_signup.click()

time.sleep(10)



