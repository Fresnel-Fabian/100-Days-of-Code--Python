from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("http://web.archive.org/web/20190201181142/http://secure-retreat-92358.herokuapp.com:80/")
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Fresnel")
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Fabian")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("frenelfabian@gmail.com")
# button = driver.find_element(By.XPATH, '/html/body/form/button')
# button.click()
driver.get('https://www.appbrewery.co/p/newsletter')
subscribe = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/a")
subscribe.click()
Name = driver.find_element(By.NAME, "name")
Name.send_keys("Fresnel Fabian")
Email = driver.find_element(By.NAME, "email")
Email.send_keys("frenelfabian@gmail.com")
checkbox = driver.find_element(By.NAME, 'gdpr')
checkbox.click()


while True:
    pass
