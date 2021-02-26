# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Reference

import copy
print('EX1-1 -')
print(dir())  # 현재 스코프 안에 있는 속성들을 다 볼 수 있음
print(__name__)

# id vs __eq__(==) 증명
x = {'name': 'Kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))  # 서로 주소가 같다 (얕은 복사)
print('EX2-2 -', x == y)  # 서로 값이 같은지
print('EX2-3 -', x is y)  # id값 같은지 볼때는 is
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)  # 객체가 복사됬고 여러 변수가 하나를 보고있음
# 코딩할때 서로 별개의 객체라고 생각하고 y를 수정하면 x도 같이 수정되므로 주의할 필요가 있음(얕은 복사의 문제점)

print()
print()


z = {'name': 'Kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z)  # id 값은 다름
print('EX2-7 -', x is not z)
print('EX2-7 -', x == z)  # 값은 같음

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple), id(tuple2))  # 값이 같아도 tuple은 불변이기에 서로 다른 객체
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple))  # '=' 기호와 __eq__는 같은것

print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()

# print(id(tl1[2]))
tl1[1] += [110, 120]
# tl1[2] += (110, 120) # 만약 튜플을 건드리지 않으면 id 같음 튜플을 건드린 경우 튜플 재할당(새로 생성)
# 리스트 안에 튜플을 넣어서 사용하는 방법은 좋지 않은 방법 리소스 낭비

print('EX4-8 -', tl1)
print('EX4-9 -', tl2)  # 튜플 재 할당(객체 새로 생성)
print('EX4-10 -', tl3)
# print(id(tl1[2]))

print()
print()

# Deep Copy

# 장바구니


class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -', id(basket1), id(basket2),
      id(basket3))  # 객체를 복사하는것은 id 값이 다 다름
print('EX5-2 -', id(basket1._products), id(basket2._products),
      id(basket3._products))  # 얕은 카피와 깊은 복사의 차이
# 참조 레퍼런스까지 deepcopy

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-3 -', basket2._products)
print('EX5-3 -', basket3._products)

print()
print()

# 함수 매개변수 전달 사용법


def mul(x, y):
    x += y
    return x


x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b)  # a가 변경됨(원본이 수정됨) 가변형 a -> 데이터 변경

c = (10, 100)
d = (5, 10)

print('EX6-2 -', mul(c, d), c, d)  # 불변형 c -> 원본 데이터 변경 안됨


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 X -> 참조 변환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]  # 처음부터 끝까지 복사

# 파이썬 자체적으로 효율성을 위해서 이런경우 같은 객체나옴
print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))  # 얘도 같음

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
# 효율성을 위해서 값이 같은 스트링이나 튜플값은 같은 id값 반환 파이썬이 그렇게 설계됨
