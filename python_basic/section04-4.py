# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary): 순서X, 중복X, 수정0, 삭제0

# Key, Value, (Json) -> MongoDB
# 선언
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4 , 5]}

print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
# 조회할시 안전하게 get 메소드를 활용해서 조회하기
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3,)
print(a)

# key, values
print(a.keys()) # 반환은 리스트 형태이지만 인덱싱으로 접근이 안됨
#print(list(a.keys())[1:3]) # 리스트형태로 변환시켜주면 접근가능
# 또는
temp = list(a.keys())
print(temp[1:3])

print(a.values()) #값만 가져옴
print(list(a.values()))

print(a.items()) # 키, 값 형식으로 가져옴
print(list(a.items()))
print(2 in b)
print('name2' not in a)



# 집합(Sets) (순서X, 중복X)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

# set은 주로 tuple로 변환해서 사용
t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))