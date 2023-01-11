import requests
from bs4 import BeautifulSoup

url = 'https://www.periodictable.one/elements'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

song_elements = soup.find_all(class_='element')

for song_element in song_elements:
    song = song_element.find('a')
    if song:
        song_name = song.get_text()
    else:
        song_name = "N/A"
    artist =song_element.find(class_='c-nr')
    if artist:
        artist_name = artist.get_text()
    else:
        artist_name = "N/A"
    print(f'{song_name} has an Atomic number of: {artist_name}')
