from bs4 import BeautifulSoup
import lxml

with open("website.html", mode="r") as website:
    content = website.read()

soup = BeautifulSoup(content, 'lxml')
print(soup.title)
