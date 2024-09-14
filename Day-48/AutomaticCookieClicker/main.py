from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)
cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
money_is_enough = False

store = driver.find_elements(By.CSS_SELECTOR, "#store div")
items = [item.text for item in store]
item_ids = [item.get_attribute("id") for item in store]

timeout = time.time()+5
five_minute = time.time() + 60*5

while not money_is_enough:
    cookie.click()

    if time.time() > timeout:
        all_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_price:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = item_ids[n]



print(money.text)
print(items)

