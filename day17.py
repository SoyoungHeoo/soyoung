# Queue : first in - first out
# en_queue : 큐에 데이터 삽입하는 작동
# de_queue : 데이터를 추출하는 작동
# front : 저장된 데이터중 첫 번째 데이터
# rear : 저장된 데이터 중 마지막 데이터

# front, rear의 초기값은 -1.
# stack 은 top 만으로도 구현 가능했으나 큐에서는 front, rear 두 개의 키워드가 필요하다.
# 값이 증가할 때 rear 1씩 증가.
# 값이 감소할 때 front가 1씩 증가.


# 큐가 꽉찼는지 확인하는 함수 : rear 값이 큐크기 -1과 같으면 큐가 꽉찬 것.
# 큐가 비어있는지 확인하는 함수 : rear 값과 front 값이 같으면 큐가 비어있는 것.

def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def is_queue_full():
    global SIZE, queue, front, rear
    if (front == (rear + 1) % SIZE):
        return True
    else:
        return False


def de_queue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("Queue is Empty!")
        return
    front = (front + 1) % len(queue)
    data = queue[front]
    queue[front] = None
    return data

def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("Queue is Full")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data
    return


def peek():  # 확인
    global SIZE, queue, front, rear
    if is_queue_empty():
        return
    return queue[front + 1]  # side effect 없음


SIZE = 5
queue = [None for _ in range(SIZE)]
front = -1
rear = -1


if __name__ == "__main__":

    en_queue("파이리")
    print(queue)
    en_queue("꼬부기")
    print(queue)
    print(de_queue())
    print(queue)
    print(de_queue())
