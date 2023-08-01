from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# import email and password using os
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
# initialize webdriver
driver = webdriver.Chrome()

driver.get("http://www.tinder.com")
sleep(2)
# Find login button
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div["
                                             "1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()
sleep(2)
# maximize window
driver.maximize_window()
base_window = driver.window_handles[0]
print(driver.title)
# accept cookies
accept_cookies = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()
# google_login = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div['
#                                              '2]/span/div/div/div/div/iframe')
# google_login.click()
more_option = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
more_option.click()
sleep(2)
fb_login = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div['
                                         '2]/button')
fb_login.click()
sleep(5)
# fb login dialog box
fb_login_window = driver.window_handles[1]
# switch to fb login
driver.switch_to.window(fb_login_window)
print(driver.title)
# enter email and password
fb_email = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
fb_email.send_keys(EMAIL)
fb_password = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
fb_password.send_keys(PASSWORD)
fb_password.send_keys(Keys.ENTER)
# google_login_window = driver.window_handles[1]
# driver.switch_to.window(google_login_window)
# print(driver.title)
# google_email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div['
#                                              '1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
# google_email.send_keys(EMAIL)
# google_email.send_keys(Keys.ENTER)

# switch back to main window
driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
# click location, notification and cookiee buttons
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# loop for 100 times because tinder only allows 100 requests
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
while True:
    pass