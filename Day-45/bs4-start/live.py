from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
# print(soup.select_one(".titleline"))
article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.getText()
article_link = article_tag.get("a")
article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)
articles = soup.find_all(name="span", class_="titleline")
texts = []
links = []
for article_tag in articles:
    print(article_tag)
    text = article_tag.getText()
    texts.append(text)
    href = article_tag.find('a')
    link = href.get('href')
    links.append(link)
votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(texts)
print(links)
print(votes)
print(max(votes))
largest_no = votes.index(max(votes))
print(texts[largest_no])
print(links[largest_no])