from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = soup.find(name="span", class_="titleline")
# print(titles.getText())

articles = soup.find_all(name="a")
article_texts = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_link.append(link)

print(article_texts)
print(article_link)









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

