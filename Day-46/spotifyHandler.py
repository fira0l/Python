import spotipy
import os
from main import *

from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= os.environ.get("USER_ID"),
    client_secret=os.environ.get("USER_SECRET"),
    redirect_uri=os.environ.get("REDIRECT_URI"),
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
song_names = songs
print(song_names)

#
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")