from selenium import webdriver


# chrome_driver = "C:\chromedriver-win64\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://fast.com/")
price = driver.find_element(by='xpath', value='//*[@id="your-speed-message"]')
print(price.tag_name)

# driver.quit()