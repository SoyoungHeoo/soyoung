# 10.1

class Thing:
    pass

example = Thing()

print(Thing) # 클래스 자체가 출력됨
print(example) # 쿨래스로 인해 만들어진 객체가 주소값과 함께 출력됨


# 10.2
class Thing2:
    letters = 'abc'

print(Thing2.letters) # 객체생성 없이 바로 클래스를 통해 속성에 접근 가능

# 10.3
class Thing3:
    def __init__(self): # 인스턴스의 속성 지정
        self.letters = 'xyz'

example2 = Thing3()
print(example2.letters) # 객체를 생성해야만 xyz 출력 가능

# 10.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    # 10.6
    # def dump(self):
    #     print(self.name, self.symbol, self.number)

    # 10.7
    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'


E1 = Element('Hydrogen','H',1)

# 10.5
el_dict = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1
}

H1 = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])

# 10.6
H2 = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])

print(H2)

# # 10.7
print(H2) #__str__만들기 전 <__main__.Element object at 0x000001EC19538970>
print(H2) #__str__만든 후 'Hydrogen, H, 1'


