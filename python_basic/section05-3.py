# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈

# if 구문
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q1.items():
    if k == "가을":
        print("1. ", v)

for k in q1.keys():
    if k == '가을':
        print(q1[k])

# 2. 아래 딕셔너리에서 '사과'가 포함되어있는지 확인하세요.

q2 = {"봄": "딸기", "여름": "토마토", "가을": "메론"}

for k, v in q2.items():
    if v == '사과':
        print("2. " ,k, v)
        break
else:
    print("2. ", "사과 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요
# 81 ~ 100 : A학점
# 61 ~ 80 : B학점
# 41 ~ 60 : C 학점
# 21 ~ 40 : D 학점
# 0 ~ 20 : E 학점

a = 77

if a >= 81:
    print('3. ', 'A학점')
elif a >= 61:
    print('3. ', 'B학점')
elif a >= 41:
    print('3. ', 'C학점')
elif a >= 21:
    print('3. ', 'D학점')
else:
    print('3. ', 'E학점')

# 4. 다음 세 개의 숫자 중 가장 큰 수를 출력하세요(if 문 사용) 12 , 6 , 18

a, b, c = 12, 6, 18

max_v = a

if b > a:
    max_v = b
if c > b:
    max_v = c
print('4. ', max_v)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요 (1,3 : 남자, 2,4 : 여자)

s = '891022-2473837'

# if s[7] == '1' or s[7] == '3':
#     print("5. ", "남자")
# else:
#     print("5. ", "여자") 

if int(s[7]) % 2 == 1:
    print("5. ", "남자")
else:
    print("5. ", "여자")


# 반복문
# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요

q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v == "정":
        continue
    else:
        print(v, end=' ')

ex5 = [x for x in q3 if x != '정']
print(ex5, "리스트 컴프리핸선 방법")

# 7. 1 부터 100까지 자연수 중 '홀수'만 한 라인으로 출력하세요

print()
for n in range(1, 101):
    if n % 2 == 1:
        print(n, end=',')

print()
ex7 = [x for x in range(1, 101) if x % 2 != 0]
print(ex7, "리스트 컴프리헨션 방법 2")

# 8. 아래 리스트 항ㅁ목 중에서 5글자 이상의 단어만 출력하세요
q4 = ["nice", "study", "python", "anaconda", "!"]

print()
for v in q4:
    if len(v) >= 5:
        print(v, end=' ')

print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요
q5 = ["A", "b", 'c', "D", 'e', 'F','G', 'h']

for v in q5:
    if v.islower():
        print(v, end=' ')

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력해보세요.
q6 = ["A", "b", "c", "D", "e", 'F', 'G', 'h']
print()
for v in q6:
    if v.islower():
        print(v.upper(), end=" ")
    else:
        print(v.lower(), end=" ")

print()

# 리스트 컴프리헨션 => 리스트를 쉽게 만들어주는 문법
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1, 101)]
print(numbers2)

# 리스트 컴프리핸션 사용방법
#x = [x for x in range(1, 100) if 조건문]