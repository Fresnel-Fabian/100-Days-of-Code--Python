from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollowers:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        

    def login(self, USERNAME, PASSWORD):
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(2)
        save_login = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_dZ"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
        save_login.click()
        sleep(2)
        notification_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_j0"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notification_button.click()

    
    def find_followers(self, SIMILAR_ACCOUNT):
        sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_lF"]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
        followers.click()

        sleep(5)
        modal = self.driver.find_element(By.XPATH, '')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in all:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()