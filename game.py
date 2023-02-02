
class Pokemon:
    def __init__(self, owner, skill): # 객체 생성시 동작. 객체 생성시 매개변수를 받아오게끔 할 수 있다.
        self.owner = owner
        self.skill = skill.split('/')
        print(f"포켓몬 생성 : ", end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 사용 가능한 스킬:', end=' ')
        # for s in self.skill:
        #     print(s, end=' ')
        for i in range(len(self.skill)):
            print(f'{i+1} : {self.skill[i]}')

    def attack(self, idx):
        print(f'{self.skill[idx]} 공격 시전!')


class Pikachu(Pokemon): # inheritance
    def __init__(self, owner, skill): # 생성자 오버라이딩. (오버라이딩하지 않으면 부모 클래스의 생성자 함수 자동 동작됨)
        super().__init__(owner, skill) # super : 부모클래스 객체.생성자 함수
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skill[idx]}공격 시전!')

class Kobugi(Pokemon): # inheritance
    def __init__(self, owner, skill): # 생성자 오버라이딩. (오버라이딩하지 않으면 부모 클래스의 생성자 함수 자동 동작됨)
        super().__init__(owner, skill) # super : 부모클래스의 생성자 실행.
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx): # override : 부모클래스의 함수를 자식클래스에서 재정의의
        print(f'{self.owner}의 {self.name}가 {self.skill[idx]}공격 시전!')

    def swim(self):
        print(f'{self.name} 가 수영을 합니다.') # 자식클래스에서만 사용 가능한 기능.


class Pairi(Pokemon): # inheritance
    def __init__(self, owner, skill): # 생성자 오버라이딩. (오버라이딩하지 않으면 부모 클래스의 생성자 함수 자동 동작됨)
        super().__init__(owner, skill) # super : 부모클래스의 생성자 실행.
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx): # override : 부모클래스의 함수를 자식클래스에서 재정의의
        print(f'{self.owner}의 {self.name}가 {self.skill[idx]}공격 시전!')


while True:
    menu = input('1) 포켓몬 생성 2) 정보 조회 3) 공격 4) 프로그램 종료 :')

    if menu == '4':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
        n = input('플레이어 이름 입력 : ')
        s = input('사용 가능 기술 입력(/ 로 구분) : ')
        if pokemon == '1':
            p = Pikachu(n, s)
        elif pokemon == '2':
            p = Kobugi(n, s)
        elif pokemon == '3':
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라주세요')
        p.info()
        info_attack = input('1) 정보조회 2) 공격')
        attack_menu = input('공격번호 선택: ')
        p.attack(int(attack_menu)-1)

    elif menu == '2':
        pass
    elif menu == '3':
        pass
    else:
        print('메뉴에서 골라주세요')