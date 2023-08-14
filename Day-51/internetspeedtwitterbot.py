from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = "5"
        self.up = "5"

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

    def tweet_at_provider(self, EMAIL, PASSWORD, USERNAME, PROMISED_DOWN, PROMISED_UP):
        self.driver.get("https://twitter.com/login")
        sleep(4)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/'
                                         'div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(10)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div'
                                            '/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)
        sleep(10)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(10)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        self.driver.quit()

