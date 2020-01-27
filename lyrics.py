import os
import requests
from bs4 import BeautifulSoup

def lyrics(artist_name):
    directory = artist_name
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    url = f'https://www.metrolyrics.com/{artist_name}-lyrics.html'
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        '''Get the link to every lyrics page '''
        links = soup.find_all('a', class_="title hasvidtable")
        for link in links:
            lyrics_url = link.get('href')
            temp_name = lyrics_url.split('/')[-1].replace(f'-{artist_name}.html','') + '.txt'
            file_name = os.path.join(parent_dir, f'{directory}/{temp_name}')
            lyrics_page = requests.get(lyrics_url)
            soup1 = BeautifulSoup(lyrics_page.text, 'html.parser')

            with open (file_name, 'a') as f:
                for i in soup1.find_all('p', class_='verse'):
                    f.write(i.get_text())
 
    
artist = input("Enter artist Name:")
lyrics(artist)
