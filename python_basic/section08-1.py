# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci #pkg 패키지에서 fibonacci 모듈안 Fibonacci 클래스를 가져오겠다는 의미
# 클래스 메소드 형태로 사용하거나 클래스 인스턴스를 생성해서 메소드 사용

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)


# 사용2(클래스)
from pkg.fibonacci import * # 전체를 가져오겠다는 의미이나 권장하지는 않음
# 사용하지 않는것들도 가져와 리소스를 낭비하게 됨

print("ex2 : ", Fibonacci.fib2(600))
print("ex2 : ", Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3 : ", fb.fib2(1600))
print("ex3 : ", fb().title)


# 사용4(함수)
import pkg.calculations as c # 함수로 선언된 모듈의 경우 모듈을 import하면 모듈안 모든 함수를 전부 가져오게 됨

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)

from pkg.calculations import div as d #필요한것만 가져오는것도 가능(이 방법 권장)

print("ex5 : ", int(d(100,10)))

# 사용6
import pkg.prints as p
p.prt1()
p.prt2()

import builtins #파이썬 기본 내장함수
print(dir(builtins)) #기본적인 내장함수 출력됨

