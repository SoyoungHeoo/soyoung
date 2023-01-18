
# closure
# closure 사용시 리턴값으로 함수를 받을 수 있다.
# closure 의 내부함수는, 외부함수로부터 생성된 변수값을 변경하고 저장할 수 있다.

def calculate():
  x = 1
  y = 2
  temp = 0
  def add_sub(n): # 내부함수. n을 계속
    nonlocal temp # 외부에 있는 변수를 변경할 수 있음.
    temp = temp + x + n - y # 외부함수에 생성된 변수값, 즉 x, y 기억함
    return temp
  return add_sub

c1 = calculate()
for i in range(5):
  print(i, c1(i))


# 연습문제
# 랜덤으로 1~100중 하나의 정수를 받아서
# 해당 함수를 제곱하는 함수 만들기

def process(no_list, f):
  for no in no_list:
    print(f(no))


# 랜덤으로 정수 생성
import random
numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x ** 2)