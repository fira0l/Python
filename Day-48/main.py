from selenium import webdriver


# chrome_driver = "C:\chromedriver-win64\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/dp/B08KT9XY9Z?ref=MARS_NAV_desktop_luna_cb_otgbundl")
price = driver.find_elements(value="a-price a-text-price a-size-medium apexPriceToPay")
print(price)

driver.quit()