from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movies_list = [
    movie_name.get_text() for movie_name in soup.find_all(name="h3", class_="title")
]

movies_list.reverse()

with open("movies.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
