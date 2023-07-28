from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/fresnel/Development/chromedriver"

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
# print(driver.title)
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link)
bug_link = driver.find_element(By.XPATH, '/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)
upcoming_events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in upcoming_events_dates:
#     print(time.text)
upcoming_events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in upcoming_events_names:
#     print(name.text)
upcoming_events = {time.text: name.text for (time, name) in zip(upcoming_events_dates, upcoming_events_names)}
print(upcoming_events)
events = {}
for n in range(len(upcoming_events_dates)):
    events[n] = {
        "time": upcoming_events_dates[n].text,
        "name": upcoming_events_dates[n].text,
    }
print(events)
event_dict = {n: {
    "time": upcoming_events_dates[n].text,
    "name": upcoming_events_names[n].text,
    }
    for n in range(len(upcoming_events_dates))
}
print(event_dict)
