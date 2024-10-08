import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
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

        time.sleep(15)

        button = self.driver.find_element(By.CSS_SELECTOR, "div button")
        button.click()

        time.sleep(10)

        self.driver.get(f"{URL}/onepiece_staff/")
        time.sleep(10)

    def find_followers(self):
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers')
        followers.click()

        time.sleep(15)
        scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')

        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the
            # modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div button ._acan")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(10)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button/div')
                cancel_button.click()
