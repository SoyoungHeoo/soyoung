def calc(x, y):
    '''
    나누기 함수
    :param x:
    :param y:
    :return: x / y
    '''
    return x / y

# 파이썬은 모든 에러가 실행에러. (runtime error)
# 여기에 대한 필연적인 해결책을 만들어두기 위한 것 = try - except 구문



# try, exception



#

# 9.2

# while 문 사용
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
# gen_odd2 = (i for i in range)

for i in gen_odd:               # for문 돌려 홀수들을 출력한다.
    print(i)                    # 1, 3, 5, 7, 9 가 차례로 출력될 것이다.


groups = {
    '빅뱅': ['GD', '태양', '탑', '대성', '승리'],
    '마마무': ['솔라', '화사']
}


# 딕셔너리 groups의 value 들의 요소들 뽑아오기
for i, j in groups.items(): # for문에 key, value 튜플로 받아오는게 핵심
    for j2 in j :
        if j2 == '승리':
            continue
        print(j2)

