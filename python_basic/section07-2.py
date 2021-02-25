# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능
# 유지보수와 코드의 길이가 줄어든다는 장점

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show()) #부모것을 사용하고 싶을때는 super() 메소드 사용하기
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) #Super
print(model1.type) #Super
print(model1.car_name) #Sub
print(model1.show()) #Super
print(model1.show_model()) #Sub
print(model1.__dict__)

# Method overriding(오버라이딩) 부모의 함수를 상속받아서 자식에 맞게 변경
model2 = BenzCar("220d", "suv", 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritance Info 상속관계를 알아보고싶을때는 mro함수 사용 (왼쪽에서 오른쪽으로 보기)
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
#다중 상속은 가능하지만 되도록이면 사용하지 말기

