from selenium import webdriver
from selenium.webdriver.common.by import By


# chrome_driver = "C:\chromedriver-win64\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://www.python.org/")
# price = driver.find_element(By.CLASS_NAME, 'menu')
# print(price.tag_name)

event_time = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_title = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events = {}
# print(event_time)
for index in range(len(event_time)):
    events[index] = {
        "time": event_time[index].text,
        "name": event_title[index].text
    }
print(events)
driver.quit()
