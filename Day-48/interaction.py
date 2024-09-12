from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main-page"

driver = webdriver.Chrome()

driver.get(URL)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "All Portals")
all_portals.click()

# driver.close()
