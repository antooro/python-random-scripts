from bs4 import BeautifulSoup
import requests
import googletrans

url = "https://status.epicgames.com/index.json"
req = requests.get(url)
data = req.json()
translator = googletrans.Translator()
a = translator.translate(data['status']['description'], src='en',dest='es')
print a.text
