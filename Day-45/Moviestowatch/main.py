import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

empire_html = response.text

# print(empire_html)

soup = BeautifulSoup(empire_html,"html.parser")

movie_list = ""

title_header = soup.select(selector="div.listicle_listicle__item__CJna4 h3")
for title in title_header:
    moviestowatch = title.getText()
    movie_list = movie_list + "\n" + moviestowatch

with open("Moviestowatch.txt", mode="w") as file:
    file.write(movie_list)

# print(movie_list.reverse())

