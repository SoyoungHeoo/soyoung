# 7장 응용예제 2 - 콜센터 응답 대기 시간 계산하기

def is_queue_full():
    global front, rear, SIZE
    if front == (rear+1) % SIZE:
        return True
    else:
        return False


def is_queue_empty():
    global front, rear, SIZE
    if front == rear:
        return True
    else:
        return False


def add_waiting(data):
    global WAITING_TIME, front, rear, SIZE
    if is_queue_full():
        print("Queue is Empty")
        return
    rear = (rear + 1) % SIZE
    queue_line[rear] = data
    calc_waiting_time(data[1])
    return


def finish_waiting():
    global WAITING_TIME, front, rear
    if is_queue_empty():
        print("Queue is Full!")
        return
    front = (front+1) % SIZE
    data = queue_line[front]
    queue_line[front] = None
    calc_waiting_time(-1 * data[1])
    return data


def calc_waiting_time(time_int):
    global WAITING_TIME
    WAITING_TIME += time_int


def peek():
    global WAITING_TIME, front, rear
    if is_queue_empty():
        return("Queue is Empty")
    return queue_line[front+1]


WAITING_TIME = 0
front = rear = -1
SIZE = 5
queue_line = [None for _ in range(SIZE)]


if __name__ == "__main__":
    add_waiting(('사용',9))
    print(f'')
    print(f'귀하의 대기시간은 {WAITING_TIME}분 입니다.')
    add_waiting(('고장',3))
    print(f'귀하의 대기시간은 {WAITING_TIME}분 입니다.')
    add_waiting(('환불',4))
    print(f'귀하의 대기시간은 {WAITING_TIME}분 입니다.')
    add_waiting(('고장',3))
    print(f'귀하의 대기시간은 {WAITING_TIME}분 입니다.')
    print(queue_line)
    print(f'귀하의 대기시간은 {WAITING_TIME}분 입니다.')

    finish_waiting()
    print(f'귀하의 대기시간은 {WAITING_TIME}분 입니다.')
    print(queue_line)

