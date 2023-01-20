# attribute / field

# def __init__ : 객체 생성시 최초로 한번만 동작. 호출할 수 없는 개념.

# 어노테이션?

# 메서드 오버라이딩

# class
import math


class Pokemon:
    def __init__(self, owner, skill): # 객체 생성시 동작. 객체 생성시 매개변수를 받아오게끔 할 수 있다.
        self.owner = owner
        self.skill = skill
        print(f"포켓몬 생성 : ", end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬:', end=' ')
        for s in self.skill:
            print(s, end=' ')
    def attack(self, idx):
        print(f'{self.skill[idx]} 공격 시전!')


class Pikachu(Pokemon): # inheritance
    def __init__(self, owner, *args): # 오버라이딩하지 않으면 부모 클래스의 생성자 함수 자동 동작됨)
        super().__init__(owner, args) # super : 부모클래스 객체.
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skill[idx]}공격 시전!')

class Kobugi(Pokemon): # inheritance
    def __init__(self, owner, *args): # 생성자 오버라이딩. (오버라이딩하지 않으면 부모 클래스의 생성자 함수 자동 동작됨)
        super().__init__(owner, args) # super : 부모클래스의 생성자 실행.
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx): # override : 부모클래스의 함수를 자식클래스에서 재정의의
        print(f'{self.owner}의 {self.name}가 {self.skill[idx]}공격 시전!')

    def swim(self):
        print(f'{self.name} 가 수영을 합니다.') # 자식클래스에서만 사용 가능한 기능.

pi1 = Pikachu('한지우', '번개')
ggo1 = Kobugi('오바람', '고속스핀', '몸통박치기')

ggo1.info()


print('\n\n')
class Animal():
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh'

class Donkey(Animal):
    def says(self):
        return 'Hee-Haw'

class Mule(Horse, Donkey): # 앞쪽 부모 클래스가 더 가까운 부모클래스. 가까운 부모클래스부터 부모의 부모클래스까지 함수를 찾아나간다.
    pass

m1 = Mule()
print(m1.says())


# JAVA는 다중상속을 지원하지 않음
# JAVA에서는 interface 라는 개념을 사용함.
# 다중상속은 유지관리측면에서 문제가 발생할 확률이 높아서 잘 사용되지는 않는다.


# 믹스인
class PrettyMixin():
    def time_print(self):
        import datetime
        print("today : ", datetime.date.today())


    def dump(self):
        import pprint
        pprint.pprint(vars(self)) # 특정 용도로만 사용되도록 import 된 라이브러리.

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = 'ichor'
t.age = 'eldritch'
t.time_print()


# 몇 객체지향 언어들에서는 외부에서 직접 접근할 수 없게 하는 기법을 제공함.
# Public, Private, default

# __ -> getter 또는 property(decorator, getter setter_?)
# property 사용하기
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name # hidden_name 반환

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name # 받아온 이름으로 hidden_name 수정
    name = property(get_name, set_name)

don = Duck("Donald")
print(don.name)

# 클래스 변수 / 클래스 메소드
# 클래스의 전체 구성 요소가 공유하는 변수 / 메소드.

# staticmethod (정적메소드)
# 클래스나 객체에 영향을 미치지 못함. @staticmethod 데커레이터. 매개변수로 self나 cls가 없음.
# 객체생성 없이 클래스 자체에서 접근 가능.

# 다형성(polymorphism) : 클래스에 상관 없이 다른 객체에 같은 동작을 적용시킬 수 있음.
# 로젤리커플?

#
# class Quote():
#     def __init__(self, person, words):
#         self.person = person
#         self.words = words
#
#     def who(self):
#         return self.person
#
#     def says(self):
#         return self.words + '.'
#
# class QuestionQuote(Quote):
#     def says(self):
#         return self.words + '?'
#
# class ExclamationQuote(Quote):
#     def says(self):
#         return self.words + '!'


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다')

class Circle(Shape):
    def __init__(self, x, y, radius): # circle 전용 변수 radius
        super().__init__(x, y)
        self.radius = radius

    def get_area(self): # 부모클래스 함수 오버라이드
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):  # 부모클래스 함수 오버라이드
        return self.width * self.length

    def __repr__(self):
        return f'사각형의 좌표는 x:{r1.x}, y={r1.y}이고 넓이는 {r1.get_area()} 입니다'

    def __add__(self, other):
        # 두 사각형 넓이의 합
        return self.get_area() + other.get_area()


c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(100, 50, 2, 2)

print('rectangle')
print(r1.__add__(r2))

print('\n')

print(f'사각형의 좌표는 x:{r1.x}, y={r1.y}이고 넓이는 {r1.get_area()} 입니다')
print(r1.get_area())
print(c1.get_area())
print(c2.get_area())

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height

    def get_area(self): # get_volume
        # return math.pi * self.radius * self.radius * self.height
        #       (      이 부분은 이미 circle에 있는 값 )
        return super().get_area() * self.height

cy1 = Cylinder(10, 10, 20, 5)
print(f"원기둥의 부피는 :{cy1.get_area()}")


# 연산자 오버로딩 __eq__

#연관관계

    # 상속
    # 매우 강한 결합관계

    # 콤퍼지션 (part of)
    # 한쪽이 망가지면 같이 기능을 잃는 것. 강한 결합관계.

    # 어그리게이션 (has a)
    # 객체들의 관계가 라이프스타일이 다름. 느슨한 결합관계.
