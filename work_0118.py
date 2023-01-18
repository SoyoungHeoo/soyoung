# 8.11
odd_set = {i for i in range(10) if i % 2 == 1}
print(odd_set)

# 8.12 제너레이터 컴프리헨션. * 튜플이 아니다.
gen = (f'Got {i}' for i in range(10))
for line in gen:
    print(line)

# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

# 9.2
def get_odds(first=0, last=10):
    '''
    입력받은 범위 안에서 홀수를 반환하는 제너레이터함수
    :param first: integer
    :param last: integer
    :return: generator
    '''
    number = first
    while number < last:        # 이번 차례의 수가 범위안에 해당할 때
        if (number % 2 == 1):   # 이번 차례의 수가 홀수라면
            yield number        # 값 내놓기
            number += 2         # 2를 더해서 다음 홀수 만들기
        else:                   # 이번 차례의 수가 홀수가 아니라면
            number += 1         # 1을 더해서 홀수로 만들기

gen_odd = get_odds()            # 함수 실행하여 변수에 저장 -> 제너레이터 객체가 gen_odd에 저장된다.

for i in gen_odd:               # for문 돌려 홀수들을 출력한다.
    print(i)                    # 1, 3, 5, 7, 9 가 차례로 출력될 것이다.

print(gen_odd)