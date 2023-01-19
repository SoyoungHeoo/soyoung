# 9.3

def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def square(n):
    return n ** 2

print(square(5))


# 9.4

class OopsException(Exception): # 예외는 Exception 클래스의 자식 클래스.
    def __init__(self):
        print('Caught an oops')

while True:
    words = input('input number: ')
    if int(words) > 100:
        raise OopsException()
