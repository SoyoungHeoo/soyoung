  # set

  # 셋에서 사용하는 함수들
  # 추가하기  add() , 삭제하기  remove() , 순회하기 for x in set , 멤버십 테스트 in

  # 일반적으로 사용하는 set의 용도
drinks = {
  'martini': {'vodka', 'vermouth'},
  'black russian': {'vodka', 'kahlua'},
  'white russian': {'cream', 'kahlua', 'vodka'},
  'mahattan': {'rye', 'vermouth', 'bitters'},
  'serewdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
  if 'vodka' in contents:
    print(name) # 보드카가 포함된음료 이름 출력

for name, contents in drinks.items():
  if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
    print(name)

  # 콤비네이션과 연산자
  # 셋의 조합 확인하기

# 교집합 &

for name, contents in drinks.items():
  if 'vodka' in contents and not contents & {'vermouth', 'cream'}: # 샛에담긴 재료중 둘중 하나라도 포함될시 교집합이 존재하므로
    print(name)

# 두 음료의 재료 셋을 변수에 저장하기
bruss = drinks['black russian'] # 블랙러시안의 재료(value) 가 저장된다.
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# & 연산자 = intersection() method
print(a & b)
print(a.intersection(b))

# 음료로 돌아가서
print(bruss & wruss) # 두 음료에 공통으로 들어가는 재료

# 합집합 구하기. | 또는 union()
a.union(b)

# 차집합. - 또는 difference()

print(a-b)
print(a.difference(b)) # b에는 없고 오로지 a에만 있는 것

# 대칭차집합 ^ 또는 symmetric_difference()  (한 쪽 집합에만 속하는 것들의 집합. 두 집합의 합집합 - 교집합)
print(a ^ b, a.symmetric_difference(b))

# 부분집합인지 판별하기. <= 또는 issubset() 메소드 사용하여 판별, True or False 반환

# 진부분집합인지 판별하기. < 연산자 사용

# 상위집합인지 판별하기. >= 또는 issuperset() 메소드

# 진상위집합 >

## 모든 집합은 자기자신의 부분집합이자 상위집합이다.

# 셋 컴프리헨션
# 리스트, 딕셔너리 컴프리헨션과 같은 모양.
a_set = {number for number in range(1, 6) if number % 2 == 0}
print(a_set)

# 불변 셋 생성하기 : frozenset(순회 가능한 객체 - ex 리스트, 딕셔너리(키값만 저장됨))
