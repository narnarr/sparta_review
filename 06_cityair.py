import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'
data = requests.get(url, headers=headers)
#print(response.status_code) #응답코드 200이면 정상적으로 값 받았다는 것
#print(response.text)
parsed = json.loads(data.text) #데이터 타입 스트링에서 딕셔너리로 변함
#soup = BeautifulSoup(data.text, 'html.parser') 이건 데이터 타입 bs4.BeautifulSoup

gu_info = parsed['RealtimeCityAir']['row']
for gus in gu_info:
    gu_name = gus['MSRSTE_NM']
    gu_mise = gus['PM10']
    print(str(gu_name)+'의 미세먼지 수치는 '+str(gu_mise)+'입니다.')