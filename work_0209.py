def notation(base, n):
    if n < base :
        print(numberChar[n], end='')
    else:
        notation(base, n // base)
        print(numberChar[n % base], end='')


numberChar = [str(i) for i in range(10)]
numberChar += ['A', 'B', 'C', 'D', 'E', 'F']


if __name__ == "__main__":
    number = 4
    notation(2, number)