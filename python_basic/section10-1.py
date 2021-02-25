# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

#print('Test)
# if True
#     pass
#x => y

# NameError: 참조변수 없음

a = 10
b = 15

# print(c)

# ZeroDivisionError: 0 나누기 에러
#print(10 / 0)

# IndexError: 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
#print(x[3]) # 예외 발생

# KeyError

dic = {'name' : 'Kim', 'Age' : 33, 'City' : 'Seoul'}

#print(dic['hobby']) 키에러 발생
print(dic.get('hobby')) # 딕셔너리에서 키 가져올떄는 이 방법 권장

# AttributeError 속성에러 : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
#print(time.month()) 예외발생

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

#x.remove(10) # 값 10이 없어서 에러
#x.index(10) # 값 10이 없어서 에러

# FileNotFoundError

#f = open('test.txt', 'r') # 예외 발생

# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

#print(x + y) # 예외, 리스트와 튜플은 결합 불가
#print(x + z)
#print(x + list(y)) 형변환을 통해 가능

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩스타일)

# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1
name = ['Kim', 'Lee', 'Park']

# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except ValueError:
#     print("Not found it! - Occurred ValueError!")
# else:
#     print('Ok! else!')

# 예제 2 #어떤 에러가 나올지 모를때는 그냥 except로 처리해도 무방
# try:
#     z = 'Jin'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except:
#     print("Not found it! - Occurred ValueError!")
# else:
#     print('Ok! else!')

# 예제3
# try:
#     z = 'Jin'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z, x+1))
# except:
#     print("Not found it! - Occurred ValueError!")
# else:
#     print('Ok! else!')
# finally:
#     print("finally ok!")

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

# try:
#     print('Try')
# finally:
#     print('Ok Finally!!!!')

# 예제5
# try:
#     z = 'Kim'
#     x = name.index(z)
#     print('{} Found it! in name'.format(z))
#     print(z, x+1)
# except ValueError as l:
#     print(l)
# except IndexError:
#     print("Not found it! - IndexError Error!")
# except Exception: # Exception은 맨 마지막으로 해야함 위로 할 시 맨 위에서 모두 걸러짐
#     print("Not found it! - Occurred Error!")
# else:
#     print('Ok! else!')
# finally:
#     print("finally ok!")

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = ''
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError # 직접 문제를 발생시켜서 예외처리
except ValueError:
    print('문제발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')