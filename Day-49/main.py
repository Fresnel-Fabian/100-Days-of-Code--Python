import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

ACCOUNT_EMAIL = "frenelfabian@gmail.com"
ACCOUNT_PASSWORD = os.environ["linkedin_password"]
PHONE = "9072622722"

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3604941388&f_AL=true&f_WT=2&keywords=python"
           "%20developer&refresh=true")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
sleep(5)
username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)
sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-containter--clickable")
print(all_listings)
# Get every job listings
for listing in all_listings:
    print("called")
    listing.click()
    sleep(2)
    # Try to find the apply button. If can't find then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        sleep(5)

        # if phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # if the submit button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CSS_SELECTOR, "artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window
        sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting application, then
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
sleep(5)
driver.quit()

while True:
    pass
