# 클래스

class Pokemon:

    def __init__(self, name, owner, *args): # 객체 생성시 동작. 객체 생성시 매개변수를 받아오게끔 할 수 있다.
        self.name = name
        self.owner = owner
        self.skill = args
        print(f"포켓몬 {name} 생성됨")

    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for s in self.skill:
            print(s)

# 각각의 객체에는 다른 주소값이 할당돼있다.
p1 = Pokemon('피카츄', '지우', '50만볼트', '번개')
p2 = Pokemon('꼬부기', '오바람', '하이드로펌프')

# print(f'{p1.owner}의 포켓몬은 {p1.name}입니다.') # 직접접근

p1.info()
p2.info() # 멤버함수에 접근하여 동작시키기


# concrete thing / abstract thing
# 구체적 / 추상적

# 강한 결속관계
# 문법적으로 class 생성할 때 class 이름 뒤에 부모 class의 이름을 적는다.

class Pikachu(Pokemon): # inheritance
    pass

pi1 = Pikachu('피카츄', '덴트', '번개')
pi1.info()
