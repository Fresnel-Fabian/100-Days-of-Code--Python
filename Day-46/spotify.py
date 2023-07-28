import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

CLIENT_ID = "0fe42660749647469bcd1105bf9d6613"
CLIENT_SECRET = os.environ["client_secret"]
URL = "https://www.billboard.com/charts/hot-100/"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(URL + date)
soup = BeautifulSoup(response.text, "html.parser")
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]
print(song_names)
song_uris = []
year = date.split("-")[0]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
