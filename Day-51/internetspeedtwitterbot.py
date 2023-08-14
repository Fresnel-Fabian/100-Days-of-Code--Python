from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
     self.driver.get('https://fast.com/')
     sleep(40)
     # time.sleep()
     show_more_info_btn = self.driver.find_element(By.ID, 'show-more-details-link')
     show_more_info_btn.click()

     down_speed = self.driver.find_element(By.ID, 'speed-value')
     print(down_speed.text)

     up_speed = self.driver.find_element(By.ID, 'upload-value')
     print(up_speed.text)
     # print(down_speed)

    

i = InternetSpeedTwitterBot()
i.get_internet_speed()
