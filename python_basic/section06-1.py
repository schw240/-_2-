# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요


# 선언 위치가 중요하다고 하는 이유
# 만약 함수 위에 선언시 에러 발생
# 선언 이후 사용

#hello("Python!")
#hello(7777)


# 예제 1
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)

# 예제 2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

# 예제 3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    #return y1, y2, y3
    return [y1, y2, y3] #리스트 , 튜플등 다양한 형식도 가능
lt = func_mul(1000)
#print(val1, val2, val3)
print(lt, type(lt))
#print(type(val1), type(val2), type(val3))


# 예제 4
# *args, *kwargs

# *args는 가변인자로 매개변수가 몇개가 넘어올지 모를때 사용
def args_function(*args):
    #print(args) #튜플로 반환
    # for t in args:
    #     print(t)

    # 인덱스와 값 동시 반환하는 enumerate
    for i, v in enumerate(args):
        print(i, v)

args_function('kim')
args_function('kim', 'Park')
args_function('kim', 'Park', 'Lee')

# kwargs 키워드 인자 별표(*, asterisk)가 2개라면 딕셔너리로 받음
def kwargs_func(**kwargs):
    #print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1="Kim")
kwargs_func(name1="Kim", name2="Park", name3="Lee")



# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs): #arg1, arg2는 필수적으로 함수를 호출할때 사용, 그 뒤는 가변적으로 사용
    print(arg1, arg2, args, kwargs)

example_mul(10, 20) #가변인자는 필수가 아니여서 없어도 됨
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)



# 예제 5
# 중첩함수(클로저) 함수안의 함수

def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)


# 예제 6(hint 사용법)
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5.0))


# 람다식 예제
# 람다식: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 너무 과도하게 사용시 가독성이 오히려 떨어진다는 단점

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))
print(var_func(10))

lambda_mul_10 = lambda num: num * 10
print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print( x * y * func(10)) #매개변수로 함수도 받을 수 있음

func_final(10, 10, lambda_mul_10)

#print(func_final(10, 10, lambda x : x * 1000))
func_final(10, 10, lambda x : x * 100000)