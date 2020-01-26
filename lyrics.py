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
        
    
artist = input("Enter artist Name:")
lyrics(artist)
