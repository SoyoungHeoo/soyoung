#  401 : 함수 3 - 자가진단 1
def rec(n):
    if n <= 0:
        pass
    else:
        print('recursive')
        return rec(n-1)

rec(int(input()))