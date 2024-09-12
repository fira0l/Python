import requests
from datetime import datetime
import pandas as pd
from Ui import main


from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
# timee = main.someFunction()
# print(timee)

date = input("Which time do u want to travel? (YYYY-MM-DD)")


def websitescraper(dateofchoice):
    response = requests.get(url=f"{URL}/{dateofchoice}")
    response.raise_for_status()

    html = response.text

    page_soup = BeautifulSoup(html, "html.parser")
    return page_soup


soup = websitescraper(date)

# print(soup)

def getsong(row_items):
    extracted_songs = []
    for item in row_items:
        rank = item.find(name="span", class_="c-label").getText().strip()
        title = item.find(name="h3", id="title-of-a-story").getText().strip()
        section = item.find(name="ul", class_="lrv-a-unstyle-list")
        artist = section.find(name="span", class_="c-label").getText().strip()
        extracted_songs.append({"title": title,
                                "artist": artist,
                                "rank": rank})
    return extracted_songs


song_item = soup.select(selector="ul.o-chart-results-list-row")
songs = getsong(song_item)

# print(songs)

dataframe = pd.DataFrame(songs, columns=("rank", "artist", "title"))
dataframe.columns = (["Rank", "Artist", "Title"])

# print(dataframe.to_string(index=False))

title = [key["title"] for key in songs]
artist = [key["artist"] for key in songs]
year = date.split("-")[0]
print(title,artist,year)
