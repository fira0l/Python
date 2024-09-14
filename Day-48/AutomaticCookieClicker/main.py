from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)
cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
money_is_enough = False
while not money_is_enough:
    cookie.click()
    if money.text == "3,000":
        money_is_enough = True
print(money.text)

