from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


# URL = "https://en.wikipedia.org/wiki/Main_page"
#
# driver = webdriver.Chrome(keep_alive=True)
#
# driver.get(URL)
# # article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
# # all_portals = driver.find_element(By.LINK_TEXT, "Nominate an article")/=
# # all_portals.click()
#
# search_button = driver.find_element(By.CLASS_NAME,"mw-ui-icon-wikimedia-search")
# search_button.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
#
#
# # driver.close()


# driver = webdriver.Chrome(keep_alive=True)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
fname.send_keys("Firaol")
fname.send_keys(Keys.TAB)

lname.send_keys("Anbessa")
lname.send_keys(Keys.TAB)

email.send_keys("FiraolAnbessa170@gmail.com")
email.send_keys(Keys.ENTER)

