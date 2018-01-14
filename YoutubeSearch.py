import os
import webbrowser

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
query = raw_input('Enter the song to be played: ')
query = query.replace(' ', '+')

# search for the best similar matching video
url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url, headers=headers, timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "lxml")


# fetches the url of the video
mydivs = soup.findAll("script")
mydivs = str(mydivs).split('videoId')

mydivs = mydivs[1].split(',')
link =  mydivs[0].replace('"','').replace(':','')


webbrowser.open('https://www.youtube.com/watch?v=' + link)
