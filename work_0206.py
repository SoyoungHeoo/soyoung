#  로또 추첨하기 (Simple Linked List, 157p)
import random

class Node():
    def __init__(self, data=None):
        self.data = data
        self.link = None

def make_lotto(num):
    global head, current, pre
    node = Node()
    node.data = num
    memory.append(node)
    if head == None: # 첫번째 노드
        head = node
        return # 함수 끝내기
    if head.data > num:
        node.link = head
        head = node # node 의 num이 더 작으므로 node가 head 가 된다.
        return

    current = head # head에서부터 시작하여 순회
    while current.link != None: # 중간노드
        pre = current # pre도 current 따라 한칸씩 이동하게됨
        current = current.link # current 이동
        if current.data > num: # num을 둘 자리를 찾음. (크기순)
            pre.link = node # current 이동 전 미리 저장해뒀던 pre 사용
            node.link = current # node와 current 연결
            return # 함수 종료
    current.link = node # current를 마지막까지 순회한 경우. node의 num이 제일 큼. node를 current.link에 연결
    return

def print_num(start):
    current = start
    if current == None:
        return
    while current.link != None:
        print(current.data, end = ' ')
        current = current.link
    print(current.data)
    return

def find_num(number):
    '''
    숫자가 로또번호리스트에 있는지 확인하기
    :param number: int
    :return: True or False
    '''
    global head, current # 값 입력하지 않을 땐 pre가 필요하지 ㅏ않음
    if head == None:
        return False # 리스트가 비어있는 경우
    if head.data == number:
        return True
    current = head
    while current.link != None:
        current = current.link
        if current.data == number:
            return True
    return False


LOTTO = [random.randint(1, 45) for _ in range(6)]
memory = list()
head, current, pre = None, None, None

if __name__ == "__main__":
    while True:
        num = random.randint(1, 45)
        if find_num(num):
            continue
        make_lotto(num)
        if len(memory) == 6:
            break
    print_num(head)