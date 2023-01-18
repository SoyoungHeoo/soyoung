
  # set {} : value 가 없는 dict
  # 중복 허용 X.
  # list, str, dict 등을 set으로 만들 수 있다. set() 함수로 묶는다.
  # # 중복 없름
  # set - intersection


  # or 또는 union -> set 합치기


a = {1, 2}
b = {2, 3}



  # symantic_difference()
  # issubset()



  # Set Comprehension

  # frozenset() : set은 mutable. 하지만 immutables 형식으로 바꿀 수 있음.



  # Make Bigger Data Structures


marxes = ['Groucho', 'cicno']



 #--------------------------------------------------

 # 함수

def isprime(n):
  '''

  :param n: 정수를 입려받아
  :return:  소수인지 아닌지 판정하여 T,F 반환
  '''
  if n <= 1:
    return False

  for k in range(2, n): # 반복문 횟수 줄이기
      if n % k == 0:
          return False
  else:
    return True

  #  ** 객체지향 설계 원칙
  #  ** 단일 책임 원리 : 하나의 함수는 하나의 역할만 하도록 설계하는 것이 유지보수에 좋다.:::#


print(isprime(43))
start = int(input("input start number: "))
end = int(input("input end number: "))

for i in range(start, end+1):
  if isprime(i):
    print(i, end=' ')

help(isprime)
#
# 가변 매개변수 *args
def calculate_fee(*args):
  '''
  놀이공원 요금 계산 프로그램
  :param args: args
  :return: 지불할 총 금액
  '''
  total = 0
  for age in args:
    if age < 20: # child
      total = total + 3000
    elif age >= 20: # adult
      total = total + 10000
  return total

# print(calculate_fee(20, 20, 25))


# v 0.2 return Dictionary
# 가변 매개변수 *args
def calculate_fee2(*args) -> dict:
  '''
  놀이공원 요금 계산 프로그램
  :param args: ages in list
  :return: {'no_of_people': len(args), 'no_of_adults': adults, 'no_of_kids': kids, 'total_fee': total}
  '''
  total = 0
  adults = 0
  kids = 0
  for age in args:
    if age < 20: # child
      total = total + 3000
      kids += 1
    elif age >= 20: # adult
      total = total + 10000
      adults += 1
  return {'no_of_people': len(args), 'no_of_adults': adults, 'no_of_kids': kids, 'total_fee': total}

print(calculate_fee2(20, 20, 25))

# document string
print(calculate_fee.__doc__)


# 함수의 매개변수로 함수를 전달할 수 있다.
def subtract(n1, n2):
  print(n1 - n2)


# 함수, 매개변수를 매개변수로 받는 함수
def run_function(f, arg1, arg2):
  f(arg1, arg2)

run_function(subtract, 99, 88)
