import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 영화 정보 DB 생성
client = MongoClient('localhost', 27017)
db = client.dbsparta_review

# 영화 정보 스크래핑
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
params = {
    'sel': 'pnt',
    'date': '20200816'
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

        # 데이터를 DB에 저장
        """
        doc = {'rank': rank,
               'title': title,
               'point': point
               }
        db.movies.insert_one(doc)
        """

# 같은 평점의 영화 제목들 출력
def same_point_movies(target_title):
    target_movie = db.movies.find_one({'title': target_title})
    target_point = target_movie['point']
    same_point = db.movies.find({'point': target_point})
    same_list = []
    for movie in same_point:
        same_list.append(movie['title'])
    return same_list

print(same_point_movies('원더'))


