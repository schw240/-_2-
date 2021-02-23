# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서0, 중복0, 수정0, 삭제0)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 1000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()
print()


# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.insert(2,7)
print(y)
y.remove(2)
print(y)
# del은 index로 지우고 remove은 값을 찾아서 지움
y.pop()
print(y)
ex = [88, 77]
y.append(ex) #리스트 자체를 추가
#y.extend(ex) #원소를 추가
print(y)

# 삭제: del, remove, pop

# 튜플 (순서0, 중복0, 수정X, 삭제X)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

#del c[2] 튜플은 삭제가 안되므로 에러

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()
print()

# 튜플 함수
z = (5, 2, 1, 3, 4, 1, 1)

print(z)
print(3 in z)
print(z.index(3)) # 값 3이 있는곳의 인덱스를 반환
print(z.count(1)) # 튜플안에 들어있는 값의 갯수를 반환