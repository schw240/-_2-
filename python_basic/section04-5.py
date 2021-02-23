# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈

# 1. 아래 문자열의 길이를 구해보세요
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print("1. ", len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요
#    apple;orange;banana;lemon
print("2. ", """apple;orange;banana;lemon""")

# 3. 화면에 * 기호 100개를 표시하세요.
print("3. ", '*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요
print("4. ", int("30"))
print("4. ", float("30"))
print("4. ", complex("30"))
print("4. ", str(30))


# 5. 다음 문자열 "Niceman"에서 "man" 문자열만 추출해보세요

q5 = "Niceman"
q5_idx = q5.index("man") #시작하는 첫번째 인덱스가 담김

print("5. ", q5[q5_idx:q5_idx+3])
print("5. ", q5[4:7])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

q6 = "Strawberry"

print("6. ", q6[::-1])
print("6. ", list(reversed(q6)))

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

q7 = "010-7777-9999"

print("7. ", q7.replace('-',''))
print("7. ", q7[0:3] + q7[4:8] + q7[9:13])

# 정규표현식
import re
print("7. ", re.sub('[^0-9]', '', q7)) #sub는 빼는것으로 q7에서 숫자가 아닌것은 빼겠다는 의미

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. "http://daum.net"

q8 = "http://daum.net"

print("8. ", q8[7:])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

print("9. ", "Niceman".upper())
print("9. ", "Niceman".lower())

# 10. 다음 문자열을 스라이싱을 사용해서 "cde"만 출력하세요. : "abcdefghijklmn"

q10 = "abcdefghijklmn"

print("10. ", q10[2:5])

# 11. 다음 리스트에서 "Apple"항목만 삭제하세요. ["Banana", "Apple", "Orange"]

q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
print("11. ", q11)

# 12. 다음 튜플을 리스트로 변환하세요 : (1,2,3,4)

q12 = (1, 2, 3, 4)

print("12. ", list(q12))

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. <성인 - 100000, 청소년 - 70000, 아동 - 30000>

# q13_dict = {
#     '성인': 100000,
#     '청소년': 70000,
#     '아동': 30000
# }

q13_dict = {}
q13_dict['성인'] = 100000
q13_dict['청소년'] = 70000
q13_dict['아동'] = 30000

print("13. ", q13_dict)

# 14. 13번에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

q13_dict['소아'] = 0

print("14. ", q13_dict)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요

print("15. ", list(q13_dict.keys()))

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요

print("16. ", list(q13_dict.values()))