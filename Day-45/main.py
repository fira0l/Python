from bs4 import BeautifulSoup
import lxml

with open("website.html", mode="r") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.p)
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h3", class_="heading")
print(heading.get("class"))
