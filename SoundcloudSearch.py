import os
import webbrowser

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
query = raw_input('Enter the song to be played: ')
query = query.replace(' ', '+')

# search for the best similar matching video
url = 'https://soundcloud.com/search?q=' + query
print url
source_code = requests.get(url, headers=headers, timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "lxml")


# fetches the url of the video
mydivs = soup.findAll("ul")[1]
mydivs = soup.findAll("li")
mydivs = soup.findAll("h2")[0]
mydivs = str(mydivs).split('"')
link = mydivs[1]

webbrowser.open('https://soundcloud.com' + link)




