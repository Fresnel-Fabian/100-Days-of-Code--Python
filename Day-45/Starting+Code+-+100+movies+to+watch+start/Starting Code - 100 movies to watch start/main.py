import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")
print(soup.find_all('h3', class_='title'))
names = [name.getText() for name in soup.find_all(name="h3", class_="title")]
names.reverse()
print(names)
with open("file.txt", "w") as file:
    for name in names:
        file.write(name+"\n")
