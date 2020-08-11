import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

records = soup.select('#regularTeamRecordList_table > tr')
for record in records:
    rank = record.select_one('th > strong').text
    team = record.select_one('td > div > span').text
    rate = record.select_one('td:nth-child(7) > strong').text
    print(rank, team, rate)
