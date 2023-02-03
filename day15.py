def print_poly(px, tx):
    poly_str = "P(x) = "
    for i in range(len(px)):
        coef = px[i]
        # if (coef >= 0):
        #     poly_str += "+"
        if i > 0 and coef > 0:
            poly_str = poly_str + "+"
        elif coef == 0:
            term = tx[i] - 1
            continue
        poly_str = poly_str + f'{coef}x^{tx[i]}'


    return poly_str

def calcPoly(value, px, tx):
    return_val = 0
    term = len(px) - 1

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]
        return_val = return_val + coef* value ** term

    return return_val


# 계수 리스트, 차수 리스트를 따로 입력받아보자. -> 불필요한 원소 제거
px = [7, -4, 0, 5]
tx = [3, 2, 1, 0]

if __name__ == "__main__":
    str =  print_poly(px, tx)
    print(str)

    x_val = int(input("x값 : "))
    px_val = calcPoly(x_val, px,tx)
    print(px_val)
