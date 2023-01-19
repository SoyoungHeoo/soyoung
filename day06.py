# Generator
# yield : 함수를 종료하지 않고 중간중간에 값을 내보낼 수 있다.
# return : stop iteration 되어 마지막에 값 하나만 내보내게 된다.


# decorator
# 함수를 입력받아 함수를 리턴하는 함수.
# 함수를 수정하고 싶지만 원본 함수를 건드리고 싶지 않을 때 유용하다.

def document_it(func):  # 데코레이터 함수
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)  ## 위치기반 인수
        print('Keyword arguments: ', kwargs)  ## 키워드 기반 인수
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function # 클로저 역할?

  # 데커레이터 함수 적용 (수동)

def sub_int(x, y):
    return x-y

print(sub_int(7, 3))
info_sub_int = document_it(sub_int)
r = info_sub_int(7, 3) # 클로저 형식으로 만들어진 데코레이터 동작하는 동안 값들이 print됨.
print(r) # 리턴된 값 자체도 프린트할 수 있음.


# 더 쉬운 사용법

@document_it
def add_int(x, y):
    return x+y

add_int(7, 3)


# 네임스페이스

# g = 1 # 전역변수. 다른 함수의 내부에서도 접근할 수 있다.

def print_global(): # 함수의 내부는 shade 되어있다. (함수밖에서 접근할 수없음)
    g = 1
    print(g)

# print(g)


# 재귀함수 (호출하는 함수)

def factorial_iter(n):
    '''
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer 팩토리얼 계산 결과 값
    '''
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result

print(factorial_iter(5))

def factorial_recu(n):
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: n!
    :return: 자기 자신 호출 또는 1
    '''
    if n == 1:
        return n
    else:
        return factorial_recu(n-1) * n

print(factorial_recu(5))


# 재귀함수는 리스트의 리스트와 같이 고르지 않은 데이터를 처리할 때 유용하다.
# flatten


