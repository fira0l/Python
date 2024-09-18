import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Username = os.environ.get("USERNAME")
Password = os.environ.get("PASSWORD")
URL = "https://www.instagram.com"


class InstaFollower:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.options)

    def login(self):
        self.driver.get(URL)
        time.sleep(30)

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(Username)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(Password)
        password.send_keys(Keys.ENTER)

        time.sleep(45)

        button = self.driver.find_element(By.CSS_SELECTOR, "div button")
        button.click()

        time.sleep(30)

        notnow = self.driver.find_element(By.XPATH,
                                     '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
                                     '/button[2]')
        notnow.click()

    def find_followers(self):
        pass


    def follow(self):
        pass


