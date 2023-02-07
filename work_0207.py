# 7장 큐 응용예제 1 - 유명 맛집의 대기줄 구현하기

def is_queue_full():
    global rear, front, SIZE
    if rear == (SIZE - 1):
        return True
    else:
        return False

def is_queue_empty():
    global rear, front
    if front == rear:
        return True
    else:
        return False

def add_guest(guest):
    global rear, front
    rear = rear + 1
    waiting[rear] = guest

def delete_guest():
    global rear, front
    front = front + 1
    data = waiting[front]
    waiting[front] = None
    for i in range(front+1, rear+1):
        waiting[i-1] = waiting[i]
        waiting[i] = None
    front -= 1
    rear -= 1

    return data

# 전역변수
front = rear = -1
SIZE = 5
waiting = [None for _ in range(SIZE)]

# 메인코드
if __name__ == "__main__":
    add_guest("정국")
    add_guest("뷔")
    add_guest("지민")
    add_guest("슈가")
    print(f'대기줄 상태 : {waiting}')

    for _ in range(rear+1):
        print(delete_guest(), " 님 입장")
        print(f'대기줄 상태 : {waiting}')
