def rec(n):
    if n <= 0:
        pass
    else:
        print(n, end=' ')
        return rec(n-1)
rec(int(input()))