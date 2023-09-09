from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://example.com"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    show_dialog=True,
    cache_path="token.txt"))

user_id = spotify.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in the YYYY-MM-DD format:\n")
date = datetime.strptime(date, "%Y-%m-%d").date()

url = "https://www.billboard.com/charts/hot-100/" + str(date)
response = requests.get(url)
response.raise_for_status()
web_page_text = response.text

soup = BeautifulSoup(web_page_text, "html.parser")

songs_list = soup.find_all(name='li', class_='chart-list__element display--flex')
songs = [song.getText() for song in soup.find_all(
    name='span',
    class_='chart-element__information__song text--truncate color--primary'
)]

songs_uri = []
playlist = spotify.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

year = str(date).split('-')[0]

for song in songs:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    print(song)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

spotify.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
