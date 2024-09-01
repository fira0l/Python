from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = soup.find(name="span", class_="titleline")
# print(titles.getText())

links = []
article = []

all_link = soup.select(selector="span.titleline a")
for link in all_link:
    title = link.getText()
    article.append(title)
    single_link = link.get("href")
    links.append(single_link)

print(links)
print(article)
#
# articles = soup.find_all(name="a")
# article_texts = []
# article_link = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_link.append(link)
#
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# print(article_texts)
# print(article_link)
print(article_upvotes)

largest = article_upvotes[0]
indexoflargest = 0

for i in range(0,len(article_upvotes)-1):
    if article_upvotes[i] > largest:
        largest = article_upvotes[i]
        indexoflargest = i

titleoflargest = article[indexoflargest]
linkoflargest  = links[indexoflargest]

print(titleoflargest)
print(linkoflargest)
print(article_upvotes[indexoflargest])








# import lxml
#
# with open("website.html", mode="r") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)

