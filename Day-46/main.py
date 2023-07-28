import requests
from bs4 import BeautifulSoup
import spotify
from spotify.oauth2 import SpotifyOAuth
import os


URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "0fe42660749647469bcd1105bf9d6613"
CLIENT_SECRET = os.environ["client_secret"]
sp = spotify.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com", scope="playlist-modify-private"))

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(URL+date)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)
print(len(song_names))
