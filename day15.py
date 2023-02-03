def print_poly(px):
    term = len(px) - 1
    poly_str = "P(x) = "
    for i in range(len(px)):
        coef = px[i]
        # if (coef >= 0):
        #     poly_str += "+"
        if i > 0 and coef > 0:
            poly_str = poly_str + "+"
        elif coef == 0:
            term = term - 1
            continue
        poly_str = poly_str + f'{coef}x^{term}'
        term = term -1

    return poly_str

def calcPoly(value, px):
    return_val = 0
    term = len(px) - 1

    for i in range(len(px)):
        coef = px[i]
        return_val = return_val + coef* value ** term
        term -= 1

    return return_val

# 전역변수
px = [7, -4, 0, 5]

if __name__ == "__main__":
    str =  print_poly(px)
    print(str)

    x_val = int(input("x값 : "))
    px_val = calcPoly(x_val, px)
    print(px_val)
