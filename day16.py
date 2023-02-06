

def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1 :
        return True
    else:
        return False

def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    return False

def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is Full")
    stack[top+1] = data
    top += 1
    return

def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is Empty")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp


def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is Empty")
        return None
    return stack[top]


SIZE = int(input("Stack Size : "))
stack= [None for _ in range(SIZE)]
top = -1


if __name__ == "__main__":

    while True:
        menu = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
        if (menu == 'X' or menu == 'x'):
            break
        if menu == 'I' or menu == 'i':
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 : ", stack)
        elif menu == 'E' or menu == 'e':
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        elif menu == 'V' or menu == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        else:
            print("입력이 잘못됨")

    print("프로그램 종료!")

    ## 데이터들의 상태를 알 수 있는 것은 가장 위(마지막) 원소의 인덱스를 저장하고 있는 top 값 떄문.

