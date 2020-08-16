from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기 - CREATE
# db.friends.insert_one({'name': '조은서', 'age': 23, 'gender': 'F'}) 등

# MongoDB에서 데이터 모두 보기 - READ
all_friends = list(db.friends.find({}))
for friends in all_friends:
    print(friends['name']+'은/는 내 친구!')

same_ages = list(db.friends.find({'age': 14}))
for friends in same_ages:
    print(friends['name']+'은 중학교 1학년 때부터 내 친구!')

# 그 중 특정 키 값을 빼고 보기
user = db.friends.find_one({'name': '안형기'}, {'_id': False})
print(user)

# 값 업데이트하기 - UPDATE
# db.friends.update_many({'gender': 'F'}, {'$set': {'age': 14}})
# db.friends.update_one({'name': '안형기'}, {'$set': {'age': 11}})

# 값 삭제하기 - DELETE
db.friends.delete_one({'age': 15}) # age값이 15인 게 여러개라면 가장 위의 것 하나만 삭제
