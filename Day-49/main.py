import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)


JOB_URL = ("https://www.linkedin.com/jobs/search/?currentJobId=4022478261&distance=25&f_AL=true&geoId=100212432&keywords"
           "=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")
URL = "https://www.linkedin.com/"
PHONE = "+251940239847"

ACCOUNT_EMAIL = os.environ.get("USER_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("USER_PASS")

driver.get(URL)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(20)

driver.get(JOB_URL)


jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")


# store current window (browser tab) id, that will help us in final step, wait for that.
main_window_id = driver.current_window_handle


for job in jobs_list:
    # click on single job from jobs list using loop
    job.click()
    time.sleep(2)


#   created exception handling, because in some cases if any element isn't available, still our code will run perfectly
    try:
        # click on easy apply button
        easy_apply_click = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button').click()
        time.sleep(5)
        # locate sumbit button element
        submit_button = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button .artdeco-button__text")
        # if submit button is available in page only than fill the form, otherwise it has multi steps to fill form.
        if submit_button.text == 'Submit application':
            add_number = driver.find_element(By.CSS_SELECTOR, '.fb-single-line-text input')
            # check if the text field is empty, only then enter your number
            if add_number.get_attribute("value") == "":
                add_number.send_keys(PHONE)
            submit_button.click()
            print('Applied')
            time.sleep(5)
            # I used another exception block because b/w the two upcoming situations only one occurs at a time,
            #                                                                                       it is unpredictable.
            try:
                # after submitting form click cross to close the confirmation banner (either this will occur)
                click_cross = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss svg').click()
            except NoSuchElementException:
                # after submission, sometimes there comes another pop up so we need to close that as well on
                #                                                               left-hand side (or this will occur)
                click_dismiss = driver.find_element(By.CSS_SELECTOR, '.artdeco-toast-item__dismiss svg').click()
        else:
            # in-case the submit button isn't available go back to the main menu using below steps
            back_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss').click()
            time.sleep(2)
            discard_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar--confirm-'
                                                                  'dialog span').click()

    # this is the main step of this project, that will make our project work properly even after errors.
    except NoSuchElementException:
        pass

    finally:
        time.sleep(2)
        # this will create list of all opened browser tab id's
        all_windows = driver.window_handles
        # this will close all tabs except the one which we want, that is jobs main page tab will remain open
        for tab in all_windows:
            if tab != main_window_id:
                driver.switch_to.window(tab)
                driver.close()
        # if we clicked on apply that will take us to another window, so this step will help us to redirect
        #                                                                                         to original main page
        driver.switch_to.window(main_window_id)
        time.sleep(3)

# driver.get(JOB_URL)
# time.sleep(15)
# easyapply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
# easyapply.click()
#
# time.sleep(30)
# mobileNumber = driver.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-app"
#                                                     "lyformcommon-easyApplyFormElement-4022478261-4243406098594063401-"
#                                                     "phoneNumber-nationalNumber")
# mobileNumber.send_keys("+251940239847")
# mobileNumber.send_keys(Keys.TAB)
#
# email = driver.find_element(By.CSS_SELECTOR, "#text-entity-list-form-component-formElement-urn-li-jobs-applyform"
#                                              "common-easyApplyFormElement-4022478261-3571792469076367172-multipleChoice")
# email.send_keys(Keys.TAB)
#
#
# next_link = driver.find_element(By.CSS_SELECTOR, "footer button")
# next_link.click()
# time.sleep(10)
# reviewButton = driver.find_elements(By.CSS_SELECTOR, "footer button")
# review = reviewButton[1]
# review.click()
# time.sleep(10)
#
# submit = driver.find_elements(By.CSS_SELECTOR, "footer div")
# submitt = submit[2]
# submitt.click()
# submitt.send_keys(Keys.ENTER)



