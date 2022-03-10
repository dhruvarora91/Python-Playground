import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

date = input(
    "Which year do you want to travel to? Type the date in the format YYYY-MM-DD: "
)

URL = f"https://www.billboard.com/charts/hot-100/{date}"

year = date.split("-")[0]

REDIRECT_URL = "http://example.com"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

songs = [
    song.get_text().replace("\n", "")
    for song in soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path=".cache",
    )
)
user_id = sp.current_user()["id"]

song_uris = []

for song in songs:
    result = sp.search(q=f"track: {song} year: {year}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
