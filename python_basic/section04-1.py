# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7,8,9}

print(type(v_tuple))
print(type(v_set))
print(type(v_list))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))

y = 100
y *= 100
print(y)

print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))
print(math.floor(3.874))