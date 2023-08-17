from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class DataEntryBot:
    def __init__(self, address, price, link, n):
        self.addresses = address
        self.prices = price
        self.links = link
        self.driver = webdriver.Chrome()
        self.n = n
        self.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdNKNGdUtnzGE81VCiRlvjMvjb-gfDZWS-AtitCf04F4WroFQ'
                        '/viewform')
        for i in range(self.n):
            self.fill(self.addresses[i], self.prices[i], self.links[i])

    def fill(self, address, price, link):
        sleep(2)
        ad = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        ad.send_keys(address)
        pr = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        pr.send_keys(price)
        lk = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        lk.send_keys(link)
        submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()
        sleep(1)
        new_entry = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        new_entry.click()

