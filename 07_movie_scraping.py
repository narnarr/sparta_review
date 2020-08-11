import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
params = {
    'sel': 'pnt',
    'date': '20180327'
}
data = requests.get(url, headers=headers, params=params)
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    tag = movie.select_one('td > img')
    if tag is not None:
        rank = movie.select_one('td > img')['alt']
        title = movie.select_one('td.title > div > a').text
        point = movie.select_one('td.point').text
        print(rank, title, point)