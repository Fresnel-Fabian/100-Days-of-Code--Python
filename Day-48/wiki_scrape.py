from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

print(driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text)
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
all_portals = driver.find_element(By.LINK_TEXT, 'Talk')
# all_portals.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# search_button = driver.find_element(By.LINK_TEXT, 'Search')
# search_button.click()
while True:
    pass
