from selenium import webdriver


# chrome_driver = "C:\chromedriver-win64\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=sr_1_1?dib=eyJ2IjoiMSJ9.lTUWuLpdsGirrUITOoJeYI8El8vkTS4dSbMbAhSM0nSKAOYMJJhunBr6WhqvXg0qYpWnvRFoboq_L96rXXzLXsKsGz2Lzlkrm03S5NsO110BVZLh2hT4DGD7W3cFrm1KCT_UQMxWxzPkuuVRly10Itwc1MTbQCyLU3Et4BwvevfN4EFbCtRRT-aRU81WjeIbta_LDEOA80lvBMhkSgR5GvlnasReyVhJW-qx9DDD8jk.9pcabvRLvygrkWdK7b4ry1cbxsVvloPRxzmo6BOxcME&dib_tag=se&keywords=instant+pot&qid=1725909477&sr=8-1")
price = driver.find_element(by="class_name", value="a-price")
print(price)

# driver.quit()