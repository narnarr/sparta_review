import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta_review

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N'
data = requests.get(url, headers = headers)

soup = BeautifulSoup(data.text, 'html.parser')
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    updown = song.select_one('td.number > span.rank')
    updown.extract()

    rank = song.select_one('td.number').text.strip()
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    singer = song.select_one('td.info > a.artist.ellipsis').text
    pro_singer = singer.replace('(', '').replace(')', '')

    doc = {'rank': rank,
           'title': title,
           'singer': pro_singer
           }

    db.genie.insert_one(doc)
